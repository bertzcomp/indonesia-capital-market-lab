import requests
from bs4 import BeautifulSoup
import json
import time
import os
import re
from datetime import datetime, timedelta
from urllib.parse import urljoin, parse_qs, urlparse
import html

class IDXChannelLoadMoreScraper:
    def __init__(self):
        self.base_url = "https://www.idxchannel.com"
        self.session = requests.Session()
        
        # Headers untuk menyerupai browser
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://www.idxchannel.com/',
            'Upgrade-Insecure-Requests': '1',
        }
        self.session.headers.update(self.headers)
    
    def parse_js_function(self, onclick_text):
        # Cari URL dalam tanda kutip
        pattern = r"myFunction\('([^']+)'\)"
        match = re.search(pattern, onclick_text)
        if match:
            return match.group(1)
        return None
    
    def extract_url_from_onclick(self, onclick_text):
        """Ekstrak URL dari atribut onclick"""
        # Coba berbagai pola
        patterns = [
            r"['\"](https?://[^'\"]+)['\"]",
            r"myFunction\('([^']+)'\)",
            r"loadMore\('([^']+)'\)",
            r"window\.location\s*=\s*['\"]([^'\"]+)['\"]"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, onclick_text)
            if match:
                url = match.group(1)
                # Pastikan URL lengkap
                if url.startswith('//'):
                    url = 'https:' + url
                elif url.startswith('/'):
                    url = self.base_url + url
                return url
        
        return None
    
    def scrape_single_day_with_loadmore(self, date_obj):
        """
        Scrape satu hari dengan menangani tombol 'Load More'
        
        Args:
            date_obj: Objek datetime.date untuk hari yang akan discrape
            
        Returns:
            List artikel untuk hari tersebut
        """
        # Format tanggal untuk URL
        date_ymd = date_obj.strftime("%Y-%m-%d")  # Format: 2025-12-15
        date_dmy = date_obj.strftime("%d-%m-%Y")  # Format: 15-12-2025
        
        # URL halaman utama untuk hari ini
        main_url = f"{self.base_url}/indeks?date={date_ymd}&idkanal=1"
        
        print(f"\n📅 Tanggal: {date_obj.strftime('%d/%m/%Y')}")
        print(f"🌐 URL: {main_url}")
        
        all_articles = []
        current_offset = 0
        batch_count = 0
        max_batches = 20  # Maksimal batch untuk mencegah infinite loop
        
        while batch_count < max_batches:
            if batch_count == 0:
                # Batch pertama - ambil dari halaman utama
                url = main_url
                print(f"  🔄 Batch {batch_count + 1}: Halaman utama")
            else:
                # Batch berikutnya - gunakan URL load more
                # Format: https://www.idxchannel.com/indeks/more/{offset}?idkanal=1&date=15-12-2025
                url = f"{self.base_url}/indeks/more/{current_offset}?idkanal=1&date={date_dmy}"
                print(f"  🔄 Batch {batch_count + 1}: Load more (offset={current_offset})")
            
            try:
                # Request halaman
                response = self.session.get(url, timeout=30)
                
                if response.status_code != 200:
                    print(f"    ⚠️ Status: {response.status_code}")
                    break
                
                # Parse HTML
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Ekstrak artikel dari batch ini
                batch_articles = self.extract_articles_from_batch(soup, date_ymd, batch_count)
                
                if not batch_articles:
                    print(f"    ℹ️ Tidak ada artikel di batch ini")
                    break
                
                print(f"    ✅ {len(batch_articles)} artikel ditemukan")
                all_articles.extend(batch_articles)
                
                # Cek apakah ada tombol "Load More"
                load_more_button = soup.find('a', id='NextRow') or \
                                 soup.find('a', class_=lambda x: x and 'load-more' in str(x)) or \
                                 soup.find('div', class_='button-default')
                
                if load_more_button:
                    # Cek atribut onclick
                    onclick_text = load_more_button.get('onclick', '')
                    
                    if onclick_text:
                        # Parse URL dari fungsi JavaScript
                        js_url = self.extract_url_from_onclick(onclick_text)
                        
                        if js_url:
                            # Ekstrak offset dari URL
                            # Contoh: https://www.idxchannel.com/indeks/more/9?idkanal=1&date=15-12-2025
                            parsed_url = urlparse(js_url)
                            path_parts = parsed_url.path.split('/')
                            
                            # Cari angka setelah 'more/'
                            for i, part in enumerate(path_parts):
                                if part == 'more' and i + 1 < len(path_parts):
                                    try:
                                        new_offset = int(path_parts[i + 1])
                                        if new_offset > current_offset:
                                            current_offset = new_offset
                                        else:
                                            # Jika offset tidak bertambah, mungkin sudah selesai
                                            print(f"    ⏹️ Tidak ada artikel baru (offset tetap)")
                                            break
                                    except:
                                        # Default: tambah 9
                                        current_offset += 9
                                    break
                            else:
                                # Jika tidak ditemukan offset, tambah 9
                                current_offset += 9
                        else:
                            # Jika tidak bisa parse URL, tambah 9
                            current_offset += 9
                    else:
                        # Jika tidak ada onclick, mungkin tombol sudah tidak aktif
                        print(f"    ⏹️ Tombol load more tidak aktif")
                        break
                else:
                    # Tidak ada tombol load more
                    print(f"    ⏹️ Tidak ada tombol load more")
                    break
                
                # Delay antar batch
                time.sleep(1)
                batch_count += 1
                
            except Exception as e:
                print(f"    ❌ Error: {str(e)[:50]}")
                break
        
        print(f"  📊 Total: {len(all_articles)} artikel dari {batch_count} batch")
        return all_articles
    
    def extract_articles_from_batch(self, soup, date_str, batch_num):
        """Ekstrak artikel dari sebuah batch HTML"""
        articles = []
        
        # Cari semua container berita
        # Coba berbagai selector
        selectors = [
            'div.bt-con',
            'div[class*="news"]',
            'article',
            'div.post',
            'div.item'
        ]
        
        for selector in selectors:
            news_elements = soup.select(selector)
            if news_elements:
                # Filter hanya yang mengandung link market-news
                filtered_elements = []
                for elem in news_elements:
                    if elem.find('a', href=lambda x: x and '/market-news/' in x):
                        filtered_elements.append(elem)
                
                if filtered_elements:
                    for element in filtered_elements:
                        article = self.extract_article_data(element, date_str, batch_num)
                        if article:
                            articles.append(article)
                    break
        
        return articles
    
    def extract_article_data(self, element, date_str, batch_num):
        """Ekstrak data artikel dari elemen HTML"""
        try:
            # 1. Judul - perbaikan selector untuk menangani perbedaan struktur
            title = "N/A"
            
            # Coba cari dengan berbagai cara
            # Cara 1: Cari langsung link dengan pattern market-news
            title_selectors = [
                '.list-berita-baru a',  # Untuk kedua struktur (h2 atau div dengan class ini)
                'h2 a',
                'h3 a', 
                'h4 a',
                'div.title-capt a',
                'a[href*="/market-news/"]'  # Link market-news langsung
            ]
            
            for selector in title_selectors:
                title_elem = element.select_one(selector)
                if title_elem:
                    title_text = title_elem.get_text(strip=True)
                    if title_text and len(title_text) > 5:
                        title = html.unescape(title_text)
                        break
            
            # Jika masih tidak ditemukan, coba cari dari tag <a> di dalam element
            if title == "N/A":
                all_links = element.find_all('a', href=lambda x: x and '/market-news/' in x)
                for link in all_links:
                    link_text = link.get_text(strip=True)
                    if link_text and len(link_text) > 5:
                        title = html.unescape(link_text)
                        break
            
            # 2. URL
            url = "N/A"
            link_elem = element.find('a', href=lambda x: x and '/market-news/' in x)
            if link_elem:
                href = link_elem.get('href', '')
                url = urljoin(self.base_url, href)
            
            # 3. Tanggal
            date_display = "N/A"
            date_selectors = [
                'span.mh-clock',
                '.date', '.time',
                'span.date',
                'time'
            ]
            
            for selector in date_selectors:
                date_elem = element.select_one(selector)
                if date_elem:
                    date_text = date_elem.get_text(strip=True)
                    if date_text:
                        date_display = date_text
                        break
            
            # 4. Gambar
            image_url = ""
            img_elem = element.find('img')
            if img_elem:
                image_url = img_elem.get('data-original') or img_elem.get('src', '')
                if image_url:
                    if image_url.startswith('//'):
                        image_url = 'https:' + image_url
                    elif image_url.startswith('/'):
                        image_url = self.base_url + image_url
            
            # 5. Parsing tanggal yang benar
            parsed_date = self.parse_article_date(date_display, date_str)
            
            # 6. Kategori
            category = "Market News"
            category_elem = element.select_one('.category, .kanal, .channel, .headline-kanal')
            if category_elem:
                category_text = category_elem.get_text(strip=True)
                if category_text:
                    category = category_text
            
            return {
                'title': title,
                'url': url,
                'date_display': date_display,
                'date': parsed_date,
                'image_url': image_url,
                'category': category,
                'batch': batch_num,
                'source': 'IDX Channel',
                'scraped_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"      ⚠️ Error ekstraksi artikel: {e}")
            return None
    
    def parse_article_date(self, date_text, default_date):
        """Parse tanggal artikel"""
        if not date_text or date_text == "N/A":
            return default_date
        
        try:
            # Coba format "15/01/2026 22:20 WIB"
            pattern = r'(\d{1,2})/(\d{1,2})/(\d{4})'
            match = re.search(pattern, date_text)
            if match:
                day, month, year = match.groups()
                return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        except:
            pass
        
        return default_date
    
    def scrape_date_range(self, start_date, end_date, delay=2):
        """
        Scrape rentang tanggal dengan menangani load more
        
        Args:
            start_date: datetime.date - Tanggal mulai
            end_date: datetime.date - Tanggal akhir
            delay: int - Delay antar hari (detik)
            
        Returns:
            List semua artikel
        """
        all_articles = []
        current_date = start_date
        days_count = (end_date - start_date).days + 1
        
        print(f"\n📊 Akan scrape {days_count} hari")
        print(f"📅 Dari {start_date.strftime('%d/%m/%Y')} hingga {end_date.strftime('%d/%m/%Y')}")
        print(f"⏰ Delay antar hari: {delay} detik")
        print("=" * 60)
        
        for day_num in range(days_count):
            print(f"\n📅 Hari {day_num + 1}/{days_count}:")
            
            # Scrape hari ini
            day_articles = self.scrape_single_day_with_loadmore(current_date)
            all_articles.extend(day_articles)
            
            print(f"  📈 Progress: {len(all_articles)} artikel terkumpul")
            
            # Pindah ke hari berikutnya
            current_date += timedelta(days=1)
            
            # Delay antar hari (kecuali hari terakhir)
            if day_num < days_count - 1:
                print(f"  ⏳ Menunggu {delay} detik...")
                time.sleep(delay)
        
        return all_articles
    
    def save_results(self, articles, start_date, end_date):
        """Simpan hasil ke file JSON"""
        if not articles:
            print("\n❌ Tidak ada artikel untuk disimpan")
            return None
        
        # Buat folder data jika belum ada
        if not os.path.exists('data'):
            os.makedirs('data')
        
        # Format nama file
        start_str = start_date.strftime("%Y%m%d")
        end_str = end_date.strftime("%Y%m%d")
        timestamp = datetime.now().strftime("%H%M%S")
        filename = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/idxchannel_market_news_summary{start_str}_{end_str}_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(articles, f, indent=2, ensure_ascii=False)
            
            print(f"\n✅ Berhasil menyimpan {len(articles)} artikel")
            print(f"📁 File: {filename}")
            
            # Tampilkan statistik
            self.print_statistics(articles)
            
            return filename
            
        except Exception as e:
            print(f"❌ Error menyimpan file: {e}")
            return None
    
    def print_statistics(self, articles):
        """Tampilkan statistik scraping"""
        print("\n📊 STATISTIK:")
        print(f"   Total artikel: {len(articles)}")
        
        # Hitung per hari
        from collections import Counter
        date_counts = Counter([a.get('date', 'Unknown')[:10] for a in articles])
        
        print(f"\n   Distribusi per hari:")
        for date, count in sorted(date_counts.items()):
            if date != 'Unknown':
                # Format ulang tanggal untuk display
                try:
                    display_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
                except:
                    display_date = date
                print(f"     {display_date}: {count} artikel")
        
        # Hitung total batch
        total_batches = sum([a.get('batch', 0) + 1 for a in articles])
        avg_batch = total_batches / len(articles) if articles else 0
        print(f"   Rata-rata batch per artikel: {avg_batch:.1f}")
        
        # Tampilkan contoh
        if articles:
            print("\n📰 CONTOH ARTIKEL (3 pertama):")
            for i, article in enumerate(articles[:3]):
                print(f"\n--- Artikel #{i+1} ---")
                print(f"Judul: {article.get('title', 'N/A')[:60]}...")
                print(f"Tanggal: {article.get('date_display', 'N/A')}")
                print(f"URL: {article.get('url', 'N/A')[:70]}...")
                print(f"Kategori: {article.get('category', 'N/A')}")

def validate_date_input(date_str):
    """Validasi input tanggal"""
    formats = ['%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d', '%d %b %Y', '%d %B %Y']
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    
    return None

def main():
    """Program utama"""
    print("="*70)
    print("IDX CHANNEL LOAD MORE SCRAPER")
    print("="*70)
    
    # Input tanggal
    print("\n📅 MASUKKAN RENTANG TANGGAL")
    print("   Format: DD/MM/YYYY atau DD-MM-YYYY")
    print("   Contoh: 15/12/2025 atau 15-12-2025")
    
    # Tanggal mulai
    while True:
        start_input = input("\nTanggal mulai: ").strip()
        start_date = validate_date_input(start_input)
        
        if start_date:
            print(f"   ✅ Tanggal mulai: {start_date.strftime('%d/%m/%Y')}")
            break
        else:
            print("   ❌ Format tanggal salah")
    
    # Tanggal akhir
    while True:
        end_input = input("\nTanggal akhir (kosong untuk hari ini): ").strip()
        
        if not end_input:
            end_date = datetime.now().date()
            print(f"   ✅ Tanggal akhir: {end_date.strftime('%d/%m/%Y')} (hari ini)")
            break
        
        end_date = validate_date_input(end_input)
        
        if end_date:
            if end_date < start_date:
                print("   ❌ Tanggal akhir tidak boleh sebelum tanggal mulai")
            else:
                print(f"   ✅ Tanggal akhir: {end_date.strftime('%d/%m/%Y')}")
                break
        else:
            print("   ❌ Format tanggal salah")
    
    # Hitung jumlah hari
    days_count = (end_date - start_date).days + 1
    
    if days_count > 10:
        print(f"\n⚠️  PERINGATAN: Akan scrape {days_count} hari")
        print("   Ini mungkin memakan waktu lama")
    
    # Delay
    delay_input = input(f"\nDelay antar hari (detik, default=2, rekomendasi untuk {days_count} hari: {min(3, days_count)}): ").strip()
    try:
        delay = float(delay_input) if delay_input else min(3, days_count)
    except:
        delay = min(3, days_count)
    
    # Konfirmasi
    print("\n" + "="*70)
    print("⚙️  KONFIGURASI SCRAPING")
    print("="*70)
    print(f"📅 Rentang: {start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')} ({days_count} hari)")
    print(f"⏰ Delay antar hari: {delay} detik")
    print(f"🌐 Mode: Load More (AJAX)")
    print(f"🔗 Pattern URL: /indeks/more/[offset]?idkanal=1&date=DD-MM-YYYY")
    
    confirm = input("\nLanjutkan scraping? (y/n): ").lower().strip()
    if confirm != 'y':
        print("❌ Dibatalkan")
        return
    
    # Inisialisasi scraper
    scraper = IDXChannelLoadMoreScraper()
    
    # Mulai scraping
    print("\n" + "="*70)
    print("🚀 MEMULAI SCRAPING...")
    print("="*70)
    
    start_time = time.time()
    
    try:
        articles = scraper.scrape_date_range(start_date, end_date, delay)
        
        elapsed_time = time.time() - start_time
        print(f"\n⏱️  Waktu eksekusi: {elapsed_time:.1f} detik")
        
        # Simpan hasil
        if articles:
            scraper.save_results(articles, start_date, end_date)
        else:
            print("\n❌ Tidak ada artikel yang ditemukan")
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Scraping dihentikan oleh pengguna")
        
        # Coba simpan data yang sudah terkumpul
        if 'scraper' in locals() and 'articles' in locals() and articles:
            timestamp = datetime.now().strftime("%H%M%S")
            temp_file = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/idxchannel_partial_{timestamp}.json"
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(articles, f, indent=2, ensure_ascii=False)
            print(f"💾 Data parsial disimpan: {temp_file}")
        else:
            print("ℹ️ Tidak ada data yang dapat disimpan")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

def test_single_day():
    """Test scraping satu hari saja"""
    print("\n🔧 MODE TEST - Scrape 1 hari")
    
    # Gunakan hari ini
    test_date = datetime.now().date()
    print(f"📅 Tanggal test: {test_date.strftime('%d/%m/%Y')}")
    
    scraper = IDXChannelLoadMoreScraper()
    articles = scraper.scrape_single_day_with_loadmore(test_date)
    
    if articles:
        # Simpan sample
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/test_loadmore_{timestamp}.json"
        
        if not os.path.exists('data'):
            os.makedirs('data')
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Berhasil: {len(articles)} artikel")
        print(f"📁 Disimpan: {filename}")
        
        # Tampilkan detail load more
        batches = set([a.get('batch', 0) for a in articles])
        print(f"🔁 Batch: {len(batches)} ({', '.join(map(str, sorted(batches)))})")
        
        # Tampilkan contoh
        for i, article in enumerate(articles[:2]):
            print(f"\n{i+1}. {article['title'][:50]}...")
            print(f"   Batch: {article.get('batch', 0)}")
            print(f"   Tanggal: {article['date_display']}")
    else:
        print("\n❌ Tidak ada artikel")

if __name__ == "__main__":
    print("="*70)
    print("PILIH MODE:")
    print("1. Scraping rentang tanggal (utama)")
    print("2. Test scraping 1 hari")
    print("3. Keluar")
    
    choice = input("\nPilihan (1-3): ").strip()
    
    if choice == '1':
        main()
    elif choice == '2':
        test_single_day()
    else:
        print("👋 Keluar...")