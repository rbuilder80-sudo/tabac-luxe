# v18 — WhatsApp button on every page

## Trigger
Owner request: the WhatsApp button must appear on every current page and any
page created in the future.

## Audit result (before)
21 of 556 HTML pages had no `wa.me` link at all:
- all 15 restored doorway pages (en/*, fr/*)
- 6 utility pages: disclaimer, legal-notice, price-list, privacy, promotions, terms

The other 535 pages already expose WhatsApp: the SPA home renders the floating
`.wafab` button (href set from `CONFIG.whatsapp`), and every category/product
page has a visible "Order via WhatsApp" CTA linking to `wa.me/35228777996`.

## Fix
- Inserted the site's floating WhatsApp button (`.wafab`, identical design and
  SVG to the SPA button) into the 21 gap pages, immediately before `</body>`.
  The snippet is self-contained: inline `<style>` + hardcoded
  `href="https://wa.me/35228777996?text=…"` with an English greeting on en/*
  pages and a French greeting elsewhere. No page content was otherwise touched;
  doorway-page ranking elements (title, description, canonical, H1, JSON-LD,
  GA) are unchanged.
- `v18/check.py` = v17 gate + new rule 7: **every** HTML page in the project
  must contain a `wa.me/` link. Any future page added without the WhatsApp
  button fails the gate and cannot be handed off.

## Canonical snippet for new pages
```html
<style>.wafab{position:fixed;right:1.4rem;bottom:1.4rem;z-index:60;width:58px;height:58px;border-radius:50%;background:#25d366;display:grid;place-items:center;box-shadow:0 10px 26px rgba(0,0,0,.28);transition:transform .25s}
.wafab:hover{transform:scale(1.08)}
.wafab svg{width:30px;height:30px;fill:#fff}</style>
<a class="wafab" href="https://wa.me/35228777996?text=Hello%20Tabac%20Luxe%2C%20I%20would%20like%20to%20order%3A" target="_blank" rel="noopener" aria-label="WhatsApp">
  <svg viewBox="0 0 32 32"><path d="M16 2.7C8.7 2.7 2.8 8.6 2.8 15.9c0 2.3.6 4.6 1.8 6.6L2.7 29.3l7-1.8c1.9 1 4 1.6 6.2 1.6 7.3 0 13.3-5.9 13.3-13.2S23.3 2.7 16 2.7zm0 24.1c-2 0-3.9-.5-5.6-1.5l-.4-.2-4.1 1.1 1.1-4-.3-.4c-1.1-1.7-1.7-3.7-1.7-5.8C5 9.6 9.9 4.7 16 4.7s11 4.9 11 11-4.9 11.1-11 11.1zm6-8.3c-.3-.2-1.9-1-2.2-1.1-.3-.1-.5-.2-.7.2s-.8 1.1-1 1.3c-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.6.1-.2.1-.4 0-.6-.1-.2-.7-1.8-1-2.4-.3-.6-.5-.5-.7-.6h-.6c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.7s1.2 3.2 1.3 3.4c.2.2 2.3 3.5 5.5 4.9.8.3 1.4.5 1.8.7.8.2 1.5.2 2 .1.6-.1 1.9-.8 2.2-1.5.3-.8.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>
</a>
```
(French pages use `?text=Bonjour%20Tabac%20Luxe%2C%20je%20souhaite%20commander%20%3A`.)

## Gate
`python3 verifier/v18/check.py` — must print PASS before any handoff.
