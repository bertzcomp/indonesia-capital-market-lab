import requests
from bs4 import BeautifulSoup
import json
import time
import os
import re
import html
from datetime import datetime
from urllib.parse import urljoin, urlparse


OUTPUT_DIR = "../data/news/macro_news/idx"

# Kanal Economics IDX Channel
KANAL_ID   = "9772"
KANAL_NAME = "Economics"

# Path URL yang valid untuk kanal ini
VALID_PATHS = ('/market-news/', '/economics/')


class IDXChannelMacroScraper:
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

    # ------------------------------------------------------------------ #
    #  BAGIAN 1: SCRAPING LISTING (SUMMARY)
    # ------------------------------------------------------------------ #

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
                'a[href*="/economics/"]',
            ]
            for selector in title_selectors:
                elem = element.select_one(selector)
                if elem:
                    text = elem.get_text(strip=True)
                    if text and len(text) > 5:
                        title = html.unescape(text)
                        break

            if title == "N/A":
                for link in element.find_all('a', href=lambda x: x and any(p in x for p in VALID_PATHS)):
                    text = link.get_text(strip=True)
                    if text and len(text) > 5:
                        title = html.unescape(text)
                        break

            # URL
            url = "N/A"
            link_elem = element.find('a', href=lambda x: x and any(p in x for p in VALID_PATHS))
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
            category = KANAL_NAME
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
                    if e.find('a', href=lambda x: x and any(p in x for p in VALID_PATHS))
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
        main_url = f"{self.base_url}/indeks?date={date_ymd}&idkanal={KANAL_ID}"

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
                url = f"{self.base_url}/indeks/more/{current_offset}?idkanal={KANAL_ID}&date={date_dmy}"
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
                                            batch_count = max_batches  # force exit
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

    # ------------------------------------------------------------------ #
    #  BAGIAN 2: SCRAPING DETAIL ARTIKEL
    # ------------------------------------------------------------------ #

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

    # ------------------------------------------------------------------ #
    #  BAGIAN 3: PIPELINE UTAMA
    # ------------------------------------------------------------------ #

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
        """Simpan hasil ke file JSON, return path file atau None"""
        if not results:
            print("❌ Tidak ada hasil untuk disimpan")
            return None

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        timestamp = datetime.now().strftime("%H%M%S")
        filename = os.path.join(
            OUTPUT_DIR,
            f"idxchannel_macro_{target_date.strftime('%Y%m%d')}_{timestamp}.json"
        )

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"\n✅ {len(results)} artikel disimpan ke: {filename}")
            return filename
        except Exception as e:
            print(f"❌ Gagal menyimpan file: {e}")
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


# ------------------------------------------------------------------ #
#  HELPERS
# ------------------------------------------------------------------ #

def validate_date_input(date_str):
    """Validasi input tanggal dengan berbagai format"""
    for fmt in ['%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d', '%d %b %Y', '%d %B %Y']:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None


# ------------------------------------------------------------------ #
#  ENTRY POINT
# ------------------------------------------------------------------ #

def main():
    print("=" * 70)
    print(f"IDX CHANNEL MACRO DAILY SCRAPER  ({KANAL_NAME} | idkanal={KANAL_ID})")
    print("=" * 70)

    # --- Input tanggal ---
    print("\n📅 Masukkan tanggal target")
    print("   Format: DD/MM/YYYY atau DD-MM-YYYY")
    print("   Kosongkan untuk hari ini")

    while True:
        date_input = input("\nTanggal: ").strip()

        if not date_input:
            target_date = datetime.now().date()
            print(f"   ✅ {target_date.strftime('%d/%m/%Y')} (hari ini)")
            break

        target_date = validate_date_input(date_input)
        if target_date:
            print(f"   ✅ {target_date.strftime('%d/%m/%Y')}")
            break
        else:
            print("   ❌ Format tanggal tidak dikenali")

    # --- Konfigurasi ---
    try:
        detail_delay = float(input("\nDelay antar request detail, detik (default=2): ").strip() or "2")
    except ValueError:
        detail_delay = 2.0

    # --- Konfirmasi ---
    print("\n" + "=" * 70)
    print("⚙️  KONFIGURASI")
    print("=" * 70)
    print(f"  📅 Tanggal target  : {target_date.strftime('%d %B %Y')}")
    print(f"  ⏰ Delay detail    : {detail_delay} detik")
    print(f"  🌐 Mode            : Load More (AJAX)")
    print(f"  🔗 Kanal           : {KANAL_NAME} (idkanal={KANAL_ID})")

    confirm = input("\nLanjutkan? (y/n): ").lower().strip()
    if confirm != 'y':
        print("❌ Dibatalkan")
        return

    # --- Jalankan ---
    print("\n" + "=" * 70)
    print("🚀 MEMULAI SCRAPING...")
    print("=" * 70)

    start_time = time.time()
    scraper = IDXChannelMacroScraper()
    results = []

    try:
        results = scraper.run(target_date, detail_delay=detail_delay)
        elapsed = time.time() - start_time

        if results:
            scraper.save_results(results, target_date)
            scraper.print_summary(results)
            print(f"\n⏱️  Selesai dalam {elapsed:.1f} detik")
        else:
            print("\n❌ Tidak ada artikel yang berhasil di-scrape")
            print("\n💡 Saran:")
            print("  1. Coba tanggal lain")
            print("  2. Periksa koneksi internet")

    except KeyboardInterrupt:
        print("\n\n⚠️  Scraping dihentikan oleh pengguna")
        if results:
            timestamp = datetime.now().strftime("%H%M%S")
            partial_file = os.path.join(OUTPUT_DIR, f"idxchannel_macro_partial_{timestamp}.json")
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            with open(partial_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"💾 Data parsial disimpan: {partial_file}")
        else:
            print("ℹ️ Tidak ada data yang dapat disimpan")

    except Exception as e:
        print(f"\n❌ Error tidak terduga: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()