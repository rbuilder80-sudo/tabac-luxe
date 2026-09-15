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

def brand_name(name):
    words = str(name or "Tabac Luxe").strip().split()
    if len(words) > 1 and words[0].lower() == "the":
        return " ".join(words[:2])
    return words[0] if words else "Tabac Luxe"

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
    brand = p["name"].split()[0]
    return ", ".join(dict.fromkeys([
        p["name"], brand, catdisp, "Tabac Luxe", "Luxembourg",
        "tabac Luxembourg", "cigares Luxembourg", "shisha Luxembourg",
        "prix tabac Luxembourg", "frontiere Belgique Luxembourg"
    ]))

def render(tpl, p, related):
    cat    = p["category"]
    catdisp = CATDISP.get(cat, cat.title())
    price  = fmt(p["price_eur"])
    img    = image_url(p)
    desc   = (f"Buy {p['name']} at Tabac Luxe, Route de Longwy 549, "
              f"Luxembourg. {catdisp} at €{price}")
    unitdiv = ""
    if p.get("unit_price"):
        desc += f" (€{fmt(p['unit_price'])}/{p['unit']})"
        unitdiv = (f'<div class="unit">Unit price: €{fmt(p["unit_price"])} '
                   f'/ {p["unit"]} · £{fmt(p["price_gbp"])}</div>')
    desc += (". Order on WhatsApp, pay in store. "
             "Mon–Fri 6:00–18:00, Sat 8:00–17:00.")
    import html as _h
    esc = lambda s: _h.escape(s, quote=True)
    rel = "".join(
        f'<a class="rcard" href="{q["slug"]}.html"><div class="ri">'
        f'<img src="{display_image_url(image_url(q))}" alt="{esc(q["name"])} at Tabac Luxe" loading="lazy"></div>'
        f'<div class="rn">{esc(q["name"])}</div><div class="rp">€{fmt(q["price_eur"])}</div></a>'
        for q in related)
    return (tpl.replace("{{ENAME}}", esc(p["name"])).replace("{{EDESC}}", esc(desc))
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

