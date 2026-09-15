#!/usr/bin/env python3
"""Tabac Luxe verifier v7 — full catalogue restored (516), brand-name images for unsourced
listings, LU pack shots where available, performance budgets."""
import os, re, sys, json, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KEY='sb_publishable_O65H3nPdVW5tA-ZZ7HoiVw_gI9M-iDr'
req=urllib.request.Request('https://ujmblinyxfjvpntfkohz.supabase.co/rest/v1/products?select=slug,name,category,image&limit=1000',
    headers={'apikey':KEY,'Authorization':'Bearer '+KEY})
prods=json.load(urllib.request.urlopen(req))

passed=failed=0
def check(name, ok, detail=''):
    global passed, failed
    if ok: passed+=1; print(f'PASS  {name}')
    else: failed+=1; print(f'FAIL  {name}  {detail}')

check('product count == 516 (full catalogue restored)', len(prods)==516, f'got {len(prods)}')

noimg=[p for p in prods if not p.get('image')]
check('every product has image field', not noimg, f'{len(noimg)} without')

missing_file=[p['slug'] for p in prods if p.get('image') and not os.path.exists(os.path.join(ROOT,p['image']))]
check('every image file exists on disk', not missing_file, f'{len(missing_file)} missing')

# image policy: LU pack shot where sourced; otherwise brand image (real or name-card)
lu=sum(1 for p in prods if (p.get('image') or '').startswith('assets/lu/'))
brand=sum(1 for p in prods if (p.get('image') or '').startswith('assets/brands/'))
prod=sum(1 for p in prods if (p.get('image') or '').startswith('assets/products/'))
print(f'  images: {lu} LU pack shots, {brand} brand images (incl. name cards), {prod} product photos')
check('image policy: LU > brand > product, all accounted', lu+brand+prod==len(prods))

WEIGHT={'seau','pot','potvol','pipe','rouler','shisha'}
bad_cat=[]
for p in prods:
    n=p['name'].lower()
    has_weight=bool(re.search(r'\d+\s*(g|kg)\s*$',n))
    has_pack=bool(re.search(r'\d+/\d+$',n))
    if p['category'] in WEIGHT and has_pack and not has_weight: bad_cat.append(p['slug'])
    if p['category']=='cigarettes' and has_weight: bad_cat.append(p['slug'])
check('category audit: no weight/pack mismatches', not bad_cat, f'{len(bad_cat)}: {bad_cat[:5]}')

nopage=[p['slug'] for p in prods if not os.path.exists(os.path.join(ROOT,'product',p['slug']+'.html'))]
check('every product has a static page', not nopage, f'{len(nopage)} missing')
stale=[f for f in os.listdir(os.path.join(ROOT,'product')) if f[:-5] not in {p['slug'] for p in prods}]
check('no stale product pages', not stale, f'{len(stale)}')

bad=[]
need=['<title>','name="description"','rel="canonical"','property="og:title"','property="og:image"',
      'name="twitter:card"','application/ld+json','"@type": "Product"','"priceCurrency": "EUR"',
      '"@type": "BreadcrumbList"','wa.me/35228777996','Cormorant']
for p in prods:
    fp=os.path.join(ROOT,'product',p['slug']+'.html')
    if not os.path.exists(fp): continue
    h=open(fp,encoding='utf8').read()
    miss=[n for n in need if n not in h]
    m=re.search(r'<img src="\.\./([^"]+)"', h)
    if not m or not os.path.exists(os.path.join(ROOT,m.group(1))): miss.append('img-file')
    if miss: bad.append((p['slug'],miss))
check('all product pages pass SEO+design field audit', not bad, f'{len(bad)} bad: {bad[:3]}')

sm=open(os.path.join(ROOT,'sitemap.xml'),encoding='utf8').read()
notmap=[p['slug'] for p in prods if f'/product/{p["slug"]}.html' not in sm]
check('sitemap covers all products', not notmap and sm.count('<url>')==len(prods)+5,
      f'missing={len(notmap)} urls={sm.count("<url>")}')

idx=open(os.path.join(ROOT,'index.html'),encoding='utf8').read()
check('SPA cards clickable via openProduct()', 'openProduct' in idx and "onclick=\"openProduct(" in idx)

# price list = full 503 rows again, no ghosts
pl=json.load(open(os.path.join(ROOT,'data','price_list.json')))
names={p['name'] for p in prods}
ghost=[it['name'] for grp in pl for it in grp['items'] if it['name'] not in names]
rows=sum(len(g['items']) for g in pl)
check('price list complete (503 rows), no ghosts', rows==503 and not ghost, f'rows={rows} ghosts={len(ghost)}')

# performance budgets
hero=os.path.getsize(os.path.join(ROOT,'assets/hero/hero-main.jpg'))
check('hero image < 500KB (was 3.2MB PNG)', hero<500*1024, f'{hero//1024}KB')
check('no >1MB PNG hero left', not os.path.exists(os.path.join(ROOT,'assets/hero/hero-main.png')))
check('hero has fetchpriority=high', 'fetchpriority="high"' in idx)
check('catalogue imgs lazy+async', 'loading="lazy" decoding="async"' in idx)
big=[f for f in os.listdir(os.path.join(ROOT,'assets/lu')) if os.path.getsize(os.path.join(ROOT,'assets/lu',f))>200*1024]
check('all LU pack shots < 200KB', not big, f'{len(big)}: {big[:5]}')

print(f'\n{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
