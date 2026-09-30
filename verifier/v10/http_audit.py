#!/usr/bin/env python3
"""HTTP and rendered-browser audit for every crawlable Tabac Luxe page."""
from pathlib import Path
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import asyncio, json, re, sys, time, threading, socketserver, http.server, functools
import requests
import xml.etree.ElementTree as ET
from playwright.async_api import async_playwright

APP = Path(__file__).resolve().parents[2]
BASE = 'https://tabacluxe.lu'
HOST = '127.0.0.1'
PORT = 8898
LOCAL = f'http://{HOST}:{PORT}'

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args): pass

def start_server():
    handler = functools.partial(QuietHandler, directory=str(APP))
    class Reuse(socketserver.ThreadingMixIn, socketserver.TCPServer):
        allow_reuse_address = True
        daemon_threads = True
        def handle_error(self, request, client_address):
            pass
    httpd = Reuse((HOST, PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd

def sitemap_urls_images():
    root = ET.parse(APP/'sitemap.xml').getroot()
    ns = {'sm':'http://www.sitemaps.org/schemas/sitemap/0.9','image':'http://www.google.com/schemas/sitemap-image/1.1'}
    urls = [u.find('sm:loc', ns).text for u in root.findall('sm:url', ns)]
    imgs = [i.find('image:loc', ns).text for i in root.findall('.//image:image', ns)]
    return urls, imgs

def local_path(url):
    path = urlparse(url).path
    if path == '/': return '/'
    if path == '/category/': return '/category/'
    return path

def http_check(url):
    path = local_path(url)
    try:
        r = requests.get(LOCAL + path, timeout=20)
        ctype = r.headers.get('content-type','')
        if r.status_code != 200: return f'{path}: HTTP {r.status_code}'
        if path.endswith(('.jpg','.jpeg','.png','.webp')) and not ctype.startswith('image/'):
            return f'{path}: wrong content-type {ctype}'
        if path.endswith('.html') or path in ['/', '/category/']:
            if b'<html' not in r.content[:2048].lower(): return f'{path}: response is not HTML'
        if len(r.content) == 0: return f'{path}: empty response'
        return None
    except Exception as e:
        return f'{path}: request failed {e}'

async def browser_page(context, url, sem, results):
    path = url[len(LOCAL):] if url.startswith(LOCAL) else local_path(url)
    async with sem:
        page = await context.new_page()
        console_errors = []
        page_errors = []
        failed_local = []
        page.on('console', lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)
        page.on('pageerror', lambda exc: page_errors.append(str(exc)))
        page.on('requestfailed', lambda req: failed_local.append(req.url) if req.url.startswith(LOCAL) else None)
        try:
            resp = await page.goto(LOCAL + path, wait_until='domcontentloaded', timeout=45000)
            status = resp.status if resp else 0
            # Trigger lazy images throughout the page, then force decode anything remaining.
            await page.evaluate("""async () => {
              const steps=[0,.2,.4,.6,.8,1];
              for (const f of steps){ window.scrollTo(0, document.body.scrollHeight*f); await new Promise(r=>setTimeout(r,120)); }
              window.scrollTo(0,0);
              await Promise.all([...document.images].map(img => img.complete ? true : img.decode().then(()=>true).catch(()=>false)));
            }""")
            await page.wait_for_timeout(250)
            data = await page.evaluate("""() => ({
              title: document.title,
              desc: document.querySelector('meta[name="description"]')?.content || '',
              h1: [...document.querySelectorAll('h1')].filter(h => !!(h.offsetWidth || h.offsetHeight || h.getClientRects().length)).length,
              images: [...document.images].map(img => ({
                src: img.currentSrc || img.src,
                alt: img.alt,
                complete: img.complete,
                naturalWidth: img.naturalWidth,
                visible: !!(img.offsetWidth || img.offsetHeight || img.getClientRects().length),
                opacity: getComputedStyle(img).opacity
              }))
            })""")
            errs = []
            if status != 200: errs.append(f'HTTP {status}')
            if not (30 <= len(data['title']) <= 65): errs.append(f'title length {len(data["title"])}')
            if not (120 <= len(data['desc']) <= 165): errs.append(f'description length {len(data["desc"])}')
            if data['h1'] != 1: errs.append(f'H1 count {data["h1"]}')
            for img in data['images']:
                if not img['complete'] or img['naturalWidth'] == 0: errs.append(f'broken image {img["src"]}')
                if not img['alt']: errs.append(f'missing alt {img["src"]}')
                if not img['visible'] or img['opacity'] == '0': errs.append(f'invisible image {img["src"]}')
            for e in console_errors:
                if 'Failed to load resource' in e and 'ERR_FAILED' in e:
                    continue  # deterministic audit blocks third-party font requests
                errs.append('console: '+e)
            for e in page_errors: errs.append('pageerror: '+e)
            for e in failed_local: errs.append('failed request: '+e)
            results[path] = {'ok': not errs, 'errors': errs, 'images': len(data['images']), 'title': data['title']}
        except Exception as e:
            results[path] = {'ok': False, 'errors': [str(e)], 'images': 0, 'title': ''}
        finally:
            await page.close()

async def browser_audit(urls):
    spa_routes = ['/#/','/#/catalogue','/#/catalogue/cigarettes','/#/promos','/#/tarifs','/#/contact','/#/cart','/#/legal/terms','/#/legal/privacy','/#/legal/disclaimer','/#/legal/notice']
    all_targets = [local_path(u) for u in urls] + spa_routes
    results = {}
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width':1366,'height':900}, ignore_https_errors=True)
        await context.add_init_script("sessionStorage.setItem('tl_adult','1'); localStorage.setItem('tl_lang','en');")
        # Block only third-party fonts to keep the local audit fast and deterministic.
        await context.route(re.compile(r'https://fonts\.(googleapis|gstatic)\.com/.*'), lambda route: route.abort())
        sem = asyncio.Semaphore(6)
        await asyncio.gather(*(browser_page(context, LOCAL + path, sem, results) for path in all_targets))
        await browser.close()
    return results

def main():
    started = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    httpd = start_server()
    errors = []
    urls, imgs = sitemap_urls_images()
    targets = urls + imgs
    with ThreadPoolExecutor(max_workers=24) as ex:
        futures = [ex.submit(http_check, u) for u in targets]
        for fut in as_completed(futures):
            e = fut.result()
            if e: errors.append('HTTP: '+e)
    browser_results = asyncio.run(browser_audit(urls))
    for path, res in browser_results.items():
        for e in res['errors']: errors.append(f'BROWSER {path}: {e}')
    image_total = sum(r.get('images',0) for r in browser_results.values())
    pages_checked = len(browser_results)
    score = 100.0 if not errors else max(0.0, 100.0 - (len(errors) / max(1,pages_checked) * 100.0))
    summary = {
        'started_utc': started,
        'http_targets': len(targets),
        'browser_pages_and_routes': pages_checked,
        'browser_images_checked': image_total,
        'errors': len(errors),
        'score': round(score, 2)
    }
    print(json.dumps(summary, indent=2))
    for e in errors[:300]: print('ERROR:', e)
    httpd.shutdown()
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())
