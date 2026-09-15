#!/usr/bin/env python3
"""Regenerate all static SEO product pages (product/<slug>.html) for Tabac Luxe.

Fetches the live catalogue from Supabase and renders build/template.html
once per product. Usage:  python3 build/generate_product_pages.py
"""
import json, os, sys, urllib.request

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

def fetch_products():
    url = (SUPA_URL + "/rest/v1/products?select=slug,name,category,price_eur,"
           "price_gbp,unit_price,unit,image&active=eq.true&order=slug")
    req = urllib.request.Request(url, headers={"apikey": SUPA_KEY,
                                               "Authorization": "Bearer " + SUPA_KEY})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def fmt(x):  # 17.9 -> "17.90"
    return f"{float(x):.2f}"

def render(tpl, p, related):
    cat    = p["category"]
    catdisp = CATDISP.get(cat, cat.title())
    price  = fmt(p["price_eur"])
    img    = STORAGE + p["image"]
    desc   = (f"Buy {p['name']} at Tabac Luxe, Route de Longwy 549, Rodange, "
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
        f'<img src="{STORAGE + q["image"]}" alt="{esc(q["name"])}" loading="lazy"></div>'
        f'<div class="rn">{esc(q["name"])}</div><div class="rp">€{fmt(q["price_eur"])}</div></a>'
        for q in related)
    return (tpl.replace("{{ENAME}}", esc(p["name"])).replace("{{EDESC}}", esc(desc))
        .replace("{{ECATDISP}}", esc(catdisp))
        .replace("{{NAME}}", p["name"]).replace("{{SLUG}}", p["slug"])
        .replace("{{CATKEY}}", cat).replace("{{CATDISP}}", catdisp)
        .replace("{{PRICENUM}}", repr(float(p["price_eur"]))).replace("{{PRICE}}", price)
        .replace("{{IMG}}", img).replace("{{BRAND}}", p["name"].split()[0])
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
