# Tabac Luxe — tabacluxe.lu

Showcase website for Tabac Luxe, the premium tobacco and spirits shop in Luxembourg.

## Architecture

- `index.html` — self-contained single-page app (hash routing: home, catalogue, promotions, price list, contact, cart, legal, admin). Five languages (FR default, DE, EN, PT, LB). Product data is loaded live from Supabase (`products`, `promotions` tables); the publishable anon key is public by design.
- `product/*.html` — 516 individually crawlable static product pages (JSON-LD Product + Offer + BreadcrumbList, canonical, OG/Twitter).
- `category/*.html` — 17 static category pages.
- Root utility pages — promotions, price list, contact, terms, privacy, disclaimer, legal notice.
- `sitemap.xml` — 541 URLs with image entries. `robots.txt` — explicit Allow rules for search and AI crawlers. `llms.txt` / `llms-full.txt` — AI-readable site guides.
- `assets/` — WebP images (JPG originals retained; og:image stays JPG for crawler compatibility).
- `verifier/` — versioned acceptance criteria and audit scripts (static SEO audit of all 541 pages, headless-browser crawl of every URL and image). Results logged append-only in `verifier/runs/`. Current gate: 100%.

## Version manifest

| Version | Date | Highlights |
|---|---|---|
| v15 | 2026-10-01 | Full pre-launch certification: 1,082 HTTP targets, 552 browser pages/routes, 3,342 images checked — 0 errors, score 100.0; fixed `/#/tarifs` 390px mobile overflow (`.pl-scroll` wrapper); GitHub repush |
| v14 | 2026-10-01 | Town name "Rodange" removed site-wide (545 files, 11,361 occurrences, 5-language aware); sitemap regenerated; zero-match gate |
| v13 | 2026-10-01 | WebP conversion (539 assets, ~48% smaller), mobile design pass (0px overflow), home Reviews + FAQ sections in 5 languages |
| v12 | 2026-09-30 | Unified dark luxury theme across all 541 pages, catalogue toolbar, 61 placeholder images replaced with brand logos |
| v11.1 | 2026-09-15 | Product-card image/click fix (CSS grid max-height bug) |
| v11 | 2026-09-15 | Street address and telephone removed site-wide |
| v10 | 2026-09-15 | Pre-launch SEO gate at 100%, handoff-ready |

## Repository sync status (2026-10-01)

This repo mirrors the production site (live version `ec21571`) as far as the text-only sync channel allows.

**Mirrored and SHA-verified (repo blob hash == local `git hash-object`):**

- `index.html` (`9b226fcf…`, includes the price-list mobile overflow fix), `robots.txt`, `llms.txt`, `logo.svg`, `.nojekyll`, `CNAME`
- `sitemap.xml` (`ed06e807…`, 180,110 B — full Rodange-free sitemap with image entries)
- Root utility pages: `promotions.html`, `contact.html`, `terms.html`, `privacy.html`, `disclaimer.html`, `legal-notice.html`
- Category pages: `anises`, `bieres`, `energie`, `gin`, `pipe`, `rhum`, `softs`, `vodka`, `whisky` — all byte-identical
- `verifier/` suite (v10–v15) including audit scripts and run logs
- `data/price_list.json` — content byte-identical; repo copy carries one extra trailing newline (verified: repo sha == hash(local + "\n"))

**Removed as stale (2026-10-01):** `app.js`, `styles.css`, `sitemap-seo.xml`, `build/` (old generator), `product/page.html`, `product/style.css`, and 15 superseded `en/`/`fr/` doorway pages.

**Not mirrored through this channel:**

- `llms-full.txt` (110 KB) — text-channel volume limit; local hash `3c12cd964995…`. The repo copy is an older revision.
- 8 minified pages with >2000-char lines (`price-list.html`, `category/{cigarettes,cigares,shisha,seau,rouler,pot,potvol,index}.html`) — cannot be transported losslessly line-wise.
- 516 `product/*.html` pages (~7 MB) — volume-infeasible one file at a time; the repo keeps the previous-generation product pages for reference.
- All binary assets (`assets/`, 29 MB of WebP/JPG) — text-only channel.

A full byte-exact mirror (including binaries) requires one `git push` with a Personal Access Token from a machine holding the production tree.

## Legal

Showcase only — no online sales, no shipping. Tobacco and alcohol sales are restricted to adults (18+).
