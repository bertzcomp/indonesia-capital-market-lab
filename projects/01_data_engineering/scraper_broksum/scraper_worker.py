import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import re
import time
import random
import argparse
import os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1'
]

def get_session():
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    return session

def scrape_broker_summary(date_str, code, session, headers_post):
    url_post = "https://www.iqplus.info/box_net_buy_sell_bydate_act.php"
    data = {
        'code': code,
        'start_date': date_str,
        'end_date': date_str,
        'submit': 'submit'
    }
    try:
        response = session.post(url_post, data=data, headers=headers_post, timeout=15)
        if response.status_code != 200:
            return None
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='greytable')
        if not table:
            return None
        # Ambil header
        thead = table.find('thead')
        headers = []
        if thead:
            for th in thead.find_all('th'):
                header_text = th.get_text(strip=True)
                header_text = re.sub(r'[^\w\s]', '', header_text)
                headers.append(header_text)
        tbody = table.find('tbody')
        rows = []
        if tbody:
            for tr in tbody.find_all('tr'):
                cells = tr.find_all('td')
                row = [td.get_text(strip=True) for td in cells]
                if row:
                    rows.append(row)
        if not rows:
            return None
        df = pd.DataFrame(rows, columns=headers)

        # Rename kolom pertama (kode broker dari tabel) menjadi broker_code
        if len(df.columns) > 0:
            df.rename(columns={df.columns[0]: 'broker_code'}, inplace=True)

        return df
    except Exception:
        return None

def scrape_with_retry(date_str, code, session, headers_post, max_retries=2):
    """Coba scrape, jika gagal tunggu dan ulangi."""
    for attempt in range(max_retries):
        df = scrape_broker_summary(date_str, code, session, headers_post)
        if df is not None:
            return df
        if attempt < max_retries - 1:
            wait = random.uniform(5, 10)
            print(f"    [{code}] Gagal, coba lagi dalam {wait:.1f} detik...")
            time.sleep(wait)
    return None

def generate_weekdays(start, end):
    dates = []
    current = start
    while current <= end:
        if current.weekday() < 5:
            dates.append(current.strftime('%Y-%m-%d'))
        current += timedelta(days=1)
    return dates

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, required=True, help="Nomor part")
    parser.add_argument("--codes", type=str, required=True, help="Daftar kode dipisah koma")
    parser.add_argument("--start", type=str, required=True, help="Tanggal awal YYYY-MM-DD")
    parser.add_argument("--end", type=str, required=True, help="Tanggal akhir YYYY-MM-DD")
    parser.add_argument("--outdir", type=str, default=".", help="Direktori output")
    args = parser.parse_args()

    codes = args.codes.split(",")
    start_date = datetime.strptime(args.start, "%Y-%m-%d")
    end_date = datetime.strptime(args.end, "%Y-%m-%d")
    part = args.part
    outdir = args.outdir

    date_list = generate_weekdays(start_date, end_date)

    session = get_session()
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
        'Referer': 'https://www.iqplus.info/market_summary/historical/net_by_sell_by_date/',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
    }

    try:
        main_url = "https://www.iqplus.info/market_summary/historical/net_by_sell_by_date/"
        session.get(main_url, headers=headers_main, timeout=10)
    except Exception as e:
        print(f"[Part {part}] Gagal akses utama: {e}")
        return

    for date_str in date_list:
        print(f"[Part {part}] Memproses tanggal {date_str}...")
        data_frames = {}
        for code in codes:
            print(f"    [{code}] Mengambil data...")
            df = scrape_with_retry(date_str, code, session, headers_post, max_retries=2)
            if df is not None:
                data_frames[code] = df
            else:
                print(f"    [{code}] Gagal setelah retry.")
            time.sleep(random.uniform(1, 3))
            
        if not data_frames:
            continue
            
        date_formatted = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d-%m-%Y')
        filename = f"broksum_{date_formatted}_IDX_part{part}.csv"
        filepath = os.path.join(outdir, filename)
        
        # Gabungkan semua saham menjadi satu CSV dengan kolom 'ticker' di posisi paling kiri
        all_parts_df = []
        for code, df in data_frames.items():
            df.insert(0, 'ticker', code)   # sebelumnya: 'StockCode'
            all_parts_df.append(df)
            
        final_df = pd.concat(all_parts_df, ignore_index=True)
        final_df.to_csv(filepath, index=False)
        print(f"[Part {part}] Data {date_str} disimpan ke {filename} dengan {len(data_frames)} saham.")

if __name__ == "__main__":
    main()