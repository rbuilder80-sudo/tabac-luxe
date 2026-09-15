import json, datetime, sys
from playwright.sync_api import sync_playwright
errors, out = [], {}
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox"]) if False else p.chromium.launch(args=["--no-sandbox"])
    pg = b.new_page()
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto("file:///mnt/agents/output/app/index.html#/")
    pg.wait_for_timeout(800)
    out["home_title"] = pg.inner_text("h1") != ""
    # gate blocks catalogue
    pg.goto("file:///mnt/agents/output/app/index.html#/catalogue")
    pg.wait_for_timeout(400)
    out["gate_shown"] = pg.locator(".gate").count() == 1 and pg.locator(".prod").count() == 0
    # unlock with demo code
    pg.fill("#gateCode", "DEMO-2026"); pg.click("#gateBtn"); pg.wait_for_timeout(400)
    out["unlocked_products"] = pg.locator(".prod").count()
    # prices visible
    out["price_visible"] = "€" in pg.inner_text(".price")
    # add to cart
    pg.click("[data-add] >> nth=0"); pg.wait_for_timeout(200)
    out["cart_badge"] = pg.inner_text("#cartN")
    # cart page + wa link
    pg.goto("file:///mnt/agents/output/app/index.html#/cart"); pg.wait_for_timeout(400)
    out["cart_rows"] = pg.locator(".cartrow").count()
    href = pg.get_attribute("#waOrder", "href") or ""
    out["wa_prefilled"] = href.startswith("https://wa.me/352691000000?text=") and "Demo" in href or "text=" in href
    # language switch to LB
    pg.click("#langs button[data-l='lb']"); pg.wait_for_timeout(300)
    out["lang_lb"] = "Weekuerf" in pg.content()
    b.close()
out["js_errors"] = errors
ok = (not errors and out.get("gate_shown") and out.get("unlocked_products",0)>=12
      and out.get("cart_rows",0)>=1 and out.get("wa_prefilled") and out.get("lang_lb"))
out["ok"] = ok
ts = datetime.datetime.now().isoformat()
rec = {"time": ts, "check": "smoke v1", "exit": 0 if ok else 1, **out}
open("/mnt/agents/output/app/verifier/runs/smoke_latest.json","w").write(json.dumps(rec, indent=2))
open(f"/mnt/agents/output/app/verifier/runs/{ts}_smoke.json","w").write(json.dumps(rec, indent=2))
print(json.dumps(rec, indent=2))
sys.exit(0 if ok else 1)
