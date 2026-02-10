import pandas as pd
from datetime import datetime, timedelta
import time
from curl_cffi import requests

def get_trading_days(year, month):
    """Hasilkan daftar hari kerja (Senin-Jumat)"""
    trading_days = []
    date = datetime(year, month, 1)
    
    while date.month == month:
        if date.weekday() < 5:  # 0-4 = Senin-Jumat
            trading_days.append(date.strftime('%Y-%m-%d'))
        date += timedelta(days=1)
    return trading_days

def fetch_idx_data(target_date):
    """Mengambil data dengan curl_cffi yang meniru browser Chrome"""
    
    url = "https://www.idx.co.id/primary/TradingSummary/GetStockSummary"
    
    # Gunakan impersonate untuk meniru browser Chrome modern
    try:
        print(f"🔄 Mengambil data untuk: {target_date}")
        
        # Parameter yang diperlukan
        params = {
            'draw': 1,
            'start': 0,
            'length': 1000,
            'date': target_date
        }
        
        # Header yang lebih lengkap
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Referer': 'https://www.idx.co.id/id/data-pasar/ringkasan-perdagangan/ringkasan-saham',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'X-Requested-With': 'XMLHttpRequest',
        }
        
        # Gunakan curl_cffi dengan impersonate Chrome
        response = requests.get(
            url, 
            params=params, 
            headers=headers,
            impersonate="chrome120",  # Meniru Chrome 120
            timeout=30
        )
        
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('data'):
                df = pd.DataFrame(data['data'])
                print(f"✅ Berhasil: {len(df)} baris data")
                return df
            else:
                print(f"⚠️ Tidak ada data untuk {target_date}")
                return None
        else:
            print(f"❌ Error {response.status_code}: {response.text[:100]}")
            return None
            
    except Exception as e:
        print(f"💥 Exception: {e}")
        return None

def main():
    # Set tahun dan bulan yang diinginkan
    TARGET_YEAR = 2025  # Ubah sesuai kebutuhan
    TARGET_MONTH = 11    # Januari
    
    print(f"🚀 Memulai pengambilan data untuk {TARGET_MONTH}/{TARGET_YEAR}")
    
    trading_days = get_trading_days(TARGET_YEAR, TARGET_MONTH)
    print(f"📅 Ditemukan {len(trading_days)} hari kerja\n")
    
    successful = 0
    
    for trade_date in trading_days:
        df = fetch_idx_data(trade_date)
        
        if df is not None and not df.empty:
            file_name = f"/Users/albert/Documents/Finances/data/raw/market_data/idx_summaries/2025/Nov/Ringkasan Saham-{trade_date.replace('-', '')}.xlsx"
            
            # Simpan dengan kolom yang relevan
            df.to_excel(file_name, index=False)
            print(f"💾 Disimpan: {file_name}\n")
            successful += 1
        else:
            print(f"⏭️ Dilewati: {trade_date}\n")
        
        # Jeda lebih lama untuk menghindari blokir
        time.sleep(4)
    
    print("="*50)
    print(f"🎉 Selesai! Berhasil mengunduh {successful} dari {len(trading_days)} file")

if __name__ == "__main__":
    main()