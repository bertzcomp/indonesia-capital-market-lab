import requests
from bs4 import BeautifulSoup
import json
import time
import os
import re
from datetime import datetime, timedelta
from urllib.parse import urljoin


OUTPUT_DIR = ["../data/news/macro_news/kb", "/Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/news/macro_news/kb"]


def get_output_dirs():
    """Return output directories as a normalized list."""
    if isinstance(OUTPUT_DIR, (list, tuple)):
        return list(OUTPUT_DIR)
    return [OUTPUT_DIR]


def save_json_to_output_dirs(payload, filename):
    """Save the same JSON payload to all configured output directories."""
    saved_files = []
    for output_dir in get_output_dirs():
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, filename)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=2, ensure_ascii=False)
            saved_files.append(path)
        except Exception as e:
            print(f"❌ Gagal menyimpan file ke {output_dir}: {e}")
    return saved_files


def validate_date_input(date_str):
    """Validasi input tanggal dengan beberapa format umum."""
    for fmt in ["%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d", "%d %b %Y", "%d %B %Y"]:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None


def prompt_date(label, allow_today=False):
    """Prompt tanggal sampai valid."""
    while True:
        value = input(f"{label}: ").strip()
        if allow_today and not value:
            target = datetime.now().date()
            print(f"   ✅ {target.strftime('%d/%m/%Y')} (hari ini)")
            return target

        parsed = validate_date_input(value)
        if parsed:
            print(f"   ✅ {parsed.strftime('%d/%m/%Y')}")
            return parsed

        print("   ❌ Format tanggal tidak dikenali. Gunakan DD/MM/YYYY, DD-MM-YYYY, atau YYYY-MM-DD.")


def iter_dates(start_date, end_date):
    """Yield tanggal dari start_date sampai end_date secara inklusif."""
    current = start_date
    while current <= end_date:
        yield current
        current += timedelta(days=1)


def select_scrape_mode():
    """Menu mode scraping interaktif."""
    while True:
        print("\nPILIH MODE:")
        print("1. Scraping rentang tanggal (utama)")
        print("   e.g input: 14/04/2026 hingga 14/05/2026")
        print("2. Test scraping 1 hari")
        print("   e.g input: 14/04/2026")
        print("3. Keluar")

        choice = input("\nPilih mode [1/2/3]: ").strip()

        if choice == "1":
            print("\n📅 Masukkan rentang tanggal")
            start_date = prompt_date("Tanggal awal  (DD/MM/YYYY)")
            end_date = prompt_date("Tanggal akhir (DD/MM/YYYY)")
            if end_date < start_date:
                print("   ❌ Tanggal akhir tidak boleh lebih kecil dari tanggal awal.")
                continue
            return "range", list(iter_dates(start_date, end_date))

        if choice == "2":
            print("\n📅 Masukkan tanggal target")
            target_date = prompt_date("Tanggal (DD/MM/YYYY)", allow_today=True)
            return "single", [target_date]

        if choice == "3":
            return "exit", []

        print("   ❌ Pilihan tidak valid. Pilih 1, 2, atau 3.")


class KabarBursaScraper:
    def __init__(self):
        self.base_url = "https://www.kabarbursa.com"
        self.market_url = f"{self.base_url}/makro"
        self.session = requests.Session()

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

    #  BAGIAN 1: SCRAPING SUMMARY (LIST ARTIKEL)
    def parse_date_string(self, date_str):
        """Parse tanggal dari format 'Terbit • 16 January 2026' -> date object"""
        if not date_str or date_str == "N/A":
            return None

        try:
            pattern = r'(\d{1,2})\s+([a-zA-Z]+)\s+(\d{4})'
            match = re.search(pattern, date_str)

            if match:
                day, month_name, year = match.groups()
                month_map = {
                    'january': 1, 'february': 2, 'march': 3,
                    'april': 4, 'may': 5, 'june': 6,
                    'july': 7, 'august': 8, 'september': 9,
                    'october': 10, 'november': 11, 'december': 12,
                }
                month_num = month_map.get(month_name.lower())
                if month_num:
                    return datetime(int(year), month_num, int(day)).date()
        except Exception as e:
            print(f"  ⚠️ Gagal parse tanggal '{date_str}': {e}")

        return None

    def scrape_listing_page(self, page_url, page_num):
        """Scrape satu halaman listing artikel, return (articles, has_next_page)"""
        try:
            print(f"  📄 Halaman {page_num}")
            response = self.session.get(page_url, timeout=10)

            if response.status_code != 200:
                return [], False

            soup = BeautifulSoup(response.text, 'html.parser')
            articles = []

            for element in soup.find_all('article'):
                try:
                    title_elem = element.find(['h2', 'h3'])
                    title = title_elem.get_text(strip=True) if title_elem else "N/A"

                    link_elem = element.find('a', href=True)
                    if not link_elem:
                        continue
                    url = urljoin(self.base_url, link_elem['href'])

                    img_elem = element.find('img')
                    image_url = img_elem.get('src', '') if img_elem else ''

                    date_elem = element.find('span', class_='text-xs')
                    date_text = date_elem.get_text(strip=True) if date_elem else "N/A"
                    parsed_date = self.parse_date_string(date_text)

                    articles.append({
                        'title': title,
                        'url': url,
                        'image_url': image_url,
                        'date_display': date_text,
                        'date': parsed_date.isoformat() if parsed_date else "N/A",
                        'page': page_num,
                    })
                except Exception:
                    continue

            # Cek halaman berikutnya
            has_next_page = False
            pagination = soup.find('div', class_='mt-10')
            if pagination:
                for link in pagination.find_all('a', href=True):
                    if link.get_text(strip=True).isdigit() and int(link.get_text(strip=True)) == page_num + 1:
                        has_next_page = True
                        break

            return articles, has_next_page

        except Exception as e:
            print(f"    ❌ Error scrape halaman: {e}")
            return [], False

    def collect_articles_for_date(self, target_date, max_pages=10):
        """
        Scrape listing pages dan return artikel yang cocok dengan target_date.
        Berhenti lebih awal jika semua artikel di halaman sudah lebih tua dari target_date.
        """
        print(f"\n🔍 Mengumpulkan artikel untuk tanggal: {target_date}")
        print("-" * 60)

        matched = []
        current_page = 1

        while current_page <= max_pages:
            url = self.market_url if current_page == 1 else f"{self.market_url}?page={current_page}"
            articles, has_next_page = self.scrape_listing_page(url, current_page)

            if not articles:
                print(f"    ⏹️ Tidak ada artikel di halaman {current_page}")
                break

            page_matched = []
            all_older = True

            for article in articles:
                date_str = article.get('date')
                if date_str and date_str != "N/A":
                    try:
                        article_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                        if article_date == target_date:
                            page_matched.append(article)
                            all_older = False
                        elif article_date > target_date:
                            all_older = False  # Artikel lebih baru, belum sampai target
                    except Exception:
                        all_older = False

            matched.extend(page_matched)
            print(f"    📊 Halaman {current_page}: {len(articles)} total, {len(page_matched)} cocok")

            if all_older:
                print(f"    ⏹️ Semua artikel lebih tua dari target tanggal")
                break

            if not has_next_page:
                print(f"    ⏹️ Tidak ada halaman berikutnya")
                break

            current_page += 1
            time.sleep(0.5)

        return matched

    #  BAGIAN 2: SCRAPING DETAIL ARTIKEL
    def scrape_article_detail(self, url):
        """Scrape konten lengkap dari URL artikel, return dict detail atau None"""
        try:
            if not url or url == 'N/A':
                return None

            print(f"  📄 Mengakses: {url[:80]}...")
            response = self.session.get(url, timeout=30)

            if response.status_code != 200:
                print(f"    ⚠️ Status: {response.status_code}")
                return None

            soup = BeautifulSoup(response.text, 'html.parser')

            # --- Konten utama ---
            content_selectors = [
                'div.prose',
                'article',
                'div.article-content',
                'div.post-content',
                'div.entry-content',
                'div.content',
                'div.article-body',
                'div[class*="content"]',
                'div[class*="article"]',
            ]

            content_text = ""
            main_content_elem = None

            for selector in content_selectors:
                elem = soup.select_one(selector)
                if elem:
                    main_content_elem = elem
                    break

            if main_content_elem:
                for tag in main_content_elem(['script', 'style', 'iframe', 'ins',
                                              'div.ad', 'div.ads', 'div.recommended-news',
                                              'div.social-share', 'aside', 'div.related-news',
                                              'div.comments-section', 'div.popular-news']):
                    tag.decompose()

                for p in main_content_elem.find_all(['p', 'h2', 'h3', 'h4', 'li', 'blockquote']):
                    text = p.get_text(strip=True)
                    if text and len(text) > 20:
                        if p.name in ['h2', 'h3', 'h4']:
                            content_text += f"\n\n{text}\n"
                        elif p.name == 'li':
                            content_text += f"• {text}\n"
                        else:
                            content_text += f"{text}\n\n"

            # Fallback jika konten terlalu pendek
            if not content_text or len(content_text.strip()) < 100:
                skip_words = ['iklan', 'advertisement', 'sponsor', 'login', 'register',
                              'sign up', 'follow us', 'share:', 'like:', 'comment:',
                              '©', 'all rights']
                long_paragraphs = [
                    p.get_text(strip=True) for p in soup.find_all('p')
                    if len(p.get_text(strip=True)) > 50
                    and not any(w in p.get_text(strip=True).lower() for w in skip_words)
                ]
                if long_paragraphs:
                    content_text = "\n\n".join(long_paragraphs[:20])

            content_text = content_text.strip()

            if not content_text:
                print(f"    ❌ Tidak ada konten yang ditemukan")
                return None

            # --- Penulis ---
            author_selectors = [
                'div.author', 'span.author', 'div[class*="author"]',
                'a[href*="/author/"]', 'div.writer', 'div.reporter',
                'div.post-author', 'div.byline',
            ]
            author = "Tidak diketahui"
            for selector in author_selectors:
                elem = soup.select_one(selector)
                if elem:
                    text = elem.get_text(strip=True)
                    if text and text.lower() not in ['', 'admin', 'editor', 'redaksi', 'newsroom']:
                        author = text
                        break

            # --- Waktu publish ---
            time_selectors = [
                'time[datetime]',
                'meta[property="article:published_time"]',
                'div.post-date', 'span.post-date',
                'div.date', 'div.published-date', 'div.time',
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

            # --- Tags ---
            tags = []
            tag_selectors = [
                'div.tags a', 'a[rel="tag"]', 'div.category a',
                'ul.tags li a', 'div[class*="tag"] a',
            ]
            for selector in tag_selectors:
                for elem in soup.select(selector):
                    tag_text = elem.get_text(strip=True)
                    if tag_text and tag_text not in tags:
                        tags.append(tag_text)

            # --- Ringkasan/lead ---
            summary_selectors = [
                'div.excerpt', 'div.lead', 'p.lead',
                'div.article-excerpt', 'meta[property="og:description"]',
            ]
            summary = ""
            for selector in summary_selectors:
                elem = soup.select_one(selector)
                if elem:
                    summary = elem.get('content', '') if selector == 'meta[property="og:description"]' else elem.get_text(strip=True)
                    if summary:
                        break

            word_count = len(content_text.split())
            read_time_minutes = max(1, word_count // 200)
            print(f"    ✅ {word_count} kata ({read_time_minutes} menit baca)")

            return {
                'full_content': content_text,
                'summary': summary,
                'author': author,
                'publish_time': publish_time,
                'tags': tags[:10],
                'word_count': word_count,
                'read_time_minutes': read_time_minutes,
                'detail_scraped_at': datetime.now().isoformat(),
            }

        except requests.RequestException as e:
            print(f"    ❌ Error request: {str(e)[:80]}")
            return None
        except Exception as e:
            print(f"    ❌ Error: {str(e)[:80]}")
            return None

    #  BAGIAN 3: PIPELINE UTAMA

    def run(self, target_date, max_pages=10, detail_delay=2.0):
        """
        Pipeline lengkap: scrape listing -> filter tanggal -> scrape detail.

        Args:
            target_date : datetime.date  — tanggal yang ingin di-scrape
            max_pages   : int            — maks halaman listing
            detail_delay: float          — jeda (detik) antar request detail
        """
        # Step 1: Kumpulkan artikel sesuai tanggal
        articles = self.collect_articles_for_date(target_date, max_pages)

        if not articles:
            print(f"\n❌ Tidak ada artikel untuk tanggal {target_date}")
            return []

        print(f"\n📋 {len(articles)} artikel ditemukan. Mulai scrape detail...")
        print("=" * 60)

        # Step 2: Scrape detail tiap artikel
        results = []
        total = len(articles)

        for i, article in enumerate(articles):
            title_preview = article.get('title', f'Artikel {i+1}')[:60]
            print(f"\n[{i+1}/{total}] {title_preview}...")

            detail = self.scrape_article_detail(article.get('url', ''))

            if detail:
                combined = {**article, **detail}
                if detail.get('author') != "Tidak diketahui":
                    print(f"  👤 {detail['author']}")
                if detail.get('tags'):
                    print(f"  🏷️ {', '.join(detail['tags'][:3])}")
            else:
                combined = {**article, 'detail_error': 'Gagal mengambil konten'}

            results.append(combined)

            if i < total - 1:
                time.sleep(detail_delay)

        return results

    def save_results(self, results, target_date):
        """Simpan hasil ke semua output directory, return list path file atau None."""
        if not results:
            print("❌ Tidak ada hasil untuk disimpan")
            return None

        timestamp = datetime.now().strftime("%H%M%S")
        filename = f"kabarbursa_macro_{target_date.strftime('%Y%m%d')}_{timestamp}.json"
        saved_files = save_json_to_output_dirs(results, filename)

        if saved_files:
            print()
            print(f"✅ {len(results)} artikel disimpan ke:")
            for path in saved_files:
                print(f"   - {path}")
            return saved_files

        print("❌ Tidak ada file yang berhasil disimpan")
        return None

    def print_summary(self, results):
        """Tampilkan ringkasan statistik hasil scraping"""
        if not results:
            return

        total = len(results)
        with_detail = sum(1 for a in results if 'full_content' in a)
        failed = total - with_detail

        print("\n" + "=" * 60)
        print("📋 RINGKASAN HASIL SCRAPING")
        print("=" * 60)
        print(f"  Total artikel  : {total}")
        print(f"  Berhasil detail: {with_detail}")
        print(f"  Gagal detail   : {failed}")

        if with_detail > 0:
            total_words = sum(a.get('word_count', 0) for a in results if 'word_count' in a)
            avg_words = total_words // with_detail
            print(f"\n📊 Statistik konten:")
            print(f"  Total kata        : {total_words:,}")
            print(f"  Rata-rata kata    : {avg_words}")
            print(f"  Rata-rata baca    : {max(1, avg_words // 200)} menit")

            print(f"\n📰 Contoh artikel:")
            for i, article in enumerate([a for a in results if 'full_content' in a][:3]):
                preview = article['full_content'][:100].replace('\n', ' ') + "..."
                print(f"\n  {i+1}. {article.get('title', 'N/A')[:55]}...")
                print(f"     📝 {article.get('word_count', 0)} kata | 👤 {article.get('author', '?')}")
                if article.get('tags'):
                    print(f"     🏷️ {', '.join(article['tags'][:3])}")
                print(f"     {preview}")

#  ENTRY POIN

def main():
    print("=" * 70)
    print("KABARBURSA MACRO NEWS SCRAPER  (summary + detail sekaligus)")
    print("=" * 70)

    mode, target_dates = select_scrape_mode()
    if mode == "exit":
        print("👋 Keluar")
        return

    try:
        print()
        max_pages = int(input("Maksimal halaman listing per tanggal (default=10): ").strip() or "10")
    except ValueError:
        max_pages = 10

    try:
        detail_delay = float(input("Delay antar request detail, detik (default=2): ").strip() or "2")
    except ValueError:
        detail_delay = 2.0

    print()
    print("=" * 70)
    print("⚙️  KONFIGURASI")
    print("=" * 70)
    if mode == "range":
        print("  🧭 Mode            : Rentang tanggal")
        print(f"  📅 Dari            : {target_dates[0].strftime('%d %B %Y')}")
        print(f"  📅 Sampai          : {target_dates[-1].strftime('%d %B %Y')}")
        print(f"  🗓️ Total hari      : {len(target_dates)}")
    else:
        print("  🧭 Mode            : Test scraping 1 hari")
        print(f"  📅 Tanggal target  : {target_dates[0].strftime('%d %B %Y')}")
    print(f"  📄 Maks halaman    : {max_pages}")
    print(f"  ⏰ Delay detail    : {detail_delay} detik")
    print("  💾 Output utama    : " + get_output_dirs()[0])
    if len(get_output_dirs()) > 1:
        print("  💾 Output mirror   : " + ", ".join(get_output_dirs()[1:]))

    print()
    confirm = input("Lanjutkan? (y/n): ").lower().strip()
    if confirm != "y":
        print("❌ Dibatalkan")
        return

    print()
    print("=" * 70)
    print("🚀 MEMULAI SCRAPING...")
    print("=" * 70)

    scraper = KabarBursaScraper()
    total_saved_days = 0
    total_articles = 0
    start_time_all = time.time()

    for day_idx, target_date in enumerate(target_dates, start=1):
        print()
        print("#" * 70)
        print(f"📆 HARI {day_idx}/{len(target_dates)}: {target_date.strftime('%d/%m/%Y')}")
        print("#" * 70)

        start_time = time.time()
        results = []

        try:
            results = scraper.run(target_date, max_pages=max_pages, detail_delay=detail_delay)
            elapsed = time.time() - start_time

            if results:
                scraper.save_results(results, target_date)
                scraper.print_summary(results)
                total_saved_days += 1
                total_articles += len(results)
                print()
                print(f"⏱️  Tanggal {target_date.strftime('%d/%m/%Y')} selesai dalam {elapsed:.1f} detik")
            else:
                print()
                print("❌ Tidak ada artikel yang berhasil di-scrape")
                print()
                print("💡 Saran:")
                print("  1. Coba tanggal lain (hari kerja bursa)")
                print("  2. Tambah jumlah halaman maksimal")
                print("  3. Periksa koneksi internet")

        except KeyboardInterrupt:
            print()
            print("⚠️  Scraping dihentikan oleh pengguna")
            if results:
                timestamp = datetime.now().strftime("%H%M%S")
                partial_name = f"kabarbursa_macro_partial_{target_date.strftime('%Y%m%d')}_{timestamp}.json"
                saved_files = save_json_to_output_dirs(results, partial_name)
                if saved_files:
                    print("💾 Data parsial disimpan ke:")
                    for path in saved_files:
                        print(f"   - {path}")
            else:
                print("ℹ️ Tidak ada data yang dapat disimpan")
            break

        except Exception as e:
            print()
            print(f"❌ Error tidak terduga pada {target_date.strftime('%d/%m/%Y')}: {e}")
            import traceback
            traceback.print_exc()

    elapsed_all = time.time() - start_time_all
    print()
    print("=" * 70)
    print("🎉 PROSES SELESAI")
    print("=" * 70)
    print(f"  Hari dengan data : {total_saved_days}/{len(target_dates)}")
    print(f"  Total artikel    : {total_articles}")
    print(f"  Total waktu      : {elapsed_all:.1f} detik")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Scraping dihentikan oleh pengguna")
    except Exception as e:
        print(f"\n❌ Error tidak terduga: {e}")
        import traceback
        traceback.print_exc()