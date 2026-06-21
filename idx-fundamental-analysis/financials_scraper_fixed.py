"""
financials_scraper.py
=====================
Scrape Financial Statements from Stockbit fro all stocks in IDX.
Menghasilkan data Income Statement, Balance Sheet, dan Cash Flow
dalam format long CSV (satu baris per metric per period).

Endpoint: GET https://exodus.stockbit.com/findata-view/company/financial
Params:
  symbol         : ticker (e.g. BBCA)
  data_type      : 1 = As Reported (satu-satunya pilihan)
  report_type    : 1=Income Statement, 2=Balance Sheet, 3=Cash Flow
  statement_type : 1=Quarterly, 2=Annual, 3=TTM, 4=Interim YTD, ...13=3yr CAGR

Output CSV schema (long format):
  ticker, report_type_id, report_type_name, statement_type_id, statement_type_name,
  period_label, period_display, metric_name, metric_level,
  value_idr, value_usd, value_pct
m
Usage:
    # Scrape semua report types, Quarterly + Annual untuk semua IDX
    python financials_scraper.py --ticker-file tickers.txt

    # Ticker spesifik, semua kombinasi
    python financials_scraper.py --tickers BBCA BBRI TLKM

    # Hanya Income Statement Quarterly
    python financials_scraper.py --tickers BBCA --report-types 1 --statement-types 1

    # Resume setelah Ctrl+C
    python financials_scraper.py --ticker-file tickers.txt --resumem

    # Retry failed
    python financials_scraper.py --retry-file output/financials/failed_tickers_xxx.txt
"""

import argparse
import csv
import json
import os
import shutil
import sys
import threading
import time
from datetime import datetime

from dotenv import load_dotenv

try:
    from bs4 import BeautifulSoup
except ImportError:
    raise ImportError("beautifulsoup4 not installed. Run: pip install beautifulsoup4")

from services.stockbit_api_client import StockbitApiClient
from utils.logger_config import logger

load_dotenv()

# Constants
BASE_URL = "https://exodus.stockbit.com"

REPORT_TYPES = {
    1: "Income Statement",
    2: "Balance Sheet",
    3: "Cash Flow",
}

STATEMENT_TYPES = {
    1:  "Quarterly",
    2:  "Annual",
    3:  "TTM",
    4:  "Interim YTD",
    5:  "LTM",
    6:  "5 Year Average",
    7:  "10 Year Average",
    8:  "3 Year Growth",
    9:  "5 Year Growth",
    10: "10 Year Growth",
    11: "1 Year CAGR",
    12: "3 Year CAGR (Alt)",
    13: "3 Year CAGR",
}

# Default combinations to scrape (most useful for fundamental analysis)
DEFAULT_REPORT_TYPES     = [1, 2, 3]       # all 3 statements
DEFAULT_STATEMENT_TYPES  = [1, 2]          # Quarterly + Annual

CSV_FIELDNAMES = [
    "ticker",
    "report_type_id",
    "report_type_name",
    "statement_type_id",
    "statement_type_name",
    "period_label",
    "period_display",
    "metric_name",
    "metric_level",
    "value_idr",
    "value_usd",
    "value_pct",
]


# HTML parser
def _clean(val: str) -> str:
    return val.strip().replace("\xa0", "")

def parse_financial_html(
    html: str,
    ticker: str,
    report_type_id: int,
    statement_type_id: int,
) -> list:
    """
    Parse html_report from Stockbit financials response.
    Returns list of flat dicts ready for CSV.

    HTML structure:
      <thead><tr>
        <th class='info'>In Million</th>
        <th class='periods-list' data-label='Q108'>Q1 2008</th>
        ...
      </tr></thead>
      <tbody>
        <tr class='dtr ... row1 ...'>
          <td class='r_head'><span class='acc-name' data-lang-1='Total Revenue'>...</span></td>
          <td class='rowval val1 ...' data-raw='...' data-value-idr='...' data-value-usd='...' data-percentage='...'> ... </td>
          ...
        </tr>
        ...
      </tbody>
    """
    rows     = []
    rtn      = REPORT_TYPES.get(report_type_id, str(report_type_id))
    stn      = STATEMENT_TYPES.get(statement_type_id, str(statement_type_id))

    if not html or not html.strip():
        return rows

    try:
        soup = BeautifulSoup(html, "html.parser")
    except Exception as e:
        logger.warning(f"[FINANCIALS] HTML parse error for {ticker}: {e}")
        return rows

    # --- Extract column headers (periods) ---
    # <th class='periods-list' data-label='Q108'>Q1 2008</th>
    headers = []
    for th in soup.select("thead th.periods-list"):
        label   = th.get("data-label", "")
        display = _clean(th.get_text())
        headers.append((label, display))

    if not headers:
        return rows

    # --- Extract data rows ---
    for tr in soup.select("tbody tr"):
        # Get metric name from acc-name span
        acc_span = tr.select_one("span.acc-name")
        if not acc_span:
            acc_span = tr.select_one("td:first-child")
        if not acc_span:
            continue

        # Use English name (data-lang-1) if available, else Indonesian
        metric_name = (
            acc_span.get("data-lang-1")
            or acc_span.get("data-lang-1-full")
            or _clean(acc_span.get_text())
        )
        if not metric_name:
            continue

        # Determine hierarchy level from tr class (row1, row2, ... = depth)
        tr_classes = tr.get("class", [])
        level = 1
        for cls in tr_classes:
            if cls.startswith("row") and cls[3:].isdigit():
                level = int(cls[3:])
                break

        # Get value cells — only cells with class 'rowval'
        val_cells = tr.select("td.rowval")

        for i, td in enumerate(val_cells):
            if i >= len(headers):
                break
            period_label, period_display = headers[i]

            raw_val  = td.get("data-raw", "").strip()
            val_idr  = td.get("data-value-idr", "").strip()
            val_usd  = td.get("data-value-usd", "").strip()
            val_pct  = td.get("data-percentage", "").strip()

            # Skip if raw value is '-' or missing
            if raw_val in ("-", "", "0") and val_idr in ("0", ""):
                val_idr = ""
                val_usd = ""

            rows.append({
                "ticker"             : ticker,
                "report_type_id"     : report_type_id,
                "report_type_name"   : rtn,
                "statement_type_id"  : statement_type_id,
                "statement_type_name": stn,
                "period_label"       : period_label,
                "period_display"     : period_display,
                "metric_name"        : metric_name,
                "metric_level"       : level,
                "value_idr"          : val_idr,
                "value_usd"          : val_usd,
                "value_pct"          : val_pct,
            })

    return rows


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
    return os.path.join(output_dir, ".financials_checkpoint.json")

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
    logger.warning(f"[FINANCIALS] {len(failed)} failed -> {path}")


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
def scrape_financials(
    tickers, report_types, statement_types,
    delay, output_dir, debug, resume,
):
    os.makedirs(output_dir, exist_ok=True)

    checkpoint  = load_checkpoint(output_dir) if resume else {}
    done_set    = set(checkpoint.get("done", []))    # "BBCA_1_1" format
    ts          = checkpoint.get("ts", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    csv_path    = checkpoint.get("csv_path",
                    os.path.join(output_dir, f"financials_{ts}.csv"))
    total_rows  = checkpoint.get("total_rows", 0)

    if resume and done_set:
        logger.info(f"[FINANCIALS] Resume: {len(done_set)} ticker-statement combos already done")

    # Build all combinations
    combos = [
        (rt, st)
        for rt in report_types
        for st in statement_types
    ]
    total_tickers = len(tickers)
    total_combos  = len(combos)
    failed        = []
    skip_flag     = SkipListener()
    api_client    = StockbitApiClient()

    file_mode    = "a" if (resume and os.path.exists(csv_path)) else "w"
    write_header = (file_mode == "w")

    logger.info(
        f"[FINANCIALS] Starting: {total_tickers} tickers x "
        f"{total_combos} combos = {total_tickers * total_combos} requests"
    )
    logger.info(f"[FINANCIALS] Report types   : {[REPORT_TYPES[r] for r in report_types]}")
    logger.info(f"[FINANCIALS] Statement types: {[STATEMENT_TYPES[s] for s in statement_types]}")
    logger.info(f"[FINANCIALS] Output: {csv_path}")

    try:
        with open(csv_path, file_mode, newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES)
            if write_header:
                writer.writeheader()

            for t_idx, ticker in enumerate(tickers, start=1):

                if skip_flag.consume():
                    logger.warning(f"[FINANCIALS] SKIP (hotkey) -> {ticker}")
                    for rt, st in combos:
                        failed.append(f"{ticker}_{rt}_{st}")
                    continue

                ticker_has_error = False

                for rt, st in combos:
                    combo_key = f"{ticker}_{rt}_{st}"

                    if combo_key in done_set:
                        continue

                    try:
                        if debug:
                            print(f"[FINANCIALS] {t_idx}/{total_tickers} {ticker} | "
                                  f"report={REPORT_TYPES[rt]} | stmt={STATEMENT_TYPES[st]}")
                        elif t_idx % 50 == 0 or t_idx == 1 or t_idx == total_tickers:
                            logger.info(
                                f"[FINANCIALS] Progress: {t_idx}/{total_tickers} ({ticker}) | "
                                f"rows so far: {total_rows}"
                            )

                        url = (
                            f"{BASE_URL}/findata-view/company/financial"
                            f"?symbol={ticker}&data_type=1"
                            f"&report_type={rt}&statement_type={st}"
                        )
                        resp = api_client.get(url)

                        if skip_flag.consume():
                            logger.warning(f"[FINANCIALS] SKIP (hotkey) -> {ticker}")
                            ticker_has_error = True
                            break

                        if not resp or "data" not in resp:
                            logger.warning(f"[FINANCIALS] {combo_key}: empty response")
                            failed.append(combo_key)
                            time.sleep(delay)
                            continue

                        html = resp["data"].get("html_report", "")
                        if not html:
                            logger.debug(f"[FINANCIALS] {combo_key}: no html_report")
                            done_set.add(combo_key)
                            time.sleep(delay)
                            continue

                        rows = parse_financial_html(html, ticker, rt, st)

                        if rows:
                            writer.writerows(rows)
                            csvfile.flush()
                            total_rows += len(rows)

                        done_set.add(combo_key)
                        save_checkpoint(output_dir, {
                            "done"      : list(done_set),
                            "ts"        : ts,
                            "csv_path"  : csv_path,
                            "total_rows": total_rows,
                        })

                    except KeyboardInterrupt:
                        raise
                    except Exception as e:
                        logger.error(f"[FINANCIALS] {combo_key}: {type(e).__name__} -- {e}")
                        failed.append(combo_key)

                    time.sleep(delay)

                if ticker_has_error:
                    for rt, st in combos:
                        failed.append(f"{ticker}_{rt}_{st}")

    except KeyboardInterrupt:
        logger.warning(
            f"\n[FINANCIALS] Interrupted. Progress saved ({len(done_set)} combos done).\n"
            f"[FINANCIALS] Resume: jalankan perintah yang sama dengan --resume"
        )

    finally:
        skip_flag.stop()

    # Clean checkpoint only if fully complete
    remaining = [
        f"{t}_{rt}_{st}"
        for t in tickers
        for rt, st in combos
        if f"{t}_{rt}_{st}" not in done_set
    ]
    if not remaining and not failed:
        delete_checkpoint(output_dir)

    logger.info(f"[FINANCIALS] Done. {total_rows} rows -> {csv_path}")
    save_failed_tickers(failed, output_dir, ts)
    return csv_path, total_rows, failed


# CLI
def parse_args():
    parser = argparse.ArgumentParser(
        description="Scrape Financial Statements dari Stockbit untuk saham IDX"
    )

    tg = parser.add_mutually_exclusive_group()
    tg.add_argument("--tickers",     nargs="+", metavar="TICKER")
    tg.add_argument("--ticker-file", type=str,  metavar="FILE")
    tg.add_argument("--retry-file",  type=str,  metavar="FILE",
                    help="Retry dari failed_tickers_*.txt (isi: TICKER_RT_ST format)")

    parser.add_argument(
        "--report-types", nargs="+", type=int,
        default=DEFAULT_REPORT_TYPES,
        choices=list(REPORT_TYPES.keys()),
        metavar="N",
        help=f"Report types: {REPORT_TYPES} (default: 1 2 3 = semua)"
    )
    parser.add_argument(
        "--statement-types", nargs="+", type=int,
        default=DEFAULT_STATEMENT_TYPES,
        choices=list(STATEMENT_TYPES.keys()),
        metavar="N",
        help=f"Statement types: 1=Quarterly 2=Annual 3=TTM ... (default: 1 2)"
    )
    parser.add_argument("--delay",      type=float, default=0.3,
                        help="Detik antar request (default: 0.3)")
    parser.add_argument("--output-dir", type=str, default="output/financials",
                        help="Folder output (default: output/financials)")
    parser.add_argument("--mirror-output-dir", type=str, default="/Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/fundamental",
                        help="Folder mirror output kedua (default: /Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/fundamental). Gunakan '' untuk disable")
    parser.add_argument("--resume",     action="store_true",
                        help="Lanjut dari checkpoint setelah Ctrl+C")
    parser.add_argument("--debug",      action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()

    # Resolve tickers
    if args.retry_file:
        # retry file may contain "BBCA_1_1" or just "BBCA"
        raw = load_tickers_from_file(args.retry_file)
        # extract unique tickers
        tickers = list(dict.fromkeys(r.split("_")[0] for r in raw))
        logger.info(f"[FINANCIALS] Retry: {len(tickers)} tickers")
    elif args.tickers:
        tickers = [t.upper() for t in args.tickers]
    elif args.ticker_file:
        tickers = load_tickers_from_file(args.ticker_file)
        logger.info(f"[FINANCIALS] Loaded {len(tickers)} tickers from {args.ticker_file}")
    else:
        tickers = get_tickers_from_idx()

    if not tickers:
        logger.error("[FINANCIALS] No tickers. Exiting.")
        sys.exit(1)

    combos = len(args.report_types) * len(args.statement_types)
    logger.info(
        f"[FINANCIALS] Config | tickers: {len(tickers)} | "
        f"report_types: {args.report_types} | statement_types: {args.statement_types} | "
        f"total requests: {len(tickers) * combos}"
    )

    start = time.time()
    csv_path, total_rows, failed = scrape_financials(
        tickers        = tickers,
        report_types   = args.report_types,
        statement_types= args.statement_types,
        delay          = args.delay,
        output_dir     = args.output_dir,
        debug          = args.debug,
        resume         = args.resume,
    )

    mirrored_paths = mirror_outputs(
        paths=[csv_path],
        mirror_dir=args.mirror_output_dir,
    )

    elapsed_min = (time.time() - start) / 60

    print(f"\n{'='*55}")
    print(f"  Financial Statements Scrape Selesai")
    print(f"{'='*55}")
    print(f"  Tickers       : {len(tickers)}")
    print(f"  Combinations  : {combos} per ticker")
    print(f"  Total rows    : {total_rows}")
    print(f"  Failed combos : {len(failed)}")
    print(f"  Output        : {csv_path}")
    if mirrored_paths:
        print(f"  Mirror        : {args.mirror_output_dir}")
        for p in mirrored_paths:
            print(f"    - {p}")
    print(f"  Elapsed       : {elapsed_min:.2f} menit")
    print(f"{'='*55}\n")
    if failed:
        print(f"  Retry: python financials_scraper.py --retry-file <failed_file>")


if __name__ == "__main__":
    main()