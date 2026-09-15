import re, os, json, sys
root = "/mnt/agents/output/app"
html = open(f"{root}/index.html", encoding="utf-8").read()
res = []
def check(name, ok): res.append((name, bool(ok)))

check("index.html exists", os.path.exists(f"{root}/index.html"))
check("noindex meta", 'name="robots" content="noindex' in html)
imgs = re.findall(r'assets/products/([\w-]+)\.jpg', html) + re.findall(r'img:"([\w-]+)"', html)
missing = [i for i in set(imgs) if not os.path.exists(f"{root}/assets/products/{i}.jpg")]
check(f"all {len(set(imgs))} referenced product images exist", not missing)
prod_ids = re.findall(r'\{id:"', html)
check(">=12 products defined", len(prod_ids) >= 12)
for lg in ["fr","de","en","pt","lb"]:
    check(f"lang {lg} dict", re.search(rf'\b{lg}:\{{', html))
check("routes", all(x in html for x in ['#/catalogue','#/trade','#/cart']))
check("trade gate demo code", "DEMO-2026" in html)
check("localStorage cart", 'ma_cart' in html)
check("wa.me link", "wa.me/" in html and "waLinkCart" in html)
check("floating wa button", "wafab" in html)
check("trade form", "tradeForm" in html)
check("MOQ display", "prod.moq" in html)
ok = all(v for _, v in res)
for n, v in res: print(("PASS " if v else "FAIL ") + n)
print("MISSING_IMGS", missing)
rec = {"check":"static v1", "passed": sum(v for _,v in res), "total": len(res), "ok": ok, "missing_imgs": missing}
open(f"{root}/verifier/runs/static_latest.json","w").write(json.dumps(rec, indent=2))
sys.exit(0 if ok else 1)
