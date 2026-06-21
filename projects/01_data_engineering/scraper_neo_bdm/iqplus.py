import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import re
import time
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os

# Daftar kode saham LQ45 (dapat disesuaikan)
LQ45_CODES = [
    "AADI", "ACES", "ADMR", "ADRO", "AKRA", "AMMN", "AMRT", "ANTM", "ARTO", "ASII",
    "BBCA", "BBNI", "BBRI", "BBTN", "BMRI", "BRIS", "BRPT", "CPIN", "CTRA", "EXCL",
    "GOTO", "ICBP", "INCO", "INDF", "INKP", "ISAT", "ITMG", "JPFA", "JSMR", "KLBF",
    "MAPA", "MAPI", "MBMA", "MDKA", "MEDC", "PGAS", "PGEO", "PTBA", "SCMA", "SMGR",
    "SMRA", "TLKM", "TOWR", "UNTR", "UNVR"
]

# Daftar User-Agent untuk rotasi
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1'
]

def get_session():
    """Membuat session dengan retry strategy."""
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    return session

def scrape_broker_summary(date_str, code):
    """
    Mengambil data broker summary untuk satu tanggal dan kode saham.
    Mengembalikan DataFrame jika berhasil, None jika gagal.
    """
    url_main = "https://www.iqplus.info/market_summary/historical/net_by_sell_by_date/"
    url_post = "https://www.iqplus.info/box_net_buy_sell_bydate_act.php"
    
    # Pilih User-Agent acak
    user_agent = random.choice(USER_AGENTS)
    
    headers_main = {
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.6',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
    }
    
    headers_post = {
        'User-Agent': user_agent,
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.6',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.iqplus.info',
        'Referer': url_main,
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
    }
    
    session = get_session()
    
    # Kunjungi halaman utama untuk mendapatkan cookie
    try:
        resp_main = session.get(url_main, headers=headers_main, timeout=10)
        if resp_main.status_code != 200:
            print(f"    [{code}] Gagal mengakses halaman utama")
            return None
    except Exception as e:
        print(f"    [{code}] Exception saat akses utama: {e}")
        return None
    
    # Data form
    data = {
        'code': code,
        'start_date': date_str,
        'end_date': date_str,
        'submit': 'submit'
    }
    
    # Kirim POST
    try:
        response = session.post(url_post, data=data, headers=headers_post, timeout=15)
        if response.status_code != 200:
            print(f"    [{code}] Status code error: {response.status_code}")
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Cari tabel data broker (class="greytable")
        table = soup.find('table', class_='greytable')
        if not table:
            print(f"    [{code}] Tabel tidak ditemukan.")
            return None
        
        # Ambil header
        thead = table.find('thead')
        headers = []
        if thead:
            for th in thead.find_all('th'):
                header_text = th.get_text(strip=True)
                header_text = re.sub(r'[^\w\s]', '', header_text)
                headers.append(header_text)
        
        # Ambil baris data
        tbody = table.find('tbody')
        rows = []
        if tbody:
            for tr in tbody.find_all('tr'):
                cells = tr.find_all('td')
                row = [td.get_text(strip=True) for td in cells]
                if row:
                    rows.append(row)
        
        if not rows:
            print(f"    [{code}] Tabel ditemukan tapi kosong.")
            return None
        
        df = pd.DataFrame(rows, columns=headers)
        print(f"    [{code}] Berhasil mengambil {len(df)} baris data.")
        return df
        
    except Exception as e:
        print(f"    [{code}] Exception saat POST: {e}")
        return None

def generate_weekdays(start, end):
    """Menghasilkan daftar hari kerja (Senin-Jumat) antara dua tanggal."""
    dates = []
    current = start
    while current <= end:
        if current.weekday() < 5:
            dates.append(current.strftime('%Y-%m-%d'))
        current += timedelta(days=1)
    return dates

def main():
    # KONFIGURASI
    codes = LQ45_CODES  # Seluruh saham LQ45
    start_date = datetime(2026, 2, 1)   # Tanggal awal
    end_date   = datetime(2026, 2, 3)   # Tanggal akhir (contoh 2 hari kerja)
    
    date_list = generate_weekdays(start_date, end_date)
    print(f"Hari kerja dalam rentang: {date_list}")
    print(f"Jumlah kode: {len(codes)}")
    print(f"Estimasi total request: {len(date_list) * len(codes)}")
    
    # Buat folder output
    output_dir = "broker_summaries"
    os.makedirs(output_dir, exist_ok=True)
    
    for date_str in date_list:
        print(f"\n=== Memproses tanggal {date_str} ===")
        data_frames = {}  # key: kode saham, value: dataframe
        
        for code in codes:
            print(f"  Mengambil data untuk {code}...")
            df = scrape_broker_summary(date_str, code)
            if df is not None:
                data_frames[code] = df
            # Jeda acak antar request
            time.sleep(random.uniform(1, 3))
        
        if not data_frames:
            print(f"Tidak ada data untuk tanggal {date_str}")
            continue
        
        # Simpan ke file Excel dengan sheet per kode
        date_formatted = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d-%m-%Y')
        filename = f"broksum_{date_formatted}_LQ45.xlsx"
        filepath = os.path.join(output_dir, filename)
        
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            for code, df in data_frames.items():
                # Batasi panjang sheet name (max 31 karakter di Excel)
                sheet_name = code[:31]
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        print(f"Data untuk {date_str} disimpan ke {filepath} dengan {len(data_frames)} sheet.")
        
        # Jeda antar tanggal (lebih lama)
        time.sleep(random.uniform(5, 10))
    
    print("\nSelesai.")

if __name__ == "__main__":
    main()