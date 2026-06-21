"""
tradebook_scraper.py
====================
Scrape Trade Book dan Orderbook dari Stockbit untuk saham IDX.

Menghasilkan 4 file CSV:
  1. tradebook_price_DATE.csv   — distribusi transaksi per price level
  2. tradebook_time_DATE.csv    — distribusi transaksi per time interval
  3. orderbook_snapshot_DATE.csv — ringkasan orderbook + market stats per ticker
  4. orderbook_levels_DATE.csv  — bid/offer levels per ticker

Endpoints:
  Trade Book by Price : GET /order-trade/trade-book?symbol={ticker}&group_by=GROUP_BY_PRICE
  Trade Book by Time  : GET /order-trade/trade-book?symbol={ticker}&group_by=GROUP_BY_TIME&time_interval=10m
  Orderbook           : GET /company-price-feed/v2/orderbook/companies/{ticker}?with_full_price_tick=false

Usage:
    python tradebook_scraper_fixed.py --ticker-file tickers.txt
    python tradebook_scraper_fixed.py --tickers KIJA BBRI TLKM
    python tradebook_scraper_fixed.py --tickers KIJA --time-interval 5m
    python tradebook_scraper_fixed.py --ticker-file tickers.txt --skip-tradebook
    python tradebook_scraper_fixed.py --ticker-file tickers.txt --skip-orderbook
    python tradebook_scraper_fixed.py --ticker-file tickers.txt --resume
    python tradebook_scraper_fixed.py --ticker-file tickers.txt --mirror-output-dir data/raw/tradebook
"""

import argparse
import csv
import json
import os
import shutil
import sys
import threading
import time
from datetime import date, datetime

from dotenv import load_dotenv

from services.stockbit_api_client import StockbitApiClient
from utils.logger_config import logger

load_dotenv()

# CSV schemas
TRADEBOOK_PRICE_FIELDS = [
    "ticker", "date",
    "price",
    "buy_lot", "buy_freq", "buy_pct",
    "sell_lot", "sell_freq", "sell_pct",
    "total_lot", "total_freq",
    # book_total summary (same for all rows of this ticker+date)
    "summary_buy_lot", "summary_buy_freq", "summary_buy_pct",
    "summary_sell_lot", "summary_sell_freq", "summary_sell_pct",
    "summary_total_lot", "summary_total_freq",
]

TRADEBOOK_TIME_FIELDS = [
    "ticker", "date", "time_interval",
    "time",
    "buy_lot", "buy_freq", "buy_pct",
    "sell_lot", "sell_freq", "sell_pct",
    "total_lot", "total_freq",
    # book_total summary
    "summary_buy_lot", "summary_buy_freq", "summary_buy_pct",
    "summary_sell_lot", "summary_sell_freq", "summary_sell_pct",
    "summary_total_lot", "summary_total_freq",
]

ORDERBOOK_SNAPSHOT_FIELDS = [
    "ticker", "date",
    "lastprice", "change", "pct_change",
    "open", "high", "low", "close", "average",
    "volume", "value", "frequency",
    "fbuy", "fsell", "fnet",
    "foreign_pct", "domestic_pct",
    "ara", "arb",
    "total_bid_freq", "total_bid_lot",
    "total_offer_freq", "total_offer_lot",
    # market_data breakdown
    "all_market_freq", "all_market_volume", "all_market_value",
    "regular_freq", "regular_volume", "regular_value",
    "nego_freq", "nego_volume", "nego_value",
    "cash_freq", "cash_volume", "cash_value",
]

ORDERBOOK_LEVELS_FIELDS = [
    "ticker", "date", "side",
    "rank", "price", "que_num", "volume",
]


# Parsers
def _clean(val) -> str:
    """Strip, handle None."""
    if val is None:
        return ""
    return str(val).strip()

def _book_total_summary(bt: dict) -> dict:
    return {
        "summary_buy_lot"    : _clean(bt.get("buy_lot")),
        "summary_buy_freq"   : _clean(bt.get("buy_frequency")),
        "summary_buy_pct"    : _clean(bt.get("buy_percentage")),
        "summary_sell_lot"   : _clean(bt.get("sell_lot")),
        "summary_sell_freq"  : _clean(bt.get("sell_frequency")),
        "summary_sell_pct"   : _clean(bt.get("sell_percentage")),
        "summary_total_lot"  : _clean(bt.get("total_lot")),
        "summary_total_freq" : _clean(bt.get("total_frequency")),
    }

def parse_tradebook_price(ticker: str, response: dict) -> list:
    rows = []
    if not response or "data" not in response:
        return rows

    data     = response["data"]
    dt       = data.get("date", "")
    bt       = data.get("book_total", {})
    summary  = _book_total_summary(bt)

    for entry in data.get("book", []):
        buy  = entry.get("buy", {})
        sell = entry.get("sell", {})
        tot  = entry.get("total", {})

        row = {
            "ticker"    : ticker,
            "date"      : dt,
            "price"     : _clean(entry.get("price")),
            "buy_lot"   : _clean(buy.get("lot")),
            "buy_freq"  : _clean(buy.get("frequency")),
            "buy_pct"   : _clean(buy.get("percentage")),
            "sell_lot"  : _clean(sell.get("lot")),
            "sell_freq" : _clean(sell.get("frequency")),
            "sell_pct"  : _clean(sell.get("percentage")),
            "total_lot" : _clean(tot.get("lot")),
            "total_freq": _clean(tot.get("frequency")),
        }
        row.update(summary)
        rows.append(row)

    return rows


def parse_tradebook_time(ticker: str, response: dict, time_interval: str) -> list:
    rows = []
    if not response or "data" not in response:
        return rows

    data     = response["data"]
    dt       = data.get("date", "")
    bt       = data.get("book_total", {})
    summary  = _book_total_summary(bt)

    for entry in data.get("book", []):
        buy  = entry.get("buy", {})
        sell = entry.get("sell", {})
        tot  = entry.get("total", {})

        row = {
            "ticker"        : ticker,
            "date"          : dt,
            "time_interval" : time_interval,
            "time"          : _clean(entry.get("time")),
            "buy_lot"       : _clean(buy.get("lot")),
            "buy_freq"      : _clean(buy.get("frequency")),
            "buy_pct"       : _clean(buy.get("percentage")),
            "sell_lot"      : _clean(sell.get("lot")),
            "sell_freq"     : _clean(sell.get("frequency")),
            "sell_pct"      : _clean(sell.get("percentage")),
            "total_lot"     : _clean(tot.get("lot")),
            "total_freq"    : _clean(tot.get("frequency")),
        }
        row.update(summary)
        rows.append(row)

    return rows


def parse_orderbook(ticker: str, response: dict) -> tuple:
    """
    Returns (snapshot_row, bid_rows, offer_rows).
    snapshot_row: dict | None
    bid_rows, offer_rows: list of dicts
    """
    if not response or "data" not in response:
        return None, [], []

    d    = response["data"]
    today = date.today().strftime("%Y-%m-%d")

    # --- market_data breakdown ---
    md_map = {}
    for md in d.get("market_data", []):
        label = md.get("label", "").lower().replace(" ", "_")
        md_map[label] = {
            "freq"  : md.get("frequency", {}).get("raw", ""),
            "volume": md.get("volume", {}).get("raw", ""),
            "value" : md.get("value", {}).get("raw", ""),
        }

    def md_get(label, field):
        return _clean(md_map.get(label, {}).get(field, ""))

    # --- total bid/offer ---
    tbo      = d.get("total_bid_offer", {})
    bid_tot  = tbo.get("bid", {})
    off_tot  = tbo.get("offer", {})

    snapshot = {
        "ticker"          : ticker,
        "date"            : today,
        "lastprice"       : _clean(d.get("lastprice")),
        "change"          : _clean(d.get("change")),
        "pct_change"      : _clean(d.get("percentage_change")),
        "open"            : _clean(d.get("open")),
        "high"            : _clean(d.get("high")),
        "low"             : _clean(d.get("low")),
        "close"           : _clean(d.get("close")),
        "average"         : _clean(d.get("average")),
        "volume"          : _clean(d.get("volume")),
        "value"           : _clean(d.get("value")),
        "frequency"       : _clean(d.get("frequency")),
        "fbuy"            : _clean(d.get("fbuy")),
        "fsell"           : _clean(d.get("fsell")),
        "fnet"            : _clean(d.get("fnet")),
        "foreign_pct"     : _clean(d.get("foreign")),
        "domestic_pct"    : _clean(d.get("domestic")),
        "ara"             : _clean(d.get("ara", {}).get("value")),
        "arb"             : _clean(d.get("arb", {}).get("value")),
        "total_bid_freq"  : _clean(bid_tot.get("freq")),
        "total_bid_lot"   : _clean(bid_tot.get("lot")),
        "total_offer_freq": _clean(off_tot.get("freq")),
        "total_offer_lot" : _clean(off_tot.get("lot")),
        "all_market_freq" : md_get("all_market", "freq"),
        "all_market_volume": md_get("all_market", "volume"),
        "all_market_value": md_get("all_market", "value"),
        "regular_freq"    : md_get("regular", "freq"),
        "regular_volume"  : md_get("regular", "volume"),
        "regular_value"   : md_get("regular", "value"),
        "nego_freq"       : md_get("nego", "freq"),
        "nego_volume"     : md_get("nego", "volume"),
        "nego_value"      : md_get("nego", "value"),
        "cash_freq"       : md_get("cash", "freq"),
        "cash_volume"     : md_get("cash", "volume"),
        "cash_value"      : md_get("cash", "value"),
    }

    # --- bid levels ---
    bid_rows = []
    for rank, b in enumerate(d.get("bid", []), start=1):
        bid_rows.append({
            "ticker"  : ticker,
            "date"    : today,
            "side"    : "bid",
            "rank"    : rank,
            "price"   : _clean(b.get("price")),
            "que_num" : _clean(b.get("que_num")),
            "volume"  : _clean(b.get("volume")),
        })

    # --- offer levels ---
    offer_rows = []
    for rank, o in enumerate(d.get("offer", []), start=1):
        offer_rows.append({
            "ticker"  : ticker,
            "date"    : today,
            "side"    : "offer",
            "rank"    : rank,
            "price"   : _clean(o.get("price")),
            "que_num" : _clean(o.get("que_num")),
            "volume"  : _clean(o.get("volume")),
        })

    return snapshot, bid_rows, offer_rows


# Hotkey listener
class SkipListener:
    def __init__(self):
        self.skip_current  = False
        self.stop_listener = False
        self._thread = threading.Thread(target=self._listen, daemon=True)
        self._thread.start()

    def _listen(self):
        print("\n  [HOTKEY] Ketik  s  + Enter  untuk skip ticker yang stuck.\n", flush=True)
        while not self.stop_listener:
            try:
                if input().strip().lower() == "s":
                    self.skip_current = True
                    print("  [HOTKEY] Skip requested.", flush=True)
            except EOFError:
                break

    def consume(self) -> bool:
        if self.skip_current:
            self.skip_current = False
            return True
        return False

    def stop(self):
        self.stop_listener = True


# Checkpoint helpers
def _cp_path(output_dir):
    return os.path.join(output_dir, ".tradebook_checkpoint.json")

def load_checkpoint(output_dir):
    p = _cp_path(output_dir)
    if os.path.exists(p):
        try:
            return json.load(open(p))
        except Exception:
            pass
    return {}

def save_checkpoint(output_dir, data):
    os.makedirs(output_dir, exist_ok=True)
    json.dump(data, open(_cp_path(output_dir), "w"))

def delete_checkpoint(output_dir):
    p = _cp_path(output_dir)
    if os.path.exists(p):
        os.remove(p)


# Helpers
def load_tickers_from_file(path):
    tickers = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                tickers.append(line.upper())
    return tickers

def get_tickers_from_idx():
    from providers.idx import IDX
    logger.info("Retrieving stock list from idx.co.id ...")
    stocks = IDX(is_full_retrieve=True).stocks()
    tickers = [s.ticker for s in stocks]
    logger.info(f"Retrieved {len(tickers)} tickers from IDX")
    return tickers

def save_failed_tickers(failed, output_dir, ts):
    if not failed:
        return
    path = os.path.join(output_dir, f"failed_tickers_{ts}.txt")
    with open(path, "w", encoding="utf-8") as f:
        for t in failed:
            f.write(t + "\n")
    logger.warning(f"[TRADEBOOK] {len(failed)} failed -> {path}")


def mirror_outputs(paths, mirror_dir):
    """
    Copy final output files to a secondary directory.

    Primary outputs remain in --output-dir, while this helper creates a
    second copy, for example:
      output/tradebook/*.csv -> data/raw/tradebook/*.csv

    Pass an empty string to --mirror-output-dir to disable mirroring.
    """
    if not mirror_dir:
        return []

    os.makedirs(mirror_dir, exist_ok=True)

    copied = []
    for src in paths:
        if src and os.path.exists(src):
            dst = os.path.join(mirror_dir, os.path.basename(src))
            shutil.copy2(src, dst)
            copied.append(dst)
        else:
            logger.warning(f"[TRADEBOOK] Mirror skipped, file not found: {src}")

    return copied


# Core scraping
def scrape(
    tickers, time_interval,
    skip_tradebook, skip_orderbook,
    delay, output_dir, debug, resume,
):
    os.makedirs(output_dir, exist_ok=True)

    checkpoint   = load_checkpoint(output_dir) if resume else {}
    done_set     = set(checkpoint.get("done", []))
    ts           = checkpoint.get("ts", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

    def _path(name):
        return checkpoint.get(name, os.path.join(output_dir, f"{name}_{ts}.csv"))

    tb_price_path   = _path("tradebook_price")
    tb_time_path    = _path("tradebook_time")
    ob_snap_path    = _path("orderbook_snapshot")
    ob_levels_path  = _path("orderbook_levels")

    if resume and done_set:
        logger.info(f"[TRADEBOOK] Resume: {len(done_set)} tickers already done")

    total  = len(tickers)
    failed = []
    skip_flag  = SkipListener()
    api_client = StockbitApiClient()
    base_url   = "https://exodus.stockbit.com"

    def _mode(path):
        return "a" if (resume and os.path.exists(path)) else "w"
    def _hdr(mode):
        return mode == "w"

    logger.info(f"[TRADEBOOK] Starting: {total} tickers | time_interval={time_interval}")
    logger.info(f"[TRADEBOOK] skip_tradebook={skip_tradebook} | skip_orderbook={skip_orderbook}")

    try:
        with (
            open(tb_price_path,  _mode(tb_price_path),  newline="", encoding="utf-8") as f_tbp,
            open(tb_time_path,   _mode(tb_time_path),   newline="", encoding="utf-8") as f_tbt,
            open(ob_snap_path,   _mode(ob_snap_path),   newline="", encoding="utf-8") as f_obs,
            open(ob_levels_path, _mode(ob_levels_path), newline="", encoding="utf-8") as f_obl,
        ):
            w_tbp = csv.DictWriter(f_tbp, fieldnames=TRADEBOOK_PRICE_FIELDS)
            w_tbt = csv.DictWriter(f_tbt, fieldnames=TRADEBOOK_TIME_FIELDS)
            w_obs = csv.DictWriter(f_obs, fieldnames=ORDERBOOK_SNAPSHOT_FIELDS)
            w_obl = csv.DictWriter(f_obl, fieldnames=ORDERBOOK_LEVELS_FIELDS)

            if _hdr(_mode(tb_price_path)):  w_tbp.writeheader()
            if _hdr(_mode(tb_time_path)):   w_tbt.writeheader()
            if _hdr(_mode(ob_snap_path)):   w_obs.writeheader()
            if _hdr(_mode(ob_levels_path)): w_obl.writeheader()

            for idx, ticker in enumerate(tickers, start=1):
                if ticker in done_set:
                    continue

                if skip_flag.consume():
                    logger.warning(f"[TRADEBOOK] SKIP (hotkey) -> {ticker}")
                    failed.append(ticker)
                    continue

                if debug:
                    print(f"[TRADEBOOK] {idx}/{total} -- {ticker}")
                elif idx % 50 == 0 or idx == 1 or idx == total:
                    logger.info(f"[TRADEBOOK] Progress: {idx}/{total} ({ticker})")

                ticker_ok = True
                try:
                    # Trade Book by PRICE
                    if not skip_tradebook:
                        url = f"{base_url}/order-trade/trade-book?symbol={ticker}&group_by=GROUP_BY_PRICE"
                        resp = api_client.get(url)
                        if skip_flag.consume():
                            failed.append(ticker); ticker_ok = False
                        elif resp:
                            rows = parse_tradebook_price(ticker, resp)
                            if rows:
                                w_tbp.writerows(rows)
                                f_tbp.flush()
                        time.sleep(delay)

                    # Trade Book by TIME
                    if not skip_tradebook and ticker_ok:
                        url = (f"{base_url}/order-trade/trade-book"
                               f"?symbol={ticker}&group_by=GROUP_BY_TIME&time_interval={time_interval}")
                        resp = api_client.get(url)
                        if skip_flag.consume():
                            failed.append(ticker); ticker_ok = False
                        elif resp:
                            rows = parse_tradebook_time(ticker, resp, time_interval)
                            if rows:
                                w_tbt.writerows(rows)
                                f_tbt.flush()
                        time.sleep(delay)

                    # Orderbook
                    if not skip_orderbook and ticker_ok:
                        url = (f"{base_url}/company-price-feed/v2/orderbook/companies/{ticker}"
                               f"?with_full_price_tick=false")
                        resp = api_client.get(url)
                        if skip_flag.consume():
                            failed.append(ticker); ticker_ok = False
                        elif resp:
                            snap, bid_rows, offer_rows = parse_orderbook(ticker, resp)
                            if snap:
                                w_obs.writerow(snap)
                                f_obs.flush()
                            if bid_rows or offer_rows:
                                w_obl.writerows(bid_rows + offer_rows)
                                f_obl.flush()
                        time.sleep(delay)

                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    logger.error(f"[TRADEBOOK] {ticker}: {type(e).__name__} -- {e}")
                    failed.append(ticker)
                    ticker_ok = False

                if ticker_ok:
                    done_set.add(ticker)
                else:
                    if ticker not in failed:
                        failed.append(ticker)

                save_checkpoint(output_dir, {
                    "done"           : list(done_set),
                    "ts"             : ts,
                    "tradebook_price": tb_price_path,
                    "tradebook_time" : tb_time_path,
                    "orderbook_snapshot": ob_snap_path,
                    "orderbook_levels"  : ob_levels_path,
                })

    except KeyboardInterrupt:
        logger.warning("\n[TRADEBOOK] Interrupted. Progress saved. Use --resume to continue.")

    finally:
        skip_flag.stop()

    remaining = [t for t in tickers if t not in done_set]
    if not remaining and not failed:
        delete_checkpoint(output_dir)

    save_failed_tickers(failed, output_dir, ts)
    return tb_price_path, tb_time_path, ob_snap_path, ob_levels_path, failed


# CLI
def parse_args():
    parser = argparse.ArgumentParser(
        description="Scrape Trade Book & Orderbook dari Stockbit untuk saham IDX"
    )

    tg = parser.add_mutually_exclusive_group()
    tg.add_argument("--tickers",     nargs="+", metavar="TICKER")
    tg.add_argument("--ticker-file", type=str,  metavar="FILE")
    tg.add_argument("--retry-file",  type=str,  metavar="FILE")

    parser.add_argument(
        "--time-interval", type=str, default="10m",
        choices=["5m", "10m", "30m", "1h"],
        help="Interval waktu untuk Trade Book by Time (default: 10m)"
    )
    parser.add_argument("--skip-tradebook", action="store_true",
                        help="Skip Trade Book (price & time), hanya ambil Orderbook")
    parser.add_argument("--skip-orderbook", action="store_true",
                        help="Skip Orderbook, hanya ambil Trade Book")
    parser.add_argument("--delay",      type=float, default=0.1,
                        help="Detik antar request (default: 0.3)")
    parser.add_argument("--output-dir", type=str, default="output/tradebook",
                        help="Folder output (default: output/tradebook)")
    parser.add_argument(
        "--mirror-output-dir",
        type=str,
        default="/Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/tradebook",
        help=(
            "Folder mirror output kedua "
            "(default: /Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/tradebook). Gunakan '' untuk disable."
        ),
    )
    parser.add_argument("--resume",     action="store_true",
                        help="Lanjut dari checkpoint setelah Ctrl+C")
    parser.add_argument("--debug",      action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()

    if args.retry_file:
        tickers = load_tickers_from_file(args.retry_file)
        logger.info(f"[TRADEBOOK] Retry: {len(tickers)} tickers")
    elif args.tickers:
        tickers = [t.upper() for t in args.tickers]
    elif args.ticker_file:
        tickers = load_tickers_from_file(args.ticker_file)
        logger.info(f"[TRADEBOOK] Loaded {len(tickers)} tickers dari {args.ticker_file}")
    else:
        tickers = get_tickers_from_idx()

    if not tickers:
        logger.error("[TRADEBOOK] No tickers. Exiting.")
        sys.exit(1)

    req_per_ticker = sum([
        2 if not args.skip_tradebook else 0,
        1 if not args.skip_orderbook else 0,
    ])
    logger.info(
        f"[TRADEBOOK] Config | tickers: {len(tickers)} | "
        f"req_per_ticker: {req_per_ticker} | "
        f"time_interval: {args.time_interval} | "
        f"total_requests: {len(tickers) * req_per_ticker}"
    )

    start = time.time()
    tb_price_path, tb_time_path, ob_snap_path, ob_levels_path, failed = scrape(
        tickers        = tickers,
        time_interval  = args.time_interval,
        skip_tradebook = args.skip_tradebook,
        skip_orderbook = args.skip_orderbook,
        delay          = args.delay,
        output_dir     = args.output_dir,
        debug          = args.debug,
        resume         = args.resume,
    )

    mirrored_paths = mirror_outputs(
        paths=[
            tb_price_path,
            tb_time_path,
            ob_snap_path,
            ob_levels_path,
        ],
        mirror_dir=args.mirror_output_dir,
    )

    elapsed_min = (time.time() - start) / 60

    print(f"\n{'='*55}")
    print(f"  Trade Book & Orderbook Scrape Selesai")
    print(f"{'='*55}")
    print(f"  Tickers       : {len(tickers)}, {len(failed)} gagal")
    print(f"  TBook (price) : {tb_price_path}")
    print(f"  TBook (time)  : {tb_time_path}")
    print(f"  OBook snapshot: {ob_snap_path}")
    print(f"  OBook levels  : {ob_levels_path}")
    if mirrored_paths:
        print(f"  Mirror dir    : {args.mirror_output_dir}")
        for p in mirrored_paths:
            print(f"    - {p}")
    print(f"  Elapsed       : {elapsed_min:.2f} menit")
    print(f"{'='*55}\n")
    if failed:
        print(f"  Retry: python tradebook_scraper.py --retry-file <failed_file>")


if __name__ == "__main__":
    main()