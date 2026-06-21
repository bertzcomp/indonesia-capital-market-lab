import os
import glob
import pandas as pd
import gc
from pathlib import Path


# KONFIGURASI
DATA_PATH   = "/Users/albert/Documents/Finances/data/raw/market_data/broker_summaries/"
OUTPUT_FILE = "/Users/albert/Documents/Finances/data/raw/market_data/broker_summaries/broksum_merged.csv"
CHUNKSIZE   = 500_000                    # jumlah baris per chunk (sesuaikan RAM)

"""
Standardisasi kolom lalu CONCAT semua broker summary CSV.
Menangani perbedaan nama kolom antar file (Code vs KodeSaham, Tanggal vs date, dll).

Output: satu file CSV gabungan yang bersih.
"""
# Mapping: nama kolom lama → nama kolom standar
COLUMN_RENAME_MAP = {
    "KodeSaham"  : "Code",
    "kode_saham" : "Code",
    "stock_code" : "Code",
    "Tanggal"    : "date",
    "tanggal"    : "date",
    "Date"       : "date",
    "TANGGAL"    : "date",
    "KodeBroker" : "broker_code",
    "kode_broker": "broker_code",
    "Broker"     : "broker_code",
}

# Kolom final yang diinginkan di output (urutan)
FINAL_COLUMNS = [
    "date",
    "Code",
    "broker_code",
    "Bfreq", "Blot", "Bval", "Bavg",
    "Sfreq", "Slot", "Sval",
    "Nlot", "Nval", "Navg",
    "source_file",
    "sheet_name",
]


def get_csv_files(folder: str) -> list:
    pattern = os.path.join(folder, "*.csv")
    files = sorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError(f"Tidak ada file CSV di folder: {folder}")
    return files


def standardize_df(df: pd.DataFrame, filename: str) -> pd.DataFrame:
    """Rename kolom ke standar, tambah kolom yang kurang."""
    df = df.rename(columns=COLUMN_RENAME_MAP)

    if "source_file" not in df.columns:
        df["source_file"] = os.path.basename(filename)

    cols_present = [c for c in FINAL_COLUMNS if c in df.columns]
    cols_missing = [c for c in FINAL_COLUMNS if c not in df.columns]

    df = df[cols_present].copy()
    for col in cols_missing:
        df[col] = pd.NA

    return df[FINAL_COLUMNS]


def process_file(filepath: str) -> pd.DataFrame:
    """Baca file (chunked jika besar) lalu standardisasi."""
    file_size = os.path.getsize(filepath)

    if file_size > CHUNKSIZE * 100:  # ~50MB threshold
        print(f"  → File besar ({file_size/1e6:.1f} MB), membaca per chunk...")
        chunks = []
        for chunk in pd.read_csv(filepath, chunksize=CHUNKSIZE, low_memory=False):
            chunks.append(standardize_df(chunk, filepath))
        df = pd.concat(chunks, ignore_index=True)
        del chunks
        gc.collect()
    else:
        df = pd.read_csv(filepath, low_memory=False)
        df = standardize_df(df, filepath)

    return df


def main():
    if not os.path.isdir(DATA_PATH):
        raise NotADirectoryError(f"Folder tidak ditemukan: '{DATA_PATH}'")

    files = get_csv_files(DATA_PATH)
    print(f"\n📂 Ditemukan {len(files)} file CSV")
    print(f"📋 Kolom standar output: {FINAL_COLUMNS}\n")

    all_dfs = []

    for i, filepath in enumerate(files, 1):
        filename = os.path.basename(filepath)
        print(f"[{i}/{len(files)}] {filename}")

        raw_cols = pd.read_csv(filepath, nrows=0).columns.tolist()
        print(f"  Kolom asli ({len(raw_cols)}): {raw_cols}")

        df = process_file(filepath)
        print(f"  ✅ Shape: {df.shape}")
        all_dfs.append(df)

    # Concat semua
    print(f"\n🔗 Menggabungkan {len(all_dfs)} dataframe...")
    result = pd.concat(all_dfs, ignore_index=True)
    del all_dfs
    gc.collect()

    print(f"   Total baris  : {len(result):,}")
    print(f"   Total kolom  : {len(result.columns)}")

    # Simpan
    os.makedirs(os.path.dirname(OUTPUT_FILE) or ".", exist_ok=True)
    print(f"\n💾 Menyimpan ke: {OUTPUT_FILE}")
    result.to_csv(OUTPUT_FILE, index=False)
    print("✅ Selesai!\n")
    print(result.head().to_string())


if __name__ == "__main__":
    main()
