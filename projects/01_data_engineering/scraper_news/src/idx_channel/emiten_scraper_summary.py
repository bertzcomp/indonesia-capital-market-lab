import requests
from bs4 import BeautifulSoup
import json
import time
import os
import re
from datetime import datetime, timedelta
from urllib.parse import urljoin, parse_qs, urlparse, quote
import html

class IDXChannelScraper:
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
    
    def extract_url_from_onclick(self, onclick_text):
        """Ekstrak URL dari atribut onclick"""
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
                if url.startswith('//'):
                    url = 'https:' + url
                elif url.startswith('/'):
                    url = self.base_url + url
                return url
        
        return None
    
    # SCRAPING BERDASARKAN TANGGAL
    def scrape_by_date_with_loadmore(self, date_obj):
        """
        Args: -> date_obj: Objek datetime.date untuk hari yang akan discrape 
        Returns: -> List artikel untuk hari tersebut
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
        max_batches = 20
        
        while batch_count < max_batches:
            if batch_count == 0:
                url = main_url
                print(f"  🔄 Batch {batch_count + 1}: Halaman utama")
            else:
                url = f"{self.base_url}/indeks/more/{current_offset}?idkanal=1&date={date_dmy}"
                print(f"  🔄 Batch {batch_count + 1}: Load more (offset={current_offset})")
            
            try:
                response = self.session.get(url, timeout=30)
                
                if response.status_code != 200:
                    print(f"    ⚠️ Status: {response.status_code}")
                    break
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Ekstrak artikel
                batch_articles = self.extract_articles_from_batch(soup, date_ymd, batch_count)
                
                if not batch_articles:
                    print(f"    ℹ️ Tidak ada artikel di batch ini")
                    break
                
                print(f"    ✅ {len(batch_articles)} artikel ditemukan")
                all_articles.extend(batch_articles)
                
                # Cek tombol "Load More"
                load_more_button = soup.find('a', id='NextRow') or \
                                 soup.find('a', class_=lambda x: x and 'load-more' in str(x)) or \
                                 soup.find('div', class_='button-default')
                
                if load_more_button:
                    onclick_text = load_more_button.get('onclick', '')
                    
                    if onclick_text:
                        js_url = self.extract_url_from_onclick(onclick_text)
                        
                        if js_url:
                            parsed_url = urlparse(js_url)
                            path_parts = parsed_url.path.split('/')
                            
                            for i, part in enumerate(path_parts):
                                if part == 'more' and i + 1 < len(path_parts):
                                    try:
                                        new_offset = int(path_parts[i + 1])
                                        if new_offset > current_offset:
                                            current_offset = new_offset
                                        else:
                                            print(f"    ⏹️ Tidak ada artikel baru (offset tetap)")
                                            break
                                    except:
                                        current_offset += 9
                                    break
                            else:
                                current_offset += 9
                        else:
                            current_offset += 9
                    else:
                        print(f"    ⏹️ Tombol load more tidak aktif")
                        break
                else:
                    print(f"    ⏹️ Tidak ada tombol load more")
                    break
                
                time.sleep(1)
                batch_count += 1
                
            except Exception as e:
                print(f"    ❌ Error: {str(e)[:50]}")
                break
        
        print(f"  📊 Total: {len(all_articles)} artikel dari {batch_count} batch")
        return all_articles
    
    # SCRAPING BERDASARKAN KEYWORD/EMITEN
    def scrape_by_keyword_with_loadmore(self, keyword, max_batches=20):
        """
        Args:
            keyword: String keyword untuk pencarian
            max_batches: Maksimal batch untuk load more
            
        Returns:
            List artikel untuk keyword tersebut
        """
        # Encode keyword untuk URL
        encoded_keyword = quote(keyword)
        
        # URL pencarian
        search_url = f"{self.base_url}/search?search={encoded_keyword}&set=keyword&idkanal=1&kategori="
        
        print(f"\n🔍 Keyword: {keyword}")
        print(f"🌐 URL: {search_url}")
        
        all_articles = []
        current_offset = 0
        batch_count = 0
        
        while batch_count < max_batches:
            if batch_count == 0:
                url = search_url
                print(f"  🔄 Batch {batch_count + 1}: Halaman utama pencarian")
            else:
                # Format load more untuk pencarian (asumsi mirip dengan indeks)
                # Perlu diverifikasi struktur URL-nya
                url = f"{self.base_url}/search/more/{current_offset}?search={encoded_keyword}&set=keyword&idkanal=1&kategori="
                print(f"  🔄 Batch {batch_count + 1}: Load more pencarian (offset={current_offset})")
            
            try:
                response = self.session.get(url, timeout=30)
                
                if response.status_code != 200:
                    print(f"    ⚠️ Status: {response.status_code}")
                    break
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Ekstrak artikel (gunakan tanggal default)
                current_date = datetime.now().strftime("%Y-%m-%d")
                batch_articles = self.extract_articles_from_batch(soup, current_date, batch_count)
                
                if not batch_articles:
                    print(f"    ℹ️ Tidak ada artikel di batch ini")
                    break
                
                print(f"    ✅ {len(batch_articles)} artikel ditemukan")
                all_articles.extend(batch_articles)
                
                # Cek tombol "Load More" di halaman pencarian
                load_more_button = soup.find('a', id='NextRow') or \
                                 soup.find('a', class_=lambda x: x and 'load-more' in str(x)) or \
                                 soup.find('div', class_='button-default') or \
                                 soup.find('a', string=lambda x: x and 'Load More' in str(x))
                
                if load_more_button:
                    onclick_text = load_more_button.get('onclick', '')
                    
                    if onclick_text:
                        js_url = self.extract_url_from_onclick(onclick_text)
                        
                        if js_url:
                            parsed_url = urlparse(js_url)
                            path_parts = parsed_url.path.split('/')
                            
                            for i, part in enumerate(path_parts):
                                if part == 'more' and i + 1 < len(path_parts):
                                    try:
                                        new_offset = int(path_parts[i + 1])
                                        if new_offset > current_offset:
                                            current_offset = new_offset
                                        else:
                                            print(f"    ⏹️ Tidak ada artikel baru (offset tetap)")
                                            break
                                    except:
                                        current_offset += 9
                                    break
                            else:
                                current_offset += 9
                        else:
                            current_offset += 9
                    else:
                        # Coba cari link ke halaman berikutnya
                        next_link = soup.find('a', href=lambda x: x and 'page=' in str(x))
                        if next_link:
                            href = next_link.get('href', '')
                            # Ekstrak page number dari URL
                            page_match = re.search(r'page=(\d+)', href)
                            if page_match:
                                current_offset = (int(page_match.group(1)) - 1) * 9
                            else:
                                current_offset += 9
                        else:
                            print(f"    ⏹️ Tombol load more tidak aktif")
                            break
                else:
                    print(f"    ⏹️ Tidak ada tombol load more")
                    break
                
                time.sleep(1)
                batch_count += 1
                
            except Exception as e:
                print(f"    ❌ Error: {str(e)[:50]}")
                break
        
        print(f"  📊 Total: {len(all_articles)} artikel dari {batch_count} batch")
        return all_articles
    
    # SCRAPING KOMBINASI KEYWORD & TANGGAL
    def scrape_keyword_date_range(self, keyword, start_date, end_date, delay=2, max_batches_per_day=10):
        """
        Scrape berdasarkan keyword dalam rentang tanggal
        
        Args:
            keyword: Keyword untuk pencarian
            start_date: Tanggal mulai
            end_date: Tanggal akhir
            delay: Delay antar hari
            max_batches_per_day: Maksimal batch per hari
            
        Returns:
            List semua artikel
        """
        all_articles = []
        current_date = start_date
        days_count = (end_date - start_date).days + 1
        
        print(f"\n📊 Akan scrape {days_count} hari untuk keyword: {keyword}")
        print(f"📅 Dari {start_date.strftime('%d/%m/%Y')} hingga {end_date.strftime('%d/%m/%Y')}")
        print(f"⏰ Delay antar hari: {delay} detik")
        print("=" * 60)
        
        for day_num in range(days_count):
            print(f"\n📅 Hari {day_num + 1}/{days_count}: {current_date.strftime('%d/%m/%Y')}")
            
            # Format tanggal untuk URL
            date_ymd = current_date.strftime("%Y-%m-%d")
            date_dmy = current_date.strftime("%d-%m-%Y")
            
            # Encode keyword
            encoded_keyword = quote(keyword)
            
            # Buat URL kombinasi keyword + tanggal
            # Format: /search?search=KEYWORD&set=keyword&idkanal=1&kategori=&date=TANGGAL
            search_url = f"{self.base_url}/search?search={encoded_keyword}&set=keyword&idkanal=1&kategori=&date={date_ymd}"
            
            print(f"  🔍 URL: {search_url}")
            
            day_articles = []
            current_offset = 0
            batch_count = 0
            
            # Scrape dengan load more untuk hari ini
            while batch_count < max_batches_per_day:
                if batch_count == 0:
                    url = search_url
                    print(f"  🔄 Batch {batch_count + 1}: Halaman utama")
                else:
                    # Asumsi format load more untuk pencarian dengan tanggal
                    url = f"{self.base_url}/search/more/{current_offset}?search={encoded_keyword}&set=keyword&idkanal=1&kategori=&date={date_dmy}"
                    print(f"  🔄 Batch {batch_count + 1}: Load more (offset={current_offset})")
                
                try:
                    response = self.session.get(url, timeout=30)
                    
                    if response.status_code != 200:
                        print(f"    ⚠️ Status: {response.status_code}")
                        break
                    
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Ekstrak artikel
                    batch_articles = self.extract_articles_from_batch(soup, date_ymd, batch_count)
                    
                    if not batch_articles:
                        print(f"    ℹ️ Tidak ada artikel di batch ini")
                        break
                    
                    print(f"    ✅ {len(batch_articles)} artikel ditemukan")
                    day_articles.extend(batch_articles)
                    
                    # Cek tombol "Load More"
                    load_more_button = soup.find('a', id='NextRow') or \
                                     soup.find('a', class_=lambda x: x and 'load-more' in str(x)) or \
                                     soup.find('div', class_='button-default')
                    
                    if load_more_button:
                        onclick_text = load_more_button.get('onclick', '')
                        
                        if onclick_text:
                            js_url = self.extract_url_from_onclick(onclick_text)
                            if js_url and 'more' in js_url:
                                parsed_url = urlparse(js_url)
                                path_parts = parsed_url.path.split('/')
                                
                                for i, part in enumerate(path_parts):
                                    if part == 'more' and i + 1 < len(path_parts):
                                        try:
                                            new_offset = int(path_parts[i + 1])
                                            if new_offset > current_offset:
                                                current_offset = new_offset
                                            else:
                                                print(f"    ⏹️ Tidak ada artikel baru (offset tetap)")
                                                break
                                        except:
                                            current_offset += 9
                                        break
                                else:
                                    current_offset += 9
                            else:
                                current_offset += 9
                        else:
                            print(f"    ⏹️ Tombol load more tidak aktif")
                            break
                    else:
                        print(f"    ⏹️ Tidak ada tombol load more")
                        break
                    
                    time.sleep(1)
                    batch_count += 1
                    
                except Exception as e:
                    print(f"    ❌ Error: {str(e)[:50]}")
                    break
            
            print(f"  📊 Hari ini: {len(day_articles)} artikel dari {batch_count} batch")
            all_articles.extend(day_articles)
            print(f"  📈 Progress total: {len(all_articles)} artikel terkumpul")
            
            # Pindah ke hari berikutnya
            current_date += timedelta(days=1)
            
            # Delay antar hari (kecuali hari terakhir)
            if day_num < days_count - 1:
                print(f"  ⏳ Menunggu {delay} detik...")
                time.sleep(delay)
        
        return all_articles
    
    # METHOD UMUM UNTUK EKSTRAKSI
    def extract_articles_from_batch(self, soup, date_str, batch_num):
        """Ekstrak artikel dari sebuah batch HTML"""
        articles = []
        
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
            # 1. Judul
            title = "N/A"
            title_selectors = [
                '.list-berita-baru a',
                'h2 a',
                'h3 a', 
                'h4 a',
                'div.title-capt a',
                'a[href*="/market-news/"]'
            ]
            
            for selector in title_selectors:
                title_elem = element.select_one(selector)
                if title_elem:
                    title_text = title_elem.get_text(strip=True)
                    if title_text and len(title_text) > 5:
                        title = html.unescape(title_text)
                        break
            
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
            
            # 5. Parsing tanggal
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
            pattern = r'(\d{1,2})/(\d{1,2})/(\d{4})'
            match = re.search(pattern, date_text)
            if match:
                day, month, year = match.groups()
                return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        except:
            pass
        
        return default_date
    
    def save_results(self, articles, filename_prefix, start_date=None, end_date=None, keyword=None):
        """Simpan hasil ke file JSON"""
        if not articles:
            print("\n❌ Tidak ada artikel untuk disimpan")
            return None
        
        if not os.path.exists('data'):
            os.makedirs('data')
        
        # Format nama file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if keyword and start_date and end_date:
            start_str = start_date.strftime("%Y%m%d")
            end_str = end_date.strftime("%Y%m%d")
            keyword_slug = re.sub(r'\W+', '_', keyword)
            filename = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/ticker/{filename_prefix}_{keyword_slug}_{start_str}_{end_str}_{timestamp}.json"
        elif keyword:
            keyword_slug = re.sub(r'\W+', '_', keyword)
            filename = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/ticker/{filename_prefix}_{keyword_slug}_{timestamp}.json"
        elif start_date and end_date:
            start_str = start_date.strftime("%Y%m%d")
            end_str = end_date.strftime("%Y%m%d")
            filename = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/ticker/{filename_prefix}_{start_str}_{end_str}_{timestamp}.json"
        else:
            filename = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/ticker/{filename_prefix}_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(articles, f, indent=2, ensure_ascii=False)
            
            print(f"\n✅ Berhasil menyimpan {len(articles)} artikel")
            print(f"📁 File: {filename}")
            
            # Tampilkan statistik
            self.print_statistics(articles, keyword)
            
            return filename
            
        except Exception as e:
            print(f"❌ Error menyimpan file: {e}")
            return None
    
    def print_statistics(self, articles, keyword=None):
        """Tampilkan statistik scraping"""
        print("\n📊 STATISTIK:")
        print(f"   Total artikel: {len(articles)}")
        if keyword:
            print(f"   Keyword: {keyword}")
        
        from collections import Counter
        date_counts = Counter([a.get('date', 'Unknown')[:10] for a in articles])
        
        print(f"\n   Distribusi per hari:")
        for date, count in sorted(date_counts.items()):
            if date != 'Unknown':
                try:
                    display_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
                except:
                    display_date = date
                print(f"     {display_date}: {count} artikel")
        
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

def main_mode_date_range():
    """Mode 1: Scraping berdasarkan rentang tanggal"""
    print("="*70)
    print("IDX CHANNEL - MODE RENTANG TANGGAL")
    print("="*70)
    
    # Input tanggal
    print("\n📅 MASUKKAN RENTANG TANGGAL")
    print("   Format: DD/MM/YYYY atau DD-MM-YYYY")
    print("   Contoh: 15/12/2025 atau 15-12-2025")
    
    while True:
        start_input = input("\nTanggal mulai: ").strip()
        start_date = validate_date_input(start_input)
        
        if start_date:
            print(f"   ✅ Tanggal mulai: {start_date.strftime('%d/%m/%Y')}")
            break
        else:
            print("   ❌ Format tanggal salah")
    
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
    
    days_count = (end_date - start_date).days + 1
    
    if days_count > 10:
        print(f"\n⚠️  PERINGATAN: Akan scrape {days_count} hari")
    
    delay_input = input(f"\nDelay antar hari (detik, default=2): ").strip()
    try:
        delay = float(delay_input) if delay_input else 2
    except:
        delay = 2
    
    # Konfirmasi
    print("\n" + "="*70)
    print("⚙️  KONFIGURASI SCRAPING")
    print("="*70)
    print(f"📅 Rentang: {start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')} ({days_count} hari)")
    print(f"⏰ Delay antar hari: {delay} detik")
    
    confirm = input("\nLanjutkan scraping? (y/n): ").lower().strip()
    if confirm != 'y':
        print("❌ Dibatalkan")
        return
    
    scraper = IDXChannelScraper()
    
    print("\n" + "="*70)
    print("🚀 MEMULAI SCRAPING...")
    print("="*70)
    
    start_time = time.time()
    
    try:
        articles = []
        current_date = start_date
        
        for day_num in range(days_count):
            print(f"\n📅 Hari {day_num + 1}/{days_count}: {current_date.strftime('%d/%m/%Y')}")
            day_articles = scraper.scrape_by_date_with_loadmore(current_date)
            articles.extend(day_articles)
            
            print(f"  📈 Progress: {len(articles)} artikel terkumpul")
            
            current_date += timedelta(days=1)
            
            if day_num < days_count - 1:
                print(f"  ⏳ Menunggu {delay} detik...")
                time.sleep(delay)
        
        elapsed_time = time.time() - start_time
        print(f"\n⏱️  Waktu eksekusi: {elapsed_time:.1f} detik")
        
        if articles:
            scraper.save_results(articles, "idxchannel_date", start_date, end_date)
        else:
            print("\n❌ Tidak ada artikel yang ditemukan")
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Scraping dihentikan oleh pengguna")
        if 'articles' in locals() and articles:
            timestamp = datetime.now().strftime("%H%M%S")
            temp_file = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/ticker/idxchannel_partial_{timestamp}.json"
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(articles, f, indent=2, ensure_ascii=False)
            print(f"💾 Data parsial disimpan: {temp_file}")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

def main_mode_keyword():
    """Mode 2: Scraping berdasarkan keyword/emiten"""
    print("="*70)
    print("IDX CHANNEL - MODE KEYWORD/EMITEN")
    print("="*70)
    
    keyword = input("\n🔍 Masukkan keyword/emiten (contoh: Bumi Resources Tbk, ANTM, BUMI): ").strip()
    if not keyword:
        print("❌ Keyword tidak boleh kosong")
        return
    
    print("\n📋 PILIH SUB-MODE:")
    print("1. Scraping semua artikel untuk keyword ini")
    print("2. Scraping dalam rentang tanggal tertentu")
    
    sub_choice = input("\nPilihan (1-2): ").strip()
    
    scraper = IDXChannelScraper()
    
    if sub_choice == '1':
        # Mode keyword saja
        max_batches_input = input("\nMaksimal batch (default=20): ").strip()
        max_batches = int(max_batches_input) if max_batches_input else 20
        
        delay_input = input("Delay antar batch (detik, default=1): ").strip()
        delay = float(delay_input) if delay_input else 1
        
        print("\n" + "="*70)
        print("⚙️  KONFIGURASI SCRAPING")
        print("="*70)
        print(f"🔍 Keyword: {keyword}")
        print(f"📄 Maksimal batch: {max_batches}")
        print(f"⏰ Delay antar batch: {delay} detik")
        
        confirm = input("\nLanjutkan scraping? (y/n): ").lower().strip()
        if confirm != 'y':
            print("❌ Dibatalkan")
            return
        
        print("\n" + "="*70)
        print("🚀 MEMULAI SCRAPING...")
        print("="*70)
        
        start_time = time.time()
        
        try:
            articles = scraper.scrape_by_keyword_with_loadmore(keyword, max_batches)
            
            elapsed_time = time.time() - start_time
            print(f"\n⏱️  Waktu eksekusi: {elapsed_time:.1f} detik")
            
            if articles:
                scraper.save_results(articles, "idxchannel_keyword", keyword=keyword)
            else:
                print("\n❌ Tidak ada artikel yang ditemukan")
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Scraping dihentikan oleh pengguna")
            if 'articles' in locals() and articles:
                timestamp = datetime.now().strftime("%H%M%S")
                temp_file = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/ticker/idxchannel_keyword_partial_{timestamp}.json"
                with open(temp_file, 'w', encoding='utf-8') as f:
                    json.dump(articles, f, indent=2, ensure_ascii=False)
                print(f"💾 Data parsial disimpan: {temp_file}")
                
    elif sub_choice == '2':
        # Mode keyword + tanggal
        print("\n📅 MASUKKAN RENTANG TANGGAL")
        print("   Format: DD/MM/YYYY atau DD-MM-YYYY")
        
        while True:
            start_input = input("\nTanggal mulai: ").strip()
            start_date = validate_date_input(start_input)
            
            if start_date:
                print(f"   ✅ Tanggal mulai: {start_date.strftime('%d/%m/%Y')}")
                break
            else:
                print("   ❌ Format tanggal salah")
        
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
        
        days_count = (end_date - start_date).days + 1
        
        delay_input = input(f"\nDelay antar hari (detik, default=2): ").strip()
        try:
            delay = float(delay_input) if delay_input else 2
        except:
            delay = 2
        
        max_batches_input = input("Maksimal batch per hari (default=10): ").strip()
        max_batches_per_day = int(max_batches_input) if max_batches_input else 10
        
        print("\n" + "="*70)
        print("⚙️  KONFIGURASI SCRAPING")
        print("="*70)
        print(f"🔍 Keyword: {keyword}")
        print(f"📅 Rentang: {start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')} ({days_count} hari)")
        print(f"📄 Maksimal batch/hari: {max_batches_per_day}")
        print(f"⏰ Delay antar hari: {delay} detik")
        
        confirm = input("\nLanjutkan scraping? (y/n): ").lower().strip()
        if confirm != 'y':
            print("❌ Dibatalkan")
            return
        
        print("\n" + "="*70)
        print("🚀 MEMULAI SCRAPING...")
        print("="*70)
        
        start_time = time.time()
        
        try:
            articles = scraper.scrape_keyword_date_range(keyword, start_date, end_date, delay, max_batches_per_day)
            
            elapsed_time = time.time() - start_time
            print(f"\n⏱️  Waktu eksekusi: {elapsed_time:.1f} detik")
            
            if articles:
                scraper.save_results(articles, "idxchannel_keyword_date", start_date, end_date, keyword)
            else:
                print("\n❌ Tidak ada artikel yang ditemukan")
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Scraping dihentikan oleh pengguna")
            if 'articles' in locals() and articles:
                timestamp = datetime.now().strftime("%H%M%S")
                temp_file = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/ticker/idxchannel_keyword_partial_{timestamp}.json"
                with open(temp_file, 'w', encoding='utf-8') as f:
                    json.dump(articles, f, indent=2, ensure_ascii=False)
                print(f"💾 Data parsial disimpan: {temp_file}")
                
    else:
        print("❌ Pilihan tidak valid")

def test_single_day():
    """Test scraping satu hari saja"""
    print("\n🔧 MODE TEST - Scrape 1 hari")
    
    test_date = datetime.now().date()
    print(f"📅 Tanggal test: {test_date.strftime('%d/%m/%Y')}")
    
    scraper = IDXChannelScraper()
    articles = scraper.scrape_by_date_with_loadmore(test_date)
    
    if articles:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/ticker/test_loadmore_{timestamp}.json"
        
        if not os.path.exists('data'):
            os.makedirs('data')
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Berhasil: {len(articles)} artikel")
        print(f"📁 Disimpan: {filename}")
        
        batches = set([a.get('batch', 0) for a in articles])
        print(f"🔁 Batch: {len(batches)} ({', '.join(map(str, sorted(batches)))})")
    else:
        print("\n❌ Tidak ada artikel")

def test_keyword():
    """Test scraping dengan keyword"""
    print("\n🔧 MODE TEST - Scrape dengan keyword")
    
    keyword = "Bumi Resources Tbk"
    print(f"🔍 Keyword test: {keyword}")
    
    scraper = IDXChannelScraper()
    articles = scraper.scrape_by_keyword_with_loadmore(keyword, max_batches=5)
    
    if articles:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/ticker/test_keyword_{timestamp}.json"
        
        if not os.path.exists('data'):
            os.makedirs('data')
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Berhasil: {len(articles)} artikel")
        print(f"📁 Disimpan: {filename}")
    else:
        print("\n❌ Tidak ada artikel")

if __name__ == "__main__":
    print("="*70)
    print("IDX CHANNEL SCRAPER - MULTI MODE")
    print("="*70)
    print("\n📋 PILIH MODE UTAMA:")
    print("1. Scraping berdasarkan rentang tanggal")
    print("2. Scraping berdasarkan keyword/emiten")
    print("3. Test scraping 1 hari (mode tanggal)")
    print("4. Test scraping dengan keyword")
    print("5. Keluar")
    
    choice = input("\nPilihan (1-5): ").strip()
    
    if choice == '1':
        main_mode_date_range()
    elif choice == '2':
        main_mode_keyword()
    elif choice == '3':
        test_single_day()
    elif choice == '4':
        test_keyword()
    else:
        print("👋 Keluar...")