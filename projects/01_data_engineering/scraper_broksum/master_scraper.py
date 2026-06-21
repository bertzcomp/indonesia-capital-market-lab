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

def combine_files(date_list, output_dir, base_name="broksum"):
    """Menggabungkan semua file part (CSV) per tanggal menjadi satu file final dan menghapus part."""
    for date_str in date_list:
        date_formatted = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d-%m-%Y')
        pattern = os.path.join(output_dir, f"{base_name}_{date_formatted}_IDX_part*.csv")
        part_files = glob.glob(pattern)
        
        if not part_files:
            continue
            
        all_dfs = []
        for part_file in part_files:
            try:
                df = pd.read_csv(part_file)
                all_dfs.append(df)
            except Exception as e:
                print(f"Gagal membaca {part_file}: {e}")
                
        if all_dfs:
            # Gabungkan semua data CSV dari berbagai part
            combined_df = pd.concat(all_dfs, ignore_index=True)
            output_file = os.path.join(output_dir, f"{base_name}_{date_formatted}_IDX.csv")
            combined_df.to_csv(output_file, index=False)
            print(f"Gabungan untuk {date_formatted} berhasil disimpan ke {output_file}")
            
            # Hapus file part/chunk agar tidak menumpuk
            for part_file in part_files:
                try:
                    os.remove(part_file)
                except OSError as e:
                    print(f"Error saat menghapus file sementara {part_file}: {e}")
            print(f"File part sementara untuk {date_formatted} telah dibersihkan.")

def main():
    # Konfigurasi
    start_date = datetime(2026, 3, 12)
    end_date   = datetime(2026, 3, 12)
    base_name = "broksum"
    output_dir = "broker_summaries"
    os.makedirs(output_dir, exist_ok=True)
    
    # Baca daftar saham
    all_stocks = read_stock_list("idx_stocks.txt")
    print(f"Total saham: {len(all_stocks)}")
    
    # Input jumlah split
    try:
        split_num = int(input("Masukkan jumlah split (misal 5, 10, 20, 50): "))
    except:
        print("Input tidak valid. Gunakan angka.")
        sys.exit(1)
 
    # Bagi daftar
    chunks = split_list(all_stocks, split_num)
    print(f"Dibagi menjadi {len(chunks)} bagian.")
    
    # Generate daftar tanggal
    date_list = generate_weekdays(start_date, end_date)
    print(f"Tanggal yang akan diproses: {date_list}")
    
    # Jalankan proses pekerja untuk setiap chunk
    processes = []
    for i, chunk in enumerate(chunks):
        if not chunk:
            continue
        # Buat argumen: part index, daftar kode (dipisah koma), start, end
        codes_str = ",".join(chunk)
        cmd = [
            sys.executable,  # Gunakan interpreter yang sama
            "scraper_worker.py",
            "--part", str(i+1),
            "--codes", codes_str,
            "--start", start_date.strftime("%Y-%m-%d"),
            "--end", end_date.strftime("%Y-%m-%d"),
            "--outdir", output_dir
        ]
        print(f"Menjalankan proses untuk part {i+1} dengan {len(chunk)} saham...")
        p = subprocess.Popen(cmd)
        processes.append(p)
        # Jeda sebelum memulai proses berikutnya agar tidak terlalu bersamaan
        time.sleep(random.uniform(2, 5))
    
    # Tunggu semua selesai
    for p in processes:
        p.wait()
    
    print("Semua proses pekerja selesai.")
    
    # Gabungkan file per tanggal (otomatis menghapus file part)
    combine_files(date_list, output_dir, base_name)
    
    print("Selesai.")

if __name__ == "__main__":
    main()