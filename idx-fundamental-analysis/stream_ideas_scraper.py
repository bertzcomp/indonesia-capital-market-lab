import os
import json
import argparse
from datetime import datetime, timezone
from pathlib import Path
import sys
import traceback

# adjust import sesuai struktur repo Anda
# jika sebelumnya dari providers.stockbit import StockBit, gunakan itu
try:
    from providers.stockbit import StockBit
except Exception:
    # fallback jika import path lain, try local file
    try:
        from stockbit import StockBit
    except Exception:
        raise

def ensure_dir(p):
    Path(p).mkdir(parents=True, exist_ok=True)

def now_iso():
    return datetime.now(timezone.utc).isoformat().replace(":", "-")

def parse_stocks_arg(s):
    if not s:
        return None
    # accept comma separated list, or single ticker
    parts = [p.strip() for p in s.split(",") if p.strip()]
    return parts if parts else None

def safe_construct_stockbit(stocks_list, debug=False):
    """
    Try to construct StockBit in a tolerant way:
    1) try StockBit(stocks=stocks_list) if stocks_list provided
    2) fallback to StockBit()
    If both fail, raise RuntimeError with helpful info.
    """
    if stocks_list:
        try:
            return StockBit(stocks=stocks_list)
        except TypeError as e:
            if debug:
                print("[debug] StockBit(stocks=...) failed, will try StockBit() fallback.")
                traceback.print_exc()
    # try no-arg constructor
    try:
        return StockBit()
    except Exception as e:
        # final attempt: try positional (some code may expect positional stocks)
        if stocks_list:
            try:
                return StockBit(stocks_list)
            except Exception:
                pass
        # cannot construct, raise informative error
        msg = (
            "Unable to construct StockBit automatically. "
            "Your StockBit.__init__ likely requires positional/keyword args. "
            "You can either:\n"
            "  - pass --stocks TICKER1,TICKER2 to this script (if StockBit expects 'stocks'), or\n"
            "  - edit stream_ideas_scraper.py to construct StockBit with the required parameters.\n\n"
            f"Original error: {e}"
        )
        raise RuntimeError(msg) from e

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--category", default="STREAM_CATEGORY_ALL_WATCHLIST")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--max-pages", type=int, default=None)
    p.add_argument("--delay", type=float, default=0.5)
    p.add_argument("--out", default="data/streams")
    p.add_argument("--start-last-stream-id", default=0)
    p.add_argument("--start-last-reply", default=None)
    p.add_argument("--stocks", default=None, help="Comma-separated tickers to pass to StockBit constructor, e.g. BBRI,TLKM")
    p.add_argument("--debug", action="store_true")
    args = p.parse_args()

    ensure_dir(args.out)
    stocks_list = parse_stocks_arg(args.stocks)

    # construct StockBit safely
    try:
        sb = safe_construct_stockbit(stocks_list, debug=args.debug)
    except Exception as e:
        print("ERROR: cannot construct StockBit instance.")
        print(str(e))
        sys.exit(1)

    last_stream_id = int(args.start_last_stream_id or 0)
    last_reply = int(args.start_last_reply) if args.start_last_reply else None

    total = 0
    batch_i = 0
    # use the tolerant call to get_stream_batches that you added in providers/stockbit
    for batch in sb.get_stream_batches(category=args.category,
                                       last_stream_id=last_stream_id,
                                       last_reply=last_reply,
                                       limit=args.limit,
                                       max_pages=args.max_pages,
                                       delay=args.delay,
                                       debug=args.debug):
        # choose filename with timestamp + cursor for traceability
        cursor = batch[-1].get("stream_id") if batch else "no-cursor"
        ts = now_iso()
        fname = os.path.join(args.out, f"streams_{ts}_cursor_{cursor}_batch_{batch_i:04d}.json")
        with open(fname, "w", encoding="utf-8") as f:
            json.dump(batch, f, ensure_ascii=False, indent=2)
        if args.debug:
            print(f"[debug] saved batch {batch_i} ({len(batch)} items) -> {fname}")
        total += len(batch)
        batch_i += 1

    print(f"Done. total_items={total}, batches={batch_i}, out={args.out}")

if __name__ == "__main__":
    main()
