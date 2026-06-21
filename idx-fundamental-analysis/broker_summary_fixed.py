"""
broker_summary.py
=================
Scrape EOD Broker Summary untuk semua saham IDX dari Stockbit.

Fitur:
  - Tekan  s + Enter  kapan saja untuk skip ticker yang sedang diproses
  - Checkpoint otomatis: Ctrl+C lalu --resume untuk lanjut dari posisi terakhir
  - Request timeout otomatis (tidak akan stuck selamanya)

Usage:

    python broker_summary_fixed.py --date 2026-06-12 --ticker-file tickers.txt

    


    python broker_summary_fixed.py --date 2026-04-28

    python broker_summary_fixed.py --date 2026-03-19 --tickers BBRI BKSL TLKM
    

    python broker_summary_fixed.py --date-from 2026-03-16 --date-to 2026-03-17
    python broker_summary_fixed.py --date 2026-03-19 --resume
    python broker_summary_fixed.py --date 2026-03-19 --retry-file output/broker_summary/failed_tickers_xxx.txt
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
from utils.logger_config import logger

load_dotenv()

# CSV schema
CSV_FIELDNAMES = [
    "stock_code", "date", "from", "to", "rank",
    "BY", "BY_type", "B.val", "B.lot", "B.freq", "B.avg",
    "SL", "SL_type", "S.val", "S.lot", "S.freq", "S.avg",
]


# Hotkey listener — background thread, non-blocking
class SkipListener:
    """
    Runs in a background daemon thread.
    Ketik  s  lalu Enter  untuk set flag skip_current = True.
    Main loop memeriksa flag ini setelah setiap ticker.
    """
    def __init__(self):
        self.skip_current  = False
        self.stop_listener = False
        self._thread = threading.Thread(target=self._listen, daemon=True)
        self._thread.start()

    def _listen(self):
        print("\n  [HOTKEY] Ketik  s  + Enter  kapan saja untuk skip ticker yang stuck.\n",
              flush=True)
        while not self.stop_listener:
            try:
                line = input()
                if line.strip().lower() == "s":
                    self.skip_current = True
                    print("  [HOTKEY] Skip akan dilakukan setelah request saat ini selesai/timeout.",
                          flush=True)
            except EOFError:
                break

    def consume(self) -> bool:
        """Return True (and reset) jika skip sedang diminta."""
        if self.skip_current:
            self.skip_current = False
            return True
        return False

    def stop(self):
        self.stop_listener = True


# Checkpoint helpers
def _checkpoint_path(output_dir: str, date_from: str, date_to: str) -> str:
    return os.path.join(output_dir, f".checkpoint_{date_from}_{date_to}.json")


def load_checkpoint(output_dir: str, date_from: str, date_to: str) -> dict:
    path = _checkpoint_path(output_dir, date_from, date_to)
    if os.path.exists(path):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save_checkpoint(output_dir: str, date_from: str, date_to: str, data: dict):
    path = _checkpoint_path(output_dir, date_from, date_to)
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f)


def delete_checkpoint(output_dir: str, date_from: str, date_to: str):
    path = _checkpoint_path(output_dir, date_from, date_to)
    if os.path.exists(path):
        os.remove(path)


# Helpers
def last_trading_day() -> str:
    d = date.today()
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d.strftime("%Y-%m-%d")


def load_tickers_from_file(path: str):
    tickers = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                tickers.append(line.upper())
    return tickers


def get_tickers_from_idx(is_full: bool = True):
    from providers.idx import IDX
    logger.info("Retrieving stock list from idx.co.id ...")
    idx = IDX(is_full_retrieve=is_full)
    stocks = idx.stocks()
    tickers = [s.ticker for s in stocks]
    logger.info(f"Retrieved {len(tickers)} tickers from IDX")
    return tickers


def save_failed_tickers(failed: list, output_dir: str, ts: str):
    if not failed:
        return
    path = os.path.join(output_dir, f"failed_tickers_{ts}.txt")
    with open(path, "w", encoding="utf-8") as f:
        for t in failed:
            f.write(t + "\n")
    logger.warning(f"[BROKSUM] {len(failed)} tickers failed -> {path}")


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
def scrape_broker_summary(
    tickers: list,
    date_from: str,
    date_to: str,
    transaction_type: str,
    market_board: str,
    investor_type: str,
    limit: int,
    delay: float,
    output_dir: str,
    debug: bool,
    resume: bool,
):
    os.makedirs(output_dir, exist_ok=True)

    # --- checkpoint / resume ---
    checkpoint = load_checkpoint(output_dir, date_from, date_to) if resume else {}
    done_set   = set(checkpoint.get("done", []))
    csv_path   = checkpoint.get("csv_path", None)
    ts         = checkpoint.get("ts", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

    if resume and done_set:
        logger.info(f"[BROKSUM] Resume: {len(done_set)} ticker sudah selesai, melanjutkan...")
    else:
        # fresh run
        done_set = set()
        ts       = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        csv_path = os.path.join(output_dir,
                                f"broker_summary_{date_from}_to_{date_to}_{ts}.csv")

    total      = len(tickers)
    failed     = []
    total_rows = 0
    skip_flag  = SkipListener()

    logger.info(f"[BROKSUM] Starting: {total} tickers | {date_from} -> {date_to} | {transaction_type}")
    logger.info(f"[BROKSUM] Output  : {csv_path}")
    logger.info(f"[BROKSUM] Timeout : 20s per request (auto-skip on timeout)")

    # open CSV: append jika resume, baru jika fresh
    file_mode  = "a" if (resume and os.path.exists(csv_path)) else "w"
    write_header = (file_mode == "w")

    sb = StockBit(stocks=[])

    try:
        with open(csv_path, file_mode, newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES)
            if write_header:
                writer.writeheader()

            for idx, ticker in enumerate(tickers, start=1):

                # skip ticker yang sudah selesai (resume mode)
                if ticker in done_set:
                    continue

                # --- cek hotkey skip SEBELUM request ---
                if skip_flag.consume():
                    logger.warning(f"[BROKSUM] SKIP (hotkey) -> {ticker}")
                    failed.append(ticker)
                    continue

                try:
                    if debug:
                        print(f"[BROKSUM] {idx}/{total} -- {ticker}")
                    elif idx % 50 == 0 or idx == total or idx == 1:
                        logger.info(f"[BROKSUM] Progress: {idx}/{total} ({ticker})")

                    summary = sb.get_broker_summary(
                        ticker=ticker,
                        date_from=date_from,
                        date_to=date_to,
                        transaction_type=transaction_type,
                        market_board=market_board,
                        investor_type=investor_type,
                        limit=limit,
                        debug=debug,
                    )

                    # --- cek hotkey skip SETELAH request ---
                    if skip_flag.consume():
                        logger.warning(f"[BROKSUM] SKIP (hotkey) -> {ticker} (setelah request)")
                        failed.append(ticker)
                        continue

                    if not summary:
                        logger.warning(f"[BROKSUM] {ticker}: empty response, skipping")
                        failed.append(ticker)
                        time.sleep(delay)
                        continue

                    buys   = summary.get("brokers_buy", [])
                    sells  = summary.get("brokers_sell", [])
                    max_len = max(len(buys), len(sells)) if (buys or sells) else 0

                    for i in range(max_len):
                        b = buys[i]  if i < len(buys)  else {}
                        s = sells[i] if i < len(sells) else {}
                        row_date = b.get("netbs_date") or s.get("netbs_date") or ""

                        row = {
                            "stock_code" : summary["symbol"],
                            "date"       : row_date,
                            "from"       : summary["from"],
                            "to"         : summary["to"],
                            "rank"       : i + 1,
                            "BY"         : b.get("netbs_broker_code", ""),
                            "BY_type"    : b.get("type", ""),
                            "B.val"      : b.get("bval", ""),
                            "B.lot"      : b.get("blot", ""),
                            "B.freq"     : b.get("freq", ""),
                            "B.avg"      : b.get("netbs_buy_avg_price", ""),
                            "SL"         : s.get("netbs_broker_code", ""),
                            "SL_type"    : s.get("type", ""),
                            "S.val"      : s.get("sval", ""),
                            "S.lot"      : s.get("slot", ""),
                            "S.freq"     : s.get("freq", ""),
                            "S.avg"      : s.get("netbs_sell_avg_price", ""),
                        }
                        writer.writerow(row)
                        total_rows += 1

                    csvfile.flush()  # tulis ke disk setelah setiap ticker

                    # tandai selesai & simpan checkpoint
                    done_set.add(ticker)
                    save_checkpoint(output_dir, date_from, date_to, {
                        "done"    : list(done_set),
                        "csv_path": csv_path,
                        "ts"      : ts,
                    })

                except KeyboardInterrupt:
                    raise  # tangkap di luar loop

                except Exception as e:
                    # Timeout masuk sini (requests.exceptions.ReadTimeout)
                    logger.error(f"[BROKSUM] {ticker}: {type(e).__name__} -- {e}")
                    failed.append(ticker)

                time.sleep(delay)

    except KeyboardInterrupt:
        logger.warning("\n[BROKSUM] Dihentikan (Ctrl+C). Progress sudah tersimpan.")
        logger.warning(f"[BROKSUM] Untuk lanjut: jalankan perintah yang sama dengan --resume")

    finally:
        skip_flag.stop()

    # hapus checkpoint kalau semua selesai (tidak ada interrupt)
    remaining = [t for t in tickers if t not in done_set]
    if not remaining and not failed:
        delete_checkpoint(output_dir, date_from, date_to)

    logger.info(f"[BROKSUM] Done. {total_rows} rows -> {csv_path}")
    save_failed_tickers(failed, output_dir, ts)
    return csv_path, total_rows, failed


# CLI
def parse_args():
    parser = argparse.ArgumentParser(
        description="Scrape EOD Broker Summary untuk saham IDX dari Stockbit",
    )

    date_group = parser.add_mutually_exclusive_group()
    date_group.add_argument("--date", type=str, metavar="YYYY-MM-DD",
                            help="Satu tanggal. Default: last trading day.")
    date_group.add_argument("--date-from", type=str, metavar="YYYY-MM-DD",
                            help="Tanggal mulai range")
    parser.add_argument("--date-to", type=str, metavar="YYYY-MM-DD",
                        help="Tanggal akhir range (dipakai bersama --date-from)")

    ticker_group = parser.add_mutually_exclusive_group()
    ticker_group.add_argument("--tickers", nargs="+", metavar="TICKER",
                              help="Ticker spesifik, misal: BBRI BKSL TLKM")
    ticker_group.add_argument("--ticker-file", type=str, metavar="FILE",
                              help="File teks dengan satu ticker per baris")
    ticker_group.add_argument("--retry-file", type=str, metavar="FILE",
                              help="Retry dari failed_tickers_*.txt hasil run sebelumnya")

    parser.add_argument("--transaction-type", type=str, default="TRANSACTION_TYPE_GROSS",
                        choices=["TRANSACTION_TYPE_GROSS", "TRANSACTION_TYPE_NET"],
                        help="Tipe transaksi (default: GROSS)")
    parser.add_argument("--market-board", type=str, default="MARKET_BOARD_ALL",
                        help="Market board (default: MARKET_BOARD_ALL)")
    parser.add_argument("--investor-type", type=str, default="INVESTOR_TYPE_ALL",
                        choices=["INVESTOR_TYPE_ALL", "INVESTOR_TYPE_FOREIGN", "INVESTOR_TYPE_LOCAL"])
    parser.add_argument("--limit", type=int, default=25,
                        help="Jumlah broker per sisi (default: 25)")
    parser.add_argument("--delay", type=float, default=0.1,
                        help="Detik antar request (default: 0.1)")
    parser.add_argument("--output-dir", type=str, default="output/broker_summary",
                        help="Folder output CSV (default: output/broker_summary)")
    parser.add_argument("--mirror-output-dir", type=str, default="/Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/broker_summary",
                        help="Folder mirror output kedua (default: /Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/broker_summary). Gunakan '' untuk disable")
    parser.add_argument("--resume", action="store_true",
                        help="Lanjut dari checkpoint terakhir (setelah Ctrl+C)")
    parser.add_argument("--debug", action="store_true",
                        help="Verbose debug output")

    return parser.parse_args()


def main():
    args = parse_args()

    # resolve dates
    if args.date:
        date_from = date_to = args.date
    elif args.date_from:
        date_from = args.date_from
        date_to   = args.date_to if args.date_to else args.date_from
    else:
        date_from = date_to = last_trading_day()
        logger.info(f"[BROKSUM] No date specified -> last trading day: {date_from}")

    # resolve tickers
    if args.retry_file:
        tickers = load_tickers_from_file(args.retry_file)
        logger.info(f"[BROKSUM] Retry: {len(tickers)} tickers dari {args.retry_file}")
    elif args.tickers:
        tickers = [t.upper() for t in args.tickers]
    elif args.ticker_file:
        tickers = load_tickers_from_file(args.ticker_file)
        logger.info(f"[BROKSUM] Loaded {len(tickers)} tickers dari {args.ticker_file}")
    else:
        tickers = get_tickers_from_idx(is_full=True)

    if not tickers:
        logger.error("[BROKSUM] Tidak ada ticker. Keluar.")
        sys.exit(1)

    logger.info(
        f"[BROKSUM] Config | tickers: {len(tickers)} | "
        f"date: {date_from}->{date_to} | type: {args.transaction_type} | "
        f"board: {args.market_board} | investor: {args.investor_type} | "
        f"limit: {args.limit} | delay: {args.delay}s"
    )

    start = time.time()

    csv_path, total_rows, failed = scrape_broker_summary(
        tickers=tickers,
        date_from=date_from,
        date_to=date_to,
        transaction_type=args.transaction_type,
        market_board=args.market_board,
        investor_type=args.investor_type,
        limit=args.limit,
        delay=args.delay,
        output_dir=args.output_dir,
        debug=args.debug,
        resume=args.resume,
    )


    mirrored_paths = mirror_outputs(
        paths=[csv_path],
        mirror_dir=args.mirror_output_dir,
    )

    elapsed_min = (time.time() - start) / 60

    print(f"\n{'='*55}")
    print(f"  Broker Summary Scrape Selesai")
    print(f"{'='*55}")
    print(f"  Date range  : {date_from} -> {date_to}")
    print(f"  Tickers     : {len(tickers)} diminta, {len(failed)} gagal")
    print(f"  Rows saved  : {total_rows}")
    print(f"  Output      : {csv_path}")
    if mirrored_paths:
        print(f"  Mirror      : {args.mirror_output_dir}")
        for p in mirrored_paths:
            print(f"    - {p}")
    print(f"  Elapsed     : {elapsed_min:.2f} menit")
    print(f"{'='*55}\n")

    if failed:
        print(f"  Gagal : {failed}")
        print(f"  Retry : python broker_summary.py --date {date_from} --retry-file <failed_file>")
    else:
        print("  Semua ticker berhasil diproses.")


if __name__ == "__main__":
    main()