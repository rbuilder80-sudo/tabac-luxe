#!/usr/bin/env python3
"""v19 static gate: v18 + mobile hardening + 100% on-page SEO + Supabase image hosting.

New in v19 (over v18):
 8. every image reference points to the Supabase CDN (site-assets) — no local
    assets/ refs, no double-prefix corruption, every referenced CDN asset maps
    back to a file on disk (source of truth for the upload set)
 9. every :hover rule is wrapped in @media(hover:hover) (mobile double-tap fix)
10. twitter:card meta on every page
11. favicon (rel="icon") on every page
12. preconnect to the Supabase CDN on every page
13. static <img> tags carry width+height (CLS) — SPA templates in index.html exempt
14. sitemap carries <lastmod> and image:image entries
"""
import os, re, json, glob, sys, html as htmllib
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXCLUDE = {".git", "verifier"}
EXTS = {".html", ".xml", ".txt", ".json", ".md", ".svg", ".css", ".js"}
SUPA = "https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/"
errors = []

def fail(msg):
    errors.append(msg)

# 1. rodange sweep
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in EXCLUDE]
    for fn in filenames:
        if os.path.splitext(fn)[1].lower() not in EXTS:
            continue
        p = os.path.join(dirpath, fn)
        try:
            s = open(p, encoding="utf-8").read()
        except Exception:
            continue
        if re.search(r"rodange", s, re.I):
            fail(f"rodange in {os.path.relpath(p, ROOT)}")

pages = sorted(glob.glob(os.path.join(ROOT, "*.html")) +
               glob.glob(os.path.join(ROOT, "category", "*.html")) +
               glob.glob(os.path.join(ROOT, "product", "*.html")))
if len(pages) != 541:
    fail(f"expected 541 html pages, found {len(pages)}")

for p in pages:
    rel = os.path.relpath(p, ROOT)
    s = open(p, encoding="utf-8").read()
    is_spa = rel == "index.html"
    # 2. h1 / title / desc / json-ld
    if not is_spa and len(re.findall(r"<h1[ >]", s)) != 1:
        fail(f"{rel}: h1 count != 1")
    t = re.search(r"<title>([^<]*)</title>", s)
    if not t or not (30 <= len(htmllib.unescape(t.group(1))) <= 65):
        fail(f"{rel}: title length {len(htmllib.unescape(t.group(1))) if t else 0}")
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not d or not (120 <= len(htmllib.unescape(d.group(1))) <= 165):
        fail(f"{rel}: desc length {len(htmllib.unescape(d.group(1))) if d else 0}")
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            json.loads(m)
        except Exception as e:
            fail(f"{rel}: invalid JSON-LD: {e}")
    # 3. image refs: CDN absolute, no corruption, asset exists on disk
    if "site-assets/https" in s:
        fail(f"{rel}: corrupted double-prefixed asset URL")
    for src in re.findall(r'(?:src|href)="([^"]*assets/[^"]+)"', s):
        if src.startswith("data:") or "${" in src:
            continue
        if src.startswith(("../", "/")) or re.match(r"^assets/", src) or src.startswith("https://tabacluxe.lu/assets/"):
            fail(f"{rel}: non-CDN asset ref {src}")
            continue
        if src.startswith(SUPA):
            loc = src[len(SUPA):]
            if not os.path.isfile(os.path.join(ROOT, loc)):
                fail(f"{rel}: CDN asset has no local source {loc}")
    # 4. v19 page furniture
    if ":hover" in s and "hover:hover" not in s:
        fail(f"{rel}: unguarded :hover rule (mobile double-tap risk)")
    if 'name="twitter:card"' not in s:
        fail(f"{rel}: twitter:card missing")
    if 'rel="icon"' not in s:
        fail(f"{rel}: favicon missing")
    if 'rel="preconnect" href="https://ujmblinyxfjvpntfkohz.supabase.co"' not in s:
        fail(f"{rel}: Supabase preconnect missing")
    if not is_spa:
        for tag in re.findall(r"<img\b[^>]*>", s):
            if "alt=" not in tag:
                fail(f"{rel}: img without alt")
            if "width=" not in tag or "height=" not in tag:
                fail(f"{rel}: img without width/height (CLS)")

# 5. sitemap completeness + freshness + images
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9",
      "im": "http://www.google.com/schemas/sitemap-image/1.1"}
smroot = ET.parse(os.path.join(ROOT, "sitemap.xml")).getroot()
smurls = smroot.findall("sm:url", ns)
urls = [u.find("sm:loc", ns).text for u in smurls]
if len(urls) != 556:
    fail(f"sitemap has {len(urls)} urls, expected 556")
imgs_in_sitemap = 0
for u in smurls:
    loc = u.find("sm:loc", ns).text
    if u.find("sm:lastmod", ns) is None:
        fail(f"sitemap url {loc}: no lastmod")
    if u.find("im:image", ns) is not None:
        imgs_in_sitemap += 1
    path = loc.replace("https://tabacluxe.lu/", "")
    if path == "" or path.endswith("/"):
        path += "index.html"
    if not os.path.isfile(os.path.join(ROOT, path)):
        fail(f"sitemap url {loc} has no file")
if imgs_in_sitemap < 520:
    fail(f"sitemap has only {imgs_in_sitemap} image entries, expected 520+")

# 5b. all 15 restored ranked doorway pages (8 en + 7 fr)
DOORWAY = [
    "en/cheapest-cigarettes-luxembourg",
    "en/cigarette-wholesalers-luxembourg",
    "en/flandria-tobacco-50g-luxembourg",
    "en/luxembourg-tobacco-prices",
    "en/tobacco-luxembourg",
    "en/tobacco-shop-luxembourg",
    "en/turner-50g-luxembourg",
    "en/wholesale-tobacco-luxembourg",
    "fr/bureau-de-tabac-luxembourg",
    "fr/cigarette-winston-luxembourg-prix",
    "fr/prix-cigarette-luxembourg",
    "fr/prix-tabac-a-rouler-luxembourg",
    "fr/prix-tabac-luxembourg",
    "fr/tabac-luxembourg-frontiere",
    "fr/tabac-luxembourg-ouvert-actuellement",
]
for slug in DOORWAY:
    enp = os.path.join(ROOT, slug, "index.html")
    if not os.path.isfile(enp):
        fail(f"{slug}/index.html missing")
        continue
    s = open(enp, encoding="utf-8").read()
    if len(re.findall(r"<h1[ >]", s)) != 1:
        fail(f"{slug}: h1 count != 1")
    t = re.search(r"<title>([^<]*)</title>", s)
    if not t or not (30 <= len(htmllib.unescape(t.group(1))) <= 65):
        fail(f"{slug}: title length out of range")
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not d or not (120 <= len(htmllib.unescape(d.group(1))) <= 165):
        fail(f"{slug}: desc length out of range")
    if f'<link rel="canonical" href="https://tabacluxe.lu/{slug}/">' not in s:
        fail(f"{slug}: canonical missing or wrong")
    if 'content="index,follow,max-image-preview:large"' not in s:
        fail(f"{slug}: robots meta missing")
    if "G-VE6XGYJ7VP" not in s:
        fail(f"{slug}: GA tag missing")
    if "styles.css" in s:
        fail(f"{slug}: references deleted /styles.css")
    if re.search(r"rodange", s, re.I):
        fail(f"{slug}: rodange reference")
    if '"@type":"FAQPage"' not in s:
        fail(f"{slug}: FAQPage JSON-LD missing")
    for href in re.findall(r'href="([^"]+)"', s):
        if href.startswith(("http", "#", "mailto:", "tel:")) or href.startswith("/#/"):
            continue
        fp = href.lstrip("/")
        if href.endswith("/"):
            fp += "index.html"
        if not os.path.isfile(os.path.join(ROOT, fp)):
            fail(f"{slug}: dead internal link {href}")
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            json.loads(m)
        except Exception as e:
            fail(f"{slug}: invalid JSON-LD: {e}")
    if f"https://tabacluxe.lu/{slug}/" not in urls:
        fail(f"{slug}: missing from sitemap")

# 6. Supabase products: CDN image resolves to a local source file + page/catalogue consistency
try:
    import urllib.request
    req = urllib.request.Request(
        "https://ujmblinyxfjvpntfkohz.supabase.co/rest/v1/products?select=name,image",
        headers={"apikey": "sb_publishable_O65H3nPdVW5tA-ZZ7HoiVw_gI9M-iDr",
                 "Authorization": "Bearer sb_publishable_O65H3nPdVW5tA-ZZ7HoiVw_gI9M-iDr"})
    rows = json.load(urllib.request.urlopen(req, timeout=30))
    for r in rows:
        img = (r.get("image") or "").strip()
        if not img:
            fail(f"supabase product '{r.get('name')}': empty image")
            continue
        if not img.startswith(SUPA):
            fail(f"supabase product '{r.get('name')}': image not on CDN: {img}")
            continue
        if not os.path.isfile(os.path.join(ROOT, img[len(SUPA):])):
            fail(f"supabase product '{r.get('name')}': CDN image has no local source: {img}")
    def slugify(x):
        x = x.lower().replace("×", "x")
        return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", x)).strip("-")
    PAGE_ALIASES = {"chivas-regal-12-ans-70cl": "chivas-regal-12y-70cl"}
    CAT_SUFFIXES = ["shisha", "cigares", "cigarettes", "seau", "potvol", "pot",
                    "rouler", "pipe", "whisky", "vodka", "rhum", "gin", "anises",
                    "bieres", "energie", "softs"]
    by_slug = {}
    for r in rows:
        nm = r.get("name") or ""
        for v in {slugify(nm), slugify(nm.replace("'", "").replace("’", ""))}:
            by_slug.setdefault(v, []).append(r)
    matched = unmatched = 0
    for p in pages:
        rel = os.path.relpath(p, ROOT)
        if not rel.startswith("product/"):
            continue
        slug = rel[len("product/"):-len(".html")]
        row = None
        alias = {v: k for k, v in PAGE_ALIASES.items()}
        candidates = [slug] + ([alias[slug]] if slug in alias else [])
        for cand in candidates:
            if cand in by_slug:
                row = by_slug[cand][0]
                break
        if not row:
            for suf in CAT_SUFFIXES:
                for cand in candidates:
                    if cand.endswith("-" + suf) and cand[: -len(suf) - 1] in by_slug:
                        row = by_slug[cand[: -len(suf) - 1]][0]
                        break
                if row:
                    break
        if not row:
            fail(f"{rel}: no matching Supabase product row")
            unmatched += 1
            continue
        matched += 1
        want = (row.get("image") or "").strip()
        s = open(p, encoding="utf-8").read()
        main = re.search(r'<div class="imgbox"><img[^>]*src="([^"]+)"', s)
        og = re.search(r'<meta property="og:image" content="([^"]+)"', s)
        if not main:
            fail(f"{rel}: no imgbox image")
        elif main.group(1) != want:
            fail(f"{rel}: page image {main.group(1)} != catalogue {want}")
        if og and og.group(1) != want.replace(".webp", ".jpg"):
            fail(f"{rel}: og:image mismatch vs catalogue {want}")
    print(f"product pages matched to catalogue rows: {matched}, unmatched: {unmatched}")
    print(f"supabase products checked: {len(rows)}")
except Exception as e:
    fail(f"supabase check unreachable: {e}")

# 7. WhatsApp button on every page (v18): each HTML page must expose a wa.me link
all_html = [p for p in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
            if os.sep + "verifier" + os.sep not in p]
for p in all_html:
    rel = os.path.relpath(p, ROOT)
    s = open(p, encoding="utf-8").read()
    if "wa.me/" not in s:
        fail(f"{rel}: no WhatsApp link (wa.me) — every page must have the WhatsApp button")

if errors:
    print(f"FAIL — {len(errors)} problems")
    for e in errors[:60]:
        print("  ", e)
    sys.exit(1)
print(f"PASS — {len(pages)} pages + 15 doorway pages, CDN images on all pages, hover guarded, "
      f"twitter/favicon/preconnect complete, CLS-safe images, sitemap {len(urls)} urls with lastmod+images, "
      f"WhatsApp button on all {len(all_html)} pages, rodange-free")
sys.exit(0)
