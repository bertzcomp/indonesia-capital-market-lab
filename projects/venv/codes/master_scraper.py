import os
import subprocess
import sys
import glob
import pandas as pd
from datetime import datetime, timedelta
import time
import random


def read_stock_list(filename="idx_stocks.txt"):
    with open(filename, "r") as f:
        stocks = [line.strip() for line in f if line.strip()]
    return stocks


def split_list(lst, n):
    """Membagi list menjadi n bagian (sebanyak mungkin merata)."""
    k, m = divmod(len(lst), n)
    return [lst[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]


def generate_weekdays(start, end):
    dates = []
    current = start
    while current <= end:
        if current.weekday() < 5:
            dates.append(current.strftime('%Y-%m-%d'))
        current += timedelta(days=1)
    return dates


def parse_date_input(date_str: str) -> datetime:
    """
    Parse input tanggal — menerima format YYYY-MM-DD atau YYYYMMDD.
    Raise ValueError dengan pesan jelas jika format tidak dikenali.
    """
    date_str = date_str.strip()
    for fmt in ('%Y-%m-%d', '%Y%m%d'):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Format tanggal tidak dikenali: '{date_str}'. Gunakan YYYY-MM-DD atau YYYYMMDD.")


def input_date(prompt: str) -> datetime:
    """Minta input tanggal dari user dengan validasi dan retry."""
    while True:
        raw = input(prompt).strip()
        try:
            dt = parse_date_input(raw)
            print(f"   ✅ {dt.strftime('%Y-%m-%d')}")
            return dt
        except ValueError as e:
            print(f"   ❌ {e}")


def combine_files(date_list, output_dir, base_name="broksum"):
    """Menggabungkan semua file part (CSV) per tanggal menjadi satu file final dan menghapus part."""
    for date_str in date_list:
        date_formatted = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d-%m-%Y')
        pattern = os.path.join(output_dir, f"{base_name}_{date_formatted}_IDX_part*.csv")
        part_files = glob.glob(pattern)

        if not part_files:
            continue

        all_dfs = []
        for part_file in sorted(part_files):
            try:
                df = pd.read_csv(part_file)
                all_dfs.append(df)
            except Exception as e:
                print(f"Gagal membaca {part_file}: {e}")

        if all_dfs:
            combined_df = pd.concat(all_dfs, ignore_index=True)
            output_file = os.path.join(output_dir, f"{base_name}_{date_formatted}_IDX.csv")
            combined_df.to_csv(output_file, index=False)
            print(f"Gabungan untuk {date_formatted} disimpan ke {output_file} "
                  f"({len(combined_df):,} rows)")

            # Hapus file part agar tidak menumpuk
            for part_file in part_files:
                try:
                    os.remove(part_file)
                except OSError as e:
                    print(f"Error menghapus {part_file}: {e}")
            print(f"File part sementara untuk {date_formatted} telah dibersihkan.")


def main():
    base_name  = "broksum"
    output_dir = "../data/raw"
    os.makedirs(output_dir, exist_ok=True)

    # ── Input tanggal ──────────────────────────────────────────────────
    print("=" * 55)
    print("  BROKER SUMMARY SCRAPER")
    print("  Format tanggal: YYYY-MM-DD  atau  YYYYMMDD")
    print("=" * 55)

    start_date = input_date("\nTanggal mulai  : ")
    end_date   = input_date("Tanggal selesai: ")

    if end_date < start_date:
        print("❌ Tanggal selesai tidak boleh sebelum tanggal mulai.")
        sys.exit(1)

    # ── Baca daftar saham ──────────────────────────────────────────────
    all_stocks = read_stock_list("idx_stocks.txt")
    print(f"\nTotal saham: {len(all_stocks)}")

    # ── Input jumlah split ─────────────────────────────────────────────
    while True:
        try:
            split_num = int(input("Masukkan jumlah split (misal 5, 10, 20, 50): "))
            if split_num < 1:
                raise ValueError
            break
        except ValueError:
            print("   ❌ Input tidak valid. Masukkan angka bulat positif.")

    chunks = split_list(all_stocks, split_num)
    print(f"Dibagi menjadi {len(chunks)} bagian.")

    # ── Generate daftar tanggal ────────────────────────────────────────
    date_list = generate_weekdays(start_date, end_date)
    print(f"Tanggal yang akan diproses ({len(date_list)} hari): {date_list}")

    # ── Konfirmasi ─────────────────────────────────────────────────────
    confirm = input("\nLanjutkan? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Dibatalkan.")
        sys.exit(0)

    # ── Jalankan worker per chunk secara paralel ───────────────────────
    processes = []
    for i, chunk in enumerate(chunks):
        if not chunk:
            continue
        codes_str = ",".join(chunk)
        cmd = [
            sys.executable,
            "scraper_worker.py",
            "--part",   str(i + 1),
            "--codes",  codes_str,
            "--start",  start_date.strftime("%Y-%m-%d"),
            "--end",    end_date.strftime("%Y-%m-%d"),
            "--outdir", output_dir,
        ]
        print(f"Menjalankan part {i+1} ({len(chunk)} saham)...")
        p = subprocess.Popen(cmd)
        processes.append(p)
        # Jeda kecil agar tidak semua proses langsung hit server bersamaan
        time.sleep(random.uniform(2, 5))

    # ── Tunggu semua selesai ───────────────────────────────────────────
    for p in processes:
        p.wait()
    print("\nSemua proses worker selesai.")

    # ── Gabungkan file part per tanggal ───────────────────────────────
    combine_files(date_list, output_dir, base_name)

    print("\nSelesai.")


if __name__ == "__main__":
    main()