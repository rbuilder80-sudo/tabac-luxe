# Verifier v12 — Professional unified theme rollout

Change requested by owner: make the whole site one consistent, professional
catalogue design; brand name "Tabac Luxe" everywhere.

## What changed
1. SPA header restyled to the dark luxury bar (ink #221e19, gold border) with
   gold cart button — same identity as static pages.
2. Catalogue view: professional sticky toolbar (search, A–Z/price sort, live
   result count) + horizontally scrollable category chips replacing the dropdown.
3. All 540 static pages: unified header (brand + nav: Catalogue, Promotions,
   Price List, Contact) and unified rich footer (Explore/Legal/Visit + legal line).
   Old thin headers/footers removed.
4. 61 product images that were grey "no image" placeholder icons replaced with
   brand logos; 11 new on-theme brand-name tiles generated (ivory, gold border,
   serif wordmark) matching the existing assets/brands/name-*.jpg style.
5. llms.txt / llms-full.txt: "luxury tobacco" wording removed -> "premium tobacco".

## Acceptance criteria
- All v11 criteria unchanged (SEO meta, headings, schema, images, links,
  no address/phone) — still passing at 100%.
- Header/footer markup identical pattern on every static page (sitehead/sitefoot).
- Zero placeholder-icon images remain in assets/lu.
- Browser audit: 0 errors across 552 pages/routes.
