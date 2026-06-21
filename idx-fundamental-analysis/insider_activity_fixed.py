"""
Scrape Insider Activity (major holder movements) from Stockbit.

Scope   : Semua saham IDX (global feed, bukan per ticker)
Endpoint: GET https://exodus.stockbit.com/insider/company/majorholder
Params  : date_start, date_end, page, limit=20, action_type, source_type
Paginasi: page=1,2,3,... sampai is_more == false (20 records per page)

Output CSV schema:
    id, date, ticker, insider_name, action_type,
    shares_changed, prev_shares, prev_pct, curr_shares, curr_pct,
    price, broker_code, nationality, source_type

Usage:
    python insider_activity_fixed.py --date-from 2021-01-01 --date-to 2021-07-30


    # Scrape 1 tahun penuh
    python insider_activity_fixed.py --date-from 2025-01-01 --date-to 2025-06-10

    # Scrape range pendek
    python insider_activity_fixed.py --date-from 2026-06-10 --date-to 2026-06-12

    
    # Filter hanya BUY
    python insider_activity_fixed.py --date-from 2025-01-01 --date-to 2025-12-31 --action-type BUY

    # Filter hanya KSEI source
    python insider_activity_fixed.py --date-from 2025-01-01 --date-to 2025-12-31 --source-type KSEI

    # Resume setelah Ctrl+C
    python insider_activity_fixed.py --date-from 2025-01-01 --date-to 2025-12-31 --resume
"""

import argparse
import csv
import json
import os
import shutil
import sys
import time
from datetime import datetime

from dotenv import load_dotenv

from services.stockbit_api_client import StockbitApiClient
from utils.logger_config import logger

load_dotenv()

# CSV schema
CSV_FIELDNAMES = [
    "id",
    "date",
    "ticker",
    "insider_name",
    "action_type",
    "shares_changed",
    "shares_changed_pct",
    "prev_shares",
    "prev_pct",
    "curr_shares",
    "curr_pct",
    "price",
    "broker_code",
    "broker_group",
    "nationality",
    "source_type",
    "source_label",
]


# Parser
def parse_movement(record: dict) -> dict:
    """Parse one insider movement record into a flat CSV row."""
    return {
        "id"                : record.get("id", ""),
        "date"              : record.get("date", ""),
        "ticker"            : record.get("symbol", ""),
        "insider_name"      : record.get("name", ""),
        "action_type"       : record.get("action_type", "").replace("ACTION_TYPE_", ""),
        "shares_changed"    : record.get("changes", {}).get("formatted_value", ""),
        "shares_changed_pct": record.get("changes", {}).get("percentage", ""),
        "prev_shares"       : record.get("previous", {}).get("value", ""),
        "prev_pct"          : record.get("previous", {}).get("percentage", ""),
        "curr_shares"       : record.get("current", {}).get("value", ""),
        "curr_pct"          : record.get("current", {}).get("percentage", ""),
        "price"             : record.get("price_formatted", ""),
        "broker_code"       : record.get("broker_detail", {}).get("code", ""),
        "broker_group"      : record.get("broker_detail", {}).get("group", "").replace("BROKER_GROUP_", ""),
        "nationality"       : record.get("nationality", "").replace("NATIONALITY_TYPE_", ""),
        "source_type"       : record.get("data_source", {}).get("type", "").replace("SOURCE_TYPE_", ""),
        "source_label"      : record.get("data_source", {}).get("label", ""),
    }


# Checkpoint helpers
def _cp_path(output_dir, date_from, date_to):
    return os.path.join(output_dir, f".insider_checkpoint_{date_from}_{date_to}.json")

def load_checkpoint(output_dir, date_from, date_to):
    p = _cp_path(output_dir, date_from, date_to)
    if os.path.exists(p):
        try:
            return json.load(open(p))
        except Exception:
            pass
    return {}

def save_checkpoint(output_dir, date_from, date_to, data):
    os.makedirs(output_dir, exist_ok=True)
    json.dump(data, open(_cp_path(output_dir, date_from, date_to), "w"))

def delete_checkpoint(output_dir, date_from, date_to):
    p = _cp_path(output_dir, date_from, date_to)
    if os.path.exists(p):
        os.remove(p)


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
def scrape_insider_activity(
    date_from, date_to,
    action_type, source_type,
    delay, output_dir, debug, resume,
):
    os.makedirs(output_dir, exist_ok=True)

    checkpoint  = load_checkpoint(output_dir, date_from, date_to) if resume else {}
    start_page  = checkpoint.get("last_page", 1)
    ts          = checkpoint.get("ts", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    csv_path    = checkpoint.get("csv_path",
                    os.path.join(output_dir,
                        f"insider_activity_{date_from}_to_{date_to}_{ts}.csv"))
    total_rows  = checkpoint.get("total_rows", 0)

    if resume and start_page > 1:
        logger.info(f"[INSIDER] Resume dari page {start_page}")

    file_mode    = "a" if (resume and os.path.exists(csv_path)) else "w"
    write_header = (file_mode == "w")

    # Build action_type and source_type param strings
    at_param = f"ACTION_TYPE_{action_type}" if action_type != "ALL" else "ACTION_TYPE_UNSPECIFIED"
    st_param = f"SOURCE_TYPE_{source_type}" if source_type != "ALL" else "SOURCE_TYPE_UNSPECIFIED"

    logger.info(
        f"[INSIDER] Starting: {date_from} -> {date_to} | "
        f"action={action_type} | source={source_type} | page_start={start_page}"
    )
    logger.info(f"[INSIDER] Output: {csv_path}")

    api_client = StockbitApiClient()
    page       = start_page
    is_more    = True

    try:
        with open(csv_path, file_mode, newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES)
            if write_header:
                writer.writeheader()

            while is_more:
                url = (
                    f"https://exodus.stockbit.com/insider/company/majorholder"
                    f"?date_start={date_from}&date_end={date_to}"
                    f"&page={page}&limit=20"
                    f"&action_type={at_param}&source_type={st_param}"
                )

                if debug:
                    print(f"[INSIDER] Fetching page {page}: {url}")
                elif page % 10 == 0 or page == 1:
                    logger.info(f"[INSIDER] Page {page} | total rows so far: {total_rows}")

                resp = api_client.get(url)

                if not resp or "data" not in resp:
                    logger.warning(f"[INSIDER] Page {page}: empty response, stopping")
                    break

                data       = resp["data"]
                is_more    = data.get("is_more", False)
                movements  = data.get("movement", [])

                if not movements:
                    logger.info(f"[INSIDER] Page {page}: no records, stopping")
                    break

                rows = [parse_movement(m) for m in movements]
                writer.writerows(rows)
                csvfile.flush()
                total_rows += len(rows)

                if debug:
                    print(f"[INSIDER] Page {page}: {len(rows)} records | total: {total_rows} | is_more: {is_more}")

                # save checkpoint after each page
                save_checkpoint(output_dir, date_from, date_to, {
                    "last_page" : page + 1,
                    "ts"        : ts,
                    "csv_path"  : csv_path,
                    "total_rows": total_rows,
                })

                page += 1
                time.sleep(delay)

    except KeyboardInterrupt:
        logger.warning(f"\n[INSIDER] Interrupted at page {page}. Progress saved.")
        logger.warning(f"[INSIDER] Resume: jalankan perintah yang sama dengan --resume")
        return csv_path, total_rows

    # Clean up checkpoint on successful completion
    delete_checkpoint(output_dir, date_from, date_to)
    logger.info(f"[INSIDER] Done. {total_rows} records -> {csv_path}")
    return csv_path, total_rows


# CLI
def parse_args():
    parser = argparse.ArgumentParser(
        description="Scrape Insider Activity dari Stockbit (semua saham IDX)"
    )

    parser.add_argument("--date-from", type=str, required=True, metavar="YYYY-MM-DD",
                        help="Tanggal mulai (required)")
    parser.add_argument("--date-to",   type=str, required=True, metavar="YYYY-MM-DD",
                        help="Tanggal akhir (required)")
    parser.add_argument("--action-type", type=str, default="ALL",
                        choices=["ALL", "BUY", "SELL"],
                        help="Filter action type (default: ALL)")
    parser.add_argument("--source-type", type=str, default="ALL",
                        choices=["ALL", "KSEI", "IDX"],
                        help="Filter sumber data (default: ALL)")
    parser.add_argument("--delay",      type=float, default=0.3,
                        help="Detik antar request (default: 0.3)")
    parser.add_argument("--output-dir", type=str, default="output/insider_activity",
                        help="Folder output (default: output/insider_activity)")
    parser.add_argument("--mirror-output-dir", type=str, default="/Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/insider_activity",
                        help="Folder mirror output kedua (default: /Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/insider_activity). Gunakan '' untuk disable")
    parser.add_argument("--resume",     action="store_true",
                        help="Lanjut dari checkpoint setelah Ctrl+C")
    parser.add_argument("--debug",      action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()

    start = time.time()
    csv_path, total_rows = scrape_insider_activity(
        date_from   = args.date_from,
        date_to     = args.date_to,
        action_type = args.action_type,
        source_type = args.source_type,
        delay       = args.delay,
        output_dir  = args.output_dir,
        debug       = args.debug,
        resume      = args.resume,
    )

    mirrored_paths = mirror_outputs(
        paths=[csv_path],
        mirror_dir=args.mirror_output_dir,
    )

    elapsed_min = (time.time() - start) / 60

    print(f"\n{'='*55}")
    print(f"  Insider Activity Scrape Selesai")
    print(f"{'='*55}")
    print(f"  Periode     : {args.date_from} -> {args.date_to}")
    print(f"  Action      : {args.action_type} | Source: {args.source_type}")
    print(f"  Total rows  : {total_rows}")
    print(f"  Output      : {csv_path}")
    if mirrored_paths:
        print(f"  Mirror      : {args.mirror_output_dir}")
        for p in mirrored_paths:
            print(f"    - {p}")
    print(f"  Elapsed     : {elapsed_min:.2f} menit")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()