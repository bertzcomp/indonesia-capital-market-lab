"""
keystats_scraper_fixed.py
===================
Scrape Key Statistics dari Stockbit untuk semua atau beberapa saham IDX.

Menghasilkan 3 file CSV per run:
  1. keystats_ratios_DATE.csv      — semua metric ratios (PE, ROE, dll)
  2. keystats_quarterly_DATE.csv   — data kuartalan (Net Income, EPS, Revenue)
  3. keystats_dividends_DATE.csv   — riwayat dividen per periode

Endpoint: GET https://exodus.stockbit.com/keystats/ratio/v1/{ticker}?year_limit=10

Usage:
    python keystats_scraper_fixed.py --ticker-file tickers.txt
    python keystats_scraper_fixed.py --tickers BBCA BBRI TLKM
    python keystats_scraper_fixed.py --ticker-file tickers.txt --resume
    python keystats_scraper_fixed.py --retry-file output/keystats/failed_tickers_xxx.txt
"""

import argparse
import csv
import json
import os
import shutil
import sys
import threading
import time
from datetime import date, datetime, timedelta

from dotenv import load_dotenv

from providers.stockbit import StockBit
from services.stockbit_api_client import StockbitApiClient
from utils.logger_config import logger

load_dotenv()

# CSV schemas
RATIOS_FIELDS = [
    "ticker", "category", "metric_name", "metric_id", "value",
]

QUARTERLY_FIELDS = [
    "ticker", "fitem_name", "most_recent_quarter_date", "most_recent_quarter_period",
    "year", "period", "quarter_value",
    "annualised_value", "ttm_value",
    "dividend", "payout_ratio", "dividend_yield",
]

DIVIDENDS_FIELDS = [
    "ticker", "period", "dividend", "ex_date", "payment_date",
]


# Parser
def parse_keystats(ticker: str, response: dict) -> dict:
    """
    Parse full keystats API response into 3 structured lists:
      - ratios:    [{ticker, category, metric_name, metric_id, value}]
      - quarterly: [{ticker, fitem_name, year, period, quarter_value, ...}]
      - dividends: [{ticker, period, dividend, ex_date, payment_date}]
    """
    ratios    = []
    quarterly = []
    dividends = []

    if not response or "data" not in response:
        return {"ratios": ratios, "quarterly": quarterly, "dividends": dividends}

    data = response["data"]

    # ------------------------------------------------------------------
    # 1. Ratios from closure_fin_items_results
    # ------------------------------------------------------------------
    for category_block in data.get("closure_fin_items_results", []):
        category_name = category_block.get("keystats_name", "")
        for item in category_block.get("fin_name_results", []):
            fitem = item.get("fitem", {})
            ratios.append({
                "ticker"      : ticker,
                "category"    : category_name,
                "metric_name" : fitem.get("name", ""),
                "metric_id"   : fitem.get("id", ""),
                "value"       : fitem.get("value", ""),
            })

    # ------------------------------------------------------------------
    # 2. Quarterly historical data from financial_year_parent
    # ------------------------------------------------------------------
    fyp = data.get("financial_year_parent", {})
    for group in fyp.get("financial_year_groups", []):
        fitem_name = group.get("fitem_name", "")
        mrq        = group.get("most_recent_quarter", {})
        mrq_date   = mrq.get("date", "")
        mrq_period = mrq.get("quarter", "")

        for yr_entry in group.get("financial_year_values", []):
            year            = yr_entry.get("year", "")
            annualised_val  = yr_entry.get("annualised_value", "")
            ttm_val         = yr_entry.get("ttm_value", "")
            div             = yr_entry.get("dividend", "")
            payout          = yr_entry.get("payout_ratio", "")
            div_yield       = yr_entry.get("dividend_yield", "")

            # One row per quarter
            for pv in yr_entry.get("period_values", []):
                quarterly.append({
                    "ticker"                    : ticker,
                    "fitem_name"                : fitem_name,
                    "most_recent_quarter_date"  : mrq_date,
                    "most_recent_quarter_period": mrq_period,
                    "year"                      : year,
                    "period"                    : pv.get("period", ""),
                    "quarter_value"             : pv.get("quarter_value", ""),
                    "annualised_value"          : annualised_val,
                    "ttm_value"                 : ttm_val,
                    "dividend"                  : div,
                    "payout_ratio"              : payout,
                    "dividend_yield"            : div_yield,
                })

    # Also include USD groups if present
    for group in fyp.get("financial_year_groups_usd", []):
        fitem_name = group.get("fitem_name", "") + " (USD)"
        mrq        = group.get("most_recent_quarter", {})
        mrq_date   = mrq.get("date", "")
        mrq_period = mrq.get("quarter", "")

        for yr_entry in group.get("financial_year_values", []):
            year           = yr_entry.get("year", "")
            annualised_val = yr_entry.get("annualised_value", "")
            ttm_val        = yr_entry.get("ttm_value", "")
            div            = yr_entry.get("dividend", "")
            payout         = yr_entry.get("payout_ratio", "")
            div_yield      = yr_entry.get("dividend_yield", "")

            for pv in yr_entry.get("period_values", []):
                quarterly.append({
                    "ticker"                    : ticker,
                    "fitem_name"                : fitem_name,
                    "most_recent_quarter_date"  : mrq_date,
                    "most_recent_quarter_period": mrq_period,
                    "year"                      : year,
                    "period"                    : pv.get("period", ""),
                    "quarter_value"             : pv.get("quarter_value", ""),
                    "annualised_value"          : annualised_val,
                    "ttm_value"                 : ttm_val,
                    "dividend"                  : div,
                    "payout_ratio"              : payout,
                    "dividend_yield"            : div_yield,
                })

    # ------------------------------------------------------------------
    # 3. Dividend history from dividend_group
    # ------------------------------------------------------------------
    div_group = data.get("dividend_group", {})
    for dv in div_group.get("dividend_year_values", []):
        dividends.append({
            "ticker"       : ticker,
            "period"       : dv.get("period", ""),
            "dividend"     : dv.get("dividend", ""),
            "ex_date"      : dv.get("ex_date", ""),
            "payment_date" : dv.get("payment_date", ""),
        })

    return {"ratios": ratios, "quarterly": quarterly, "dividends": dividends}


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
    return os.path.join(output_dir, ".keystats_checkpoint.json")

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
    logger.warning(f"[KEYSTATS] {len(failed)} failed -> {path}")


def mirror_outputs(paths, mirror_dir):
    """Copy final output files to secondary data/raw directory."""
    if not mirror_dir:
        return []

    os.makedirs(mirror_dir, exist_ok=True)
    copied = []

    for src in paths:
        if src and os.path.exists(src):
            dst = os.path.join(mirror_dir, os.path.basename(src))
            if os.path.abspath(src) != os.path.abspath(dst):
                shutil.copy2(src, dst)
            copied.append(dst)

    return copied


# Core scraping
def scrape_keystats(
    tickers, year_limit, delay, output_dir, debug, resume
):
    os.makedirs(output_dir, exist_ok=True)

    checkpoint  = load_checkpoint(output_dir) if resume else {}
    done_set    = set(checkpoint.get("done", []))
    ts          = checkpoint.get("ts", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    ratios_path = checkpoint.get("ratios_path",
                    os.path.join(output_dir, f"keystats_ratios_{ts}.csv"))
    qtr_path    = checkpoint.get("qtr_path",
                    os.path.join(output_dir, f"keystats_quarterly_{ts}.csv"))
    div_path    = checkpoint.get("div_path",
                    os.path.join(output_dir, f"keystats_dividends_{ts}.csv"))

    if resume and done_set:
        logger.info(f"[KEYSTATS] Resume: {len(done_set)} tickers already done")

    total      = len(tickers)
    failed     = []
    skip_flag  = SkipListener()
    api_client = StockbitApiClient()

    r_mode = "a" if (resume and os.path.exists(ratios_path)) else "w"
    q_mode = "a" if (resume and os.path.exists(qtr_path))    else "w"
    d_mode = "a" if (resume and os.path.exists(div_path))    else "w"

    logger.info(f"[KEYSTATS] Starting: {total} tickers | year_limit={year_limit}")
    logger.info(f"[KEYSTATS] Ratios   -> {ratios_path}")
    logger.info(f"[KEYSTATS] Quarterly-> {qtr_path}")
    logger.info(f"[KEYSTATS] Dividends-> {div_path}")

    try:
        with (
            open(ratios_path, r_mode, newline="", encoding="utf-8") as rf,
            open(qtr_path,    q_mode, newline="", encoding="utf-8") as qf,
            open(div_path,    d_mode, newline="", encoding="utf-8") as df,
        ):
            rw = csv.DictWriter(rf, fieldnames=RATIOS_FIELDS)
            qw = csv.DictWriter(qf, fieldnames=QUARTERLY_FIELDS)
            dw = csv.DictWriter(df, fieldnames=DIVIDENDS_FIELDS)

            if r_mode == "w": rw.writeheader()
            if q_mode == "w": qw.writeheader()
            if d_mode == "w": dw.writeheader()

            for idx, ticker in enumerate(tickers, start=1):
                if ticker in done_set:
                    continue

                if skip_flag.consume():
                    logger.warning(f"[KEYSTATS] SKIP (hotkey) -> {ticker}")
                    failed.append(ticker)
                    continue

                try:
                    if debug:
                        print(f"[KEYSTATS] {idx}/{total} -- {ticker}")
                    elif idx % 50 == 0 or idx == 1 or idx == total:
                        logger.info(f"[KEYSTATS] Progress: {idx}/{total} ({ticker})")

                    url  = f"https://exodus.stockbit.com/keystats/ratio/v1/{ticker}?year_limit={year_limit}"
                    resp = api_client.get(url)

                    if skip_flag.consume():
                        logger.warning(f"[KEYSTATS] SKIP (hotkey) -> {ticker}")
                        failed.append(ticker)
                        continue

                    if not resp:
                        logger.warning(f"[KEYSTATS] {ticker}: empty response")
                        failed.append(ticker)
                        time.sleep(delay)
                        continue

                    parsed = parse_keystats(ticker, resp)

                    if parsed["ratios"]:
                        rw.writerows(parsed["ratios"])
                    if parsed["quarterly"]:
                        qw.writerows(parsed["quarterly"])
                    if parsed["dividends"]:
                        dw.writerows(parsed["dividends"])

                    # flush to disk
                    rf.flush(); qf.flush(); df.flush()

                    done_set.add(ticker)
                    save_checkpoint(output_dir, {
                        "done"       : list(done_set),
                        "ts"         : ts,
                        "ratios_path": ratios_path,
                        "qtr_path"   : qtr_path,
                        "div_path"   : div_path,
                    })

                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    logger.error(f"[KEYSTATS] {ticker}: {type(e).__name__} -- {e}")
                    failed.append(ticker)

                time.sleep(delay)

    except KeyboardInterrupt:
        logger.warning("\n[KEYSTATS] Interrupted. Progress saved. Use --resume to continue.")

    finally:
        skip_flag.stop()

    remaining = [t for t in tickers if t not in done_set]
    if not remaining and not failed:
        delete_checkpoint(output_dir)

    save_failed_tickers(failed, output_dir, ts)
    return ratios_path, qtr_path, div_path, failed


# CLI
def parse_args():
    parser = argparse.ArgumentParser(
        description="Scrape Key Statistics dari Stockbit untuk saham IDX"
    )

    tg = parser.add_mutually_exclusive_group()
    tg.add_argument("--tickers", nargs="+", metavar="TICKER")
    tg.add_argument("--ticker-file", type=str, metavar="FILE")
    tg.add_argument("--retry-file",  type=str, metavar="FILE")

    parser.add_argument("--year-limit", type=int, default=10,
                        help="Jumlah tahun historical data (default: 10)")
    parser.add_argument("--delay",      type=float, default=0.3,
                        help="Detik antar request (default: 0.3)")
    parser.add_argument("--output-dir", type=str, default="output/keystats",
                        help="Folder output (default: output/keystats)")
    parser.add_argument("--mirror-output-dir", type=str, default="/Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/fundamental",
                        help="Folder mirror output kedua (default: /Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/fundamental). Gunakan '' untuk disable")
    parser.add_argument("--resume",     action="store_true",
                        help="Lanjut dari checkpoint setelah Ctrl+C")
    parser.add_argument("--debug",      action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()

    if args.retry_file:
        tickers = load_tickers_from_file(args.retry_file)
        logger.info(f"[KEYSTATS] Retry: {len(tickers)} tickers")
    elif args.tickers:
        tickers = [t.upper() for t in args.tickers]
    elif args.ticker_file:
        tickers = load_tickers_from_file(args.ticker_file)
        logger.info(f"[KEYSTATS] Loaded {len(tickers)} tickers from {args.ticker_file}")
    else:
        tickers = get_tickers_from_idx()

    if not tickers:
        logger.error("[KEYSTATS] No tickers. Exiting.")
        sys.exit(1)

    start = time.time()
    ratios_path, qtr_path, div_path, failed = scrape_keystats(
        tickers    = tickers,
        year_limit = args.year_limit,
        delay      = args.delay,
        output_dir = args.output_dir,
        debug      = args.debug,
        resume     = args.resume,
    )

    mirrored_paths = mirror_outputs(
        paths=[ratios_path, qtr_path, div_path],
        mirror_dir=args.mirror_output_dir,
    )

    elapsed_min = (time.time() - start) / 60

    print(f"\n{'='*55}")
    print(f"  Key Stats Scrape Selesai")
    print(f"{'='*55}")
    print(f"  Tickers   : {len(tickers)} diminta, {len(failed)} gagal")
    print(f"  Ratios    : {ratios_path}")
    print(f"  Quarterly : {qtr_path}")
    print(f"  Dividends : {div_path}")
    if mirrored_paths:
        print(f"  Mirror dir: {args.mirror_output_dir}")
        for p in mirrored_paths:
            print(f"    - {p}")
    print(f"  Elapsed   : {elapsed_min:.2f} menit")
    print(f"{'='*55}\n")
    if failed:
        print(f"  Retry: python keystats_scraper.py --retry-file <failed_file>")


if __name__ == "__main__":
    main()