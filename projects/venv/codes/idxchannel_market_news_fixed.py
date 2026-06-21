import requests
from bs4 import BeautifulSoup
import json
import time
import os
import re
import html
from datetime import datetime, timedelta
from urllib.parse import urljoin, urlparse


OUTPUT_DIR = ["../data/news/market_news/idx", "/Users/albert/Documents/Finances/projects/02_alpha_research/alpha_research/data/pure_raw/news/market_news/idx"]


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

class IDXChannelScraper:
    def __init__(self):
        self.base_url = "https://www.idxchannel.com"
        self.session = requests.Session()

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

    # SCRAPING LISTING (SUMMARY)
    def extract_url_from_onclick(self, onclick_text):
        """Ekstrak URL dari atribut onclick tombol load more"""
        patterns = [
            r"['\"](https?://[^'\"]+)['\"]",
            r"myFunction\('([^']+)'\)",
            r"loadMore\('([^']+)'\)",
            r"window\.location\s*=\s*['\"]([^'\"]+)['\"]",
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

    def parse_article_date(self, date_text, default_date):
        """Parse tanggal artikel dari teks display ke format YYYY-MM-DD"""
        if not date_text or date_text == "N/A":
            return default_date
        try:
            match = re.search(r'(\d{1,2})/(\d{1,2})/(\d{4})', date_text)
            if match:
                day, month, year = match.groups()
                return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        except Exception:
            pass
        return default_date

    def extract_article_summary(self, element, date_str, batch_num):
        """Ekstrak data summary (judul, url, tanggal, dll.) dari satu elemen HTML"""
        try:
            # Judul
            title = "N/A"
            title_selectors = [
                '.list-berita-baru a',
                'h2 a', 'h3 a', 'h4 a',
                'div.title-capt a',
                'a[href*="/market-news/"]',
            ]
            for selector in title_selectors:
                elem = element.select_one(selector)
                if elem:
                    text = elem.get_text(strip=True)
                    if text and len(text) > 5:
                        title = html.unescape(text)
                        break

            if title == "N/A":
                for link in element.find_all('a', href=lambda x: x and '/market-news/' in x):
                    text = link.get_text(strip=True)
                    if text and len(text) > 5:
                        title = html.unescape(text)
                        break

            # URL
            url = "N/A"
            link_elem = element.find('a', href=lambda x: x and '/market-news/' in x)
            if link_elem:
                url = urljoin(self.base_url, link_elem.get('href', ''))

            # Tanggal
            date_display = "N/A"
            for selector in ['span.mh-clock', '.date', '.time', 'span.date', 'time']:
                elem = element.select_one(selector)
                if elem:
                    text = elem.get_text(strip=True)
                    if text:
                        date_display = text
                        break

            # Gambar
            image_url = ""
            img_elem = element.find('img')
            if img_elem:
                image_url = img_elem.get('data-original') or img_elem.get('src', '')
                if image_url.startswith('//'):
                    image_url = 'https:' + image_url
                elif image_url.startswith('/'):
                    image_url = self.base_url + image_url

            # Kategori
            category = "Market News"
            cat_elem = element.select_one('.category, .kanal, .channel, .headline-kanal')
            if cat_elem:
                cat_text = cat_elem.get_text(strip=True)
                if cat_text:
                    category = cat_text

            parsed_date = self.parse_article_date(date_display, date_str)

            return {
                'title': title,
                'url': url,
                'date_display': date_display,
                'date': parsed_date,
                'image_url': image_url,
                'category': category,
                'batch': batch_num,
                'source': 'IDX Channel',
                'scraped_at': datetime.now().isoformat(),
            }

        except Exception as e:
            print(f"      ⚠️ Error ekstraksi summary: {e}")
            return None

    def extract_articles_from_batch(self, soup, date_str, batch_num):
        """Ekstrak semua artikel dari satu batch HTML listing"""
        articles = []
        selectors = ['div.bt-con', 'div[class*="news"]', 'article', 'div.post', 'div.item']

        for selector in selectors:
            elements = soup.select(selector)
            if elements:
                filtered = [
                    e for e in elements
                    if e.find('a', href=lambda x: x and '/market-news/' in x)
                ]
                if filtered:
                    for element in filtered:
                        article = self.extract_article_summary(element, date_str, batch_num)
                        if article:
                            articles.append(article)
                    break

        return articles

    def collect_articles_for_day(self, date_obj):
        """
        Scrape semua artikel pada satu hari dengan menangani tombol 'Load More'.
        Return list artikel (summary saja, belum ada detail konten).
        """
        date_ymd = date_obj.strftime("%Y-%m-%d")
        date_dmy = date_obj.strftime("%d-%m-%Y")
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
                print(f"  🔄 Batch 1: Halaman utama")
            else:
                url = f"{self.base_url}/indeks/more/{current_offset}?idkanal=1&date={date_dmy}"
                print(f"  🔄 Batch {batch_count + 1}: Load more (offset={current_offset})")

            try:
                response = self.session.get(url, timeout=30)
                if response.status_code != 200:
                    print(f"    ⚠️ Status: {response.status_code}")
                    break

                soup = BeautifulSoup(response.text, 'html.parser')
                batch_articles = self.extract_articles_from_batch(soup, date_ymd, batch_count)

                if not batch_articles:
                    print(f"    ℹ️ Tidak ada artikel di batch ini")
                    break

                print(f"    ✅ {len(batch_articles)} artikel ditemukan")
                all_articles.extend(batch_articles)

                # Cek tombol Load More
                load_more = (
                    soup.find('a', id='NextRow') or
                    soup.find('a', class_=lambda x: x and 'load-more' in str(x)) or
                    soup.find('div', class_='button-default')
                )

                if load_more:
                    onclick_text = load_more.get('onclick', '')
                    if onclick_text:
                        js_url = self.extract_url_from_onclick(onclick_text)
                        if js_url:
                            path_parts = urlparse(js_url).path.split('/')
                            for i, part in enumerate(path_parts):
                                if part == 'more' and i + 1 < len(path_parts):
                                    try:
                                        new_offset = int(path_parts[i + 1])
                                        if new_offset > current_offset:
                                            current_offset = new_offset
                                        else:
                                            print(f"    ⏹️ Offset tidak bertambah, berhenti")
                                            batch_count = max_batches  # Force exit
                                    except Exception:
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
                print(f"    ❌ Error: {str(e)[:80]}")
                break

        print(f"  📊 Total: {len(all_articles)} artikel dari {batch_count + 1} batch")
        return all_articles

    # SCRAPING DETAIL ARTIKEL
    def get_soup(self, url):
        """Request URL dan return BeautifulSoup, atau None jika gagal"""
        try:
            r = self.session.get(url, timeout=15)
            if r.status_code == 200:
                return BeautifulSoup(r.text, 'html.parser')
            print(f"    ⚠️ Status {r.status_code} untuk {url}")
            return None
        except Exception as e:
            print(f"    ❌ Error request: {str(e)[:80]}")
            return None

    def extract_paragraphs(self, soup):
        """Ekstrak paragraf konten dari container artikel"""
        paragraphs = []
        container = soup.find('div', class_='detail--article') or \
                    soup.find('div', class_='detail-content--left')

        if container:
            for p in container.find_all('p'):
                text = p.get_text(strip=True)
                if text and len(text) > 20:
                    lower = text.lower()
                    if 'baca juga:' in lower or 'simak:' in lower:
                        continue
                    paragraphs.append(text)

        return paragraphs

    def extract_pagination_links(self, soup, current_url):
        """Ekstrak link halaman lanjutan (multi-page article)"""
        pagination = soup.find('div', class_='paging')
        if not pagination:
            return []

        links = []
        for a in pagination.find_all('a', href=True):
            full_url = urljoin(self.base_url, a['href'])
            if full_url != current_url and full_url not in links:
                links.append(full_url)
        return links

    def extract_tags(self, soup):
        """Ekstrak tags dari div.article--tags-link"""
        tags = []
        tags_div = soup.find('div', class_='article--tags-link')
        if tags_div:
            for a in tags_div.find_all('a', href=True):
                tag_text = a.get_text(strip=True)
                if tag_text and tag_text not in tags:
                    tags.append(tag_text)
        return tags

    def extract_metadata(self, soup):
        """Ekstrak metadata: penulis, waktu publish, gambar utama, ringkasan"""
        # Penulis
        author = "Reporter IDX Channel"
        author_elem = soup.find('a', href=lambda x: x and '/author/' in x)
        if author_elem:
            author = author_elem.get_text(strip=True)
        else:
            creator_div = soup.find('div', class_='article--creator')
            if creator_div:
                link = creator_div.find('a', href=lambda x: x and '/author/' in x)
                if link:
                    author = link.get_text(strip=True)

        # Waktu publish
        publish_time = ""
        time_elem = soup.find('div', class_='article--creator')
        if time_elem:
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

        # Ringkasan
        summary = ""
        excerpt_div = soup.find('div', class_='article--excerpt')
        if excerpt_div:
            summary = excerpt_div.get_text(strip=True)

        return {
            'author': author,
            'publish_time': publish_time,
            'main_image': main_image,
            'summary': summary,
        }

    def scrape_article_detail(self, url):
        """
        Scrape konten lengkap dari URL artikel (termasuk multi-halaman).
        Return dict detail atau None jika gagal.
        """
        print(f"  📄 Mengakses: {url[:80]}...")
        soup = self.get_soup(url)
        if not soup:
            return None

        metadata = self.extract_metadata(soup)
        all_paragraphs = self.extract_paragraphs(soup)

        # Halaman lanjutan (artikel multi-halaman)
        for page_url in self.extract_pagination_links(soup, url):
            print(f"    ➡️  Halaman tambahan: {page_url}")
            page_soup = self.get_soup(page_url)
            if page_soup:
                all_paragraphs.extend(self.extract_paragraphs(page_soup))
                time.sleep(1)

        full_content = "\n\n".join(all_paragraphs)

        if not full_content.strip():
            print(f"    ❌ Tidak ada konten yang ditemukan")
            return None

        tags = self.extract_tags(soup)
        word_count = len(full_content.split())
        read_time = max(1, word_count // 200)

        print(f"    ✅ {word_count} kata ({read_time} menit baca)")

        return {
            'full_content': full_content,
            'summary': metadata['summary'],
            'author': metadata['author'],
            'publish_time': metadata['publish_time'],
            'main_image': metadata['main_image'],
            'tags': tags,
            'word_count': word_count,
            'read_time_minutes': read_time,
            'detail_scraped_at': datetime.now().isoformat(),
        }

    # MAIN PIPELINE 
    def run(self, target_date, detail_delay=2.0):
        """
        Pipeline lengkap: scrape listing -> scrape detail tiap artikel.

        Args:
            target_date  : datetime.date — tanggal yang ingin di-scrape
            detail_delay : float         — jeda (detik) antar request detail
        """
        # Step 1: Kumpulkan semua artikel listing untuk hari ini
        articles = self.collect_articles_for_day(target_date)

        if not articles:
            print(f"\n❌ Tidak ada artikel untuk tanggal {target_date}")
            return []

        # Filter hanya artikel dengan URL valid
        valid_articles = [
            a for a in articles
            if a.get('title', 'N/A') != 'N/A' and a.get('url', 'N/A') != 'N/A'
        ]

        print(f"\n📋 {len(valid_articles)} artikel valid ditemukan. Mulai scrape detail...")
        print("=" * 60)

        # Step 2: Scrape detail tiap artikel
        results = []
        total = len(valid_articles)

        for i, article in enumerate(valid_articles):
            title_preview = article.get('title', f'Artikel {i+1}')[:60]
            print(f"\n[{i+1}/{total}] {title_preview}...")

            detail = self.scrape_article_detail(article.get('url', ''))

            if detail and detail.get('full_content'):
                combined = {**article, **detail}
                if detail.get('author') != "Reporter IDX Channel":
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
        filename = f"idxchannel_{target_date.strftime('%Y%m%d')}_{timestamp}.json"
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
            print(f"  Total kata     : {total_words:,}")
            print(f"  Rata-rata kata : {avg_words}")
            print(f"  Rata-rata baca : {max(1, avg_words // 200)} menit")

            detailed = [a for a in results if 'full_content' in a]
            print(f"\n📰 Contoh artikel:")
            for i, article in enumerate(detailed[:3]):
                preview = article['full_content'][:100].replace('\n', ' ') + "..."
                print(f"\n  {i+1}. {article.get('title', 'N/A')[:55]}...")
                print(f"     📝 {article.get('word_count', 0)} kata | 👤 {article.get('author', '?')}")
                if article.get('tags'):
                    print(f"     🏷️ {', '.join(article['tags'][:3])}")
                print(f"     {preview}")

#  ENTRY POINT
def main():
    print("=" * 70)
    print("IDX CHANNEL MARKET NEWS SCRAPER  (listing + detail sekaligus)")
    print("=" * 70)

    mode, target_dates = select_scrape_mode()
    if mode == "exit":
        print("👋 Keluar")
        return

    try:
        print()
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
    print(f"  ⏰ Delay detail    : {detail_delay} detik")
    print(f"  🌐 Mode            : Load More (AJAX)")
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

    scraper = IDXChannelScraper()
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
            results = scraper.run(target_date, detail_delay=detail_delay)
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
                print("  2. Periksa koneksi internet")

        except KeyboardInterrupt:
            print()
            print("⚠️  Scraping dihentikan oleh pengguna")
            if results:
                timestamp = datetime.now().strftime("%H%M%S")
                partial_name = f"idxchannel_partial_{target_date.strftime('%Y%m%d')}_{timestamp}.json"
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
    main()