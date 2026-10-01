#!/usr/bin/env python3
"""One-shot: insert the 14 restored doorway URLs into sitemap.xml after the
en/wholesale-tobacco-luxembourg entry. Deterministic; aborts on any mismatch."""
import sys

pairs = [
    ("https://tabacluxe.lu/en/cheapest-cigarettes-luxembourg/", "Cheapest Cigarettes in Luxembourg"),
    ("https://tabacluxe.lu/en/cigarette-wholesalers-luxembourg/", "Cigarette Wholesalers Luxembourg"),
    ("https://tabacluxe.lu/en/flandria-tobacco-50g-luxembourg/", "Flandria Tobacco 50g Luxembourg"),
    ("https://tabacluxe.lu/en/luxembourg-tobacco-prices/", "Luxembourg Tobacco Prices"),
    ("https://tabacluxe.lu/en/tobacco-luxembourg/", "Tobacco in Luxembourg"),
    ("https://tabacluxe.lu/en/tobacco-shop-luxembourg/", "Tobacco Shop Luxembourg"),
    ("https://tabacluxe.lu/en/turner-50g-luxembourg/", "The Turner 50g Luxembourg"),
    ("https://tabacluxe.lu/fr/bureau-de-tabac-luxembourg/", "Bureau de Tabac Luxembourg"),
    ("https://tabacluxe.lu/fr/cigarette-winston-luxembourg-prix/", "Cigarette Winston Luxembourg Prix"),
    ("https://tabacluxe.lu/fr/prix-cigarette-luxembourg/", "Prix Cigarette Luxembourg"),
    ("https://tabacluxe.lu/fr/prix-tabac-a-rouler-luxembourg/", "Prix Tabac a Rouler Luxembourg"),
    ("https://tabacluxe.lu/fr/prix-tabac-luxembourg/", "Prix Tabac Luxembourg"),
    ("https://tabacluxe.lu/fr/tabac-luxembourg-frontiere/", "Tabac Luxembourg Frontiere"),
    ("https://tabacluxe.lu/fr/tabac-luxembourg-ouvert-actuellement/", "Tabac Luxembourg Ouvert Actuellement"),
]

xml = open("sitemap.xml", encoding="utf-8").read()
n = xml.count("<url>")
if n != 542:
    sys.exit(f"unexpected url count {n}")

blocks = []
for url, title in pairs:
    if url in xml:
        sys.exit(f"already present: {url}")
    blocks.append(
        "<url>\n"
        f"<loc>{url}</loc><lastmod>2026-10-01</lastmod><changefreq>monthly</changefreq><priority>0.7</priority>\n"
        f"<image:image><image:loc>https://tabacluxe.lu/assets/hero/boutique.jpg</image:loc><image:title>{title}</image:title></image:image>\n"
        "</url>\n"
    )

anchor = ("<loc>https://tabacluxe.lu/en/wholesale-tobacco-luxembourg/</loc>"
          "<lastmod>2026-10-01</lastmod><changefreq>monthly</changefreq><priority>0.7</priority>\n"
          "<image:image><image:loc>https://tabacluxe.lu/assets/hero/boutique.jpg</image:loc>"
          "<image:title>Tobacco Wholesalers Luxembourg</image:title></image:image>\n</url>\n")
if anchor not in xml:
    sys.exit("anchor not found")
xml = xml.replace(anchor, anchor + "".join(blocks), 1)

if xml.count("<url>") != 556:
    sys.exit("post-insert count mismatch")
open("sitemap.xml", "w", encoding="utf-8").write(xml)
print("sitemap now has 556 urls")
