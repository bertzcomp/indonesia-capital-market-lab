            # file_name = f"/Users/albert/Documents/Finances/data/raw/market_data/idx_summaries/2020/Feb/Ringkasan Saham-{trade_date.replace('-', '')}.xlsx"

import pandas as pd
from datetime import datetime, timedelta
import time
import os
from curl_cffi import requests

BASE_DIR = "/Users/albert/Documents/Finances/data/raw/market_data/idx_summaries"

MONTH_NAMES = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
    5: "Mei", 6: "Jun", 7: "Jul", 8: "Agu",
    9: "Sep", 10: "Okt", 11: "Nov", 12: "Des"
}

def get_trading_days(year, month):
    """Hasilkan daftar hari kerja (Senin-Jumat) dalam 1 bulan"""
    trading_days = []
    date = datetime(year, month, 1)
    
    while date.month == month:
        if date.weekday() < 5:  # 0-4 = Senin-Jumat
            trading_days.append(date.strftime('%Y-%m-%d'))
        date += timedelta(days=1)
    return trading_days

def fetch_idx_data(target_date):
    """Mengambil data dengan curl_cffi"""
    
    url = "https://www.idx.co.id/primary/TradingSummary/GetStockSummary"
    
    try:
        print(f"🔄 Mengambil data untuk: {target_date}")
        
        params = {
            'draw': 1,
            'start': 0,
            'length': 1000,
            'date': target_date
        }
        
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.idx.co.id/id/data-pasar/ringkasan-perdagangan/ringkasan-saham',
            'X-Requested-With': 'XMLHttpRequest',
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
            if data.get('data'):
                df = pd.DataFrame(data['data'])
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

def main():
    TARGET_YEAR = 2026  # <<< Ganti tahun di sini
    
    print(f"🚀 Download data IDX tahun {TARGET_YEAR}\n")
    
    total_success = 0
    total_attempt = 0
    
    for month in range(1, 13):
        month_name = MONTH_NAMES[month]
        print(f"\n📆 Processing {month_name} {TARGET_YEAR}")
        
        # Path folder bulan
        month_dir = os.path.join(BASE_DIR, str(TARGET_YEAR), month_name)
        os.makedirs(month_dir, exist_ok=True)
        
        trading_days = get_trading_days(TARGET_YEAR, month)
        
        for trade_date in trading_days:
            total_attempt += 1
            
            df = fetch_idx_data(trade_date)
            
            if df is not None and not df.empty:
                file_name = f"RingkasanSaham-{trade_date.replace('-', '')}.xlsx"
                file_path = os.path.join(month_dir, file_name)
                
                df.to_excel(file_path, index=False)
                print(f"💾 Disimpan: {file_path}\n")
                total_success += 1
            else:
                print(f"⏭️ Skip: {trade_date}\n")
            
            time.sleep(3)  # Jeda anti blokir
    
    print("="*60)
    print(f"🎉 SELESAI")
    print(f"Berhasil: {total_success}")
    print(f"Total dicoba: {total_attempt}")

if __name__ == "__main__":
    main()