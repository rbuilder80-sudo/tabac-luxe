# Tabac Luxe — tabacluxe.lu

Showcase website for Tabac Luxe, the premium tobacco and spirits shop in Rodange, Luxembourg.

## Architecture

- `index.html` — self-contained single-page app (hash routing: home, catalogue, promotions, price list, contact, cart, legal, admin). Five languages (FR default, DE, EN, PT, LB). Product data is loaded live from Supabase (`products`, `promotions` tables); the publishable anon key is public by design.
- `product/*.html` — 516 individually crawlable static product pages (JSON-LD Product + Offer + BreadcrumbList, canonical, OG/Twitter).
- `category/*.html` — 17 static category pages.
- Root utility pages — promotions, price list, contact, terms, privacy, disclaimer, legal notice.
- `sitemap.xml` — 541 URLs with image entries. `robots.txt` — explicit Allow rules for search and AI crawlers. `llms.txt` / `llms-full.txt` — AI-readable site guides.
- `assets/` — WebP images (JPG originals retained; og:image stays JPG for crawler compatibility).
- `verifier/` — versioned acceptance criteria and audit scripts (`v11/check.py` static SEO audit of all 541 pages, `v11/http_audit.py` headless-browser crawl of every URL and image). Results logged append-only in `verifier/runs/`. Current gate: 100%.

## Version manifest

| Version | Date | Highlights |
|---|---|---|
| v13 | 2026-10-01 | WebP conversion (539 assets, ~48% smaller), mobile design pass (0px overflow), home Reviews + FAQ sections in 5 languages |
| v12 | 2026-09-30 | Unified dark luxury theme across all 541 pages, catalogue toolbar, 61 placeholder images replaced with brand logos |
| v11.1 | 2026-09-15 | Product-card image/click fix (CSS grid max-height bug) |
| v11 | 2026-09-15 | Street address and telephone removed site-wide |
| v10 | 2026-09-15 | Pre-launch SEO gate at 100%, handoff-ready |

## Legal

Showcase only — no online sales, no shipping. Tobacco and alcohol sales are restricted to adults (18+).
