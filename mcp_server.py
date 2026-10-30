import sys
import json
from client import PriceTrackerEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "evaluate_price_drop",
                "description": "Evaluate current SKU price against historical records for discount drops",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string"},
                        "current_price": {"type": "number"},
                        "historical_prices": {"type": "array"},
                        "target_discount_pct": {"type": "number", "default": 15.0}
                    },
                    "required": ["sku", "current_price", "historical_prices"]
                }
            }]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        out = PriceTrackerEngine.evaluate_price_drop(
            args.get("sku", ""),
            float(args.get("current_price", 0.0)),
            [float(p) for p in args.get("historical_prices", [])],
            float(args.get("target_discount_pct", 15.0))
        )
        return {"content": [{"type": "text", "text": json.dumps(out, indent=2)}]}
    return {"error": "Unsupported method"}

if __name__ == "__main__":
    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()
