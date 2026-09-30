#!/usr/bin/env python3
"""Final static SEO audit for Tabac Luxe. Exits non-zero on any acceptance failure."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json, re, sys, xml.etree.ElementTree as ET
from collections import Counter

APP = Path(__file__).resolve().parents[2]
BASE = 'https://tabacluxe.lu'
TODAY = '2026-09-15'
CATS = ['cigarettes','cigares','shisha','seau','rouler','pot','potvol','pipe','bieres','rhum','vodka','whisky','anises','energie','gin','softs']
UTILS = ['promotions.html','price-list.html','contact.html','terms.html','privacy.html','disclaimer.html','legal-notice.html']
errors = []
warnings = []
stats = Counter()

def err(msg): errors.append(msg)
def warn(msg): warnings.append(msg)
def rel(path): return str(path.relative_to(APP))
def esc_text(s): return re.sub(r'\s+', ' ', s or '').strip()

def expected_canonical(path):
    r = rel(path)
    if r == 'index.html': return BASE + '/'
    if r == 'category/index.html': return BASE + '/category/'
    return BASE + '/' + r

def local_target(page, href):
    if not href or href.startswith(('#','mailto:','tel:','sms:','javascript:','data:')): return None
    if href.startswith(('http://','https://')): return None
    href = href.split('#',1)[0].split('?',1)[0]
    if not href: return None
    target = (page.parent / href).resolve()
    try: target.relative_to(APP.resolve())
    except ValueError:
        err(f'{rel(page)}: internal link escapes site root: {href}')
        return None
    if target.is_dir(): target = target / 'index.html'
    return target

def jsonld_blocks(soup, page):
    blocks = []
    for i, script in enumerate(soup.find_all('script', attrs={'type':'application/ld+json'}), 1):
        raw = script.string or script.get_text()
        try: blocks.append(json.loads(raw))
        except Exception as e: err(f'{rel(page)}: JSON-LD block {i} invalid: {e}')
    return blocks

def check_heading_hierarchy(soup, page):
    hs = soup.find_all(re.compile('^h[1-6]$'))
    if not hs:
        err(f'{rel(page)}: missing headings')
        return
    levels = [int(h.name[1]) for h in hs]
    if levels[0] != 1:
        err(f'{rel(page)}: first heading is H{levels[0]}, expected H1')
    for prev, cur in zip(levels, levels[1:]):
        if cur > prev + 1:
            err(f'{rel(page)}: heading hierarchy skips H{prev} to H{cur}')
            break

def check_images(soup, page):
    for img in soup.find_all('img'):
        src = img.get('src','')
        alt = img.get('alt')
        if not src: err(f'{rel(page)}: image missing src')
        elif not src.startswith(('http://','https://','data:')):
            target = local_target(page, src)
            if target and not target.exists(): err(f'{rel(page)}: missing image file {src}')
        if alt is None or not alt.strip(): err(f'{rel(page)}: image missing alt text: {src}')
    # CSS/JS local asset references in the raw source.
    raw = page.read_text(encoding='utf-8')
    for ref in sorted(set(re.findall(r'assets/[A-Za-z0-9_./%()+-]+', raw))):
        ref = ref.rstrip('.,;:!?)]}\'"')
        if not (APP / ref).exists(): err(f'{rel(page)}: missing referenced asset {ref}')

def check_common(page, soup):
    r = rel(page)
    title = esc_text(soup.title.string if soup.title else '')
    desc_tag = soup.find('meta', attrs={'name':'description'})
    desc = desc_tag.get('content','').strip() if desc_tag else ''
    if not (30 <= len(title) <= 65): err(f'{r}: title length {len(title)} outside 30-65: {title}')
    if not (120 <= len(desc) <= 165): err(f'{r}: meta description length {len(desc)} outside 120-165')
    canonical = soup.find('link', rel='canonical')
    if not canonical or canonical.get('href') != expected_canonical(page): err(f'{r}: canonical mismatch')
    robots = soup.find('meta', attrs={'name':'robots'})
    robots_c = robots.get('content','') if robots else ''
    for needle in ['index','follow','max-image-preview:large']:
        if needle not in robots_c: err(f'{r}: robots meta missing {needle}')
    required = [
        ('property','og:title'), ('property','og:description'), ('property','og:url'),
        ('property','og:image'), ('property','og:image:alt'), ('property','og:site_name'),
        ('name','twitter:card'), ('name','twitter:title'), ('name','twitter:description'),
        ('name','twitter:image'), ('name','twitter:image:alt'), ('name','theme-color'),
        ('name','geo.region'), ('name','geo.placename'), ('name','geo.position'), ('name','ICBM')]
    for attr, name in required:
        tag = soup.find('meta', attrs={attr:name})
        if not tag or not tag.get('content'): err(f'{r}: missing meta {name}')
    if not soup.find('link', rel='help', href=BASE + '/llms.txt'): err(f'{r}: missing llms.txt link')
    h1s = soup.find_all('h1')
    if len(h1s) != 1: err(f'{r}: expected exactly one H1, found {len(h1s)}')
    check_heading_hierarchy(soup, page)
    check_images(soup, page)
    for a in soup.find_all('a', href=True):
        target = local_target(page, a['href'])
        if target and not target.exists(): err(f'{r}: broken internal link {a["href"]}')
    text = soup.get_text(' ', strip=True)
    for bad in ['1 references', 'TODO', 'Lorem ipsum', 'undefined', '[object Object]']:
        
        if bad == '1 references':
            if re.search(r'(?<!\d)1\s+references', text): err(f'{r}: suspicious content "1 references"')
        elif bad in text: err(f'{r}: suspicious content "{bad}"')
    return title, desc, jsonld_blocks(soup, page)

html_pages = [APP/'index.html'] + sorted((APP/'category').glob('*.html')) + sorted((APP/'product').glob('*.html')) + [APP/u for u in UTILS]
stats['html_pages'] = len(html_pages)
if len(html_pages) != 541: err(f'expected 541 HTML pages, found {len(html_pages)}')

titles, descs = [], []
for page in html_pages:
    soup = BeautifulSoup(page.read_text(encoding='utf-8'), 'html.parser')
    title, desc, blocks = check_common(page, soup)
    titles.append(title); descs.append(desc)
    types = [b.get('@type') for b in blocks if isinstance(b, dict)]
    r = rel(page)
    if r == 'index.html':
        for typ in ['Store','WebSite','FAQPage']:
            if typ not in types: err(f'index.html: missing {typ} JSON-LD')
    elif r.startswith('product/'):
        if 'Product' not in types or 'BreadcrumbList' not in types: err(f'{r}: missing Product/BreadcrumbList JSON-LD')
        product = next((b for b in blocks if isinstance(b,dict) and b.get('@type')=='Product'), {})
        offer = product.get('offers', {}) if isinstance(product, dict) else {}
        for key in ['name','image','description','category','brand']:
            if not product.get(key): err(f'{r}: Product schema missing {key}')
        for key in ['price','priceCurrency','priceValidUntil','availability','itemCondition','seller','url']:
            if key not in offer: err(f'{r}: Offer schema missing {key}')
        if not soup.find('a', href=re.compile(r'^https://wa\.me/35228777996')): err(f'{r}: missing WhatsApp CTA')
        if not soup.find('nav', class_='crumbs', attrs={'aria-label':'Breadcrumb'}): err(f'{r}: missing accessible breadcrumbs')
    elif r.startswith('category/'):
        if 'CollectionPage' not in types or 'BreadcrumbList' not in types: err(f'{r}: missing CollectionPage/BreadcrumbList JSON-LD')
        if r != 'category/index.html' and 'ItemList' not in str(blocks): err(f'{r}: missing ItemList schema')
    else:
        if 'BreadcrumbList' not in types: err(f'{r}: missing BreadcrumbList JSON-LD')

for value, label in [(titles,'title'), (descs,'meta description')]:
    dupes = [v for v,c in Counter(value).items() if c > 1]
    if dupes: err(f'duplicate {label}: {dupes[:5]}')

# Sitemap.
sitemap = APP/'sitemap.xml'
root = ET.parse(sitemap).getroot()
ns = {'sm':'http://www.sitemaps.org/schemas/sitemap/0.9','image':'http://www.google.com/schemas/sitemap-image/1.1'}
urls = [u.find('sm:loc', ns).text for u in root.findall('sm:url', ns)]
imgs = [i.find('image:loc', ns).text for i in root.findall('.//image:image', ns)]
stats['sitemap_urls'] = len(urls); stats['sitemap_images'] = len(imgs)
if len(urls) != 541: err(f'sitemap URL count {len(urls)} != 541')
if len(set(urls)) != len(urls): err('sitemap contains duplicate URLs')
if len(imgs) != 541: err(f'sitemap image count {len(imgs)} != 541')
for loc in urls:
    if loc == BASE + '/': target = APP/'index.html'
    elif loc == BASE + '/category/': target = APP/'category/index.html'
    else: target = APP / loc.replace(BASE + '/', '')
    if not target.exists(): err(f'sitemap target missing: {loc}')
for loc in imgs:
    target = APP / loc.replace(BASE + '/', '')
    if not target.exists(): err(f'sitemap image missing: {loc}')

# Robots and AI guides.
robots = (APP/'robots.txt').read_text(encoding='utf-8')
for bot in ['GPTBot','OAI-SearchBot','ChatGPT-User','ClaudeBot','Claude-User','PerplexityBot','Perplexity-User','Google-Extended','Bingbot','Applebot','Meta-ExternalAgent']:
    if f'User-agent: {bot}' not in robots: err(f'robots.txt missing {bot}')
if f'Sitemap: {BASE}/sitemap.xml' not in robots: err('robots.txt missing sitemap')
for name in ['llms.txt','llms-full.txt']:
    text = (APP/name).read_text(encoding='utf-8')
    for needle in ['Route de Longwy 549','WhatsApp','18+','Rodange']:
        if needle not in text: err(f'{name}: missing {needle}')
if (APP/'llms-full.txt').read_text(encoding='utf-8').count('https://tabacluxe.lu/product/') < 516:
    err('llms-full.txt does not contain all 516 product URLs')

# Performance guardrails.
hero = APP/'assets/hero/hero-main.jpg'
if not hero.exists(): err('hero-main.jpg missing')
elif hero.stat().st_size > 500_000: err(f'hero-main.jpg too large: {hero.stat().st_size} bytes')

score = 100.0 if not errors else max(0.0, 100.0 - (len(errors) / max(1, len(html_pages)) * 100.0))
print(f'pages={len(html_pages)}')
print(f'sitemap_urls={len(urls)} sitemap_images={len(imgs)}')
print(f'errors={len(errors)} warnings={len(warnings)} score={score:.2f}%')
for e in errors[:200]: print('ERROR:', e)
for w in warnings[:200]: print('WARNING:', w)
sys.exit(1 if errors else 0)
