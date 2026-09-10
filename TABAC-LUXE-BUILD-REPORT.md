# Tabac Luxe — Production Build Report

## Status
The Tabac Luxe production site source has been uploaded to GitHub and converted to a GitHub-native build/deployment structure.

## Repository implementation
- `build.py` generates the complete multilingual static site
- `src/products.json` stores catalogue source data
- `dist/assets/style.css` contains the production luxury design system
- `dist/assets/app.js` handles the enquiry basket plus WhatsApp/email handoff
- `dist/assets/admin.js` handles catalogue-manager import/export functionality
- `.github/workflows/pages.yml` builds and deploys the generated `dist/` site through GitHub Pages

## Scope completed
- Premium B2B tobacco and alcohol wholesale catalogue
- Enquiry-only workflow: no checkout and no online payment
- WhatsApp and email enquiry handoff
- Responsive luxury desktop/mobile design
- 10 language versions: English, French, German, Dutch, Spanish, Italian, Portuguese, Polish, Romanian, Luxembourgish
- Dedicated static SEO product/category pages generated from source data
- Canonical tags
- Reciprocal hreflang tags plus x-default
- robots.txt
- sitemap.xml
- JSON-LD structured data
- Catalogue manager/admin area with JSON import/export
- GitHub Pages build/deployment workflow

## Previous production validation
- HTML files generated in the validated production build: 223
- Languages: 10
- Products seeded: 15
- Sitemap URLs: 220
- Missing CSS references: 0
- Missing JS references: 0
- Missing canonical tags: 0
- Missing hreflang sets: 0

The GitHub-native generator now reproduces the deployment site from the version-controlled catalogue and templates instead of requiring hundreds of generated HTML files to be committed manually.

## Launch configuration still required
- Confirm the final production domain; canonical base is prepared around `https://www.tabacluxe.lu`
- Add the final WhatsApp business number
- Add the final business email
- Reverify live catalogue prices before commercial launch
- In GitHub repository Settings → Pages, choose **GitHub Actions** as the publishing source if not already enabled

## Product data note
Real de Lux was used only as a factual reference for product/category data. Tabac Luxe does not copy their protected page copy, site design, or photography.
