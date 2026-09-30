# v13 — 2026-10-01

Change wave: WebP conversion, mobile design pass, home Reviews + FAQ sections (5 languages), GitHub push.

Acceptance criteria = v12 gate (static check.py at 100%) plus:
1. All `assets/**` `<img>`/CSS references resolve to existing `.webp` files (og:image/JSON-LD stay JPG).
2. Mobile (390px) horizontal overflow is 0px on home, catalogue, contact, cart.
3. Home renders 3 review cards and 5 FAQ entries; FAQ content matches FAQPage JSON-LD.
4. `http_audit.py` adds a post-decode settle loop (up to 30s) for SPA routes so the
   Supabase data fetch cannot race the image check; 0 errors required as before.
