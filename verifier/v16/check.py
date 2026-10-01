#!/usr/bin/env python3
"""v16 static gate: v15 + restored /en/wholesale-tobacco-luxembourg/ SEO landing page (542 sitemap URLs)."""
import os, re, re as _re, json, glob, sys, html as htmllib
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXCLUDE = {".git", "verifier"}
EXTS = {".html", ".xml", ".txt", ".json", ".md", ".svg", ".css", ".js"}
errors = []
ok_count = 0

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
    # 3. local images exist (skip SPA templates — rendered DOM is browser-audited)
    if not is_spa:
        for src in re.findall(r'<img[^>]+src="([^"]+)"', s):
            if src.startswith(("http", "data:")) or "${" in src:
                continue
            fp = os.path.normpath(os.path.join(os.path.dirname(p), src))
            if not os.path.isfile(fp):
                fail(f"{rel}: missing image {src}")
    # 4. product image correctness — deferred to Supabase consistency pass below

# 5. sitemap completeness
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = [u.find("sm:loc", ns).text for u in ET.parse(os.path.join(ROOT, "sitemap.xml")).getroot().findall("sm:url", ns)]
if len(urls) != 542:
    fail(f"sitemap has {len(urls)} urls, expected 542")
for u in urls:
    path = u.replace("https://tabacluxe.lu/", "")
    if path == "" or path.endswith("/"):
        path += "index.html"
    if not os.path.isfile(os.path.join(ROOT, path)):
        fail(f"sitemap url {u} has no file")


# 5b. restored SEO landing page /en/wholesale-tobacco-luxembourg/
enp = os.path.join(ROOT, "en", "wholesale-tobacco-luxembourg", "index.html")
if not os.path.isfile(enp):
    fail("en/wholesale-tobacco-luxembourg/index.html missing")
else:
    s = open(enp, encoding="utf-8").read()
    if len(re.findall(r"<h1[ >]", s)) != 1:
        fail("en landing: h1 count != 1")
    t = re.search(r"<title>([^<]*)</title>", s)
    if not t or not (30 <= len(htmllib.unescape(t.group(1))) <= 65):
        fail("en landing: title length out of range")
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not d or not (120 <= len(htmllib.unescape(d.group(1))) <= 165):
        fail("en landing: desc length out of range")
    if '<link rel="canonical" href="https://tabacluxe.lu/en/wholesale-tobacco-luxembourg/">' not in s:
        fail("en landing: canonical missing or wrong")
    if "styles.css" in s:
        fail("en landing: references deleted /styles.css")
    for href in re.findall(r'href="([^"]+)"', s):
        if href.startswith(("http", "#", "mailto:", "tel:")) or href.startswith("/#/"):
            continue
        fp = href.lstrip("/")
        if href.endswith("/"):
            fp += "index.html"
        if not os.path.isfile(os.path.join(ROOT, fp)):
            fail(f"en landing: dead internal link {href}")
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            json.loads(m)
        except Exception as e:
            fail(f"en landing: invalid JSON-LD: {e}")

# 6. Supabase products: image resolves + correctness rule
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
        if not os.path.isfile(os.path.join(ROOT, img)):
            fail(f"supabase product '{r.get('name')}': image missing on disk: {img}")
    # 4. product page image == Supabase row image (catalogue source of truth)
    def slugify(x):
        x = x.lower().replace("×", "x")
        return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", x)).strip("-")
    # documented slug alias: static page uses the '12y' abbreviation of '12 ans'
    PAGE_ALIASES = {"chivas-regal-12-ans-70cl": "chivas-regal-12y-70cl"}
    CAT_SUFFIXES = ["shisha", "cigares", "cigarettes", "seau", "potvol", "pot",
                    "rouler", "pipe", "whisky", "vodka", "rhum", "gin", "anises",
                    "bieres", "energie", "softs"]
    by_slug = {}
    for r in rows:
        nm = r.get("name") or ""
        # the page generator was inconsistent about apostrophes
        # ("Ballantine's" -> ballantines, but "Mehari's" -> mehari-s): index both
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
        main = re.search(r'<div class="imgbox"><img src="([^"]+)"', open(p, encoding="utf-8").read())
        s = open(p, encoding="utf-8").read()
        main = re.search(r'<div class="imgbox"><img src="([^"]+)"', s)
        og = re.search(r'<meta property="og:image" content="([^"]+)"', s)
        if not main:
            fail(f"{rel}: no imgbox image")
        elif main.group(1) != "../" + want:
            fail(f"{rel}: page image {main.group(1)} != catalogue {want}")
        if og and og.group(1) != "https://tabacluxe.lu/" + want.replace(".webp", ".jpg"):
            fail(f"{rel}: og:image mismatch vs catalogue {want}")
    print(f"product pages matched to catalogue rows: {matched}, unmatched: {unmatched}")
    print(f"supabase products checked: {len(rows)}")
except Exception as e:
    fail(f"supabase check unreachable: {e}")

if errors:
    print(f"FAIL — {len(errors)} problems")
    for e in errors[:60]:
        print("  ", e)
    sys.exit(1)
print(f"PASS — 541 pages + en landing page, rodange-free, images present and correct, sitemap complete")
sys.exit(0)
