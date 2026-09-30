# Verifier v10 — Final pre-launch SEO, rendering and content audit

Created: 2026-09-15

v10 extends v9 after the crawlable utility pages were added. The audited crawlable surface is now 541 pages: the SPA entry point, 17 catalogue/category pages, 516 product pages, promotions, price list, contact and four legal/information pages.

## Acceptance criteria

1. Every crawlable HTML page exists locally, returns HTTP 200, and contains exactly one H1 in source or rendered state.
2. Every page has a unique title of 30–65 characters and a unique meta description of 120–165 characters.
3. Every page has a self-referencing absolute canonical URL, index/follow robots metadata, Open Graph title/description/URL/image/image-alt, Twitter card/title/description/image/image-alt, theme-color and local geo metadata.
4. Heading hierarchy contains no skipped levels on rendered primary routes and static pages.
5. Every JSON-LD block parses as JSON. Product pages include Product, Offer, price, currency, priceValidUntil, image, seller and BreadcrumbList. Category pages include CollectionPage, ItemList and BreadcrumbList. The index includes Store, WebSite and FAQPage. Contact includes ContactPage and Store schema.
6. Every image referenced by HTML, CSS, JavaScript product data or sitemap exists locally, returns HTTP 200 with an image content type, has non-empty alt text where rendered as an `<img>`, and loads with non-zero natural dimensions in browser checks.
7. Catalogue images are visible by default even if JavaScript reveal observers fail; the first catalogue product images are eager-loaded, while below-the-fold images remain lazy.
8. All internal links and canonical targets resolve to existing local files. No product or category page contains broken related-product links.
9. Sitemap XML validates, contains 541 unique canonical URLs, includes 541 image entries, and every sitemap image exists.
10. Robots.txt allows the site and major AI/search crawlers and references the sitemap. `llms.txt` and `llms-full.txt` contain accurate store facts and product inventory.
11. Browser smoke checks on home, catalogue, category index, category page, product page, promotions, price list, contact and legal pages report zero console errors, zero failed requests, zero broken images and zero invisible images after scrolling.
12. Performance guardrails: hero image remains below 500 KB; no local HTML references missing assets; product images use lazy/async loading except primary/above-the-fold images.

## Method

- `check.py` performs static HTML, SEO, schema, link, sitemap, robots, AI-file and image-file checks across all 541 pages.
- `http_audit.py` starts a local HTTP server, requests every sitemap URL and image URL, then uses headless Chromium to render the SPA routes and all static pages, checking H1 presence, console errors, failed requests and image dimensions.
- Every run appends a timestamped log to `verifier/runs/`.
