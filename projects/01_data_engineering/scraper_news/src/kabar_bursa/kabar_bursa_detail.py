import json
import requests
from bs4 import BeautifulSoup
import time
import os
from datetime import datetime
import re
from urllib.parse import urljoin

class KabarBursaDetailScraper:
    def __init__(self):
        self.base_url = "https://www.kabarbursa.com"
        self.session = requests.Session()
        
        # Headers untuk menyerupai browser
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://www.kabarbursa.com/',
            'Upgrade-Insecure-Requests': '1',
        }
        self.session.headers.update(self.headers)
    
    def load_json_file(self, file_path):
        """Load data dari file JSON"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ File tidak ditemukan: {file_path}")
            return None
        except json.JSONDecodeError:
            print(f"❌ File JSON tidak valid: {file_path}")
            return None
    
    def scrape_article_detail(self, url):
        """Scrape detail lengkap dari sebuah artikel KabarBursa"""
        try:
            if not url or url == 'N/A':
                return None
            
            print(f"  📄 Mengakses: {url[:80]}...")
            response = self.session.get(url, timeout=30)
            
            if response.status_code != 200:
                print(f"    ⚠️ Status: {response.status_code}")
                return None
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # DEBUG: Simpan HTML untuk inspeksi jika perlu
            # with open(f"debug_article.html", "w", encoding="utf-8") as f:
            #     f.write(response.text)
            
            # 1. Cari konten utama artikel
            # KabarBursa biasanya menggunakan struktur berikut:
            content_selectors = [
                'div.prose',  # Tailwind prose class untuk konten artikel
                'article',  # Tag article
                'div.article-content',
                'div.post-content',
                'div.entry-content',
                'div.content',
                'div.article-body',
                'div[class*="content"]',
                'div[class*="article"]'
            ]
            
            content_text = ""
            main_content_elem = None
            
            for selector in content_selectors:
                elem = soup.select_one(selector)
                if elem:
                    main_content_elem = elem
                    print(f"    ✅ Konten ditemukan dengan selector: {selector}")
                    break
            
            if main_content_elem:
                # Hapus elemen yang tidak diinginkan
                for tag in main_content_elem(['script', 'style', 'iframe', 'ins', 'div.ad', 'div.ads', 
                                             'div.recommended-news', 'div.social-share', 'aside',
                                             'div.related-news', 'div.comments-section', 'div.popular-news']):
                    tag.decompose()
                
                # Ekstrak teks dari elemen konten
                # Prioritaskan paragraf dan heading
                paragraphs = main_content_elem.find_all(['p', 'h2', 'h3', 'h4', 'li', 'blockquote'])
                
                for p in paragraphs:
                    text = p.get_text(strip=True)
                    # Filter teks yang terlalu pendek atau tidak relevan
                    if text and len(text) > 20:
                        # Tambah formatting untuk heading
                        if p.name in ['h2', 'h3', 'h4']:
                            content_text += f"\n\n{text}\n"
                        elif p.name == 'li':
                            content_text += f"• {text}\n"
                        else:
                            content_text += f"{text}\n\n"
            
            # 2. Jika konten masih kosong, coba alternatif
            if not content_text or len(content_text.strip()) < 100:
                print(f"    ⚠️ Konten pendek, cari alternatif...")
                
                # Cari semua paragraf di dalam artikel
                all_p = soup.find_all('p')
                long_paragraphs = []
                
                for p in all_p:
                    text = p.get_text(strip=True)
                    # Ambil paragraf yang cukup panjang dan bukan navigasi/iklan
                    if text and len(text) > 50:
                        if not any(word in text.lower() for word in ['iklan', 'advertisement', 'sponsor', 
                                                                     'login', 'register', 'sign up', 'follow us',
                                                                     'share:', 'like:', 'comment:', '©', 'all rights']):
                            long_paragraphs.append(text)
                
                if long_paragraphs:
                    content_text = "\n\n".join(long_paragraphs[:20])  # Maksimal 20 paragraf
            
            content_text = content_text.strip()
            
            if not content_text:
                print(f"    ❌ Tidak ada konten yang ditemukan")
                return None
            
            # 3. Cari penulis
            author_selectors = [
                'div.author',
                'span.author',
                'div[class*="author"]',
                'a[href*="/author/"]',
                'div.writer',
                'div.reporter',
                'div.post-author',
                'div.byline'
            ]
            
            author = "Tidak diketahui"
            for selector in author_selectors:
                elem = soup.select_one(selector)
                if elem:
                    author_text = elem.get_text(strip=True)
                    # Filter teks yang tidak relevan
                    if author_text and author_text.lower() not in ['', 'admin', 'editor', 'redaksi', 'newsroom']:
                        author = author_text
                        break
            
            # 4. Cari waktu publish yang lebih detail
            time_selectors = [
                'time[datetime]',
                'meta[property="article:published_time"]',
                'div.post-date',
                'span.post-date',
                'div.date',
                'div.published-date',
                'div.time'
            ]
            
            publish_time = ""
            for selector in time_selectors:
                elem = soup.select_one(selector)
                if elem:
                    if selector == 'meta[property="article:published_time"]':
                        publish_time = elem.get('content', '')
                    elif elem.get('datetime'):
                        publish_time = elem.get('datetime', '')
                    else:
                        publish_time = elem.get_text(strip=True)
                    if publish_time:
                        break
            
            # 5. Cari kategori/tags
            tags = []
            tag_selectors = [
                'div.tags a',
                'a[rel="tag"]',
                'div.category a',
                'ul.tags li a',
                'div[class*="tag"] a'
            ]
            
            for selector in tag_selectors:
                elems = soup.select(selector)
                for elem in elems:
                    tag_text = elem.get_text(strip=True)
                    if tag_text and tag_text not in tags:
                        tags.append(tag_text)
            
            # 6. Cari ringkasan/lead
            summary_selectors = [
                'div.excerpt',
                'div.lead',
                'p.lead',
                'div.article-excerpt',
                'meta[property="og:description"]'
            ]
            
            summary = ""
            for selector in summary_selectors:
                elem = soup.select_one(selector)
                if elem:
                    if selector == 'meta[property="og:description"]':
                        summary = elem.get('content', '')
                    else:
                        summary = elem.get_text(strip=True)
                    if summary:
                        break
            
            # 7. Hitung statistik
            word_count = len(content_text.split())
            read_time_minutes = max(1, word_count // 200)  # Asumsi 200 kata per menit
            
            print(f"    ✅ {word_count} kata ({read_time_minutes} menit baca)")
            
            return {
                'full_content': content_text,
                'summary': summary,
                'author': author,
                'publish_time': publish_time,
                'tags': tags[:10],  # Maksimal 10 tags
                'word_count': word_count,
                'read_time_minutes': read_time_minutes,
                'detail_scraped_at': datetime.now().isoformat()
            }
            
        except requests.RequestException as e:
            print(f"    ❌ Error request: {str(e)[:50]}")
            return None
        except Exception as e:
            print(f"    ❌ Error: {str(e)[:50]}")
            return None
    
    def scrape_all_details(self, articles, start_index=0, max_articles=None, delay=1.0, save_interval=5):
        """
        Scrape detail untuk semua artikel
        
        Args:
            articles: List artikel
            start_index: Indeks mulai
            max_articles: Jumlah maksimal artikel
            delay: Delay antar request (detik)
            save_interval: Interval auto-save
        """
        total_articles = len(articles)
        
        if max_articles:
            end_index = min(start_index + max_articles, total_articles)
        else:
            end_index = total_articles
        
        print(f"📊 Memulai scraping detail untuk {end_index - start_index} artikel")
        print(f"⏰ Delay: {delay} detik | Auto-save setiap {save_interval} artikel")
        print("-" * 60)
        
        results = []
        scraped_count = 0
        failed_count = 0
        
        for i in range(start_index, end_index):
            article = articles[i]
            url = article.get('url', '')
            title = article.get('title', f'Artikel {i+1}')
            
            print(f"\n[{i+1}/{total_articles}] {title[:60]}...")
            
            # Scrape detail
            detail = self.scrape_article_detail(url)
            
            if detail:
                # Gabungkan data asli dengan detail
                combined = {**article, **detail}
                results.append(combined)
                scraped_count += 1
                
                if detail.get('author') != "Tidak diketahui":
                    print(f"  👤 {detail['author']}")
                
                if detail.get('tags'):
                    print(f"  🏷️ {', '.join(detail['tags'][:3])}")
            else:
                # Simpan artikel asli saja
                article['detail_error'] = 'Gagal mengambil konten'
                results.append(article)
                failed_count += 1
            
            # Delay antar request
            if i < end_index - 1:
                time.sleep(delay)
            
            # Auto-save setiap interval
            if (i + 1) % save_interval == 0:
                print(f"  💾 Auto-save progress...")
        
        print(f"\n✅ SELESAI! Berhasil: {scraped_count} | Gagal: {failed_count}")
        return results
    
    def save_results(self, results, output_filename):
        """Simpan hasil ke file JSON"""
        try:
            # Buat folder jika belum ada
            os.makedirs(os.path.dirname(output_filename), exist_ok=True)
            
            with open(output_filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            
            print(f"\n💾 Data disimpan ke: {output_filename}")
            return True
            
        except Exception as e:
            print(f"❌ Error menyimpan file: {e}")
            return False
    
    def print_summary(self, results):
        """Tampilkan ringkasan hasil"""
        if not results:
            print("❌ Tidak ada hasil untuk ditampilkan")
            return
        
        total_articles = len(results)
        articles_with_detail = sum(1 for a in results if 'full_content' in a)
        
        print("\n" + "="*60)
        print("📋 RINGKASAN HASIL SCRAPING DETAIL")
        print("="*60)
        print(f"Total artikel: {total_articles}")
        print(f"Artikel dengan konten lengkap: {articles_with_detail}")
        
        if articles_with_detail > 0:
            # Hitung statistik
            total_words = sum(a.get('word_count', 0) for a in results if 'word_count' in a)
            avg_words = total_words // articles_with_detail if articles_with_detail > 0 else 0
            
            print(f"\n📊 Statistik konten:")
            print(f"  • Total kata: {total_words:,}")
            print(f"  • Rata-rata kata per artikel: {avg_words}")
            print(f"  • Rata-rata waktu baca: {max(1, avg_words // 200)} menit")
            
            # Tampilkan contoh
            detailed_articles = [a for a in results if 'full_content' in a]
            if detailed_articles:
                print(f"\n📰 Contoh artikel ({min(3, len(detailed_articles))} contoh):")
                for i, article in enumerate(detailed_articles[:3]):
                    content_preview = article['full_content'][:100].replace('\n', ' ') + "..."
                    print(f"\n  {i+1}. {article.get('title', 'N/A')[:50]}...")
                    print(f"     📝 {article.get('word_count', 0)} kata")
                    print(f"     👤 {article.get('author', 'Tidak diketahui')}")
                    if article.get('tags'):
                        print(f"     🏷️ {', '.join(article['tags'][:3])}")
                    print(f"     📄 {content_preview}")

def select_json_file():
    """Pilih file JSON dari folder"""
    # Cari file di berbagai folder yang mungkin
    possible_folders = ['/Users/albert/Documents/Finances/data/raw/alternative_data/news/kabar_bursa/data', 'kabarbursa_data', '.']
    
    for folder in possible_folders:
        if os.path.exists(folder):
            files = [f for f in os.listdir(folder) if f.endswith('.json') and 'DETAILED' not in f]
            if files:
                print(f"\n📁 File di folder '{folder}/':")
                for i, f in enumerate(files, 1):
                    file_path = os.path.join(folder, f)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as json_file:
                            data = json.load(json_file)
                            article_count = len(data) if isinstance(data, list) else 1
                            print(f"{i:2}. {f} ({article_count} artikel)")
                    except:
                        print(f"{i:2}. {f}")
                
                return folder, files
    
    print("❌ Tidak ditemukan file JSON di folder manapun")
    return None, None

def main():
    """Program utama"""
    print("="*70)
    print("KABARBURSA DETAIL ARTICLE SCRAPER")
    print("="*70)
    
    # Cari file JSON
    folder, files = select_json_file()
    if not files:
        print("❌ Tidak ada file JSON yang ditemukan")
        return
    
    # Pilih file
    try:
        choice = int(input("\nPilih file (nomor): "))
        if 1 <= choice <= len(files):
            input_file = os.path.join(folder, files[choice-1])
        else:
            print("❌ Pilihan tidak valid")
            return
    except:
        print("❌ Input tidak valid")
        return
    
    print(f"\n📂 File dipilih: {input_file}")
    
    # Load data
    scraper = KabarBursaDetailScraper()
    articles = scraper.load_json_file(input_file)
    
    if not articles:
        return
    
    print(f"📊 {len(articles)} artikel ditemukan")
    
    # Tampilkan contoh artikel pertama
    if articles and len(articles) > 0:
        print("\n📰 Contoh artikel pertama:")
        first_article = articles[0]
        print(f"Judul: {first_article.get('title', 'N/A')[:60]}...")
        print(f"Tanggal: {first_article.get('date_display', 'N/A')}")
        print(f"URL: {first_article.get('url', 'N/A')[:70]}...")
    
    # Konfigurasi scraping
    print("\n⚙️ KONFIGURASI SCRAPING DETAIL")
    print("-" * 50)
    
    # Pilih jumlah artikel
    try:
        n_input = input("Jumlah artikel (0 untuk semua): ").strip()
        if n_input == '0' or not n_input:
            n = len(articles)
            print(f"  ✅ Akan scrape semua {n} artikel")
        else:
            n = int(n_input)
            if n <= 0 or n > len(articles):
                n = len(articles)
                print(f"  ⚠️ Input tidak valid, akan scrape semua {n} artikel")
            else:
                print(f"  ✅ Akan scrape {n} artikel pertama")
    except:
        n = len(articles)
        print(f"  ⚠️ Input tidak valid, akan scrape semua {n} artikel")
    
    # Pilih indeks mulai (untuk resume)
    try:
        start_idx = int(input("Indeks mulai (0 untuk pertama): ") or "0")
        if start_idx < 0 or start_idx >= n:
            start_idx = 0
            print(f"  ⚠️ Indeks tidak valid, mulai dari 0")
    except:
        start_idx = 0
        print(f"  ⚠️ Input tidak valid, mulai dari 0")
    
    # Delay
    delay_input = input("Delay antar request (detik, default=2): ").strip()
    try:
        delay = float(delay_input) if delay_input else 2.0
    except:
        delay = 2.0
    
    print(f"  ⏰ Delay: {delay} detik")
    
    # Estimasi waktu
    articles_to_scrape = min(n - start_idx, len(articles) - start_idx)
    estimated_time = articles_to_scrape * delay / 60
    print(f"  ⏱️ Perkiraan waktu: {estimated_time:.1f} menit")
    
    # Konfirmasi
    confirm = input("\nLanjutkan scraping detail? (y/n): ").lower().strip()
    if confirm != 'y':
        print("❌ Dibatalkan")
        return
    
    # Mulai scraping
    print("\n" + "="*70)
    print("🚀 MEMULAI SCRAPING DETAIL...")
    print("="*70)
    
    start_time = time.time()
    
    results = scraper.scrape_all_details(
        articles=articles,
        start_index=start_idx,
        max_articles=n,
        delay=delay,
        save_interval=5
    )
    
    elapsed_time = time.time() - start_time
    
    # Buat nama file output
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = "/Users/albert/Documents/Finances/data/raw/alternative_data/news/kabar_bursa/kabarbursa_detailed"
    output_file = os.path.join(output_dir, f"{base_name}_DETAILED_{timestamp}.json")
    
    # Simpan hasil
    if scraper.save_results(results, output_file):
        print(f"\n⏱️  Waktu eksekusi: {elapsed_time:.1f} detik")
        
        # Tampilkan ringkasan
        scraper.print_summary(results)
        
        print(f"\n✅ SELESAI! File tersimpan di: {output_file}")
    else:
        print("\n❌ Gagal menyimpan hasil")

def test_single_article():
    """Test scraping satu artikel saja"""
    print("\n🔧 MODE TEST - Scrape Satu Artikel")
    
    url = input("Masukkan URL artikel KabarBursa: ").strip()
    if not url:
        print("❌ URL tidak boleh kosong")
        return
    
    scraper = KabarBursaDetailScraper()
    detail = scraper.scrape_article_detail(url)
    
    if detail:
        print(f"\n✅ BERHASIL!")
        print(f"Jumlah kata: {detail['word_count']}")
        print(f"Penulis: {detail['author']}")
        print(f"Tags: {', '.join(detail['tags'][:5])}" if detail['tags'] else "Tags: Tidak ada")
        print(f"Waktu publish: {detail['publish_time']}")
        
        print(f"\n📄 PREVIEW KONTEN (200 karakter pertama):")
        print("-" * 60)
        content = detail.get('full_content', '')
        print(content[:200] + "..." if len(content) > 200 else content)
        print("-" * 60)
        
        # Simpan ke file untuk inspeksi
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_file = f"kabarbursa_test_{timestamp}.json"
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump(detail, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Test data disimpan: {test_file}")
    else:
        print("\n❌ Gagal mengambil konten")

if __name__ == "__main__":
    print("="*70)
    print("PILIH MODE:")
    print("1. Scrape detail dari file JSON (utama)")
    print("2. Test satu artikel")
    print("3. Keluar")
    
    try:
        choice = input("\nPilihan (1-3): ").strip()
        
        if choice == '1':
            main()
        elif choice == '2':
            test_single_article()
        else:
            print("👋 Keluar...")
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Program dihentikan oleh pengguna")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()