# Verifier v11 — Pre-launch acceptance criteria (contact-data removal)

Supersedes v10. Change requested by site owner: remove the street address
(Route de Longwy 549, L-4832) and the telephone number (+352 28 77 79 96)
from every page and file. WhatsApp ordering buttons are retained — the number
exists only inside wa.me link URLs and is never displayed.

## Scope
- 541 crawlable HTML pages (516 products, 17 category pages, index, 7 utility pages)
- sitemap.xml, robots.txt, llms.txt, llms-full.txt

## Criteria (all must pass)
1. Everything from v10 (titles 30–65, descriptions 120–165, unique; one H1;
   heading hierarchy; canonicals; OG/Twitter; JSON-LD validity and required
   types; image alt/src; internal links; sitemap integrity; robots AI rules).
2. geo.position / ICBM meta tags no longer required (precise coordinates removed).
3. Forbidden anywhere (excluding wa.me URLs): "Longwy", "tel:", "L-4832",
   coordinates 49.5469/5.8411, visible "+352" phone numbers.
4. HTTP/browser audit: every sitemap URL + image returns 200; every rendered
   page/route has correct title, 120–165 char description, one visible H1,
   all images loaded (naturalWidth > 0), zero console/page errors.

## Run
python3 v11/check.py
python3 v11/http_audit.py
