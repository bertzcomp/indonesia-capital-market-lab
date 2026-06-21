import pandas as pd
from datetime import datetime, timedelta
import time
import os
import shutil
from curl_cffi import requests

BASE_DIR = "../data/raw/"
MIRROR_DIR = "/Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/trading_summary"

MONTH_NAMES = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
    5: "Mei", 6: "Jun", 7: "Jul", 8: "Agu",
    9: "Sep", 10: "Okt", 11: "Nov", 12: "Des"
}


def get_trading_days_range(start_date, end_date):
    """Generate trading days (Monday - Friday) in range date"""
    
    start = datetime.strptime(start_date, "%d-%m-%Y")
    end = datetime.strptime(end_date, "%d-%m-%Y")
    trading_days = []
    while start <= end:
        if start.weekday() < 5:  # Monday - Friday
            trading_days.append(start.strftime("%Y-%m-%d"))
        start += timedelta(days=1)

    return trading_days


def fetch_idx_data(target_date):
    url = "https://www.idx.co.id/primary/TradingSummary/GetStockSummary"
    try:
        print(f"🔄 Mengambil data untuk: {target_date}")
        params = {
            "draw": 1,
            "start": 0,
            "length": 1000,
            "date": target_date
        }
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Referer": "https://www.idx.co.id/id/data-pasar/ringkasan-perdagangan/ringkasan-saham",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = requests.get(
            url,
            params=params,
            headers=headers,
            impersonate="chrome120",
            timeout=30
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("data"):
                df = pd.DataFrame(data["data"])
                print(f"✅ {len(df)} baris")
                return df
            else:
                print("⚠️ Tidak ada data")
                return None
        else:
            print(f"❌ Error {response.status_code}")
            return None
    except Exception as e:
        print(f"💥 Exception: {e}")
        return None


def save_data(df, trade_date):
    """Save file based on structure of IDX dir"""
    date_obj = datetime.strptime(trade_date, "%Y-%m-%d")
    year = date_obj.year
    month = MONTH_NAMES[date_obj.month]

    _dir = BASE_DIR
    os.makedirs(_dir, exist_ok=True)

    file_name = f"RingkasanSaham-{trade_date.replace('-', '')}.xlsx"
    file_path = os.path.join(_dir, file_name)

    df.to_excel(file_path, index=False)

    mirror_path = None
    if MIRROR_DIR:
        os.makedirs(MIRROR_DIR, exist_ok=True)
        mirror_path = os.path.join(MIRROR_DIR, file_name)
        if os.path.abspath(file_path) != os.path.abspath(mirror_path):
            shutil.copy2(file_path, mirror_path)

    print(f"Disimpan: {file_path}")
    if mirror_path:
        print(f"Mirror : {mirror_path}")
    print()


def main():
    FROM_DATE = "12-06-2026"
    END_DATE = "12-06-2026"
    print(f"Download IDX dari {FROM_DATE} sampai {END_DATE}\n")

    trading_days = get_trading_days_range(FROM_DATE, END_DATE)
    total_success = 0
    total_attempt = 0

    for trade_date in trading_days:
        total_attempt += 1
        df = fetch_idx_data(trade_date)
        if df is not None and not df.empty:
            save_data(df, trade_date)
            total_success += 1
        else:
            print(f"⏭️ Skip: {trade_date}\n")
        time.sleep(3)

    print("=" * 60)
    print("SELESAI")
    print(f"Berhasil: {total_success}")
    print(f"Total dicoba: {total_attempt}")


if __name__ == "__main__":
    main()