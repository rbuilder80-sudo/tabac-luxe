#!/usr/bin/env python3
"""Tabac Luxe verifier v6 — Playwright smoke: SPA cards open product pages; LU images render."""
import os, sys
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
res={}
with sync_playwright() as pw:
    b=pw.chromium.launch(args=['--no-sandbox'])
    pg=b.new_page()
    pg.add_init_script("try{sessionStorage.setItem('tl_adult','1')}catch(e){}")
    errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://'+ROOT+'/index.html'); pg.wait_for_timeout(2500)
    res['featured_cards']=pg.locator('.pcard').count()
    res['broken_imgs']=pg.evaluate("Array.from(document.images).filter(i=>i.complete&&i.naturalWidth===0).length")
    # click first product card -> should navigate to a product page
    first=pg.locator('.pcard').first
    first.click()
    pg.wait_for_timeout(1200)
    res['url_after_click']=pg.url
    res['pp_h1']=pg.locator('h1').inner_text() if pg.locator('h1').count() else ''
    res['pp_img_ok']=pg.evaluate("(()=>{const i=document.querySelector('.imgbox img');return !!(i&&i.complete&&i.naturalWidth>0)})()")
    res['pp_jsonld']=pg.locator('script[type="application/ld+json"]').count()
    res['pp_related']=pg.locator('.rcard').count()
    res['pp_crumbs']=pg.locator('.crumbs').count()
    res['js_errors']=errs
    b.close()
for k,v in res.items(): print(k,'=',v)
assert '/product/' in res['url_after_click'] and res['url_after_click'].endswith('.html'), 'card click did not open product page'
# related strip check on a multi-item category page
pg2ok=True
with sync_playwright() as pw:
    b=pw.chromium.launch(args=['--no-sandbox'])
    pg=b.new_page()
    pg.goto('file://'+ROOT+'/product/winston-volume-red-250g-seau.html'); pg.wait_for_timeout(1000)
    rel=pg.locator('.rcard').count()
    print('related_on_bucket_page =', rel)
    pg2ok = rel>=1
    b.close()
assert pg2ok, 'related products strip missing'
assert res['pp_img_ok'] and res['pp_jsonld']>=2 and res['pp_crumbs']==1
assert res['broken_imgs']==0 and not res['js_errors']
print('SMOKE OK')
