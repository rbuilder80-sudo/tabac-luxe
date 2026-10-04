# Verifier v19 — Mobile hardening + 100% on-page SEO + CDN image hosting

**Trigger:** User report (2026-10-04) — on mobile phones the site layout/listing images
did not match PC, and product images needed two taps; plus the requirement that every
page scores 100% on-page SEO and the site is maximally search- and AI-crawler-friendly.

## Audit findings (live site, 2026-10-04)

1. **All images 404 on tabacluxe.lu.** The repo contained only 6 asset files; the
   1,080 referenced images (23 MB under `assets/`) existed only in the build
   environment. PC looked fine only because the preview serves local files / cache.
2. **8 category pages 404 live** (cigarettes, shisha, cigares, pot, potvol, rouler,
   seau, index) — never deployed; `llms-full.txt` missing too.
3. **Mobile double-tap:** all 556 pages had unguarded `:hover` rules — on iOS the
   first tap only applies hover, the second tap navigates.
4. **CLS risk:** 534 pages had `<img>` without `width`/`height`.
5. 15 doorway pages lacked Twitter cards; no favicon; no CDN preconnect.

## Fixes applied

- Uploaded all 1,081 assets (1,080 images + price-list PDF) to Supabase Storage
  bucket `site-assets` (public, `Cache-Control: max-age=31536000, immutable`),
  same relative paths. Verified: 1,081 objects, 26 MB, public URLs 200.
- Rewrote every asset reference in all 556 pages to
  `https://ujmblinyxfjvpntfkohz.supabase.co/storage/v1/object/public/site-assets/...`
  and updated all 516 `products.image` rows in Supabase to the CDN URLs.
- Wrapped every `:hover` rule in `@media(hover:hover) and (pointer:fine)` and added
  `touch-action:manipulation` — fixes the iOS double-tap.
- Injected `width`/`height` (from the actual image files) + `decoding="async"` into
  every static `<img>` (CLS-safe). SPA templates exempt (fixed-height containers).
- Added Twitter cards (15 doorway pages), SVG favicon, and Supabase preconnect
  site-wide.
- Mobile listing density: 2-column product grid at ≤560px on category pages and SPA.
- Regenerated `sitemap.xml`: 556 URLs, `lastmod` 2026-10-04, `image:image` entries.
- `robots.txt` already explicitly allows Google-Extended, GPTBot, OAI-SearchBot,
  ClaudeBot, PerplexityBot etc. (verified).

## Gate

`python3 verifier/v19/check.py` — must print PASS before any handoff. Covers all v18
rules plus: CDN-only asset refs with local-source mapping, hover guards, twitter card,
favicon, preconnect, img dims, sitemap lastmod+images, Supabase catalogue consistency.

**Any new page** must use the CDN asset base URL above, carry the standard head
furniture (canonical, description, OG+Twitter, JSON-LD, favicon, preconnect), guard
hover rules, dimension its images and include the WhatsApp button — v19 fails otherwise.
