#!/usr/bin/env python3
"""Apply the unified Tabac Luxe design system to all static pages:
same dark luxury header with nav, same rich footer, same tokens as the SPA."""
import re, glob, os

ROOT = "/mnt/agents/output/app"

OLD_CSS = [
    "header{background:var(--ink);padding:0 24px;display:flex;justify-content:space-between;align-items:center;height:72px;border-bottom:2px solid var(--gold)}",
    ".logo{color:var(--gold);font-family:'Cormorant Garamond',Georgia,serif;font-size:1.7rem;letter-spacing:5px;text-decoration:none;font-weight:600}",
    ".back{color:var(--ivory);text-decoration:none;font-size:.8rem;letter-spacing:2px;text-transform:uppercase;border:1px solid var(--gold);padding:9px 20px;transition:.25s}",
    ".back:hover{background:var(--gold);color:var(--ink)}",
    "footer{background:var(--ink);color:#b5ab9d;text-align:center;padding:30px 16px;font-size:.82rem;margin-top:70px;letter-spacing:1px}",
    "footer a{color:var(--gold);text-decoration:none}",
    ".foot{margin-top:56px;border-top:1px solid var(--line);padding-top:24px;font-size:.85rem;color:var(--mut)}",
    ".foot a{color:var(--gold);text-decoration:none}",
]

NEW_CSS = """
/* unified site header/footer — Tabac Luxe design system */
header.sitehead{background:#221e19;border-bottom:2px solid var(--gold);padding:0}
header.sitehead .hwrap2{max-width:1240px;margin:0 auto;padding:16px 24px;display:flex;align-items:center;gap:28px;flex-wrap:wrap}
.brandx{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.6rem;color:#f6f1e6;text-decoration:none;line-height:1.1}
.brandx em{color:var(--gold);font-style:italic}
.brandx small{display:block;font-family:'Jost',Arial,sans-serif;font-size:.56rem;letter-spacing:.4em;text-transform:uppercase;color:#b7ab93;margin-top:2px}
.snav{display:flex;gap:26px;margin-left:auto;flex-wrap:wrap}
.snav a{color:#cfc4ac;text-decoration:none;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;padding:6px 0;border-bottom:1px solid transparent;transition:.25s}
.snav a:hover{color:var(--goldlt);border-color:var(--goldlt)}
footer.sitefoot{background:#221e19;color:#b7ab93;margin-top:70px;padding:56px 24px 26px;text-align:left;letter-spacing:normal}
footer.sitefoot .fgrid{max-width:1240px;margin:0 auto;display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr;gap:40px}
footer.sitefoot h2{font-family:'Cormorant Garamond',Georgia,serif;color:#efe7d6;font-size:1.2rem;margin-bottom:14px;font-weight:500}
footer.sitefoot ul{list-style:none;padding:0}
footer.sitefoot li{margin-bottom:8px}
footer.sitefoot a{color:#b7ab93;text-decoration:none;font-size:.86rem;transition:.25s}
footer.sitefoot a:hover{color:var(--goldlt)}
footer.sitefoot p{font-size:.86rem;margin-bottom:10px}
.fbrand{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.7rem;color:#efe7d6;margin-bottom:12px}
.fbrand em{color:var(--gold);font-style:italic}
.w18{display:inline-grid;place-items:center;width:30px;height:30px;border:2px solid #9c2b2b;color:#d98a8a;border-radius:50%;font-weight:600;font-size:.68rem;margin-right:8px;vertical-align:middle}
footer.sitefoot .legal-line{max-width:1240px;margin:34px auto 0;padding-top:20px;border-top:1px solid rgba(233,223,200,.14);font-size:.72rem;color:#8d8168;line-height:1.7;text-align:center}
@media(max-width:900px){footer.sitefoot .fgrid{grid-template-columns:1fr 1fr}}
@media(max-width:560px){footer.sitefoot .fgrid{grid-template-columns:1fr}.snav{gap:14px;margin-left:0}}
"""

HEADER = """<header class="sitehead">
<div class="hwrap2">
<a class="brandx" href="{d}index.html">Tabac <em>Luxe</em><small>Rodange · Luxembourg</small></a>
<nav class="snav" aria-label="Site">
<a href="{d}category/index.html">Catalogue</a>
<a href="{d}promotions.html">Promotions</a>
<a href="{d}price-list.html">Price List</a>
<a href="{d}contact.html">Contact</a>
</nav>
</div>
</header>"""

FOOTER = """<footer class="sitefoot">
<div class="fgrid">
<div>
<div class="fbrand">Tabac <em>Luxe</em></div>
<p>Premium tobacco, cigars, shisha and spirits in Rodange, Luxembourg. Reserve on WhatsApp and collect in store.</p>
<p><span class="w18">18+</span>Sale restricted to adults.</p>
</div>
<div><h2>Explore</h2><ul>
<li><a href="{d}category/index.html">Catalogue</a></li>
<li><a href="{d}promotions.html">Promotions</a></li>
<li><a href="{d}price-list.html">Price List</a></li>
<li><a href="{d}contact.html">Contact</a></li>
</ul></div>
<div><h2>Legal</h2><ul>
<li><a href="{d}terms.html">Terms &amp; Conditions</a></li>
<li><a href="{d}privacy.html">Privacy Policy</a></li>
<li><a href="{d}disclaimer.html">Disclaimer</a></li>
<li><a href="{d}legal-notice.html">Legal Notice</a></li>
</ul></div>
<div><h2>Visit</h2>
<p>Rodange, Luxembourg</p>
<p>Mon–Fri 06:00–18:00<br>Sat 08:00–17:00<br>Sun closed</p>
<p><a href="mailto:info@tabacluxe.lu">info@tabacluxe.lu</a></p>
</div>
</div>
<div class="legal-line">© 2026 Tabac Luxe — Rodange, Luxembourg · Tobacco and alcohol sales restricted to adults aged 18+ · In-store purchase only, no online payment or shipping</div>
</footer>"""

def targets():
    for p in glob.glob(os.path.join(ROOT, "product", "*.html")):
        yield p, "../"
    for p in glob.glob(os.path.join(ROOT, "category", "*.html")):
        yield p, "../"
    for name in ["promotions.html","price-list.html","contact.html","terms.html","privacy.html","disclaimer.html","legal-notice.html"]:
        yield os.path.join(ROOT, name), ""

report = {"css":0,"header":0,"footer":0,"skipped_css":[]}
for path, d in targets():
    s = open(path, encoding="utf-8").read()
    orig = s
    # 1. CSS: remove old header/footer rules, append unified design-system CSS
    if "header.sitehead" not in s:
        for rule in OLD_CSS:
            s = s.replace(rule + "\n", "").replace(rule, "")
        s = s.replace("</style>", NEW_CSS + "</style>", 1)
        report["css"] += 1
    # 2. header markup
    s2 = re.sub(r"<header>.*?</header>", HEADER.format(d=d), s, flags=re.S)
    if s2 != s:
        report["header"] += 1
        s = s2
    # 3. footer: remove old .foot div / <footer>, insert unified footer before </body>
    s = re.sub(r"\s*<div class=\"foot\">.*?</div>", "", s, flags=re.S)
    s = re.sub(r"\s*<footer>.*?</footer>", "", s, flags=re.S)
    if "sitefoot" not in s:
        s = s.replace("</body>", FOOTER.format(d=d) + "\n</body>", 1)
        report["footer"] += 1
    if s != orig:
        open(path, "w", encoding="utf-8").write(s)

print(report)

# sanity: no leftover old shell pieces
for pat in ['class="logo"', 'class="back"', 'class="foot"', "<header>"]:
    hits = [p for p in glob.glob(ROOT+"/**/*.html", recursive=True)
            if "verifier" not in p and pat in open(p, encoding="utf-8").read()]
    print(pat, "->", len(hits), hits[:3])
