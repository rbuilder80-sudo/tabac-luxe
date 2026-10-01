# v17 — restore all 15 ranked doorway pages

## Trigger
A spreadsheet of first-page Google rankings showed 15 keywords whose landing URLs
all returned 404 after the 2026-09-30 doorway-page cleanup. v16 restored the first
(`en/wholesale-tobacco-luxembourg`); v17 restores the remaining 14 (7 en + 7 fr)
from the last pre-deletion commit `dc12bca4653f1e96f4c4b080bcb48674ca518f89`, at
their exact original URLs (GitHub Pages cannot issue redirects, so the URL itself
carries the ranking).

## Restored pages (14, in addition to v16's one)
- en/cheapest-cigarettes-luxembourg
- en/cigarette-wholesalers-luxembourg
- en/flandria-tobacco-50g-luxembourg
- en/luxembourg-tobacco-prices
- en/tobacco-luxembourg
- en/tobacco-shop-luxembourg
- en/turner-50g-luxembourg
- fr/bureau-de-tabac-luxembourg
- fr/cigarette-winston-luxembourg-prix
- fr/prix-cigarette-luxembourg
- fr/prix-tabac-a-rouler-luxembourg
- fr/prix-tabac-luxembourg
- fr/tabac-luxembourg-frontiere
- fr/tabac-luxembourg-ouvert-actuellement

## Changes vs v16
- Ranking elements preserved byte-for-byte from the pre-deletion commit: title,
  meta description, robots meta, canonical, OG tags, H1, body copy, WebPage +
  FAQPage JSON-LD, GA tag G-VE6XGYJ7VP.
- Only repair: removed `<link rel="stylesheet" href="/styles.css?...">` (file
  retired; inline `<style>` block covers layout). No other content edits.
- Doorway cross-links (e.g. `/en/tobacco-luxembourg/`, `/fr/prix-tabac-luxembourg/`)
  kept as-is: all 15 pages exist again, so every link resolves.
- Sitemap gains 14 URLs (556 total), lastmod 2026-10-01, changefreq monthly,
  priority 0.7, to prompt re-crawl.
- `v17/check.py` extends the v16 single-page check to all 15 doorway pages:
  exists; exactly one h1; title 30-65 chars; description 120-165 chars;
  self-referencing canonical; robots index,follow; GA tag present; FAQPage
  JSON-LD present and valid; no `/styles.css` reference; rodange-free; every
  internal link resolves; page listed in sitemap. Core gate unchanged
  (541 root/category/product pages).

## Gate
`python3 verifier/v17/check.py` — must print PASS before any handoff.
