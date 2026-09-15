# Tabac Luxe — Rodange, Luxembourg

Luxury tobacco & spirits boutique website for Tabac Luxe, Route de Longwy 549, L-4832 Rodange.

## Stack
- Single-file SPA (`index.html`) — vanilla JS, hash routing, 5 languages (FR · DE · EN · PT · LB), age gate
- Backend: Supabase (products catalogue, promos, admin) — public read key, data fetched client-side
- `product/page.html?p=<slug>` — dynamic product detail view (Supabase-driven, same layout as the static SEO pages)
- `build/template.html` + `build/generate_product_pages.py` — regenerates all **516 static SEO product pages** (`product/<slug>.html`: unique meta, canonical, OG/Twitter cards, JSON-LD Product + BreadcrumbList, WhatsApp CTA, related products) with one command:
  ```
  python3 build/generate_product_pages.py
  ```
- `product/style.css` — shared stylesheet for all product pages
- `sitemap.xml` / `robots.txt` — canonical base https://tabacluxe.lu
- `data/price_list.json` — full price list (503 items, 8 categories)
- Images served from Supabase Storage (`site-assets` bucket): 435 Luxembourg pack shots, brand photos, brand-name cards
- `verifier/` — automated QA suites (content, SEO, performance budgets) + Playwright smoke tests

## Local preview
Serve this folder with any static server, e.g. `python3 -m http.server`, then open `http://localhost:8000/`.
