import requests
from bs4 import BeautifulSoup
import json
import time
import os
import re
from datetime import datetime, timedelta
from urllib.parse import urljoin

class KabarBursaDateScraper:
    def __init__(self):
        self.base_url = "https://www.kabarbursa.com"
        self.market_url = f"{self.base_url}/market-hari-ini"
        self.session = requests.Session()
        
        # Headers sederhana
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        }
    
    def parse_date_string(self, date_str):
        """
        Parse tanggal dari string KabarBursa
        Format: "Terbit • 16 January 2026" -> "2026-01-16"
        """
        if not date_str or date_str == "N/A":
            return None
        
        try:
            # Ekstrak bagian tanggal menggunakan regex
            pattern = r'(\d{1,2})\s+([a-zA-Z]+)\s+(\d{4})'
            match = re.search(pattern, date_str)
            
            if match:
                day, month_name, year = match.groups()
                
                # Mapping bulan ke angka
                month_map = {
                    'january': 1, 'february': 2, 'march': 3,
                    'april': 4, 'may': 5, 'june': 6,
                    'july': 7, 'august': 8, 'september': 9,
                    'october': 10, 'november': 11, 'december': 12,
                    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
                    'may': 5, 'jun': 6, 'jul': 7, 'aug': 8,
                    'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
                }
                
                month_lower = month_name.lower()
                month_num = month_map.get(month_lower)
                
                if month_num:
                    return datetime(int(year), month_num, int(day)).date()
        
        except Exception as e:
            print(f"Warning: Gagal parse tanggal '{date_str}': {e}")
        
        return None
    
    def scrape_page(self, page_url, page_num):
        """Scrape satu halaman"""
        try:
            print(f"  📄 Halaman {page_num}")
            response = requests.get(page_url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                return [], False
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Cari semua artikel
            articles = []
            article_elements = soup.find_all('article')
            
            for element in article_elements:
                try:
                    # Judul
                    title_elem = element.find(['h2', 'h3'])
                    title = title_elem.get_text(strip=True) if title_elem else "N/A"
                    
                    # URL
                    link_elem = element.find('a', href=True)
                    if not link_elem:
                        continue
                    
                    url = urljoin(self.base_url, link_elem['href'])
                    
                    # Gambar
                    img_elem = element.find('img')
                    image_url = img_elem.get('src', '') if img_elem else ''
                    
                    # Tanggal
                    date_elem = element.find('span', class_='text-xs')
                    date_text = date_elem.get_text(strip=True) if date_elem else "N/A"
                    
                    # Parse tanggal
                    parsed_date = self.parse_date_string(date_text)
                    
                    articles.append({
                        'title': title,
                        'url': url,
                        'image_url': image_url,
                        'date_display': date_text,
                        'date': parsed_date.isoformat() if parsed_date else "N/A",
                        'page': page_num
                    })
                    
                except Exception as e:
                    continue
            
            # Cek apakah ada halaman berikutnya
            has_next_page = False
            pagination = soup.find('div', class_='mt-10')
            if pagination:
                # Cari link dengan angka halaman berikutnya
                for link in pagination.find_all('a', href=True):
                    link_text = link.get_text(strip=True)
                    if link_text.isdigit() and int(link_text) == page_num + 1:
                        has_next_page = True
                        break
            
            return articles, has_next_page
            
        except Exception as e:
            print(f"    ❌ Error: {e}")
            return [], False
    
    def scrape_by_date_range(self, start_date, end_date, max_pages=20):
        """
        Scrape KabarBursa dan filter berdasarkan rentang tanggal
        
        Args:
            start_date: datetime.date - Tanggal mulai
            end_date: datetime.date - Tanggal akhir
            max_pages: int - Maksimal halaman yang discrape
        """
        print(f"\n🔍 Scraping berita dari {start_date} sampai {end_date}")
        print(f"📄 Maksimal {max_pages} halaman")
        print("-" * 60)
        
        all_articles = []
        current_page = 1
        current_url = self.market_url
        
        while current_page <= max_pages:
            articles, has_next_page = self.scrape_page(current_url, current_page)
            
            if not articles:
                print(f"    ⏹️ Tidak ada artikel di halaman {current_page}")
                break
            
            # Filter berdasarkan tanggal
            filtered_articles = []
            for article in articles:
                article_date_str = article.get('date')
                
                if article_date_str and article_date_str != "N/A":
                    try:
                        article_date = datetime.strptime(article_date_str, "%Y-%m-%d").date()
                        
                        if start_date <= article_date <= end_date:
                            filtered_articles.append(article)
                            print(f"    ✅ {article_date}: {article['title'][:40]}...")
                        elif article_date < start_date:
                            # Jika artikel lebih tua dari start_date, kita catat tapi tidak masukkan
                            print(f"    ⏹️ {article_date}: Lewat (lebih tua dari rentang)")
                    except:
                        # Jika parsing gagal, abaikan artikel ini
                        pass
            
            all_articles.extend(filter_articles)
            
            print(f"    📊 Halaman {current_page}: {len(articles)} total, {len(filtered_articles)} cocok")
            
            # Cek kondisi berhenti
            if not has_next_page:
                print(f"    ⏹️ Tidak ada halaman berikutnya")
                break
            
            # Jika semua artikel di halaman ini lebih tua dari end_date, kita bisa berhenti
            # (karena biasanya artikel terurut dari yang terbaru)
            all_older = all(article.get('date', '') != "N/A" and 
                          datetime.strptime(article['date'], "%Y-%m-%d").date() < start_date 
                          for article in articles if article.get('date') != "N/A")
            
            if all_older and len(articles) > 0:
                print(f"    ⏹️ Semua artikel di halaman ini lebih tua dari rentang")
                break
            
            # Lanjut ke halaman berikutnya
            current_page += 1
            current_url = f"{self.market_url}?page={current_page}"
            
            # Delay untuk menghormati server
            time.sleep(1)
        
        return all_articles
    
    def scrape_all_and_filter(self, max_pages=10):
        """
        Scrape semua halaman lalu filter di memori
        Lebih akurat karena kita bisa melihat semua data
        """
        print(f"\n📊 Scraping semua {max_pages} halaman terlebih dahulu...")
        
        all_raw_articles = []
        
        for page_num in range(1, max_pages + 1):
            if page_num == 1:
                url = self.market_url
            else:
                url = f"{self.market_url}?page={page_num}"
            
            articles, has_next_page = self.scrape_page(url, page_num)
            
            if articles:
                all_raw_articles.extend(articles)
                print(f"  ✅ Halaman {page_num}: {len(articles)} artikel")
            else:
                print(f"  ⏹️ Halaman {page_num}: Tidak ada artikel")
                break
            
            if not has_next_page:
                print(f"  ⏹️ Tidak ada halaman berikutnya")
                break
            
            time.sleep(0.5)
        
        return all_raw_articles
    
    def filter_articles_by_date(self, articles, start_date, end_date):
        """Filter artikel berdasarkan rentang tanggal"""
        filtered = []
        
        for article in articles:
            article_date_str = article.get('date')
            
            if article_date_str and article_date_str != "N/A":
                try:
                    article_date = datetime.strptime(article_date_str, "%Y-%m-%d").date()
                    
                    if start_date <= article_date <= end_date:
                        filtered.append(article)
                except:
                    # Jika parsing gagal, skip
                    continue
        
        return filtered
    
    def save_results(self, articles, start_date, end_date):
        """Simpan hasil ke file JSON"""
        if not articles:
            print("❌ Tidak ada artikel untuk disimpan")
            return None
        
        # Buat folder berdasarkan tanggal
        date_dir = "/Users/albert/Documents/Finances/data/raw/alternative_data/news/kabar_bursa/data"
        
        # Generate nama file
        timestamp = datetime.now().strftime("%H%M%S")
        filename = f"{date_dir}/kabarbursa_{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(articles, f, indent=2, ensure_ascii=False)
            
            print(f"\n✅ Berhasil menyimpan {len(articles)} artikel")
            print(f"📁 File: {filename}")
            
            # Tampilkan statistik berdasarkan tanggal
            print(f"\n📅 Distribusi tanggal:")
            date_counts = {}
            for article in articles:
                date = article.get('date', 'N/A')
                date_counts[date] = date_counts.get(date, 0) + 1
            
            for date, count in sorted(date_counts.items()):
                print(f"  {date}: {count} artikel")
            
            return filename
            
        except Exception as e:
            print(f"❌ Error menyimpan file: {e}")
            return None

def main():
    """Program utama dengan filter tanggal"""
    print("="*70)
    print("KABARBURSA DATE-FILTER SCRAPER")
    print("="*70)
    
    scraper = KabarBursaDateScraper()
    
    # Input tanggal
    print("\n📅 MASUKKAN RENTANG TANGGAL")
    print("   Format: DD/MM/YYYY")
    print("   Contoh: 15/01/2026")
    
    # Tanggal mulai
    while True:
        start_input = input("\nTanggal mulai: ").strip()
        try:
            start_date = datetime.strptime(start_input, "%d/%m/%Y").date()
            print(f"   ✅ {start_date.strftime('%d/%m/%Y')}")
            break
        except ValueError:
            print("   ❌ Format salah. Gunakan DD/MM/YYYY")
    
    # Tanggal akhir
    while True:
        end_input = input("\nTanggal akhir (kosong untuk hari ini): ").strip()
        
        if not end_input:
            end_date = datetime.now().date()
            print(f"   ✅ {end_date.strftime('%d/%m/%Y')} (hari ini)")
            break
        
        try:
            end_date = datetime.strptime(end_input, "%d/%m/%Y").date()
            
            if end_date < start_date:
                print("   ❌ Tanggal akhir tidak boleh sebelum tanggal mulai")
            else:
                print(f"   ✅ {end_date.strftime('%d/%m/%Y')}")
                break
        except ValueError:
            print("   ❌ Format salah. Gunakan DD/MM/YYYY")
    
    # Pilih metode scraping
    print("\n⚡ PILIH METODE:")
    print("1. Scrape dengan filter real-time (lebih cepat)")
    print("2. Scrape semua lalu filter (lebih akurat)")
    
    try:
        method = int(input("\nPilihan (1-2): "))
    except:
        method = 1
    
    # Jumlah halaman maksimal
    try:
        max_pages = int(input("\nMaksimal halaman (default=10): ") or "10")
    except:
        max_pages = 10
    
    # Konfirmasi
    print("\n" + "="*70)
    print("⚙️  KONFIGURASI")
    print("="*70)
    print(f"📅 Rentang: {start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')}")
    print(f"📄 Maksimal halaman: {max_pages}")
    print(f"⚡ Metode: {'Real-time filter' if method == 1 else 'Scrape semua lalu filter'}")
    
    confirm = input("\nLanjutkan? (y/n): ").lower().strip()
    if confirm != 'y':
        print("❌ Dibatalkan")
        return
    
    # Mulai scraping
    print("\n" + "="*70)
    print("🚀 MEMULAI SCRAPING...")
    print("="*70)
    
    start_time = time.time()
    
    if method == 1:
        # Metode 1: Filter real-time
        articles = scraper.scrape_by_date_range(start_date, end_date, max_pages)
    else:
        # Metode 2: Scrape semua lalu filter
        all_articles = scraper.scrape_all_and_filter(max_pages)
        articles = scraper.filter_articles_by_date(all_articles, start_date, end_date)
    
    elapsed_time = time.time() - start_time
    
    # Simpan hasil
    if articles:
        scraper.save_results(articles, start_date, end_date)
        
        print(f"\n⏱️  Waktu eksekusi: {elapsed_time:.1f} detik")
        print(f"📊 Total artikel yang sesuai: {len(articles)}")
        
        # Tampilkan contoh
        if articles:
            print("\n📰 CONTOH ARTIKEL:")
            for i, article in enumerate(articles[:3]):
                print(f"\n{i+1}. {article['title'][:60]}...")
                print(f"   Tanggal: {article['date_display']}")
                print(f"   URL: {article['url'][:70]}...")
                print(f"   Halaman: {article.get('page', 'N/A')}")
    else:
        print("\n❌ Tidak ada artikel dalam rentang tanggal tersebut")
        print("\n💡 Saran:")
        print("1. Coba rentang tanggal yang berbeda")
        print("2. Tingkatkan jumlah halaman maksimal")
        print("3. Website mungkin hanya memiliki artikel dengan tanggal tertentu")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Scraping dihentikan oleh pengguna")
    except Exception as e:
        print(f"\n❌ Error: {e}")
