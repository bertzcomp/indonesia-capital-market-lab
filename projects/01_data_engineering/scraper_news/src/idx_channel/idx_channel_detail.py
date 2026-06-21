import json
import requests
from bs4 import BeautifulSoup
import time
import os
from datetime import datetime
import re
import html
from urllib.parse import urljoin, urlparse

class IDXDetailScraper:
    def __init__(self):
        self.base_url = "https://www.idxchannel.com"
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://www.idxchannel.com/',
        }
        self.session.headers.update(self.headers)

    def get_soup(self, url):
        """Ambil BeautifulSoup dari URL"""
        try:
            r = self.session.get(url, timeout=15)
            if r.status_code == 200:
                return BeautifulSoup(r.text, 'html.parser')
            else:
                print(f"    ⚠️ Status {r.status_code} untuk {url}")
                return None
        except Exception as e:
            print(f"    ❌ Error request: {str(e)[:50]}")
            return None

    def extract_paragraphs(self, soup):
        """Ekstrak teks dari semua tag <p> di dalam container detail--article"""
        paragraphs = []
        # Cari container utama
        container = soup.find('div', class_='detail--article')
        if not container:
            # Fallback ke container lain
            container = soup.find('div', class_='detail-content--left')
        
        if container:
            # Ambil semua tag <p> di dalam container
            for p in container.find_all('p'):
                text = p.get_text(strip=True)
                # Filter teks yang terlalu pendek atau mengandung kata kunci iklan/navigasi
                if text and len(text) > 20:
                    # Abaikan paragraf yang mengandung "Baca Juga:" atau tautan serupa
                    lower_text = text.lower()
                    if 'baca juga:' in lower_text or 'simak:' in lower_text:
                        continue
                    paragraphs.append(text)
        return paragraphs

    def extract_pagination_links(self, soup, current_url):
        """Ekstrak semua link halaman dari div.paging (kecuali halaman saat ini)"""
        pagination = soup.find('div', class_='paging')
        if not pagination:
            return []
        
        links = []
        for a in pagination.find_all('a', href=True):
            href = a['href']
            # Hanya link yang berbeda dari current_url (hindari duplikat)
            full_url = urljoin(self.base_url, href)
            if full_url != current_url and full_url not in links:
                links.append(full_url)
        return links

    def extract_tags(self, soup):
        """Ekstrak tag dari div.article--tags"""
        tags = []
        tags_div = soup.find('div', class_='article--tags-link')
        if tags_div:
            # Cari semua link di dalam div tersebut
            for a in tags_div.find_all('a', href=True):
                tag_text = a.get_text(strip=True)
                if tag_text and tag_text not in tags:
                    tags.append(tag_text)
        return tags

    def extract_metadata(self, soup):
        """Ekstrak metadata: penulis, tanggal, gambar utama, dll."""
        # Penulis
        author = "Reporter IDX Channel"
        author_elem = soup.find('a', href=lambda x: x and '/author/' in x)
        if author_elem:
            author = author_elem.get_text(strip=True)
        else:
            # Coba dari div.article--creator
            creator_div = soup.find('div', class_='article--creator')
            if creator_div:
                author_link = creator_div.find('a', href=lambda x: x and '/author/' in x)
                if author_link:
                    author = author_link.get_text(strip=True)

        # Tanggal
        publish_time = ""
        time_elem = soup.find('div', class_='article--creator')
        if time_elem:
            # Cari div dengan teks tanggal (biasanya div tanpa link)
            for div in time_elem.find_all('div'):
                text = div.get_text(strip=True)
                if re.search(r'\d{2}/\d{2}/\d{4}', text):
                    publish_time = text
                    break

        # Gambar utama
        main_image = ""
        img_div = soup.find('div', class_='article--image')
        if img_div:
            img = img_div.find('img')
            if img:
                src = img.get('data-src') or img.get('src', '')
                if src:
                    if src.startswith('//'):
                        main_image = 'https:' + src
                    elif src.startswith('/'):
                        main_image = self.base_url + src
                    else:
                        main_image = src

        # Ringkasan/lead
        summary = ""
        excerpt_div = soup.find('div', class_='article--excerpt')
        if excerpt_div:
            summary = excerpt_div.get_text(strip=True)

        return {
            'author': author,
            'publish_time': publish_time,
            'main_image': main_image,
            'summary': summary
        }

    def scrape_article(self, url):
        """Scrape artikel dengan menangani multi halaman"""
        print(f"  Mengakses: {url[:80]}...")
        soup = self.get_soup(url)
        if not soup:
            return None

        # Ekstrak metadata dari halaman pertama
        metadata = self.extract_metadata(soup)

        # Ekstrak paragraf dari halaman pertama
        all_paragraphs = self.extract_paragraphs(soup)

        # Cari link ke halaman lain
        page_links = self.extract_pagination_links(soup, url)

        # Scrape setiap halaman tambahan
        for page_url in page_links:
            print(f"    ➡️  Halaman tambahan: {page_url}")
            page_soup = self.get_soup(page_url)
            if page_soup:
                paragraphs = self.extract_paragraphs(page_soup)
                all_paragraphs.extend(paragraphs)
                # Jeda antar halaman
                time.sleep(1)

        # Gabungkan semua paragraf menjadi satu teks
        full_content = "\n\n".join(all_paragraphs)

        # Ekstrak tags (bisa dari halaman mana saja, asumsikan sama)
        tags = self.extract_tags(soup)

        # Hitung jumlah kata
        word_count = len(full_content.split())
        read_time = max(1, word_count // 200)

        # Kembalikan data lengkap
        return {
            'full_content': full_content,
            'summary': metadata['summary'],
            'author': metadata['author'],
            'publish_time': metadata['publish_time'],
            'main_image': metadata['main_image'],
            'tags': tags,
            'word_count': word_count,
            'read_time_minutes': read_time
        }


def scrape_detail(url, title=""):
    """Wrapper function untuk kompatibilitas dengan kode lama"""
    scraper = IDXDetailScraper()
    return scraper.scrape_article(url)


def main():
    print("="*60)
    print("IDX CHANNEL DETAIL SCRAPER v3 (MULTI HALAMAN)")
    print("="*60)
    
    # Cari file JSON di folder data
    data_dir = "/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data"
    output_dir = "/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/detailed"
    
    if not os.path.exists(data_dir):
        print(f"❌ Folder '{data_dir}' tidak ditemukan")
        return
    
    files = [f for f in os.listdir(data_dir) if f.endswith('.json') and 'DETAILED' not in f]
    
    if not files:
        print("❌ Tidak ada file JSON di folder 'data/'")
        return
    
    # Tampilkan file
    print(f"\n📁 File di folder '{data_dir}/':")
    for i, f in enumerate(files, 1):
        file_path = os.path.join(data_dir, f)
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                article_count = len(data) if isinstance(data, list) else 1
                print(f"{i:2}. {f} ({article_count} artikel)")
        except:
            print(f"{i:2}. {f}")
    
    # Pilih file
    try:
        choice = int(input("\nPilih file (nomor): "))
        if 1 <= choice <= len(files):
            input_file = os.path.join(data_dir, files[choice-1])
        else:
            print("❌ Pilihan tidak valid")
            return
    except:
        print("❌ Input tidak valid")
        return
    
    print(f"\n📂 Membaca: {input_file}")
    
    # Load data
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ File tidak ditemukan: {input_file}")
        return
    except json.JSONDecodeError:
        print(f"❌ File JSON tidak valid: {input_file}")
        return
    
    print(f"📊 Ditemukan {len(data)} artikel")
    
    # Tampilkan preview
    print("\n📰 PREVIEW ARTIKEL:")
    valid_articles = []
    for i, article in enumerate(data[:5]):
        title = article.get('title', 'N/A')
        url = article.get('url', '')
        if title and title != 'N/A' and url and url != 'N/A':
            valid_articles.append(article)
            print(f"{i+1}. {title[:60]}...")
            print(f"   URL: {url[:70]}...")
        else:
            print(f"{i+1}. ⚠️ Artikel tidak valid (judul/URL kosong)")
    
    if not valid_articles:
        print("❌ Tidak ada artikel valid untuk di-scrape")
        return
    
    # Konfigurasi
    print("\n⚙️ KONFIGURASI:")
    
    try:
        n_input = input("Jumlah artikel (0 untuk semua): ").strip()
        if n_input == '0' or not n_input:
            n = len(data)
            print(f"   ✅ Akan scrape semua {n} artikel")
        else:
            n = int(n_input)
            if n <= 0 or n > len(data):
                n = len(data)
                print(f"   ⚠️ Input tidak valid, akan scrape semua {n} artikel")
            else:
                print(f"   ✅ Akan scrape {n} artikel pertama")
    except:
        n = len(data)
        print(f"   ⚠️ Input tidak valid, akan scrape semua {n} artikel")
    
    # Filter artikel yang valid
    valid_data = []
    for article in data[:n]:
        title = article.get('title', '')
        url = article.get('url', '')
        if title and title != 'N/A' and url and url != 'N/A':
            valid_data.append(article)
    
    print(f"   📋 {len(valid_data)} artikel memiliki judul dan URL yang valid")
    
    if not valid_data:
        print("❌ Tidak ada artikel valid untuk di-scrape")
        return
    
    delay = float(input("\nDelay antar request (detik, default=2): ") or "2")
    print(f"   ⏰ Delay: {delay} detik")
    
    estimated_time = len(valid_data) * delay * 1.5 / 60  # perkiraan dengan multi halaman
    print(f"   ⏱️ Perkiraan waktu: {estimated_time:.1f} menit")
    
    confirm = input("\nLanjutkan? (y/n): ").lower().strip()
    if confirm != 'y':
        print("❌ Dibatalkan")
        return
    
    # Proses scraping
    print("\n" + "="*60)
    print("🚀 MEMULAI SCRAPING DETAIL...")
    print("="*60)
    
    results = []
    success = 0
    failed = 0
    
    start_time = time.time()
    
    for i, article in enumerate(valid_data):
        url = article.get('url', '')
        title = article.get('title', f'Artikel {i+1}')
        
        print(f"\n[{i+1}/{len(valid_data)}] {title[:60]}...")
        
        detail_data = scrape_detail(url, title)
        
        if detail_data and detail_data.get('full_content'):
            # Gabungkan data asli dengan detail
            updated_article = {**article, **detail_data}
            updated_article['detail_scraped_at'] = datetime.now().isoformat()
            results.append(updated_article)
            success += 1
        else:
            # Simpan artikel asli saja
            article['detail_error'] = 'Gagal mengambil konten'
            results.append(article)
            failed += 1
        
        # Delay antar request
        if i < len(valid_data) - 1:
            time.sleep(delay)
    
    elapsed_time = time.time() - start_time
    
    # Simpan hasil
    print("\n" + "="*60)
    print("💾 MENYIMPAN HASIL...")
    
    # Buat folder output jika belum ada
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Buat nama file output
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/detailed/{base_name}_DETAILED_{timestamp}.json")
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ SELESAI!")
        print(f"📊 Statistik:")
        print(f"   • Total diproses: {len(valid_data)}")
        print(f"   • Berhasil: {success}")
        print(f"   • Gagal: {failed}")
        print(f"⏱️  Waktu eksekusi: {elapsed_time:.1f} detik")
        print(f"📁 Hasil disimpan di: {output_file}")
        
        # Tampilkan contoh hasil
        if success > 0:
            detailed_articles = [a for a in results if 'full_content' in a]
            if detailed_articles:
                print(f"\n📝 CONTOH HASIL ({len(detailed_articles)} artikel dengan konten):")
                for i, article in enumerate(detailed_articles[:2]):
                    content_preview = article['full_content'][:100].replace('\n', ' ') + "..."
                    print(f"\n   {i+1}. {article.get('title', 'N/A')[:50]}...")
                    print(f"      📝 {article.get('word_count', 0)} kata")
                    print(f"      👤 {article.get('author', 'Tidak diketahui')}")
                    if article.get('tags'):
                        print(f"      🏷️ Tags: {', '.join(article['tags'][:3])}")
                    print(f"      📄 {content_preview}")
        
    except Exception as e:
        print(f"❌ Error menyimpan file: {e}")
    
    print("\n" + "="*60)


def debug_single_article():
    """Debug satu artikel saja"""
    print("\n🔧 MODE DEBUG - Satu Artikel")
    
    url = input("Masukkan URL artikel: ").strip()
    if not url:
        print("❌ URL tidak boleh kosong")
        return
    
    detail_data = scrape_detail(url, "Debug Artikel")
    
    if detail_data:
        print(f"\n✅ BERHASIL!")
        print(f"Judul: {detail_data.get('title', 'N/A')}")
        print(f"Penulis: {detail_data.get('author', 'N/A')}")
        print(f"Jumlah kata: {detail_data.get('word_count', 0)}")
        print(f"Tags: {', '.join(detail_data.get('tags', []))}")
        print(f"Gambar utama: {detail_data.get('main_image', 'N/A')[:80]}...")
        
        print(f"\n📄 PREVIEW KONTEN (200 karakter pertama):")
        print("-" * 60)
        content = detail_data.get('full_content', '')
        print(content[:200] + "..." if len(content) > 200 else content)
        print("-" * 60)
        
        # Simpan ke file untuk inspeksi
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        debug_file = f"debug_article_{timestamp}.json"
        with open(debug_file, 'w', encoding='utf-8') as f:
            json.dump(detail_data, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Debug data disimpan: {debug_file}")
    else:
        print("\n❌ Gagal mengambil konten")


if __name__ == "__main__":
    print("="*60)
    print("PILIH MODE:")
    print("1. Scrape detail dari file JSON")
    print("2. Debug satu artikel")
    print("3. Keluar")
    
    try:
        choice = input("\nPilihan (1-3): ").strip()
        
        if choice == '1':
            main()
        elif choice == '2':
            debug_single_article()
        else:
            print("👋 Keluar...")
    except KeyboardInterrupt:
        print("\n\n⚠️  Program dihentikan")
    except Exception as e:
        print(f"\n❌ Error: {e}")