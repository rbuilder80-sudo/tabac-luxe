#!/usr/bin/env python3
"""Regenerate all static SEO product pages (product/<slug>.html) for Tabac Luxe.

Fetches the live catalogue from Supabase and renders build/template.html
once per product. Usage:  python3 build/generate_product_pages.py
"""
import json, os, sys, urllib.request
import re
from urllib.parse import quote

SUPA_URL = "https://ujmblinyxfjvpntfkohz.supabase.co"
SUPA_KEY = "sb_publishable_O65H3nPdVW5tA-ZZ7HoiVw_gI9M-iDr"  # public read-only key
STORAGE  = SUPA_URL + "/storage/v1/object/public/site-assets/"

CATDISP = {"shisha":"Shisha Tobacco","cigarettes":"Cigarettes","cigares":"Cigars",
 "seau":"Tobacco Bucket","potvol":"Tobacco Tin High Volume","rhum":"Rum",
 "pot":"Tobacco Tin","rouler":"Rolling Tobacco","pipe":"Pipe Tobacco",
 "whisky":"Whisky","vodka":"Vodka","bieres":"Beer","gin":"Gin",
 "anises":"Anisette","energie":"Energy Drinks","softs":"Soft Drinks"}

TOBACCO_CATS = {"cigarettes", "rouler", "seau", "pot", "potvol", "pipe"}
TOBACCO_SEO = {
    "cigarettes": {
        "noun": "cigarettes",
        "buy": "buy cigarettes in Luxembourg",
        "price": "cigarette prices Luxembourg",
        "list": "Luxembourg cigarette price list",
        "format": "carton cigarettes Luxembourg",
        "h2": "More cigarette prices in Luxembourg",
    },
    "rouler": {
        "noun": "rolling tobacco",
        "buy": "buy rolling tobacco in Luxembourg",
        "price": "rolling tobacco prices Luxembourg",
        "list": "Luxembourg rolling tobacco price list",
        "format": "50g rolling tobacco Luxembourg",
        "h2": "More rolling tobacco prices in Luxembourg",
    },
    "seau": {
        "noun": "tobacco bucket",
        "buy": "buy tobacco buckets in Luxembourg",
        "price": "tobacco bucket prices Luxembourg",
        "list": "Luxembourg tobacco bucket price list",
        "format": "large tobacco tubs Luxembourg",
        "h2": "More tobacco bucket prices in Luxembourg",
    },
    "pot": {
        "noun": "tobacco tin",
        "buy": "buy tobacco tins in Luxembourg",
        "price": "tobacco tin prices Luxembourg",
        "list": "Luxembourg tobacco tin price list",
        "format": "boxed tobacco Luxembourg",
        "h2": "More tobacco tin prices in Luxembourg",
    },
    "potvol": {
        "noun": "volume tobacco tin",
        "buy": "buy volume tobacco in Luxembourg",
        "price": "volume tobacco prices Luxembourg",
        "list": "Luxembourg volume tobacco price list",
        "format": "large volume tobacco Luxembourg",
        "h2": "More volume tobacco prices in Luxembourg",
    },
    "pipe": {
        "noun": "pipe tobacco",
        "buy": "buy pipe tobacco in Luxembourg",
        "price": "pipe tobacco prices Luxembourg",
        "list": "Luxembourg pipe tobacco price list",
        "format": "pipe tobacco pouch Luxembourg",
        "h2": "More pipe tobacco prices in Luxembourg",
    },
}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(ROOT, "product")
FORCE_LOGO_SLUGS = {"the-turner-original-50g-rouler"}
BRAND_LOGOS = {
    "agio": "assets/brand-logos/agio.svg",
    "the turner": "assets/brand-logos/the-turner.svg",
}

def fetch_products():
    url = (SUPA_URL + "/rest/v1/products?select=slug,name,category,price_eur,"
           "price_gbp,unit_price,unit,image&active=eq.true&order=slug")
    req = urllib.request.Request(url, headers={"apikey": SUPA_KEY,
                                               "Authorization": "Bearer " + SUPA_KEY})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def fmt(x):  # 17.9 -> "17.90"
    return f"{float(x):.2f}"

def title_case_product(name):
    small = {"and", "or", "the", "de", "du", "la", "le", "les", "y"}
    parts = []
    for i, word in enumerate(str(name or "").split()):
        if word.isupper() or any(ch.isdigit() for ch in word):
            parts.append(word)
        elif i and word.lower() in small:
            parts.append(word.lower())
        else:
            parts.append(word[:1].upper() + word[1:])
    return " ".join(parts)

def brand_name(name):
    words = str(name or "Tabac Luxe").strip().split()
    if len(words) > 1 and words[0].lower() == "the":
        return " ".join(words[:2])
    return words[0] if words else "Tabac Luxe"

def product_tokens(name):
    text = str(name or "")
    weights = re.findall(r"\b\d+(?:[,.]\d+)?\s?(?:g|kg|cl|ml)\b", text, re.I)
    counts = re.findall(r"\b\d+\s*/\s*\d+\b|\b\d+\s*x\s*\d+\b|\b\d+\s?(?:sticks?|cigares?|cigarettes?)\b", text, re.I)
    variants = []
    for word in re.findall(r"[A-Za-zÀ-ÿ0-9']+", text):
        if word.lower() not in {"g", "kg", "cl", "ml"} and len(word) > 2:
            variants.append(word)
    return {
        "weights": [w.replace(" ", "") for w in weights],
        "counts": [c.replace(" ", "") for c in counts],
        "variants": variants[:5],
    }

def seo_title(p, catdisp):
    name = title_case_product(p["name"])
    cat = p["category"]
    price = fmt(p["price_eur"])
    if cat == "cigarettes":
        return fit_text(f"{name} Cigarettes €{price} | Luxembourg Prices", 75)
    if cat in {"rouler", "seau", "pot", "potvol", "pipe"}:
        noun = TOBACCO_SEO[cat]["noun"].title()
        return fit_text(f"{name} {noun} €{price} | Tabac Luxembourg", 75)
    return fit_text(f"{name} — €{price} | Tabac Luxe Luxembourg", 75)

def fit_text(text, limit):
    if len(text) <= limit:
        return text
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    cut = text[:limit - 1].rsplit(" ", 1)[0].rstrip(" ,-|")
    return cut or text[:limit - 1]

def h1_text(p, catdisp):
    name = title_case_product(p["name"])
    cat = p["category"]
    if cat == "cigarettes":
        return f"{name} Cigarettes"
    if cat in TOBACCO_SEO:
        return f"{name} {TOBACCO_SEO[cat]['noun'].title()}"
    return name

def seo_description(p, catdisp):
    cat = p["category"]
    name = title_case_product(p["name"])
    brand = brand_name(p["name"])
    price = fmt(p["price_eur"])
    unit = ""
    if p.get("unit_price"):
        unit = f" (€{fmt(p['unit_price'])}/{p['unit']})"
    if cat in TOBACCO_SEO:
        data = TOBACCO_SEO[cat]
        return fit_text(
            f"{name} {data['noun']} in Luxembourg: €{price}{unit}. "
            f"Compare {brand} prices at Tabac Luxe. WhatsApp order, in-store collection. Adults 18+ only.",
            178,
        )
    return (f"Buy {name} at Tabac Luxe, Route de Longwy 549, Luxembourg. "
            f"{catdisp} at €{price}{unit}. Order on WhatsApp, pay in store. "
            "Mon-Fri 6:00-18:00, Sat 8:00-17:00.")

def category_cta(cat, catdisp):
    if cat in TOBACCO_SEO:
        return TOBACCO_SEO[cat]["list"]
    return f"More {catdisp}"

def related_h2(p, catdisp):
    cat = p["category"]
    brand = brand_name(p["name"])
    if cat in TOBACCO_SEO:
        noun = TOBACCO_SEO[cat]["noun"]
        label = "cigarette" if noun == "cigarettes" else noun
        return f"More {brand} {label} prices in Luxembourg"
    return "You may also like"

def norm(s):
    return re.sub(r"[^a-z0-9]+", "", str(s or "").lower())

def image_matches_product(p):
    if not p.get("image") or p.get("slug") in FORCE_LOGO_SLUGS:
        return False
    return norm(brand_name(p["name"])) in norm(p["image"])

def brand_logo_url(name):
    brand = brand_name(name)[:28]
    logo = BRAND_LOGOS.get(brand.lower())
    if logo:
        return "https://tabacluxe.lu/" + logo
    initials = "".join(w[0] for w in brand.split())[:3].upper() or "TL"
    import html as _h
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600">'
           f'<rect width="600" height="600" rx="24" fill="#faf8f4"/>'
           f'<rect x="36" y="36" width="528" height="528" rx="18" fill="#fff" stroke="#d9c08a" stroke-width="10"/>'
           f'<text x="300" y="280" font-family="Georgia,serif" font-size="118" font-weight="700" fill="#b08d3e" text-anchor="middle">{_h.escape(initials)}</text>'
           f'<text x="300" y="370" font-family="Arial,sans-serif" font-size="44" font-weight="700" fill="#2b2620" text-anchor="middle">{_h.escape(brand)}</text>'
           f'<text x="300" y="430" font-family="Arial,sans-serif" font-size="25" letter-spacing="5" fill="#6d6353" text-anchor="middle">TABAC LUXE</text>'
           f'</svg>')
    return "data:image/svg+xml;charset=UTF-8," + quote(svg, safe="")

def display_image_url(url):
    if url.startswith("https://tabacluxe.lu/assets/"):
        return "../" + url.replace("https://tabacluxe.lu/", "")
    return url

def image_url(p):
    path = p.get("image")
    if not image_matches_product(p):
        return brand_logo_url(p.get("name", "Tabac Luxe"))
    if str(path).startswith(("http://", "https://")):
        return path
    return STORAGE + str(path).lstrip("/")

def keywords(p, catdisp):
    name = title_case_product(p["name"])
    brand = brand_name(p["name"])
    cat = p["category"]
    tokens = product_tokens(name)
    base = [
        name,
        f"{name} price",
        f"{name} Luxembourg",
        f"{brand} Luxembourg",
        brand,
        catdisp,
        "Tabac Luxe",
        "Luxembourg",
    ]
    if cat in TOBACCO_SEO:
        data = TOBACCO_SEO[cat]
        base += [
            data["buy"],
            data["price"],
            data["list"],
            data["format"],
            f"{brand} {data['noun']}",
            f"{brand} {data['noun']} Luxembourg",
            f"{brand} {data['noun']} price",
            f"{brand} tabac Luxembourg",
            "tabac Luxembourg prices",
            "tobacco shop Luxembourg",
            "Luxembourg tobacco prices",
            "frontiere Belgique Luxembourg tabac",
        ]
        for w in tokens["weights"]:
            base += [
                f"{brand} {w}",
                f"{brand} {w} Luxembourg",
                f"{data['noun']} {w} price",
            ]
        for c in tokens["counts"]:
            base += [
                f"{brand} {c}",
                f"{brand} {c} Luxembourg",
                f"{data['noun']} {c} price",
            ]
    else:
        base += [
            "tabac Luxembourg",
            "cigares Luxembourg",
            "shisha Luxembourg",
            "prix tabac Luxembourg",
            "frontiere Belgique Luxembourg",
        ]
    return ", ".join(dict.fromkeys([x for x in base if x and len(x) <= 80]))

def render(tpl, p, related):
    cat    = p["category"]
    catdisp = CATDISP.get(cat, cat.title())
    price  = fmt(p["price_eur"])
    img    = image_url(p)
    desc   = seo_description(p, catdisp)
    unitdiv = ""
    if p.get("unit_price"):
        unitdiv = (f'<div class="unit">Unit price: €{fmt(p["unit_price"])} '
                   f'/ {p["unit"]} · £{fmt(p["price_gbp"])}</div>')
    import html as _h
    esc = lambda s: _h.escape(s, quote=True)
    rel = "".join(
        f'<a class="rcard" href="{q["slug"]}.html"><div class="ri">'
        f'<img src="{display_image_url(image_url(q))}" alt="{esc(q["name"])} at Tabac Luxe" loading="lazy"></div>'
        f'<div class="rn">{esc(q["name"])}</div><div class="rp">€{fmt(q["price_eur"])}</div></a>'
        for q in related)
    return (tpl.replace("{{ENAME}}", esc(title_case_product(p["name"]))).replace("{{EDESC}}", esc(desc))
        .replace("{{SEO_TITLE}}", esc(seo_title(p, catdisp)))
        .replace("{{H1}}", esc(h1_text(p, catdisp)))
        .replace("{{CATEGORY_CTA}}", esc(category_cta(cat, catdisp)))
        .replace("{{RELATED_H2}}", esc(related_h2(p, catdisp)))
        .replace("{{ECATDISP}}", esc(catdisp))
        .replace("{{NAME}}", p["name"]).replace("{{SLUG}}", p["slug"])
        .replace("{{CATKEY}}", cat).replace("{{CATDISP}}", catdisp)
        .replace("{{PRICENUM}}", repr(float(p["price_eur"]))).replace("{{PRICE}}", price)
        .replace("{{IMG}}", img).replace("{{IMG_SRC}}", display_image_url(img)).replace("{{BRAND}}", p["name"].split()[0])
        .replace("{{KEYWORDS}}", esc(keywords(p, catdisp)))
        .replace("{{UNITDIV}}", unitdiv).replace("{{DESC}}", desc)
        .replace("{{RELATED}}", rel))

def main():
    tpl = open(os.path.join(ROOT, "build", "template.html"), encoding="utf-8").read()
    products = fetch_products()
    os.makedirs(OUT, exist_ok=True)
    for p in products:
        related = [q for q in products
                   if q["category"] == p["category"] and q["slug"] != p["slug"]][:4]
        html = render(tpl, p, related)
        with open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
    print(f"generated {len(products)} product pages into product/")

if __name__ == "__main__":
    sys.exit(main())

