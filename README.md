# Tabac Luxe

Deployment-ready multilingual B2B tobacco & alcohol wholesale catalogue.

## Production architecture
The repository contains a GitHub-native static-site generator (`build.py`) plus catalogue data and production assets. On every push to `main`, GitHub Actions runs the generator, creates the full multilingual `dist/` site, and deploys that output to GitHub Pages.

## Included
- 10 language versions: English, French, German, Dutch, Spanish, Italian, Portuguese, Polish, Romanian, Luxembourgish
- Tobacco and alcohol catalogue architecture
- Luxury responsive design
- Enquiry basket only — no online checkout or payment
- WhatsApp and email enquiry handoff
- Product/category pages and catalogue manager
- Canonical tags, reciprocal hreflang, x-default, robots.txt, sitemap.xml and structured data
- GitHub Pages build/deployment workflow

## Main source files
- `build.py` — multilingual static-site generator
- `src/products.json` — catalogue source data
- `dist/assets/style.css` — production styling
- `dist/assets/app.js` — enquiry basket / WhatsApp / email logic
- `dist/assets/admin.js` — catalogue-manager logic
- `.github/workflows/pages.yml` — build and GitHub Pages deployment
- `TABAC-LUXE-BUILD-REPORT.md` — completion and validation report

## Deployment
In Repository Settings → Pages, select **GitHub Actions** as the source if it is not already enabled. The included workflow then builds and publishes the full `dist/` site automatically.

## Launch configuration still required
Before a custom-domain launch, confirm the final domain if different from `https://www.tabacluxe.lu`, and add the final WhatsApp number and business email.
