import json
import requests
from bs4 import BeautifulSoup
import time
import os
from datetime import datetime
import re
import html

def scrape_detail(url, title=""):
    """Scrape detail dari URL IDX Channel"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://www.idxchannel.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }
        
        print(f"  Mengakses: {url[:80]}...")
        r = requests.get(url, headers=headers, timeout=15)
        
        if r.status_code != 200:
            print(f"    ⚠️ Status: {r.status_code}")
            return "", "", [], "", ""
        
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # DEBUG: Simpan HTML untuk inspeksi
        # with open(f"debug_{title[:20]}.html", "w", encoding="utf-8") as f:
        #     f.write(r.text)
        
        # 1. Cari konten utama - selector khusus IDX Channel
        content_selectors = [
            'div.detail-content',  # Selector utama IDX Channel
            'div.article-detail',
            'div.story-detail',
            'div.post-content',
            'div.entry-content',
            'article .content',
            'div.content-detail',
            'div.article-body',
            'div.article-content',
            'article',
            'div.content'
        ]
        
        content = ""
        main_content_elem = None
        
        for selector in content_selectors:
            elem = soup.select_one(selector)
            if elem:
                main_content_elem = elem
                print(f"    ✅ Found with selector: {selector}")
                break
        
        if main_content_elem:
            # Hapus elemen yang tidak diinginkan
            for tag in main_content_elem(['script', 'style', 'iframe', 'ins', 'div.advertisement', 
                                         'div.ads', 'div.recommended-news', 'div.social-share',
                                         'div.related-news', 'div.comments-section', 'aside',
                                         'div.popular-news', 'div.tags-bottom']):
                tag.decompose()
            
            # Ambil semua paragraf dan heading
            paragraphs = main_content_elem.find_all(['p', 'h2', 'h3', 'h4', 'li', 'blockquote'])
            
            for p in paragraphs:
                text = p.get_text(strip=True)
                # Filter teks yang terlalu pendek atau tidak relevan
                if text and len(text) > 20 and not any(word in text.lower() for word in ['baca juga:', 'simak:', 'baca:', 'lihat:', 'follow', 'instagram', 'facebook', 'twitter']):
                    # Tambahkan heading dengan formatting khusus
                    if p.name in ['h2', 'h3', 'h4']:
                        content += f"\n\n{text}\n"
                    else:
                        content += f"{text}\n\n"
        
        # 2. Jika masih kosong, coba metode alternatif
        if not content or len(content.strip()) < 100:
            print(f"    ⚠️ Konten pendek, cari alternatif...")
            
            # Cari semua paragraf di dalam article atau main
            all_p = soup.find_all('p')
            long_paragraphs = []
            
            for p in all_p:
                text = p.get_text(strip=True)
                # Hanya ambil paragraf yang cukup panjang dan tidak navigasi/iklan
                if text and len(text) > 50:
                    # Filter iklan dan navigasi
                    if not any(word in text.lower() for word in ['iklan', 'advertisement', 'sponsor', 'banner', 
                                                                 'login', 'register', 'sign up', 'follow us',
                                                                 'share:', 'like:', 'comment:', '©', 'all rights']):
                        long_paragraphs.append(text)
            
            if long_paragraphs:
                content = "\n\n".join(long_paragraphs[:20])  # Ambil maksimal 20 paragraf
        
        content = content.strip()
        
        # 3. Cari penulis - selector khusus IDX Channel
        author_selectors = [
            'div.author-name',
            'span.author-name',
            'div.author span',
            'div.writer',
            'div.reporter',
            'div[class*="author"]',
            'meta[name="author"]',
            'div.post-author'
        ]
        
        author = "Reporter IDX Channel"
        for selector in author_selectors:
            elem = soup.select_one(selector)
            if elem:
                if selector == 'meta[name="author"]':
                    author = elem.get('content', 'Reporter IDX Channel')
                else:
                    author_text = elem.get_text(strip=True)
                    if author_text and author_text.lower() not in ['', 'admin', 'editor', 'redaksi', 'newsroom']:
                        author = author_text
                        break
        
        # 4. Cari waktu publish
        time_selectors = [
            'div.post-date',
            'span.post-date',
            'div.date',
            'time',
            'div.published-date',
            'meta[property="article:published_time"]',
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
        
        # 5. Cari gambar utama
        image_selectors = [
            'meta[property="og:image"]',
            'meta[name="twitter:image"]',
            'div.featured-image img',
            'figure img',
            'div.article-image img',
            'img.wp-post-image'
        ]
        
        main_image = ""
        for selector in image_selectors:
            elem = soup.select_one(selector)
            if elem:
                if selector.startswith('meta'):
                    main_image = elem.get('content', '')
                else:
                    main_image = elem.get('src') or elem.get('data-src') or elem.get('data-original', '')
                if main_image:
                    # Pastikan URL lengkap
                    if main_image.startswith('//'):
                        main_image = 'https:' + main_image
                    elif main_image.startswith('/'):
                        main_image = 'https://www.idxchannel.com' + main_image
                    break
        
        # 6. Cari tags/kategori
        tags = []
        tag_selectors = [
            'div.tags a',
            'a[rel="tag"]',
            'div.category a',
            'ul.tags li a'
        ]
        
        for selector in tag_selectors:
            elems = soup.select(selector)
            for elem in elems:
                tag_text = elem.get_text(strip=True)
                if tag_text and tag_text not in tags:
                    tags.append(tag_text)
        
        # 7. Cari ringkasan/lead
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
        
        if content:
            word_count = len(content.split())
            print(f"    ✅ {word_count} kata")
            
            # Kembalikan semua data
            return {
                'full_content': content,
                'summary': summary,
                'author': author,
                'publish_time': publish_time,
                'main_image': main_image,
                'tags': tags[:10],  # Maksimal 10 tag
                'word_count': word_count,
                'read_time_minutes': max(1, word_count // 200)
            }
        else:
            print(f"    ❌ Tidak ada konten yang ditemukan")
            return None
        
    except requests.RequestException as e:
        print(f"    ❌ Error request: {str(e)[:50]}")
        return None
    except Exception as e:
        print(f"    ❌ Error: {str(e)[:50]}")
        return None

def main():
    print("="*60)
    print("IDX CHANNEL DETAIL SCRAPER v2")
    print("="*60)
    
    # Cari file JSON di folder data
    data_dir = "/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data"
    output_dir = "/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/data/detailed"
    
    if not os.path.exists(data_dir):
        print(f"❌ Folder '{data_dir}' tidak ditemukan")
        print(f"   Buat folder '{data_dir}' terlebih dahulu")
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
    
    estimated_time = len(valid_data) * delay / 60
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
        
        if detail_data:
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
        debug_file = f"/Users/albert/Documents/Finances/data/raw/alternative_data/news/idx_channel/detailed/debug_article_{timestamp}.json"
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