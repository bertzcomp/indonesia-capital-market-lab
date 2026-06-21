import time
import json
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import os
import csv
from dotenv import load_dotenv

load_dotenv()


#  Helper: verifikasi ticker sudah terpilih di UI
def _verify_ticker_selected(driver, expected_ticker: str) -> bool:
    """Cek apakah .item di selectize-input sudah menampilkan ticker yang benar."""
    try:
        item = driver.find_element(
            By.CSS_SELECTOR,
            "#input-broksum-ticker + .selectize-control .selectize-input .item"
        )
        return item.get_attribute("data-value") == expected_ticker
    except NoSuchElementException:
        return False


class NeoBDMBrokerScraper:
    def __init__(self, username=None, password=None, headless=False):
        self.username = username or os.getenv("NEOBDM_USERNAME")
        self.password = password or os.getenv("NEOBDM_PASSWORD")
        if not self.username or not self.password:
            raise ValueError("Username dan password harus disediakan melalui parameter atau file .env")
        self.driver = None
        self.wait = None
        self.cookies = None
        self.session = None          # requests.Session untuk mode Turbo API
        self.output_dir = "broker_summary_data"
        self.create_output_dir()
        self.setup_driver(headless)

    
    #  Setup
    def setup_driver(self, headless=False):
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        if headless:
            chrome_options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        self.wait = WebDriverWait(self.driver, 20)
        print("✓ Browser initialized")

    def create_output_dir(self):
        os.makedirs(self.output_dir, exist_ok=True)

    def save_screenshot(self, filename):
        try:
            self.driver.save_screenshot(filename)
            print(f"  📸 Screenshot: {filename}")
        except Exception:
            pass

    
    #  Login
    
    def login(self) -> bool:
        print("\n" + "=" * 60)
        print("LOGIN")
        print("=" * 60)
        try:
            self.driver.get("https://neobdm.tech/accounts/login/")
            time.sleep(2)

            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "id_login")))
            password_field = self.driver.find_element(By.ID, "id_password")
            login_button   = self.driver.find_element(By.CSS_SELECTOR, "button.primaryAction")

            username_field.clear()
            username_field.send_keys(self.username)
            password_field.clear()
            password_field.send_keys(self.password)
            login_button.click()
            time.sleep(4)

            current_url = self.driver.current_url
            print(f"  URL setelah login: {current_url}")

            if "login" not in current_url:
                print("✓ Login berhasil")
                self.cookies = self.driver.get_cookies()
                self._init_requests_session()
                return True

            # Cek elemen dashboard
            try:
                self.wait.until(
                    EC.any_of(
                        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Dashboard')]")),
                        EC.url_contains("dashboard"),
                        EC.url_contains("screener"),
                    )
                )
                print("✓ Login berhasil (dashboard ditemukan)")
                self.cookies = self.driver.get_cookies()
                self._init_requests_session()
                return True
            except TimeoutException:
                print("✗ Login gagal")
                self.save_screenshot("99_login_failed.png")
                return False

        except Exception as e:
            print(f"✗ Login error: {e}")
            self.save_screenshot("99_login_error.png")
            return False

    def manual_login_assist(self) -> bool:
        print("\nSilakan login secara manual di browser yang terbuka.")
        input("Setelah login berhasil, tekan ENTER...")
        self.cookies = self.driver.get_cookies()
        self._init_requests_session()
        return True

    def _init_requests_session(self):
        """Buat requests.Session dari cookies Selenium untuk mode Turbo API."""
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            ),
            "Referer": "https://neobdm.tech/broker_summary/",
            "X-Requested-With": "XMLHttpRequest",
        })
        for ck in self.cookies:
            self.session.cookies.set(ck["name"], ck["value"], domain=ck.get("domain", ""))
        # Tambahkan CSRF token ke header
        csrf = next((c["value"] for c in self.cookies if c["name"] == "csrftoken"), None)
        if csrf:
            self.session.headers["X-CSRFToken"] = csrf
        print("✓ requests.Session siap (mode Turbo API aktif)")

    
    #  Navigasi
    
    def navigate_to_broker_summary(self) -> bool:
        print("\n" + "=" * 60)
        print("NAVIGASI KE BROKER SUMMARY")
        print("=" * 60)
        self.driver.get("https://neobdm.tech/broker_summary/")
        time.sleep(3)

        if "login" in self.driver.current_url:
            print("✗ Di-redirect ke halaman login. Session hilang.")
            return False

        try:
            # Tunggu Selectize selesai di-initialize (ada .selectize-control)
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".selectize-control"))
            )
            print("✓ Halaman broker summary berhasil dimuat")
            return True
        except TimeoutException:
            print("✗ Halaman tidak termuat dengan benar")
            self.save_screenshot("99_nav_failed.png")
            return False

    
    #  SET TICKER — Inti perbaikan
    
    def set_ticker(self, ticker: str) -> bool:
        """
        Pilih ticker di dropdown Selectize.

        Urutan percobaan:
          1. Selectize JS API  → paling reliable, langsung panggil .setValue()
          2. ActionChains      → simulasi keyboard jika JS API gagal
        """
        ticker = ticker.upper().strip()
        print(f"  → Mengatur ticker: {ticker}")

        # ── Metode 1: Selectize JavaScript API ────────────────
        try:
            result = self.driver.execute_script(
                """
                var selectEl = document.getElementById('input-broksum-ticker');
                if (!selectEl)              return 'ERR:no_element';
                if (!selectEl.selectize)    return 'ERR:no_selectize_instance';

                var sz = selectEl.selectize;

                // Pastikan opsi ada
                if (!sz.options[arguments[0]]) return 'ERR:option_not_found';

                // setValue(value, silent=false) → silent=false agar onChange terpanggil
                sz.setValue(arguments[0], false);
                return 'OK';
                """,
                ticker,
            )

            if result == "OK":
                time.sleep(0.4)
                if _verify_ticker_selected(self.driver, ticker):
                    print(f"  ✓ Ticker {ticker} berhasil dipilih (Selectize JS API)")
                    return True
                else:
                    print("  ⚠ setValue dipanggil tapi verifikasi gagal, lanjut fallback...")

            elif result == "ERR:option_not_found":
                print(f"  ✗ Ticker {ticker} tidak ada dalam daftar opsi")
                return False

            else:
                print(f"  ⚠ JS API: {result}, mencoba fallback...")

        except Exception as e:
            print(f"  ⚠ JS API exception: {e}, mencoba fallback...")

        # ── Metode 2: ActionChains (fallback) ─────────────────
        return self._set_ticker_actionchains(ticker)

    def _set_ticker_actionchains(self, ticker: str) -> bool:
        """Fallback: simulasi klik + ketik + klik opsi dengan ActionChains & WebDriverWait."""
        try:
            # 2a. Klik container untuk membuka dropdown
            container = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     "#input-broksum-ticker + .selectize-control .selectize-input")
                )
            )
            container.click()
            time.sleep(0.3)

            # 2b. Ambil input yang sekarang visible/aktif
            input_elem = self.driver.find_element(By.ID, "input-broksum-ticker-selectized")

            # 2c. Hapus konten lama dan ketik ticker baru
            ActionChains(self.driver)\
                .triple_click(input_elem)\
                .send_keys(Keys.DELETE)\
                .perform()
            time.sleep(0.2)
            input_elem.send_keys(ticker)

            # 2d. Tunggu dropdown muncul (visible)
            WebDriverWait(self.driver, 6).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR,
                     "#input-broksum-ticker + .selectize-control .selectize-dropdown")
                )
            )

            # 2e. Klik opsi yang data-value-nya persis sama
            option_selector = (
                f"#input-broksum-ticker + .selectize-control "
                f".selectize-dropdown .option[data-value='{ticker}']"
            )
            option = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, option_selector))
            )
            option.click()
            time.sleep(0.5)

            if _verify_ticker_selected(self.driver, ticker):
                print(f"  ✓ Ticker {ticker} berhasil dipilih (ActionChains fallback)")
                return True
            else:
                print(f"  ✗ ActionChains: verifikasi gagal untuk {ticker}")
                return False

        except TimeoutException:
            print(f"  ✗ Timeout menunggu dropdown atau opsi untuk ticker {ticker}")
            return False
        except Exception as e:
            print(f"  ✗ ActionChains fallback error: {e}")
            return False

    
    #  SET Mode, Filter, Tanggal
    
    def set_mode(self, mode: str):
        """mode: 'Net' atau 'Val'"""
        try:
            select = Select(self.wait.until(EC.presence_of_element_located((By.ID, "bs-mode-select"))))
            val = "true" if mode.lower() == "net" else "false"
            select.select_by_value(val)
            print(f"  ✓ Mode: {mode}")
        except Exception as e:
            print(f"  ✗ Error set mode: {e}")

    def set_filter(self, filter_value: str):
        """filter: 'All', 'F', atau 'D'"""
        try:
            select = Select(self.wait.until(EC.presence_of_element_located((By.ID, "bs-fda-select"))))
            mapping = {"all": "A", "f": "F", "d": "D"}
            select.select_by_value(mapping[filter_value.lower()])
            print(f"  ✓ Filter: {filter_value}")
        except Exception as e:
            print(f"  ✗ Error set filter: {e}")

    def _detect_datepicker_format(self) -> str:
        """
        Baca format yang dikonfigurasi Bootstrap Datepicker dari elemen start-date.
        Kembalikan format strftime Python yang setara.
        """
        result = self.driver.execute_script(
            """
            try {
                var el = document.getElementById('broksum-start-date');
                // Bootstrap Datepicker menyimpan instance di $.data
                var dp = $(el).data('datepicker');
                if (dp && dp.o && dp.o.format) return dp.o.format.toValue || dp.o.format;
                // Coba juga via _d
                if (dp && dp.format) return dp.format;
                return 'unknown';
            } catch(e) { return 'err:' + e.message; }
            """
        )
        print(f"  ℹ Datepicker format raw: {result}")

        # Mapping Bootstrap Datepicker format → strftime Python
        fmt_map = {
            "dd M yyyy":   "%d %b %Y",   # "03 Mar 2026"
            "dd MM yyyy":  "%d %B %Y",   # "03 March 2026"
            "dd/mm/yyyy":  "%d/%m/%Y",
            "mm/dd/yyyy":  "%m/%d/%Y",
            "yyyy-mm-dd":  "%Y-%m-%d",
            "d M yyyy":    "%-d %b %Y",
        }
        return fmt_map.get(str(result).lower(), "%d %b %Y")  # default yg paling umum

    def set_date(self, date_obj: datetime):
        """
        Set tanggal start & end menggunakan Bootstrap Datepicker jQuery API.

        Urutan percobaan:
          1. jQuery datepicker('update') / datepicker('setDate')  — paling benar
          2. ActionChains: triple-click + ketik tanggal + Enter   — fallback UI
        """
        # ── Coba deteksi format, fallback ke format paling umum ──
        py_fmt   = self._detect_datepicker_format()
        date_str = date_obj.strftime(py_fmt)
        print(f"  → Mengatur tanggal: {date_str} (fmt: {py_fmt})")

        # ── Metode 1: jQuery Bootstrap Datepicker API ─────────────
        js_result = self.driver.execute_script(
            """
            var dateStr = arguments[0];
            var results = {};

            var ids = ['broksum-start-date', 'broksum-end-date'];
            for (var i = 0; i < ids.length; i++) {
                var el = document.getElementById(ids[i]);
                if (!el) { results[ids[i]] = 'ERR:no_element'; continue; }

                try {
                    // Bootstrap Datepicker: $.fn.datepicker('update', dateStr)
                    $(el).datepicker('update', dateStr);
                    results[ids[i]] = 'OK:update';
                } catch(e1) {
                    try {
                        // Alternatif: setDate dengan Date object
                        $(el).datepicker('setDate', new Date(dateStr));
                        results[ids[i]] = 'OK:setDate';
                    } catch(e2) {
                        // Terakhir: langsung set value + trigger changeDate
                        el.value = dateStr;
                        $(el).trigger('changeDate');
                        $(el).trigger('change');
                        results[ids[i]] = 'OK:manual';
                    }
                }
            }
            return JSON.stringify(results);
            """,
            date_str,
        )
        print(f"  ℹ Datepicker JS result: {js_result}")

        # Verifikasi nilai tersimpan
        time.sleep(0.4)
        actual_start = self.driver.execute_script(
            "return document.getElementById('broksum-start-date').value;"
        )
        actual_end = self.driver.execute_script(
            "return document.getElementById('broksum-end-date').value;"
        )
        print(f"  ℹ Nilai aktual di field: start='{actual_start}' end='{actual_end}'")

        if actual_start and actual_end:
            print(f"  ✓ Tanggal berhasil diset: {actual_start}")
            return

        # ── Metode 2: ActionChains fallback ─────────────────────
        print("  ⚠ jQuery API tidak meng-update field, mencoba ActionChains...")
        self._set_date_actionchains(date_str)

    def _set_date_actionchains(self, date_str: str):
        """Fallback: klik field + ketik tanggal + tekan Enter."""
        for field_id in ("broksum-start-date", "broksum-end-date"):
            try:
                field = self.wait.until(
                    EC.element_to_be_clickable((By.ID, field_id))
                )
                # Triple-click untuk select-all, lalu ketik
                ActionChains(self.driver)\
                    .triple_click(field)\
                    .send_keys(Keys.DELETE)\
                    .perform()
                time.sleep(0.2)
                field.send_keys(date_str)
                time.sleep(0.3)
                field.send_keys(Keys.ENTER)
                time.sleep(0.3)
                # Klik di luar untuk dismiss datepicker popup
                self.driver.find_element(By.TAG_NAME, "body").click()
                time.sleep(0.2)
            except Exception as e:
                print(f"  ✗ ActionChains date error ({field_id}): {e}")

        actual = self.driver.execute_script(
            "return document.getElementById('broksum-start-date').value;"
        )
        print(f"  {'✓' if actual else '✗'} ActionChains date: '{actual}'")

    
    #  Load Data & Ekstrak Tabel
    
    def load_data(self) -> bool:
        """
        Klik tombol Load dan tunggu hingga AJAX benar-benar selesai.

        Masalah umum: "Data tidak tersedia" muncul sebentar sebagai
        placeholder SAAT data sedang dimuat, lalu diganti dengan tabel asli.
        Solusi: tunggu tabel stabil selama 2 detik berturut-turut sebelum
        menyimpulkan respons final.
        """
        try:
            load_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "broksum-button-load")))
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", load_btn)
            time.sleep(0.3)
            load_btn.click()
            print("  → Tombol Load diklik, menunggu AJAX selesai...")

            # ── Fase 1: tunggu tanda bahwa AJAX sudah mulai berjalan ──
            # (baris tbody sempat hilang / jadi 0, atau container di-clear)
            time.sleep(0.8)   # beri waktu JS memproses klik

            # ── Fase 2: polling hingga DOM stabil ─────────────────────
            # "Stabil" = jumlah baris tbody tidak berubah selama 2× check
            # berturut-turut dengan jeda 1 detik.
            STABLE_NEEDED = 2   # berapa kali berturut-turut harus sama
            POLL_INTERVAL = 1.0 # detik antar poll
            MAX_POLLS     = 15  # maksimum 15 detik total

            prev_rows = -1
            stable_count = 0

            for _ in range(MAX_POLLS):
                time.sleep(POLL_INTERVAL)
                try:
                    rows_now = len(
                        self.driver.find_elements(
                            By.CSS_SELECTOR, "#broker-summary-table tbody tr"
                        )
                    )
                except Exception:
                    rows_now = 0

                if rows_now == prev_rows:
                    stable_count += 1
                    if stable_count >= STABLE_NEEDED:
                        print(f"  ✓ DOM stabil ({rows_now} baris), AJAX selesai")
                        return True
                else:
                    stable_count = 0
                    prev_rows = rows_now

            # Timeout tapi tetap lanjut — mungkin data memang tidak ada
            print(f"  ⚠ Polling timeout, lanjut dengan kondisi saat ini ({prev_rows} baris)")
            return True

        except Exception as e:
            print(f"  ✗ Error klik load: {e}")
            return False

    def extract_table(self) -> list[dict]:
        rows = []
        try:
            # Periksa apakah tabel ada dan punya baris
            tbody_rows = self.driver.find_elements(
                By.CSS_SELECTOR, "#broker-summary-table tbody tr"
            )

            if not tbody_rows:
                # Tidak ada <tr> sama sekali — cek apakah ada pesan "tidak tersedia"
                try:
                    self.driver.find_element(
                        By.XPATH, "//*[contains(text(),'Data tidak tersedia')]"
                    )
                    print("  ℹ Data tidak tersedia (confirmed: pesan ditemukan)")
                except NoSuchElementException:
                    print("  ℹ Tabel kosong (0 baris, tanpa pesan error — mungkin hari libur)")
                return rows

            # Tabel ada, ambil datanya
            for tr in tbody_rows:
                tds = tr.find_elements(By.TAG_NAME, "td")
                if len(tds) < 8:
                    continue

                def safe_text(el):
                    return el.text.strip()

                def broker_code(td):
                    try:
                        span = td.find_element(By.CSS_SELECTOR, "span.broksum-broker")
                        return span.text.strip(), span.get_attribute("title") or ""
                    except NoSuchElementException:
                        return td.text.strip(), ""

                buy_code,  buy_name  = broker_code(tds[0])
                sell_code, sell_name = broker_code(tds[4])

                rows.append({
                    "buy_broker":  buy_code,
                    "buy_name":    buy_name,
                    "buy_blot":    safe_text(tds[1]),
                    "buy_bval":    safe_text(tds[2]),
                    "buy_bavg":    safe_text(tds[3]),
                    "sell_broker": sell_code,
                    "sell_name":   sell_name,
                    "sell_slot":   safe_text(tds[5]),
                    "sell_sval":   safe_text(tds[6]),
                    "sell_savg":   safe_text(tds[7]),
                })

            print(f"  ✓ Berhasil mengambil {len(rows)} baris")

        except Exception as e:
            print(f"  ✗ Error ekstrak tabel: {e}")
            self.save_screenshot("99_extract_error.png")
        return rows

    
    #  MODE TURBO: Direct API (10× lebih cepat)
    
    def fetch_via_api(
        self,
        ticker: str,
        mode: str,
        filter_value: str,
        date_obj: datetime,
    ) -> list[dict]:
        """
        Ambil data langsung dari endpoint /api/broker-summary
        menggunakan session cookies dari Selenium.
        Tidak memerlukan interaksi browser sama sekali.
        """
        if not self.session:
            print("  ✗ Session belum diinisialisasi. Jalankan login() lebih dulu.")
            return []

        date_str = date_obj.strftime("%Y-%m-%d")
        mode_val = "true" if mode.lower() == "net" else "false"
        fda_val  = {"all": "A", "f": "F", "d": "D"}.get(filter_value.lower(), "A")

        params = {
            "ticker":      ticker.upper(),
            "start_date":  date_str,
            "end_date":    date_str,
            "mode":        mode_val,
            "fda":         fda_val,
        }

        try:
            resp = self.session.get(
                "https://neobdm.tech/api/broker-summary",
                params=params,
                timeout=15,
            )
            resp.raise_for_status()
            data = resp.json()

            # Normalisasi respons — sesuaikan dengan struktur JSON aktual
            rows = []
            if isinstance(data, list):
                rows = data
            elif isinstance(data, dict):
                rows = data.get("data", data.get("results", []))

            print(f"  ✓ [API] {ticker} {date_str}: {len(rows)} baris")
            return rows

        except requests.HTTPError as e:
            print(f"  ✗ HTTP Error {e.response.status_code}: {e}")
        except requests.ConnectionError:
            print("  ✗ Koneksi gagal")
        except json.JSONDecodeError:
            print("  ✗ Respons bukan JSON. Mungkin perlu re-login.")
        except Exception as e:
            print(f"  ✗ API error: {e}")
        return []

    
    #  Scraping per-tanggal
    
    def scrape_date(
        self,
        ticker: str,
        mode: str,
        filter_value: str,
        date: datetime,
        use_api: bool = False,
    ) -> list[dict]:
        print(f"\n  ─── {date.strftime('%Y-%m-%d')} ───")

        if use_api:
            return self.fetch_via_api(ticker, mode, filter_value, date)

        # ── Mode UI (Selenium) ─────────────────────────────────
        if not self.set_ticker(ticker):
            print(f"  ✗ Lewati {date.strftime('%Y-%m-%d')} (ticker gagal diset)")
            return []
        self.set_mode(mode)
        self.set_filter(filter_value)
        self.set_date(date)
        self.diagnose()   # ← cetak state semua field sebelum submit
        if not self.load_data():
            return []
        return self.extract_table()

    def generate_weekdays(self, start_date: datetime, end_date: datetime) -> list[datetime]:
        delta = end_date - start_date
        return [
            start_date + timedelta(days=i)
            for i in range(delta.days + 1)
            if (start_date + timedelta(days=i)).weekday() < 5
        ]

    def scrape_date_range(
        self,
        ticker: str,
        mode: str,
        filter_value: str,
        start_date: datetime,
        end_date: datetime,
        use_api: bool = False,
    ) -> dict[str, list[dict]]:
        dates = self.generate_weekdays(start_date, end_date)
        print(f"\nScraping {len(dates)} hari kerja untuk {ticker}...")
        all_data: dict[str, list[dict]] = {}
        for date in dates:
            data = self.scrape_date(ticker, mode, filter_value, date, use_api=use_api)
            all_data[date.strftime("%Y-%m-%d")] = data or []
            time.sleep(1.0 if use_api else 2.5)
        return all_data

    
    #  Simpan Excel per-ticker
    
    def save_to_excel(
        self,
        all_data: dict[str, list[dict]],
        ticker: str,
        start_str: str,
        end_str: str,
        subdir: str = "",
    ) -> str:
        folder = os.path.join(self.output_dir, subdir) if subdir else self.output_dir
        os.makedirs(folder, exist_ok=True)
        filename = f"broker_summary_{ticker}_{start_str}_to_{end_str}.xlsx"
        filepath = os.path.join(folder, filename)

        with pd.ExcelWriter(filepath, engine="openpyxl") as writer:
            summary_rows = []
            for date_str, rows in all_data.items():
                for row in rows:
                    summary_rows.append({"date": date_str, **row})
            if summary_rows:
                pd.DataFrame(summary_rows).to_excel(writer, sheet_name="ALL", index=False)
            for date_str, rows in all_data.items():
                df = pd.DataFrame(rows)
                df.to_excel(writer, sheet_name=date_str.replace("-", "")[:31], index=False)

        return filepath

    
    #  MULTI-TICKER: Turbo API paralel
    
    def _fetch_one(
        self,
        ticker: str,
        mode: str,
        filter_value: str,
        dates: list[datetime],
    ) -> dict[str, list[dict]]:
        """Worker untuk satu ticker — dipanggil dari thread pool."""
        result: dict[str, list[dict]] = {}
        for date in dates:
            rows = self.fetch_via_api(ticker, mode, filter_value, date)
            result[date.strftime("%Y-%m-%d")] = rows or []
            time.sleep(0.3)
        return result

    def scrape_multiple_tickers_api(
        self,
        tickers: list[str],
        mode: str,
        filter_value: str,
        start_date: datetime,
        end_date: datetime,
        max_workers: int = 8,
        resume: bool = True,
        start_str: str = "",
        end_str: str = "",
    ) -> None:
        """
        Scrape banyak ticker secara paralel menggunakan Turbo API + ThreadPoolExecutor.

        Output:
          broker_summary_data/
          └── {start_str}_to_{end_str}/
              ├── _progress.csv          ← daftar ticker selesai (untuk resume)
              ├── broker_summary_BBCA_...xlsx
              ├── broker_summary_BBRI_...xlsx
              └── ...
          └── MASTER_{start_str}_to_{end_str}.csv  ← gabungan semua ticker & tanggal
        """
        dates       = self.generate_weekdays(start_date, end_date)
        subdir      = f"{start_str}_to_{end_str}"
        folder      = os.path.join(self.output_dir, subdir)
        done_file   = os.path.join(folder, "_progress.csv")
        master_file = os.path.join(self.output_dir, f"MASTER_{subdir}.csv")
        os.makedirs(folder, exist_ok=True)

        # ── Load daftar ticker yang sudah selesai ─────────────
        done_set: set[str] = set()
        if resume and os.path.exists(done_file):
            with open(done_file, newline="") as f:
                done_set = {row[0] for row in csv.reader(f) if row}
            print(f"  ℹ Resume aktif: {len(done_set)} ticker sudah selesai, di-skip")

        pending = [t for t in tickers if t not in done_set]
        total   = len(tickers)

        print(f"\n{'='*60}")
        print(f"  MULTI-TICKER SCRAPING  (Turbo API Paralel)")
        print(f"  Total    : {total} ticker")
        print(f"  Pending  : {len(pending)} ticker")
        print(f"  Threads  : {max_workers}")
        print(f"  Hari kerja: {len(dates)} hari")
        print(f"  Output   : {folder}/")
        print(f"  Master   : {master_file}")
        print(f"{'='*60}\n")

        done_n        = len(done_set)
        progress_lock = Lock()
        master_lock   = Lock()

        def _process_ticker(ticker: str):
            nonlocal done_n
            try:
                data = self._fetch_one(ticker, mode, filter_value, dates)
                has_data = any(rows for rows in data.values())

                # Simpan Excel per-ticker
                self.save_to_excel(data, ticker, start_str, end_str, subdir=subdir)

                # Append ke master CSV (thread-safe)
                if has_data:
                    master_rows = [
                        {"ticker": ticker, "date": date_str, **row}
                        for date_str, rows in data.items()
                        for row in rows
                    ]
                    df_chunk = pd.DataFrame(master_rows)
                    with master_lock:
                        write_header = not os.path.exists(master_file)
                        df_chunk.to_csv(master_file, mode="a", header=write_header, index=False)

                # Catat progress
                with progress_lock:
                    done_n += 1
                    pct    = done_n / total * 100
                    icon   = "✓" if has_data else "○"
                    print(f"  {icon} [{done_n}/{total} | {pct:5.1f}%] {ticker}")
                    with open(done_file, "a", newline="") as f:
                        csv.writer(f).writerow([ticker])

                return ticker, True

            except Exception as e:
                with progress_lock:
                    print(f"  ✗ [{ticker}] error: {e}")
                return ticker, False

        # ── Eksekusi paralel ───────────────────────────────────
        failed = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(_process_ticker, t): t for t in pending}
            for future in as_completed(futures):
                ticker_done, ok = future.result()
                if not ok:
                    failed.append(ticker_done)

        print(f"\n{'='*60}")
        print(f"  SELESAI")
        print(f"  Sukses  : {len(pending) - len(failed)} ticker")
        print(f"  Gagal   : {len(failed)} ticker{(' → ' + str(failed)) if failed else ''}")
        print(f"  Master CSV: {master_file}")
        print(f"{'='*60}")

    
    #  MULTI-TICKER: Selenium UI (sequential)
    
    def scrape_multiple_tickers_ui(
        self,
        tickers: list[str],
        mode: str,
        filter_value: str,
        start_date: datetime,
        end_date: datetime,
        resume: bool = True,
        start_str: str = "",
        end_str: str = "",
    ) -> None:
        """Scrape banyak ticker satu per satu via Selenium UI."""
        subdir    = f"{start_str}_to_{end_str}"
        done_file = os.path.join(self.output_dir, subdir, "_progress.csv")
        os.makedirs(os.path.join(self.output_dir, subdir), exist_ok=True)

        done_set: set[str] = set()
        if resume and os.path.exists(done_file):
            with open(done_file, newline="") as f:
                done_set = {row[0] for row in csv.reader(f) if row}

        pending = [t for t in tickers if t not in done_set]
        print(f"\n  MULTI-TICKER UI: {len(pending)} / {len(tickers)} ticker pending\n")

        for i, ticker in enumerate(pending, 1):
            print(f"\n{'─'*60}")
            print(f"  [{i}/{len(pending)}] {ticker}")
            print(f"{'─'*60}")
            try:
                data = self.scrape_date_range(
                    ticker, mode, filter_value, start_date, end_date, use_api=False
                )
                self.save_to_excel(data, ticker, start_str, end_str, subdir=subdir)
                with open(done_file, "a", newline="") as f:
                    csv.writer(f).writerow([ticker])
                print(f"  ✓ {ticker} tersimpan")
            except Exception as e:
                print(f"  ✗ {ticker} gagal: {e}")
            time.sleep(1.5)

    
    #  Diagnostik (debugging)
    
    def diagnose(self):
        """Cetak state semua input form sebelum submit."""
        print("\n" + "─" * 50)
        print("  DIAGNOSTIK STATE FORM")
        print("─" * 50)
        info = self.driver.execute_script(
            """
            function val(id) {
                var el = document.getElementById(id);
                return el ? el.value : 'NOT_FOUND';
            }
            return {
                ticker:     val('input-broksum-ticker'),
                mode:       val('bs-mode-select'),
                filter:     val('bs-fda-select'),
                start_date: val('broksum-start-date'),
                end_date:   val('broksum-end-date'),
                url:        window.location.href,
            };
            """
        )
        for k, v in info.items():
            print(f"  {k:<14}: {v}")
        print("─" * 50 + "\n")

    def close(self):
        if self.driver:
            self.driver.quit()
            print("Browser ditutup.")


#  Daftar ticker IDX (≈800 saham)
ALL_TICKERS = ['KBLI', 'KBLM', 'KBLV', 'KBRI', 'KDSI', 'KDTN', 'KEEN', 'KEJU', 'KETR', 'KIAS', 'KICI', 'KIJA', 'KING', 'KINO', 'KIOS', 'KJEN', 'KKES', 'KKGI', 'KLAS', 'KLBF', 'KLIN', 'KMDS', 'KMTR', 'KOBX', 'KOCI', 'KOIN', 'KOKA', 'KONI', 'KOPI', 'KOTA', 'KPIG', 'KRAS', 'KREN', 'KRYA', 'KSIX', 'KUAS', 'LABA', 'LABS', 'LAJU', 'LAND', 'LAPD', 'LCGP', 'LCKM', 'LEAD', 'LFLO', 'LIFE', 'LINK', 'LION', 'LIVE', 'LMAS', 'LMAX', 'LMPI', 'LMSH', 'LOPI', 'LPCK', 'LPGI', 'LPIN', 'LPKR', 'LPLI', 'LPPF', 'LPPS', 'LRNA', 'LSIP', 'LTLS', 'LUCK', 'LUCY', 'MABA', 'MAGP', 'MAHA', 'MAIN', 'MANG', 'MAPA', 'MAPB', 'MAPI', 'MARI', 'MARK', 'MASB', 'MAXI', 'MAYA', 'MBAP', 'MBMA', 'MBSS', 'MBTO', 'MCAS', 'MCOL', 'MCOR', 'MDIA', 'MDIY', 'MDKA', 'MDKI', 'MDLA', 'MDLN', 'MDRN', 'MEDC', 'MEDS', 'MEGA', 'MEJA', 'MENN', 'MERI', 'MERK', 'META', 'MFMI', 'MGLV', 'MGNA', 'MGRO', 'MHKI', 'MICE', 'MIDI', 'MIKA', 'MINA', 'MINE', 'MIRA', 'MITI', 'MKAP', 'MKNT', 'MKPI', 'MKTR', 'MLBI', 'MLIA', 'MLPL', 'MLPT', 'MMIX', 'MMLP', 'MNCN', 'MOLI', 'MORA', 'MPIX', 'MPMX', 'MPOW', 'MPPA', 'MPRO', 'MPXL', 'MRAT', 'MREI', 'MSIE', 'MSIN', 'MSJA', 'MSKY', 'MSTI', 'MTDL', 'MTEL', 'MTFN', 'MTLA', 'MTMH', 'MTPS', 'MTRA', 'MTSM', 'MTWI', 'MUTU', 'MYOH', 'MYOR', 'MYTX', 'NAIK', 'NANO', 'NASA', 'NASI', 'NATO', 'NAYZ', 'NCKL', 'NELY', 'NEST', 'NETV', 'NFCX', 'NICE', 'NICK', 'NICL', 'NIKL', 'NINE', 'NIRO', 'NISP', 'NOBU', 'NPGF', 'NRCA', 'NSSS', 'NTBK', 'NUSA', 'NZIA', 'OASA', 'OBAT', 'OBMD', 'OCAP', 'OILS', 'OKAS', 'OLIV', 'OMED', 'OMRE', 'OPMS', 'PACK', 'PADA', 'PADI', 'PALM', 'PAMG', 'PANI', 'PANR', 'PANS', 'PART', 'PBID', 'PBRX', 'PBSA', 'PCAR', 'PDES', 'PDPP', 'PEGE', 'PEHA', 'PEVE', 'PGAS', 'PGEO', 'PGJO', 'PGLI', 'PGUN', 'PICO', 'PIPA', 'PJAA', 'PJHB', 'PKPK', 'PLAN', 'PLAS', 'PLIN', 'PMJS', 'PMMP', 'PMUI', 'PNBN', 'PNBS', 'PNGO', 'PNIN', 'PNLF', 'PNSE', 'POLA', 'POLI', 'POLL', 'POLU', 'POLY', 'POOL', 'PORT', 'POSA', 'POWR', 'PPGL', 'PPRE', 'PPRI', 'PPRO', 'PRAY', 'PRDA', 'PRIM', 'PSAB', 'PSAT', 'PSDN', 'PSGO', 'PSKT', 'PSSI', 'PTBA', 'PTDU', 'PTIS', 'PTMP', 'PTMR', 'PTPP', 'PTPS', 'PTPW', 'PTRO', 'PTSN', 'PTSP', 'PUDP', 'PURA', 'PURE', 'PURI', 'PWON', 'PYFA', 'PZZA', 'RAAM', 'RAFI', 'RAJA', 'RALS', 'RANC', 'RATU', 'RBMS', 'RCCC', 'RDTX', 'REAL', 'RELF', 'RELI', 'RGAS', 'RICY', 'RIGS', 'RIMO', 'RISE', 'RLCO', 'RMKE', 'RMKO', 'ROCK', 'RODA', 'RONY', 'ROTI', 'RSCH', 'RSGK', 'RUIS', 'RUNS', 'SAFE', 'SAGE', 'SAME', 'SAMF', 'SAPX', 'SATU', 'SBAT', 'SBMA', 'SCCO', 'SCMA', 'SCNP', 'SCPI', 'SDMU', 'SDPC', 'SDRA', 'SEMA', 'SFAN', 'SGER', 'SGRO', 'SHID', 'SHIP', 'SICO', 'SIDO', 'SILO', 'SIMA', 'SIMP', 'SINI', 'SIPD', 'SKBM', 'SKLT', 'SKRN', 'SKYB', 'SLIS', 'SMAR', 'SMBR', 'SMCB', 'SMDM', 'SMDR', 'SMGA', 'SMGR', 'SMIL', 'SMKL', 'SMKM', 'SMLE', 'SMMA', 'SMMT', 'SMRA', 'SMRU', 'SMSM', 'SNLK', 'SOCI', 'SOFA', 'SOHO', 'SOLA', 'SONA', 'SOSS', 'SOTS', 'SOUL', 'SPMA', 'SPRE', 'SPTO', 'SQMI', 'SRAJ', 'SRIL', 'SRSN', 'SRTG', 'SSIA', 'SSMS', 'SSTM', 'STAA', 'STAR', 'STRK', 'STTP', 'SUGI', 'SULI', 'SUNI', 'SUPA', 'SUPR', 'SURE', 'SURI', 'SWAT', 'SWID', 'TALF', 'TAMA', 'TAMU', 'TAPG', 'TARA', 'TAXI', 'TAYS', 'TBIG', 'TBLA', 'TBMS', 'TCID', 'TCPI', 'TDPM', 'TEBE', 'TECH', 'TELE', 'TFAS', 'TFCO', 'TGKA', 'TGRA', 'TGUK', 'TIFA', 'TINS', 'TIRA', 'TIRT', 'TKIM', 'TLDN', 'TLKM', 'TMAS', 'TMPO', 'TNCA', 'TOBA', 'TOOL', 'TOPS', 'TOSK', 'TOTL', 'TOTO', 'TOWR', 'TOYS', 'TPIA', 'TPMA', 'TRAM', 'TRGU', 'TRIL', 'TRIM', 'TRIN', 'TRIO', 'TRIS', 'TRJA', 'TRON', 'TRST', 'TRUE', 'TRUK', 'TRUS', 'TSPC', 'TUGU', 'TYRE', 'UANG', 'UCID', 'UDNG', 'UFOE', 'ULTJ', 'UNIC', 'UNIQ', 'UNIT', 'UNSP', 'UNTD', 'UNTR', 'UNVR', 'URBN', 'UVCR', 'VAST', 'VERN', 'VICI', 'VICO', 'VINS', 'VISI', 'VIVA', 'VKTR', 'VOKS', 'VRNA', 'VTNY', 'WAPO', 'WEGE', 'WEHA', 'WGSH', 'WICO', 'WIDI', 'WIFI', 'WIIM', 'WIKA', 'WINE', 'WINR', 'WINS', 'WIRG', 'WMPP', 'WMUU', 'WOMF', 'WOOD', 'WOWS', 'WSBP', 'WSKT', 'WTON', 'YELO', 'YOII', 'YPAS', 'YULE', 'YUPI', 'ZATA', 'ZBRA', 'ZINC', 'ZONE', 'ZYRX']

#  Main
def main():
    print("=" * 70)
    print("NEO BDM BROKER SUMMARY SCRAPER — MULTI-TICKER")
    print("=" * 70)

    username = os.getenv("NEOBDM_USERNAME") or input("Neo BDM username: ").strip()
    password = os.getenv("NEOBDM_PASSWORD") or input("Neo BDM password: ").strip()

    # ── Pilihan scope ticker ───────────────────────────────────
    print("\nScope ticker:")
    print("  [1] Satu ticker saja")
    print("  [2] Beberapa ticker (pisahkan koma, contoh: BBCA,BBRI,BMRI)")
    print(f"  [3] Semua ticker IDX ({len(ALL_TICKERS)} saham)")
    scope = input("Pilih (1/2/3, default 1): ").strip() or "1"

    if scope == "1":
        ticker_input = input("Ticker (default BBCA): ").strip().upper() or "BBCA"
        tickers = [ticker_input]
    elif scope == "2":
        raw = input("Ticker (pisahkan koma): ").strip().upper()
        tickers = [t.strip() for t in raw.split(",") if t.strip()]
        if not tickers:
            print("✗ Tidak ada ticker valid.")
            return
    else:
        tickers = ALL_TICKERS
        print(f"  → Akan scrape {len(tickers)} ticker")

    mode       = (input("\nMode (Net/Val, default Net): ").strip() or "Net")
    filter_val = (input("Filter (All/F/D, default All): ").strip() or "All")
    start_str  = input("Start date (DD-MM-YYYY): ").strip()
    end_str    = input("End date   (DD-MM-YYYY): ").strip()

    try:
        start_date = datetime.strptime(start_str, "%d-%m-%Y")
        end_date   = datetime.strptime(end_str,   "%d-%m-%Y")
    except ValueError:
        print("✗ Format tanggal salah! Gunakan DD-MM-YYYY")
        return
    if start_date > end_date:
        print("✗ Tanggal akhir harus setelah tanggal mulai.")
        return

    multi = len(tickers) > 1

    # ── Pilihan mode scraping ──────────────────────────────────
    print("\nMode scraping:")
    print("  [1] Turbo API  — paralel requests (sangat direkomendasikan)")
    print("  [2] Selenium UI — interaksi browser (lambat, tapi lebih aman)")
    mode_choice = input("Pilih (1/2, default 1): ").strip() or "1"
    use_api     = (mode_choice == "1")

    max_workers = 1
    if use_api and multi:
        w = input("Jumlah thread paralel (default 8, max 15): ").strip() or "8"
        max_workers = min(int(w), 15)

    start_label = start_str.replace("-", "")
    end_label   = end_str.replace("-", "")

    # ── Login ──────────────────────────────────────────────────
    scraper = NeoBDMBrokerScraper(username, password, headless=use_api)

    try:
        if not scraper.login():
            print("\nLogin otomatis gagal.")
            if input("Login manual? (y/n): ").strip().lower() == "y":
                scraper.manual_login_assist()
            else:
                return

        # ── Jalankan scraping ──────────────────────────────────
        if not multi:
            # Single ticker
            if not use_api and not scraper.navigate_to_broker_summary():
                print("✗ Gagal mengakses halaman broker summary.")
                return
            data = scraper.scrape_date_range(
                tickers[0], mode, filter_val, start_date, end_date, use_api=use_api
            )
            if any(rows for rows in data.values()):
                fp = scraper.save_to_excel(data, tickers[0], start_label, end_label)
                print(f"\n✓ Tersimpan: {fp}")
            else:
                print("✗ Tidak ada data yang berhasil diambil.")

        elif use_api:
            resume = input("\nResume dari ticker yang belum selesai? (y/n, default y): ").strip().lower() != "n"
            scraper.scrape_multiple_tickers_api(
                tickers, mode, filter_val, start_date, end_date,
                max_workers=max_workers,
                resume=resume,
                start_str=start_label,
                end_str=end_label,
            )
        else:
            resume = input("\nResume dari ticker yang belum selesai? (y/n, default y): ").strip().lower() != "n"
            if not scraper.navigate_to_broker_summary():
                print("✗ Gagal mengakses halaman broker summary.")
                return
            scraper.scrape_multiple_tickers_ui(
                tickers, mode, filter_val, start_date, end_date,
                resume=resume,
                start_str=start_label,
                end_str=end_label,
            )

    except KeyboardInterrupt:
        print("\n\nDihentikan. Progress tersimpan — jalankan ulang untuk resume.")
    finally:
        scraper.close()


if __name__ == "__main__":
    main()