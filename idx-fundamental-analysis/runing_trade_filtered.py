import os, csv, json, argparse
from datetime import datetime
from providers.stockbit import StockBit

def parse_price(price_raw):
    if price_raw is None:
        return None
    if isinstance(price_raw, (int, float)):
        return float(price_raw)
    s = str(price_raw)
    # remove percent and plus/minus
    s = s.replace("%", "").replace("+", "").replace("−", "-")
    # remove thousands separators (commas)
    s = s.replace(",", "").strip()
    try:
        return float(s)
    except Exception:
        import re
        digits = re.sub(r"[^\d\-\.]", "", s)
        try:
            return float(digits) if digits else None
        except Exception:
            return None

def parse_lot(lot_raw):
    if lot_raw is None:
        return None
    if isinstance(lot_raw, (int, float)):
        return float(lot_raw)
    s = str(lot_raw)
    s = s.replace(",", "").strip()
    try:
        return float(s)
    except Exception:
        import re
        digits = re.sub(r"[^\d\.\-]", "", s)
        try:
            return float(digits) if digits else None
        except Exception:
            return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--price-from", type=int, default=1)
    parser.add_argument("--price-to", type=int, default=10)
    parser.add_argument("--min-lot", type=int, default=100)
    parser.add_argument("--action", type=str, default="RUNNING_TRADE_ACTION_TYPE_ALL")
    parser.add_argument("--max-scroll", type=int, default=1000, help="How many batches (50 items each) to fetch")
    parser.add_argument("--delay", type=float, default=0.4)
    parser.add_argument("--output-dir", type=str, default="/Users/albert/Documents/Finances/data/raw/market_data/running_trade/filtered_rt")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    sb = StockBit(stocks=["BBRI"])  # formalitas

    trades = sb.get_filtered_running_trade_batches(
        max_scroll=args.max_scroll,
        delay=args.delay,
        price_range_from=args.price_from,
        price_range_to=args.price_to,
        minimum_lot=args.min_lot,
        action_type=args.action,
        debug=args.debug
    )

    print(f"Collected {len(trades)} trades after server-side filtering (price {args.price_from}-{args.price_to}, min_lot {args.min_lot})")

    if not trades:
        print("No trade data to save.")
        return

    # optional client-side sanity-filter (if you want to double-check)
    filtered = []
    for t in trades:
        p = None
        l = None
        # try common keys
        for pk in ("price", "trade_price", "last_price"):
            if pk in t:
                p = parse_price(t.get(pk))
                break
        for lk in ("lot", "volume", "size"):
            if lk in t:
                l = parse_lot(t.get(lk))
                break
        # if any missing, keep the record (server already filtered)
        t["_parsed_price"] = p
        t["_parsed_lot"] = l
        filtered.append(t)

    os.makedirs(args.output_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    csv_path = os.path.join(args.output_dir, f"running_trade_filtered_51_100_{ts}.csv")
    # json_path = os.path.join(args.output_dir, f"running_trade_filtered_{ts}.json")

    # union keys
    keys = set()
    for it in filtered:
        keys.update(it.keys())
    keys = list(keys)
    keys = [k for k in keys if not k.startswith("_")] + [k for k in keys if k.startswith("_")]

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(filtered)

    # with open(json_path, "w", encoding="utf-8") as f:
    #     json.dump(filtered, f, indent=2, ensure_ascii=False)

    print(f"Saved CSV -> {csv_path}")
    # print(f"Saved JSON -> {json_path}")

if __name__ == "__main__":
    main()


# python runing_trade_filtered.py --price-from 1 --price-to 10 --min-lot 10 --max-scroll 1000 --debug


# python runing_trade_filtered.py --price-from 11 --price-to 50 --min-lot 10 --max-scroll 1000 --debug

# python runing_trade_filtered.py --price-from 51 --price-to 100 --min-lot 100 --max-scroll 1000 --debug
