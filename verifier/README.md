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
