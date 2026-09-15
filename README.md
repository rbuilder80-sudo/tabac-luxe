# Tabac Luxe — Rodange, Luxembourg

Luxury tobacco & spirits boutique website for Tabac Luxe, Route de Longwy 549, L-4832 Rodange.

## Stack
- Single-file SPA (`index.html`) — vanilla JS, hash routing, 5 languages (FR · DE · EN · PT · LB), age gate
- Backend: Supabase (products catalogue, promos, admin)
- `product/<slug>.html` — 516 static SEO product pages (unique meta, JSON-LD Product + BreadcrumbList, WhatsApp CTA, related products), sharing `product/style.css`
- `sitemap.xml` / `robots.txt` — canonical base https://tabacluxe.lu
- `data/price_list.json` — full price list (503 items, 8 categories)
- Images served from Supabase Storage (`site-assets` bucket): Luxembourg pack shots, brand photos, brand-name cards
- `verifier/` — automated QA suites (content, SEO, performance budgets) + smoke tests

## Local preview
Serve this folder with any static server, e.g. `python3 -m http.server`.
