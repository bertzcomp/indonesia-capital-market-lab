"""
IDX Disclosure Information Scraper (Card-based with Pagination)
Scrape dari: https://www.idx.co.id/id/perusahaan-tercatat/keterbukaan-informasi/
Author: Albert
Last Updated: 2025-01-15
"""

from playwright.sync_api import sync_playwright
import pandas as pd
import requests
import os
import time
import json
import re
from datetime import datetime
from urllib.parse import urljoin
import logging
from pathlib import Path

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('idx_scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class IDXDisclosureScraper:
    def __init__(self, headless=False, slow_mo=100, timeout=60000):
        """
        Inisialisasi scraper IDX
        
        Args:
            headless (bool): Jalankan browser tanpa GUI
            slow_mo (int): Delay antar aksi (ms)
            timeout (int): Timeout untuk wait (ms)
        """
        self.url = "https://www.idx.co.id/id/perusahaan-tercatat/keterbukaan-informasi/"
        self.headless = headless
        self.slow_mo = slow_mo
        self.timeout = timeout
        self.pdf_dir = Path("idx_pdfs")
        self.data_dir = Path("data")
        
        # Buat direktori jika belum ada
        self.pdf_dir.mkdir(exist_ok=True)
        self.data_dir.mkdir(exist_ok=True)
    
    def scrape_with_retry(self, max_retries=3, retry_delay=5, max_pages=None):
        """
        Scrape data dengan mekanisme retry dan pagination
        
        Args:
            max_retries (int): Jumlah maksimal percobaan ulang
            retry_delay (int): Delay antar percobaan (detik)
            max_pages (int): Maksimal halaman yang di-scrape (None = semua)
        
        Returns:
            pd.DataFrame: Data yang berhasil di-scrape
        """
        for attempt in range(max_retries):
            try:
                logger.info(f"Percobaan scraping ke-{attempt + 1}")
                df = self._scrape_disclosures_with_pagination(max_pages)
                
                if not df.empty:
                    logger.info(f"Berhasil scrape {len(df)} baris data")
                    return df
                else:
                    logger.warning("Data kosong, coba lagi...")
                    
            except Exception as e:
                logger.error(f"Error pada percobaan {attempt + 1}: {str(e)}")
                
                if attempt < max_retries - 1:
                    logger.info(f"Menunggu {retry_delay} detik sebelum mencoba lagi...")
                    time.sleep(retry_delay)
                else:
                    logger.error("Semua percobaan gagal")
                    raise
        
        return pd.DataFrame()
    
    def _extract_emiten_code(self, text):
        """
        Ekstrak kode emiten dari teks judul
        Contoh: "Laporan Bulanan Registrasi Pemegang Efek [RAFI]"
        """
        if not text:
            return ""
        
        pattern = r'\[([A-Za-z0-9]+)\s*\]'
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
        return ""
    
    def _extract_judul_tanpa_kode(self, text):
        """
        Ekstrak judul tanpa kode emiten dalam kurung siku
        """
        if not text:
            return ""
        
        pattern = r'(.+?)\s*\[[A-Za-z0-9]+\s*\]'
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
        return text.strip()
    
    def _parse_datetime(self, datetime_str):
        """
        Parse string tanggal waktu dari HTML
        Contoh: "10 Februari 2026\n\t\t22:44:41"
        """
        if not datetime_str:
            return "", "", ""
        
        try:
            # Bersihkan whitespace dan newline
            cleaned = datetime_str.strip().replace('\n', ' ').replace('\t', ' ')
            # Gabungkan multiple spaces
            cleaned = ' '.join(cleaned.split())
            
            # Parse format Indonesia
            bulan_map = {
                'Januari': 'January',
                'Februari': 'February',
                'Maret': 'March',
                'April': 'April',
                'Mei': 'May',
                'Juni': 'June',
                'Juli': 'July',
                'Agustus': 'August',
                'September': 'September',
                'Oktober': 'October',
                'November': 'November',
                'Desember': 'December'
            }
            
            for id_bulan, en_bulan in bulan_map.items():
                cleaned = cleaned.replace(id_bulan, en_bulan)
            
            # Split tanggal dan waktu
            parts = cleaned.split()
            if len(parts) >= 4:
                date_part = ' '.join(parts[:3])
                time_part = parts[3]
                
                # Parse ke datetime object
                dt_str = f"{date_part} {time_part}"
                dt_obj = datetime.strptime(dt_str, "%d %B %Y %H:%M:%S")
                
                return dt_obj.strftime("%Y-%m-%d %H:%M:%S"), dt_obj.strftime("%Y-%m-%d"), dt_obj.strftime("%H:%M:%S")
            
        except Exception as e:
            logger.error(f"Gagal parse datetime '{datetime_str}': {e}")
        
        return cleaned, cleaned.split()[0] if cleaned else "", ""
    
    def _scrape_disclosures_with_pagination(self, max_pages=None):
        """
        Scrape dengan pagination handling
        """
        results = []
        
        with sync_playwright() as p:
            # Launch browser dengan konfigurasi
            browser = p.chromium.launch(
                headless=self.headless,
                slow_mo=self.slow_mo,
                args=[
                    '--disable-blink-features=AutomationControlled',
                    '--disable-dev-shm-usage',
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-web-security',
                    '--disable-features=IsolateOrigins,site-per-process',
                    '--disable-site-isolation-trials'
                ]
            )
            
            # Buat context dengan viewport realistis
            context = browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                locale='id-ID',
                timezone_id='Asia/Jakarta',
                accept_downloads=True  # Izinkan download
            )
            
            # Tambahkan headers tambahan
            context.set_extra_http_headers({
                'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'Referer': 'https://www.idx.co.id/',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            })
            
            page = context.new_page()
            
            try:
                # Navigasi ke URL
                logger.info(f"Membuka halaman: {self.url}")
                page.goto(self.url, timeout=self.timeout, wait_until='networkidle')
                
                # Tunggu konten muncul
                logger.info("Menunggu konten muncul...")
                page.wait_for_selector(".attach-card", timeout=self.timeout)
                time.sleep(2)
                
                page_num = 1
                total_cards = 0
                
                while True:
                    if max_pages and page_num > max_pages:
                        logger.info(f"Mencapai batas maksimal {max_pages} halaman")
                        break
                    
                    logger.info(f"=== Memproses halaman {page_num} ===")
                    
                    # Scroll sedikit untuk memastikan semua card terload
                    page.evaluate("window.scrollTo(0, 0)")
                    time.sleep(1)
                    
                    # Scroll ke bawah secara bertahap
                    for i in range(3):
                        page.evaluate(f"window.scrollTo(0, {300 * (i + 1)})")
                        time.sleep(0.5)
                    
                    # Tunggu cards muncul
                    try:
                        page.wait_for_selector(".attach-card", timeout=10000)
                    except:
                        logger.warning("Tidak ada card ditemukan di halaman ini")
                        break
                    
                    # Ambil semua cards di halaman ini
                    cards = page.query_selector_all(".attach-card")
                    logger.info(f"Ditemukan {len(cards)} cards di halaman {page_num}")
                    
                    if not cards:
                        logger.warning("Tidak ada cards ditemukan")
                        break
                    
                    # Proses setiap card
                    for idx, card in enumerate(cards):
                        try:
                            # 1. Ambil tanggal dan waktu
                            time_element = card.query_selector("time.text-small")
                            datetime_str = time_element.inner_text().strip() if time_element else ""
                            
                            # Parse tanggal waktu
                            full_datetime, tanggal, waktu = self._parse_datetime(datetime_str)
                            
                            # 2. Ambil judul dan link utama
                            title_element = card.query_selector("h6.f-m-20.title a")
                            if title_element:
                                judul_full = title_element.inner_text().strip()
                                link_utama = title_element.get_attribute("href") or ""
                                
                                # Ekstrak kode emiten dari judul
                                kode_emiten = self._extract_emiten_code(judul_full)
                                
                                # Ekstrak judul tanpa kode
                                judul = self._extract_judul_tanpa_kode(judul_full)
                            else:
                                judul_full = ""
                                judul = ""
                                link_utama = ""
                                kode_emiten = ""
                            
                            # 3. Ambil lampiran (bisa multiple)
                            lampiran_elements = card.query_selector_all("ul.list-nostyle li a")
                            lampiran_data = []
                            
                            for lampiran in lampiran_elements:
                                try:
                                    lampiran_text = lampiran.inner_text().strip()
                                    lampiran_link = lampiran.get_attribute("href") or ""
                                    lampiran_filename = lampiran.get_attribute("download") or ""
                                    
                                    lampiran_data.append({
                                        "text": lampiran_text,
                                        "link": lampiran_link,
                                        "filename": lampiran_filename
                                    })
                                except Exception as e:
                                    logger.error(f"Error processing attachment: {e}")
                                    continue
                            
                            # 4. Hitung jumlah lampiran
                            jumlah_lampiran = len(lampiran_data)
                            
                            # 5. Cari nama emiten (bisa dari judul atau kode)
                            nama_emiten = kode_emiten
                            
                            # Tambahkan ke hasil
                            results.append({
                                "No": total_cards + idx + 1,
                                "Halaman": page_num,
                                "Tanggal": tanggal,
                                "Waktu": waktu,
                                "TanggalWaktu": full_datetime,
                                "KodeEmiten": kode_emiten,
                                "NamaEmiten": nama_emiten,
                                "Judul": judul,
                                "JudulFull": judul_full,
                                "LinkUtama": link_utama,
                                "JumlahLampiran": jumlah_lampiran,
                                "LampiranData": json.dumps(lampiran_data, ensure_ascii=False),
                                "ScrapedAt": datetime.now().isoformat()
                            })
                            
                            logger.debug(f"Card {total_cards + idx + 1}: {kode_emiten} - {judul[:50]}...")
                            
                        except Exception as e:
                            logger.error(f"Error processing card {idx} di halaman {page_num}: {str(e)}")
                            continue
                    
                    total_cards += len(cards)
                    logger.info(f"Total sementara: {total_cards} cards")
                    
                    # Cari tombol next page
                    next_button = None
                    
                    # Coba berbagai selector untuk tombol next
                    selectors = [
                        "button.btn-arrow.--next",
                        "button[aria-label*='next']",
                        "button[aria-label*='Next']",
                        "li.pagination-item button.--next",
                        ".pagination button.--next"
                    ]
                    
                    for selector in selectors:
                        try:
                            next_button = page.query_selector(selector)
                            if next_button:
                                break
                        except:
                            continue
                    
                    # Jika tidak ditemukan dengan selector, coba dengan XPath
                    if not next_button:
                        try:
                            next_button = page.query_selector("//button[contains(@class, '--next') or contains(@aria-label, 'next') or contains(@aria-label, 'Next')]")
                        except:
                            pass
                    
                    # Cek apakah tombol next ada dan enabled
                    if not next_button:
                        logger.info("Tombol next tidak ditemukan, sudah di halaman terakhir")
                        break
                    
                    # Cek apakah tombol disabled
                    is_disabled = next_button.is_disabled()
                    if is_disabled:
                        logger.info("Tombol next disabled, sudah di halaman terakhir")
                        break
                    
                    # Scroll ke tombol next untuk memastikan terlihat
                    try:
                        next_button.scroll_into_view_if_needed()
                        time.sleep(0.5)
                    except:
                        pass
                    
                    # Klik tombol next
                    logger.info(f"Pindah ke halaman {page_num + 1}...")
                    try:
                        next_button.click()
                    except Exception as e:
                        logger.error(f"Gagal klik tombol next: {e}")
                        # Fallback: gunakan JavaScript click
                        try:
                            page.evaluate("(btn) => btn.click()", next_button)
                        except:
                            logger.error("Juga gagal dengan JavaScript click")
                            break
                    
                    # Tunggu halaman berikutnya dimuat
                    time.sleep(3)
                    
                    # Tunggu sampai konten baru muncul
                    try:
                        page.wait_for_selector(".attach-card", timeout=10000)
                    except:
                        logger.warning("Timeout menunggu card di halaman baru")
                        # Coba scroll sedikit
                        page.evaluate("window.scrollTo(0, 100)")
                        time.sleep(2)
                    
                    page_num += 1
                    
                    # Safety break - maksimal 1000 halaman
                    if page_num > 1000:
                        logger.warning("Mencapai batas maksimal 1000 halaman")
                        break
                
                logger.info(f"Scraping selesai. Total {len(results)} baris data dari {page_num} halaman")
                
            except Exception as e:
                logger.error(f"Error during scraping: {str(e)}")
                raise
            
            finally:
                # Selalu tutup browser
                browser.close()
        
        return pd.DataFrame(results)
    
    def download_files_with_playwright(self, df, file_types=None, delay=1, max_retries=3):
        """
        Download file menggunakan Playwright (mengatasi error 403)
        
        Args:
            df (pd.DataFrame): DataFrame dengan kolom 'LinkUtama' dan 'LampiranData'
            file_types (list): Jenis file yang didownload (None = semua)
            delay (int): Delay antar download (detik)
            max_retries (int): Maksimal percobaan ulang per file
        """
        if df.empty:
            logger.warning("DataFrame kosong, tidak ada file yang di-download")
            return
        
        if file_types is None:
            file_types = ['.pdf', '.xlsx', '.xls', '.doc', '.docx']
        
        success_count = 0
        fail_count = 0
        skip_count = 0
        
        logger.info(f"Mendownload file dengan tipe: {file_types} menggunakan Playwright")
        
        # Download link utama
        for idx, row in df.iterrows():
            url = row['LinkUtama']
            
            if not url or pd.isna(url):
                continue
            
            # Cek apakah URL sesuai dengan tipe file yang diinginkan
            if not any(file_type in url.lower() for file_type in file_types):
                continue
            
            # Buat nama file yang aman
            safe_kode = row['KodeEmiten'] if pd.notna(row['KodeEmiten']) and row['KodeEmiten'] else f"unknown_{idx}"
            safe_tanggal = row['Tanggal'].replace('-', '') if pd.notna(row['Tanggal']) and row['Tanggal'] else f"date_{idx}"
            
            # Ambil ekstensi file dari URL
            file_ext = '.pdf'  # default
            for ext in file_types:
                if ext in url.lower():
                    file_ext = ext
                    break
            
            # Tambahkan nomor unik untuk menghindari duplikat
            unique_id = f"{safe_kode}_{safe_tanggal}_{idx}"
            filename = f"{unique_id}_utama{file_ext}"
            filepath = self.pdf_dir / filename
            
            # Skip jika file sudah ada
            if filepath.exists():
                logger.debug(f"File sudah ada: {filename}")
                skip_count += 1
                continue
            
            # Download dengan Playwright
            downloaded = self._download_with_playwright(url, filepath, filename, max_retries)
            
            if downloaded:
                success_count += 1
            else:
                fail_count += 1
            
            # Delay antar download
            if delay > 0:
                time.sleep(delay)
        
        # Download lampiran
        for idx, row in df.iterrows():
            lampiran_data = row.get('LampiranData')
            
            if not lampiran_data or pd.isna(lampiran_data):
                continue
            
            try:
                lampiran_list = json.loads(lampiran_data)
                
                for lamp_idx, lampiran in enumerate(lampiran_list):
                    url = lampiran.get('link')
                    
                    if not url:
                        continue
                    
                    # Cek apakah URL sesuai dengan tipe file yang diinginkan
                    if not any(file_type in url.lower() for file_type in file_types):
                        continue
                    
                    # Gunakan filename dari atribut download atau buat sendiri
                    original_filename = lampiran.get('filename')
                    if original_filename and len(original_filename) > 0:
                        # Bersihkan filename
                        safe_filename = re.sub(r'[^\w\-_.]', '_', original_filename)
                        filename = safe_filename
                    else:
                        safe_kode = row['KodeEmiten'] if pd.notna(row['KodeEmiten']) and row['KodeEmiten'] else f"unknown_{idx}"
                        safe_tanggal = row['Tanggal'].replace('-', '') if pd.notna(row['Tanggal']) and row['Tanggal'] else f"date_{idx}"
                        
                        # Ambil ekstensi file dari URL
                        file_ext = '.pdf'  # default
                        for ext in file_types:
                            if ext in url.lower():
                                file_ext = ext
                                break
                        
                        filename = f"{safe_kode}_{safe_tanggal}_lamp{lamp_idx + 1}{file_ext}"
                    
                    filepath = self.pdf_dir / filename
                    
                    # Skip jika file sudah ada
                    if filepath.exists():
                        logger.debug(f"File sudah ada: {filename}")
                        skip_count += 1
                        continue
                    
                    # Download dengan Playwright
                    downloaded = self._download_with_playwright(url, filepath, filename, max_retries)
                    
                    if downloaded:
                        success_count += 1
                    else:
                        fail_count += 1
                    
                    # Delay antar download
                    if delay > 0:
                        time.sleep(delay)
                        
            except Exception as e:
                logger.error(f"Error processing attachments for row {idx}: {e}")
                continue
        
        # Log summary
        logger.info(f"Download summary: {success_count} berhasil, {fail_count} gagal, {skip_count} skip")
    
    def _download_with_playwright(self, url, filepath, filename, max_retries):
        """Download file menggunakan Playwright"""
        for retry in range(max_retries):
            try:
                logger.info(f"Downloading dengan Playwright: {filename}")
                
                with sync_playwright() as p:
                    browser = p.chromium.launch(
                        headless=True,  # Headless untuk download
                        args=[
                            '--disable-blink-features=AutomationControlled',
                            '--no-sandbox',
                        ]
                    )
                    
                    context = browser.new_context(
                        accept_downloads=True,
                        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        viewport={'width': 1920, 'height': 1080}
                    )
                    
                    page = context.new_page()
                    
                    try:
                        # Set up download event
                        download_promise = page.wait_for_event("download")
                        
                        # Navigasi ke URL
                        page.goto(url, timeout=30000, wait_until='networkidle')
                        
                        # Jika tidak otomatis download, coba klik link
                        if "application/pdf" not in page.content():
                            # Cari elemen download
                            download_selector = "a[download], button[download], [href*='.pdf'], [href*='.xlsx']"
                            elements = page.query_selector_all(download_selector)
                            
                            if elements:
                                elements[0].click()
                        
                        # Tunggu download
                        download = download_promise.value
                        
                        # Simpan file
                        download.save_as(filepath)
                        
                        # Tunggu hingga file benar-benar tersimpan
                        time.sleep(1)
                        
                        # Verifikasi file berhasil disimpan
                        if filepath.exists() and filepath.stat().st_size > 0:
                            logger.info(f"✓ Berhasil download: {filename}")
                            return True
                        else:
                            logger.error(f"File kosong atau tidak tersimpan: {filename}")
                            return False
                        
                    except Exception as e:
                        logger.error(f"Error download dengan Playwright: {e}")
                        
                        # Fallback: coba dengan API request langsung dari page context
                        try:
                            response = page.request.get(url, timeout=30000)
                            if response.status == 200:
                                with open(filepath, 'wb') as f:
                                    f.write(response.body())
                                logger.info(f"✓ Berhasil download (fallback): {filename}")
                                return True
                        except Exception as e2:
                            logger.error(f"Fallback juga gagal: {e2}")
                            return False
                            
                    finally:
                        browser.close()
                        
            except Exception as e:
                logger.error(f"Percobaan {retry + 1} gagal untuk {filename}: {str(e)}")
                
                if retry < max_retries - 1:
                    wait_time = 2 * (retry + 1)  # Exponential backoff
                    logger.info(f"Menunggu {wait_time} detik sebelum mencoba lagi...")
                    time.sleep(wait_time)
                else:
                    logger.error(f"Gagal download setelah {max_retries} percobaan: {filename}")
                    return False
        
        return False
    
    def save_results(self, df, format='all'):
        """
        Simpan hasil scraping
        
        Args:
            df (pd.DataFrame): Data yang akan disimpan
            format (str): Format simpan ('csv', 'json', 'excel', 'all')
        """
        if df.empty:
            logger.warning("Tidak ada data untuk disimpan")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Simpan dalam berbagai format
        try:
            if format in ['csv', 'all']:
                csv_path = self.data_dir / f"idx_disclosures_{timestamp}.csv"
                df.to_csv(csv_path, index=False, encoding='utf-8-sig')
                logger.info(f"Data disimpan ke CSV: {csv_path}")
            
            if format in ['json', 'all']:
                json_path = self.data_dir / f"idx_disclosures_{timestamp}.json"
                # Konversi tipe data untuk JSON
                json_df = df.copy()
                # Konversi semua kolom dengan tipe object ke string
                for col in json_df.columns:
                    if json_df[col].dtype == 'object':
                        json_df[col] = json_df[col].astype(str)
                
                json_df.to_json(json_path, orient='records', indent=2, force_ascii=False)
                logger.info(f"Data disimpan ke JSON: {json_path}")
            
            if format in ['excel', 'all']:
                excel_path = self.data_dir / f"idx_disclosures_{timestamp}.xlsx"
                
                # Untuk Excel, kita perlu menangani kolom dengan data JSON
                excel_df = df.copy()
                if 'LampiranData' in excel_df.columns:
                    excel_df['LampiranData'] = excel_df['LampiranData'].apply(
                        lambda x: str(x)[:1000] + "..." if isinstance(x, str) and len(x) > 1000 else x
                    )
                
                excel_df.to_excel(excel_path, index=False)
                logger.info(f"Data disimpan ke Excel: {excel_path}")
            
            # Simpan juga summary statistik
            self.save_statistics(df, timestamp)
            
        except Exception as e:
            logger.error(f"Error saving results: {e}")
            raise
    
    def save_statistics(self, df, timestamp):
        """Simpan statistik scraping"""
        try:
            # Konversi nilai numpy ke Python native
            total_records = int(len(df))
            
            unique_emiten = 0
            if 'KodeEmiten' in df.columns:
                unique_emiten = int(df['KodeEmiten'].nunique())
            
            # Tangani nilai NaN untuk date_range
            date_min = ""
            date_max = ""
            if 'Tanggal' in df.columns:
                tanggal_min = df['Tanggal'].min()
                tanggal_max = df['Tanggal'].max()
                if pd.notna(tanggal_min):
                    date_min = str(tanggal_min)
                if pd.notna(tanggal_max):
                    date_max = str(tanggal_max)
            
            pdf_count = 0
            if 'LinkUtama' in df.columns:
                pdf_count = int(df['LinkUtama'].str.contains('.pdf', case=False, na=False).sum())
            
            total_attachments = 0
            if 'JumlahLampiran' in df.columns:
                total_attachments = int(df['JumlahLampiran'].sum())
            
            total_pages = 0
            if 'Halaman' in df.columns:
                total_pages = int(df['Halaman'].max())
            
            stats = {
                "total_records": total_records,
                "unique_emiten": unique_emiten,
                "date_range": {
                    "min": date_min,
                    "max": date_max
                },
                "pdf_count": pdf_count,
                "total_attachments": total_attachments,
                "total_pages": total_pages,
                "scraped_at": datetime.now().isoformat(),
            }
            
            stats_path = self.data_dir / f"scraping_stats_{timestamp}.json"
            with open(stats_path, 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Statistik disimpan: {stats_path}")
            
            # Print summary ke console
            print("\n" + "="*50)
            print("📊 SCRAPING SUMMARY")
            print("="*50)
            print(f"Total Data: {stats['total_records']}")
            print(f"Perusahaan Unik: {stats['unique_emiten']}")
            print(f"Total Halaman: {stats['total_pages']}")
            print(f"Rentang Tanggal: {stats['date_range']['min']} hingga {stats['date_range']['max']}")
            print(f"Jumlah PDF Utama: {stats['pdf_count']}")
            print(f"Total Lampiran: {stats['total_attachments']}")
            print("="*50)
            
        except Exception as e:
            logger.error(f"Error saving statistics: {e}")


def main():
    """Fungsi utama"""
    print("="*70)
    print("IDX DISCLOSURE INFORMATION SCRAPER (WITH PAGINATION)")
    print("="*70)
    
    # Konfigurasi
    config = {
        'headless': False,          # Set True untuk production, False untuk debugging
        'slow_mo': 100,             # Delay antar aksi (ms)
        'max_retries': 3,           # Maksimal percobaan ulang
        'max_pages': 3,             # Maksimal halaman yang di-scrape (None untuk semua)
        'download_files': True,     # Download file
        'file_types': ['.pdf'],     # Tipe file yang didownload
        'download_delay': 2,        # Delay antar download (detik) - lebih lama untuk Playwright
        'save_format': 'csv'        # Format penyimpanan
    }
    
    # Prompt konfigurasi
    print("\n⚙️  KONFIGURASI SCRAPER")
    print(f"1. Mode Browser: {'HEADLESS' if config['headless'] else 'VISIBLE'}")
    print(f"2. Max Retries: {config['max_retries']}")
    print(f"3. Max Pages: {config['max_pages'] or 'Semua'}")
    print(f"4. Download File: {'YA' if config['download_files'] else 'TIDAK'}")
    print(f"5. File Types: {', '.join(config['file_types'])}")
    print(f"6. Save Format: {config['save_format']}")
    
    change = input("\nUbah konfigurasi? (y/N): ").strip().lower()
    
    if change == 'y':
        headless_input = input("Mode headless? (y/N): ").strip().lower()
        config['headless'] = headless_input == 'y'
        
        retries_input = input(f"Max retries [{config['max_retries']}]: ").strip()
        if retries_input:
            config['max_retries'] = int(retries_input)
        
        pages_input = input(f"Max pages (0 untuk semua) [{config['max_pages']}]: ").strip()
        if pages_input:
            if pages_input == "0":
                config['max_pages'] = None
            else:
                config['max_pages'] = int(pages_input)
        
        download_input = input("Download files? (Y/n): ").strip().lower()
        if download_input == 'n':
            config['download_files'] = False
        
        filetypes_input = input("File types (comma separated) [.pdf]: ").strip()
        if filetypes_input:
            config['file_types'] = [ft.strip() for ft in filetypes_input.split(',')]
        
        delay_input = input(f"Download delay (detik) [{config['download_delay']}]: ").strip()
        if delay_input:
            config['download_delay'] = float(delay_input)
        
        format_input = input("Save format (csv/json/excel/all) [csv]: ").strip().lower()
        if format_input in ['csv', 'json', 'excel', 'all']:
            config['save_format'] = format_input
    
    # Inisialisasi scraper
    scraper = IDXDisclosureScraper(
        headless=config['headless'],
        slow_mo=config['slow_mo']
    )
    
    try:
        # Mulai scraping
        print("\n" + "="*70)
        print("🚀 MEMULAI SCRAPING...")
        print("="*70)
        
        start_time = time.time()
        
        # Scrape data dengan pagination
        df = scraper.scrape_with_retry(
            max_retries=config['max_retries'],
            max_pages=config['max_pages']
        )
        
        if df.empty:
            print("\n❌ Tidak ada data yang berhasil di-scrape")
            return
        
        elapsed_time = time.time() - start_time
        print(f"\n⏱️  Waktu scraping: {elapsed_time:.2f} detik")
        
        # Tampilkan preview data
        print("\n📋 PREVIEW DATA (5 baris pertama):")
        if not df.empty:
            print(df[['Halaman', 'Tanggal', 'KodeEmiten', 'Judul', 'JumlahLampiran']].head().to_string())
        else:
            print("DataFrame kosong")
        
        # Simpan hasil
        scraper.save_results(df, format=config['save_format'])
        
        # Download file jika diaktifkan (gunakan Playwright)
        if config['download_files'] and not df.empty:
            print("\n" + "="*70)
            print("📥 MENDOWNLOAD FILE (menggunakan Playwright)...")
            print("="*70)
            
            pdf_start = time.time()
            scraper.download_files_with_playwright(
                df, 
                file_types=config['file_types'], 
                delay=config['download_delay']
            )
            pdf_time = time.time() - pdf_start
            
            print(f"\n⏱️  Waktu download file: {pdf_time:.2f} detik")
        
        print("\n" + "="*70)
        print("✅ SCRAPING SELESAI!")
        print("="*70)
        
        # Tampilkan lokasi file
        print("\n📁 FILE YANG DIBUAT:")
        print(f"Data: {scraper.data_dir.absolute()}/")
        if config['download_files']:
            print(f"PDF/Files: {scraper.pdf_dir.absolute()}/")
        print(f"Log: idx_scraper.log")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Scraping dihentikan oleh pengguna")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()