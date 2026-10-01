# v16 — restored SEO landing page

## Trigger
`/en/wholesale-tobacco-luxembourg/` returned 404 after the 2026-09-30 doorway-page
cleanup, despite holding a first-page Google ranking. Restored on 2026-10-01 with all
ranking-critical elements preserved byte-for-byte (title, meta description, canonical,
H1, body copy, WebPage + FAQPage JSON-LD, GA tag).

## Changes vs v15
- Page count for the core gate unchanged (541 root/category/product pages).
- Sitemap gains one URL (542 total): `https://tabacluxe.lu/en/wholesale-tobacco-luxembourg/`
  with lastmod 2026-10-01 to prompt re-crawl.
- New dedicated checks for the restored page (`v16/check.py`):
  exists; exactly one h1; title 30-65 chars; description 120-165 chars;
  self-referencing canonical; no reference to deleted `/styles.css`;
  every internal link resolves to an existing file; valid JSON-LD; rodange-free
  (site-wide sweep carried from v14/v15).

## Dead-link repairs vs the deleted original
- Removed `<link rel="stylesheet" href="/styles.css?...">` (file retired; inline styles
  already cover the layout).
- Nav and "Related pages" links repointed from deleted en/fr doorway URLs to live
  targets: `/category/`, `/price-list.html`, `/promotions.html`, `/contact.html`,
  `/category/cigarettes.html`, `/category/rouler.html`.

## Gate
`python3 verifier/v16/check.py` — must print PASS before any handoff.
