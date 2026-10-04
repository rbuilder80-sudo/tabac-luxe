# Verifier index

## v1 — 2026-09-15
Acceptance criteria for the Luxembourg B2B trade site (single-file HTML package):

1. `index.html` exists in `/mnt/agents/output/app/` and is self-contained apart from local `assets/products/*` images and Google Fonts CDN.
2. Every product listing references a real image file that exists on disk (>= 12 products).
3. Five languages implemented (fr, de, en, pt, lb) with persisted selection; FR default.
4. Hash routing with routes: home (#/), catalogue (#/catalogue), trade application (#/trade), cart (#/cart).
5. Trade gate: catalogue prices hidden and ordering blocked until trade access verified; demo account entry unlocks; persisted.
6. Cart: localStorage persistence, quantity steppers, MOQ display, totals.
7. WhatsApp ordering: wa.me link with prefilled message including cart lines and company/VAT details; floating WhatsApp button on all views.
8. Trade application form with verification-success flow.
9. noindex meta present.
10. Page loads without JS errors (checked via headless browser), catalogue gate works, add-to-cart works.

Method: `verifier/check.py` runs static checks; headless Chromium smoke test via `verifier/smoke.py`. Results appended to `verifier/runs/`.

## v2 — 2026-09-15
Redesign per client request: light luxury palette (ivory/champagne-gold), catalogue mirrors realdelux.lu (categories, products, real pricing where published). Changes vs v1:
- Gourmet catalogue replaced by border-shop catalogue: bières, whisky, rhum, vodka, gin, anisés, alcopop, énergisants, soft drinks, cigarettes, shisha.
- Prices: real realdelux.lu prices for drinks; tobacco/shisha prices legally gated ("price via WhatsApp"), matching the reference site's behaviour.
- Trade gate replaced by 18+ age gate (legal requirement for alcohol/tobacco).
- Still required: 5 languages (fr default, de, en, pt, lb), hash routing, cart with localStorage + steppers + totals, WhatsApp ordering with prefilled message, noindex, all 16 product images exist on disk, no JS errors, smoke test passes (age gate → catalogue → add → cart → wa.me).
- New: hero uses light background; verifier checks absence of the old dark palette (--bg:#171512).


## v3 — Tabac Luxe (Supabase backend, 503-item price list, legal pages, admin, generated heroes)
- check.py: brand, hours, 5 langs, routes, supabase wiring, legal x4, images, 503 items, PDF, admin
- smoke.py: age gate, hero, 8 cats, featured carousel, cart, price list 503 rows, privacy page, admin 516 rows, EN switch

## v4 — SEO product pages + 100% real-image coverage
- check.py: 516 products, image field set for all, image files exist, 516 static product pages,
  full SEO audit per page (title/description/canonical/OG/Twitter/JSON-LD Product+Offer/WA CTA),
  sitemap coverage, robots.txt, index LocalBusiness JSON-LD + OG + card links to product pages
- smoke.py: SPA home renders 8 featured cards with 0 broken images / 0 JS errors;
  static product page renders h1, real image, JSON-LD, canonical, WhatsApp CTA
- brand library: 40 brand photos in assets/brands/ + 30 product photos in assets/products/;
  category-level branded fallbacks guarantee 100% coverage

## v5 — BreadcrumbList rich results
- check.py: v4 audit + requires "@type": "BreadcrumbList" JSON-LD on every product page (Google breadcrumb rich-result eligibility)
- smoke.py: unchanged from v4

## v6 — Luxembourg-only images, category audit, clickable products, designer product pages
- Catalogue reduced 516 -> 441: 75 listings removed because no genuine Luxembourg-market
  pack shot exists (source of truth: tabac-lux.lu + tabasprix.lu WooCommerce catalogs, 2041 LU products)
- check.py: v5 audit + all tobacco images must be assets/lu/ (LU pack shots), category
  weight/pack consistency audit, no stale product pages, price_list.json has no removed
  products, SPA cards clickable via openProduct() with working Add-to-cart
- smoke.py: age gate bypassed via sessionStorage; clicks a real product card and asserts
  navigation to its static page (image, 2x JSON-LD, breadcrumbs); related-products strip
  verified on a multi-item category page
- product pages redesigned (Cormorant Garamond/Jost, gold frame, related-products strip,
  visible breadcrumbs) and price_list.json regenerated from the 441-product catalogue (428 rows)

## v7 — full 516 catalogue restored + performance pass
- 75 previously-removed listings restored with brand images: real brand photo where available
  (25), elegant generated brand-name cards otherwise (50; 19 unique cards in assets/brands/name-*.jpg)
- image policy now: LU pack shot (435) > real brand/product photo (60+21) > brand-name card
- check.py: v6 audit + 516 count, image policy accounting, price list back to 503 rows,
  performance budgets (hero < 500KB, no heavy PNG, fetchpriority, lazy+async imgs, LU shots < 200KB)
- speed: hero-main.png 3.2MB -> hero-main.jpg 381KB, cigars.png 1.7MB -> 127KB,
  decoding=async on catalogue images, fetchpriority=high on hero

## v9 — 2026-09-15
Pre-launch 99% on-page SEO and rendering gate. Adds full-page title/meta length and uniqueness checks,
rendered H1 checks for SPA routes, static category-index coverage, OG/Twitter image-alt metadata,
AI crawler/llms.txt checks, sitemap image validation, local HTTP crawl of every sitemap URL/image,
and browser image-visibility checks. Also captures the fix for catalogue images being hidden by
reveal animation timing: reveal content is visible by default and the first catalogue images are eager-loaded.
See `verifier/v9/README.md` for the full acceptance criteria.

## v10 — 2026-09-15
Final pre-launch gate after adding crawlable static utility pages (promotions, price list, contact,
terms, privacy, disclaimer and legal notice). The audit surface becomes 541 HTML pages plus the XML
sitemap, robots.txt and AI-readable files. v10 keeps all v9 checks and adds static utility-page schema,
link and browser-render coverage. See `verifier/v10/README.md`.

## v11 — 2026-09-15T15:11:20Z
- Owner request: removed street address (Route de Longwy 549, L-4832) and telephone (+352 28 77 79 96) from all pages, schema, meta and llms files.
- geo.position/ICBM coordinates also removed; WhatsApp ordering links retained (number only inside wa.me URLs).
- See v11/README.md for updated acceptance criteria.

## v11.1 — 2026-09-15
- UX fix: product-card images in grid containers used max-height:100% (cyclic percentage in grid -> unresolved), causing images to render at natural height, overlap neighbouring cards and intercept taps. Fixed with explicit max-height in index.html (.pimg img) and all 17 static category pages (.pcard .im img).
- http_audit.py: human-like viewport-step scrolling, decode retry loop, evaluate timeouts, progress logging.

## v12 — 2026-09-30T21:40:03Z
- Unified professional theme: dark luxury header + rich footer across all 541 pages; catalogue toolbar with search/sort/chips; 61 placeholder product images replaced with brand logos/tiles.

## v13 — 2026-10-01T06:00:00Z
- Improvement bundle: WebP conversion (539 assets, ~48% smaller, og:image kept as JPG), mobile design pass (two-row header, 0px horizontal overflow verified), home Reviews section (3 testimonials) + visible FAQ section (5 Q&A matching FAQPage JSON-LD), all i18n keys in 5 languages, remaining hero JPG backgrounds switched to WebP.

## v14 — 2026-10-01
Remove town name "Rodange" site-wide (545 files, 11,361 occurrences; FR/DE/EN/PT/LB-aware). Gate: zero case-insensitive "rodange" in public files + all JSON-LD valid + no new legacy-check failures + live http audit 0 errors. Scripts: v14/apply.py (migration), v14/check.py (gate).

## v15 — 2026-10-01
Pre-launch full-site certification + GitHub repush of the Rodange-removal text changes. Carries the
v14 rodange sweep; adds per-page h1/title/description/JSON-LD gates on all 541 pages, image-existence
and Supabase-equality image-correctness checks (516 catalogue rows as source of truth), exact sitemap
coverage, browser audit with per-product-page layout assertions (visible .imgbox/.nm/.price/.cta) and
390px horizontal-overflow check on every page, and SHA-verified GitHub repush. See `verifier/v15/README.md`.

## v16 — 2026-10-01
Restore `/en/wholesale-tobacco-luxembourg/` (first-page Google ranking lost to the 2026-09-30 doorway
cleanup). Ranking-critical elements preserved byte-for-byte; dead stylesheet/ doorway links repaired;
sitemap gains the URL (542 total, lastmod 2026-10-01). Gate: v15 checks + dedicated en-landing checks.
See `verifier/v16/README.md`.

## v17 — 2026-10-01
Restore all 15 ranked doorway pages deleted in the 2026-09-30 cleanup (spreadsheet of first-page
Google keywords → 15 URLs, all 404). v16 restored one; v17 restores the remaining 14 (7 en + 7 fr)
from pre-deletion commit dc12bca4 at their exact original URLs. Ranking elements byte-for-byte;
only repair is removing the retired /styles.css link. Sitemap 542 → 556 (lastmod 2026-10-01).
Gate: v16 checks generalized to all 15 doorway pages. See `verifier/v17/README.md`.

## v18 — 2026-10-01
WhatsApp button on every page. Audit found 21 of 556 HTML pages without any wa.me link
(15 restored doorway pages + 6 utility pages). Fix: floating `.wafab` button (same design/SVG
as the SPA, self-contained inline style + hardcoded wa.me/35228777996 href, EN/FR greeting)
inserted before `</body>` on all 21; all other pages already expose WhatsApp (SPA floating
button, product/category "Order via WhatsApp" CTA). Gate: v17 checks + every HTML page must
contain a wa.me/ link — any future page without the button fails the gate.
See `verifier/v18/README.md`.

## v19 — 2026-10-04 — Mobile hardening + 100% on-page SEO + CDN image hosting
User report: mobile layout/listing images wrong vs PC, product image needed two taps;
requirement: 100% on-page score on every page, maximum search/AI-crawler friendliness.
Audit found ALL images 404 live (1,080 assets never deployed — repo had only 6 asset
files), 8 category pages 404 live, unguarded :hover on all 556 pages (iOS double-tap),
missing img width/height (CLS), missing twitter cards on 15 doorway pages, no favicon.
Fix: uploaded all 1,081 assets to Supabase Storage bucket `site-assets` (public,
immutable cache), rewrote every asset ref in all 556 pages + 516 Supabase product rows
to the CDN URL, guarded all hover rules (@media(hover:hover)), added touch-action,
injected img width/height + decoding, added twitter cards/favicon/preconnect site-wide,
2-col mobile listing grid, regenerated sitemap (556 urls, lastmod, image entries).
Gate: v18 checks + CDN-only asset refs + hover guard + twitter/favicon/preconnect +
img dims + sitemap lastmod/images. See `verifier/v19/README.md`.
