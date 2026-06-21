"""
NeoBDM Broker Summary Scraper
==============================
Solusi untuk Selectize dropdown:
  1. PRIMARY  → Selectize JS API  : element.selectize.setValue(ticker)
  2. FALLBACK → ActionChains      : simulasi klik + ketik + klik opsi
  3. TURBO    → Direct API        : requests + session cookies (tanpa UI, 10× lebih cepat)
"""

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
from threading import Lock, Event
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


class RateLimitError(Exception):
    """Raised ketika API mengembalikan 429 dan semua retry habis."""
    pass


class GlobalRateLimiter:
    """
    Serialisasi semua HTTP request dari semua thread.
    Request dikirim satu per satu dengan jeda minimum `min_interval` detik.
    Ini mencegah multiple thread memborbardir server secara bersamaan.
    """
    def __init__(self, min_interval: float = 1.5):
        self._lock        = Lock()
        self._last_req    = 0.0
        self.min_interval = min_interval

    def acquire(self):
        """Panggil ini SEBELUM setiap HTTP request."""
        with self._lock:
            now  = time.monotonic()
            wait = self.min_interval - (now - self._last_req)
            if wait > 0:
                time.sleep(wait)
            self._last_req = time.monotonic()

    def backoff(self, seconds: float):
        """Paksa semua thread berhenti selama `seconds` detik (setelah 429)."""
        with self._lock:
            print(f"  🛑 Global backoff {seconds}s — semua thread berhenti...")
            time.sleep(seconds)
            self._last_req = time.monotonic()


# Instance global — dibuat sekali, dipakai semua thread
_rate_limiter = GlobalRateLimiter(min_interval=1.5)


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

    #  MODE TURBO: Direct API (POST) — dengan GlobalRateLimiter
    def fetch_via_api(
        self,
        ticker: str,
        mode: str,
        filter_value: str,
        date_obj: datetime,
        _retry: int = 0,
    ) -> list[dict]:
        """
        POST ke /api/broker-summary.
        Setiap request melewati _rate_limiter.acquire() — semua thread antri,
        request dikirim satu per satu dengan jeda 1.5 detik.
        Ini mencegah 429 akibat concurrent requests.
        """
        if not self.session:
            return []

        date_str = date_obj.strftime("%d %b %Y")
        net_val  = "true" if mode.lower() == "net" else "false"
        fv       = filter_value.lower()
        csrf     = self.session.cookies.get("csrftoken", "")

        payload = {
            "csrfmiddlewaretoken":   csrf,
            "tick":                  ticker.upper(),
            "start_date":            date_str,
            "end_date":              date_str,
            "event":                 "load",
            "net":                   net_val,
            "foreign_only":          "true" if fv == "f" else "false",
            "domestic_only":         "true" if fv == "d" else "false",
            "show_broker_inventory": "false",
        }
        headers = {
            "X-CSRFToken":      csrf,
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type":     "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept":           "*/*",
            "Referer":          "https://neobdm.tech/broker_summary/",
        }

        MAX_RETRIES  = 5
        BACKOFF_SECS = [10, 20, 40, 60, 120]

        try:
            # ── Semua thread antri di sini ─────────────────────
            _rate_limiter.acquire()

            resp = self.session.post(
                "https://neobdm.tech/api/broker-summary",
                data=payload, headers=headers, timeout=20,
            )

            if resp.status_code == 429:
                if _retry < MAX_RETRIES:
                    wait = BACKOFF_SECS[_retry]
                    print(f"  ⏳ [{ticker}] 429, global backoff {wait}s (retry {_retry+1}/{MAX_RETRIES})")
                    _rate_limiter.backoff(wait)
                    return self.fetch_via_api(ticker, mode, filter_value, date_obj, _retry + 1)
                raise RateLimitError(f"{ticker}: rate limit setelah {MAX_RETRIES} retry")

            resp.raise_for_status()

            data = resp.json()
            rows = data if isinstance(data, list) else data.get("data", data.get("results", []))
            if rows:
                print(f"  ✓ {ticker} {date_str}: {len(rows)} baris")
            return rows

        except RateLimitError:
            raise
        except requests.HTTPError as e:
            print(f"  ✗ [{ticker}] HTTP {e.response.status_code}: {e.response.text[:80]}")
        except requests.ConnectionError:
            if _retry < 3:
                wait = BACKOFF_SECS[_retry]
                print(f"  ⏳ [{ticker}] Koneksi gagal, backoff {wait}s dan retry...")
                _rate_limiter.backoff(wait)
                return self.fetch_via_api(ticker, mode, filter_value, date_obj, _retry + 1)
            print(f"  ✗ [{ticker}] Koneksi gagal setelah retry")
        except json.JSONDecodeError:
            print(f"  ✗ [{ticker}] Respons bukan JSON")
        except Exception as e:
            print(f"  ✗ [{ticker}] error: {e}")
        return []

    def _fetch_via_api_json(self, *args, **kwargs) -> list[dict]:
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
    def sniff_real_request(self, ticker: str = "BBCA") -> dict:
        """
        Gunakan Chrome DevTools Protocol (CDP) untuk capture PERSIS apa yang
        dikirim browser ke /api/broker-summary saat klik Load.
        Jalankan ini sekali sebelum scraping massal untuk mengetahui
        method, headers, dan body yang benar.
        """
        print("\n" + "═" * 60)
        print("  SNIFF REAL REQUEST via CDP")
        print("═" * 60)

        captured = {}

        # ── Aktifkan CDP Network ───────────────────────────────
        self.driver.execute_cdp_cmd("Network.enable", {})

        # Inject JS untuk intercept XHR & fetch
        self.driver.execute_script("""
            window.__sniffed = null;

            // Intercept fetch()
            const _fetch = window.fetch;
            window.fetch = function(url, opts={}) {
                if (String(url).includes('broker-summary')) {
                    window.__sniffed = {
                        type: 'fetch', url: url,
                        method: opts.method || 'GET',
                        headers: JSON.stringify(opts.headers || {}),
                        body: opts.body ? String(opts.body) : null
                    };
                }
                return _fetch.apply(this, arguments);
            };

            // Intercept XMLHttpRequest
            const _open = XMLHttpRequest.prototype.open;
            const _send = XMLHttpRequest.prototype.send;
            const _setHdr = XMLHttpRequest.prototype.setRequestHeader;
            XMLHttpRequest.prototype.open = function(m, u) {
                this._sniff_url = u; this._sniff_method = m; this._sniff_hdrs = {};
                return _open.apply(this, arguments);
            };
            XMLHttpRequest.prototype.setRequestHeader = function(k, v) {
                if (this._sniff_hdrs) this._sniff_hdrs[k] = v;
                return _setHdr.apply(this, arguments);
            };
            XMLHttpRequest.prototype.send = function(body) {
                if (this._sniff_url && String(this._sniff_url).includes('broker-summary')) {
                    window.__sniffed = {
                        type: 'xhr', url: this._sniff_url,
                        method: this._sniff_method,
                        headers: JSON.stringify(this._sniff_hdrs || {}),
                        body: body ? String(body) : null
                    };
                }
                return _send.apply(this, arguments);
            };
        """)

        # Set form dan klik Load
        self.navigate_to_broker_summary()
        time.sleep(1)
        self.driver.execute_script("""
            window.__sniffed = null;  // reset setelah navigate
        """)
        # Re-inject setelah navigate (page reload)
        self.driver.execute_script("""
            window.__sniffed = null;
            const _fetch = window.fetch;
            window.fetch = function(url, opts={}) {
                if (String(url).includes('broker-summary')) {
                    window.__sniffed = {type:'fetch',url:url,method:opts.method||'GET',
                        headers:JSON.stringify(opts.headers||{}),body:opts.body?String(opts.body):null};
                }
                return _fetch.apply(this,arguments);
            };
            const _open=XMLHttpRequest.prototype.open,_send=XMLHttpRequest.prototype.send,
                  _sh=XMLHttpRequest.prototype.setRequestHeader;
            XMLHttpRequest.prototype.open=function(m,u){this._u=u;this._m=m;this._h={};return _open.apply(this,arguments);};
            XMLHttpRequest.prototype.setRequestHeader=function(k,v){if(this._h)this._h[k]=v;return _sh.apply(this,arguments);};
            XMLHttpRequest.prototype.send=function(b){
                if(this._u&&String(this._u).includes('broker-summary')){
                    window.__sniffed={type:'xhr',url:this._u,method:this._m,
                        headers:JSON.stringify(this._h||{}),body:b?String(b):null};
                }
                return _send.apply(this,arguments);
            };
        """)

        self.set_ticker(ticker)
        self.set_mode("net")
        self.set_filter("all")
        self.set_date(datetime.today())

        # Klik load (jangan pakai load_data karena itu tunggu DOM — kita perlu sniff dulu)
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.ID, "broksum-button-load")))
            btn.click()
        except Exception:
            pass
        time.sleep(2)

        result = self.driver.execute_script("return window.__sniffed;")

        if result:
            print(f"\n  ✓ REQUEST BERHASIL DI-INTERCEPT")
            print(f"  Type   : {result.get('type')}")
            print(f"  Method : {result.get('method')}")
            print(f"  URL    : {result.get('url')}")
            print(f"  Headers: {result.get('headers')}")
            print(f"  Body   : {result.get('body')}")
            captured = result
        else:
            # Fallback: ambil dari CDP performance log
            print("  ⚠ JS intercept gagal (mungkin full page form submit)")
            print("  → Mencoba baca dari CDP performance log...")
            try:
                logs = self.driver.execute_script(
                    "return window.performance.getEntriesByType('resource')"
                    ".filter(e => e.name.includes('broker-summary'))"
                    ".map(e => ({url: e.name, duration: e.duration}));"
                )
                if logs:
                    print(f"  Resource entries: {logs}")
            except Exception:
                pass
            print("\n  PETUNJUK MANUAL:")
            print("  1. Buka browser yang terbuka")
            print("  2. Tekan F12 → tab Network")
            print("  3. Filter: 'broker-summary'")
            print("  4. Klik Load di halaman")
            print("  5. Klik request → lihat 'Headers' dan 'Payload'")
            print("  6. Salin nama field dan nilainya ke sini")

        print("═" * 60 + "\n")
        return captured

    def _fetch_one(
        self,
        ticker: str,
        mode: str,
        filter_value: str,
        dates: list[datetime],
    ) -> dict[str, list[dict]]:
        """
        Worker untuk satu ticker — dipanggil dari thread pool.
        RateLimitError dibiarkan naik ke _process_ticker agar ticker
        TIDAK dicatat sebagai selesai di _progress.csv.
        """
        result: dict[str, list[dict]] = {}
        for date in dates:
            rows = self.fetch_via_api(ticker, mode, filter_value, date)
            result[date.strftime("%Y-%m-%d")] = rows or []
            # Tidak perlu sleep di sini — _rate_limiter.acquire() sudah menangani jeda
        return result

    def scrape_multiple_tickers_api(
        self,
        tickers: list[str],
        mode: str,
        filter_value: str,
        start_date: datetime,
        end_date: datetime,
        max_workers: int = 1,   # diabaikan — server tidak support concurrent
        resume: bool = True,
        start_str: str = "",
        end_str: str = "",
    ) -> None:
        """
        Scrape banyak ticker secara SEQUENTIAL via Turbo API.
        Threading dihapus — server konsisten menolak concurrent requests (429).
        Kecepatan: ~1.5 detik/ticker × 935 ticker ≈ 25 menit untuk 1 hari data.

        Output:
          broker_summary_data/
          └── {start_str}_to_{end_str}/
              ├── _progress.csv          ← daftar ticker selesai (untuk resume)
              └── broker_summary_TICKER_...xlsx
          └── MASTER_{start_str}_to_{end_str}.csv
        """
        dates       = self.generate_weekdays(start_date, end_date)
        subdir      = f"{start_str}_to_{end_str}"
        folder      = os.path.join(self.output_dir, subdir)
        done_file   = os.path.join(folder, "_progress.csv")
        master_file = os.path.join(self.output_dir, f"MASTER_{subdir}.csv")
        os.makedirs(folder, exist_ok=True)

        # ── Resume: skip ticker yang sudah selesai ─────────────
        done_set: set[str] = set()
        if resume and os.path.exists(done_file):
            with open(done_file, newline="") as f:
                done_set = {row[0] for row in csv.reader(f) if row}
            print(f"  ℹ Resume: {len(done_set)} ticker sudah selesai, di-skip")

        pending = [t for t in tickers if t not in done_set]
        total   = len(tickers)
        done_n  = len(done_set)

        print(f"\n{'='*60}")
        print(f"  MULTI-TICKER SCRAPING  (Turbo API Sequential)")
        print(f"  Total     : {total} ticker")
        print(f"  Pending   : {len(pending)} ticker")
        print(f"  Hari kerja: {len(dates)} hari")
        print(f"  Est. waktu: ~{len(pending) * len(dates) * 1.5 / 60:.0f} menit")
        print(f"  Output    : {folder}/")
        print(f"  Master    : {master_file}")
        print(f"{'='*60}\n")

        rate_limited = []
        failed       = []

        for ticker in pending:
            try:
                # Ambil semua tanggal untuk ticker ini
                data = self._fetch_one(ticker, mode, filter_value, dates)
                has_data = any(rows for rows in data.values())

                # Simpan Excel per-ticker
                self.save_to_excel(data, ticker, start_str, end_str, subdir=subdir)

                # Append ke master CSV
                if has_data:
                    master_rows = [
                        {"ticker": ticker, "date": date_str, **row}
                        for date_str, rows in data.items()
                        for row in rows
                    ]
                    df_chunk    = pd.DataFrame(master_rows)
                    write_hdr   = not os.path.exists(master_file)
                    df_chunk.to_csv(master_file, mode="a", header=write_hdr, index=False)

                # Progress & catat selesai
                done_n += 1
                pct  = done_n / total * 100
                icon = "✓" if has_data else "○"
                print(f"  {icon} [{done_n}/{total} | {pct:5.1f}%] {ticker}")
                with open(done_file, "a", newline="") as f:
                    csv.writer(f).writerow([ticker])

            except RateLimitError:
                done_n += 1
                pct = done_n / total * 100
                print(f"  ⚠ [{done_n}/{total} | {pct:5.1f}%] {ticker} — rate limit habis, skip")
                rate_limited.append(ticker)
                # TIDAK tulis ke done_file → akan di-retry saat resume

            except KeyboardInterrupt:
                print(f"\n  ⚠ Dihentikan saat {ticker}. Jalankan ulang untuk resume.")
                break

            except Exception as e:
                done_n += 1
                print(f"  ✗ [{ticker}] error: {e}")
                failed.append(ticker)

        print(f"\n{'='*60}")
        print(f"  SELESAI")
        print(f"  Sukses       : {len(pending) - len(failed) - len(rate_limited)} ticker")
        print(f"  Rate-limited : {len(rate_limited)} ticker (jalankan ulang → resume)")
        print(f"  Error lain   : {len(failed)} ticker{(' → ' + str(failed)) if failed else ''}")
        print(f"  Master CSV   : {master_file}")
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
ALL_TICKERS = [
    'AIMS', 'AISA', 'AKKU', 'AKPI', 'AKRA', 'AKSI', 'ALDO', 'ALII', 'ALKA', 'ALMI',
    'ALTO', 'AMAG', 'AMAN', 'AMAR', 'AMFG', 'AMIN', 'AMMN', 'AMMS', 'AMOR', 'AMRT',
    'ANDI', 'ANJT', 'ANTM', 'APEX', 'APIC', 'APII', 'APLI', 'APLN', 'ARCI', 'AREA',
    'ARGO', 'ARII', 'ARKA', 'ARKO', 'ARMY', 'ARNA', 'ARTA', 'ARTI', 'ARTO', 'ASBI',
    'ASDM', 'ASGR', 'ASHA', 'ASII', 'ASJT', 'ASLC', 'ASLI', 'ASMI', 'ASPI', 'ASPR',
    'ASRI', 'ASRM', 'ASSA', 'ATAP', 'ATIC', 'ATLA', 'AUTO', 'AVIA', 'AWAN', 'AXIO',
    'AYAM', 'AYLS', 'BABP', 'BABY', 'BACA', 'BAIK', 'BAJA', 'BALI', 'BANK', 'BAPA',
    'BAPI', 'BATA', 'BATR', 'BAUT', 'BAYU', 'BBCA', 'BBHI', 'BBKP', 'BBLD', 'BBMD',
    'BBNI', 'BBRI', 'BBRM', 'BBSI', 'BBSS', 'BBTN', 'BBYB', 'BCAP', 'BCIC', 'BCIP',
    'BDKR', 'BDMN', 'BEBS', 'BEEF', 'BEER', 'BEKS', 'BELI', 'BELL', 'BESS', 'BEST',
    'BFIN', 'BGTG', 'BHAT', 'BHIT', 'BIKA', 'BIKE', 'BIMA', 'BINA', 'BINO', 'BIPI',
    'BIPP', 'BIRD', 'BISI', 'BJBR', 'BJTM', 'BKDP', 'BKSL', 'BKSW', 'BLES', 'BLOG',
    'BLTA', 'BLTZ', 'BLUE', 'BMAS', 'BMBL', 'BMHS', 'BMRI', 'BMSR', 'BMTR', 'BNBA',
    'BNBR', 'BNGA', 'BNII', 'BNLI', 'BOAT', 'BOBA', 'BOGA', 'BOLA', 'BOLT', 'BOSS',
    'BPFI', 'BPII', 'BPTR', 'BRAM', 'BREN', 'BRIS', 'BRMS', 'BRNA', 'BRPT', 'BRRC',
    'BSBK', 'BSDE', 'BSIM', 'BSML', 'BSSR', 'BSWD', 'BTEK', 'BTEL', 'BTON', 'BTPN',
    'BTPS', 'BUAH', 'BUDI', 'BUKA', 'BUKK', 'BULL', 'BUMI', 'BUVA', 'BVIC', 'BWPT',
    'BYAN', 'CAKK', 'CAMP', 'CANI', 'CARE', 'CARS', 'CASA', 'CASH', 'CASS', 'CBDK',
    'CBMF', 'CBPE', 'CBRE', 'CBUT', 'CCSI', 'CDIA', 'CEKA', 'CENT', 'CFIN', 'CGAS',
    'CHEK', 'CHEM', 'CHIP', 'CINT', 'CITA', 'CITY', 'CLAY', 'CLEO', 'CLPI', 'CMNP',
    'CMNT', 'CMPP', 'CMRY', 'CNKO', 'CNMA', 'CNTX', 'COAL', 'COCO', 'COIN', 'COWL',
    'CPIN', 'CPRI', 'CPRO', 'CRAB', 'CRSN', 'CSAP', 'CSIS', 'CSMI', 'CSRA', 'CTBN',
    'CTRA', 'CTTH', 'CUAN', 'CYBR', 'DAAZ', 'DADA', 'DART', 'DATA', 'DAYA', 'DCII',
    'DEAL', 'DEFI', 'DEPO', 'DEWA', 'DEWI', 'DFAM', 'DGIK', 'DGNS', 'DGWG', 'DIGI',
    'DILD', 'DIVA', 'DKFT', 'DKHH', 'DLTA', 'DMAS', 'DMMX', 'DMND', 'DNAR', 'DNET',
    'DOID', 'DOOH', 'DOSS', 'DPNS', 'DPUM', 'DRMA', 'DSFI', 'DSNG', 'DSSA', 'DUCK',
    'DUTI', 'DVLA', 'DWGL', 'DYAN', 'EAST', 'ECII', 'EDGE', 'EKAD', 'ELIT', 'ELPI',
    'ELSA', 'ELTY', 'EMAS', 'EMDE', 'EMTK', 'ENAK', 'ENRG', 'ENVY', 'ENZO', 'EPAC',
    'EPMT', 'ERAA', 'ERAL', 'ERTX', 'ESIP', 'ESSA', 'ESTA', 'ESTI', 'ETWA', 'EURO',
    'EXCL', 'FAPA', 'FAST', 'FASW', 'FILM', 'FIMP', 'FIRE', 'FISH', 'FITT', 'FLMC',
    'FMII', 'FOLK', 'FOOD', 'FORE', 'FORU', 'FPNI', 'FUJI', 'FUTR', 'FWCT', 'GAMA',
    'GDST', 'GDYR', 'GEMA', 'GEMS', 'GGRM', 'GGRP', 'GHON', 'GIAA', 'GJTL', 'GLOB',
    'GLVA', 'GMFI', 'GMTD', 'GOLD', 'GOLF', 'GOLL', 'GOOD', 'GOTO', 'GPRA', 'GPSO',
    'GRIA', 'GRPH', 'GRPM', 'GSMF', 'GTBO', 'GTRA', 'GTSI', 'GULA', 'GUNA', 'GWSA',
    'GZCO', 'HADE', 'HAIS', 'HAJJ', 'HALO', 'HATM', 'HBAT', 'HDFA', 'HDIT', 'HEAL',
    'HELI', 'HERO', 'HEXA', 'HGII', 'HILL', 'HITS', 'HKMU', 'HMSP', 'HOKI', 'HOME',
    'HOMI', 'HOPE', 'HOTL', 'HRME', 'HRTA', 'HRUM', 'HUMI', 'HYGN', 'IATA', 'IBFN',
    'IBOS', 'IBST', 'ICBP', 'ICON', 'IDEA', 'IDPR', 'IFII', 'IFSH', 'IGAR', 'IIKP',
    'IKAI', 'IKAN', 'IKBI', 'IKPM', 'IMAS', 'IMJS', 'IMPC', 'INAF', 'INAI', 'INCF',
    'INCI', 'INCO', 'INDF', 'INDO', 'INDR', 'INDS', 'INDX', 'INDY', 'INET', 'INKP',
    'INOV', 'INPC', 'INPP', 'INPS', 'INRU', 'INTA', 'INTD', 'INTP', 'IOTF', 'IPAC',
    'IPCC', 'IPCM', 'IPOL', 'IPPE', 'IPTV', 'IRRA', 'IRSX', 'ISAP', 'ISAT', 'ISEA',
    'ISSP', 'ITIC', 'ITMA', 'ITMG', 'JARR', 'JAST', 'JATI', 'JAWA', 'JAYA', 'JECC',
    'JGLE', 'JIHD', 'JKON', 'JMAS', 'JPFA', 'JRPT', 'JSKY', 'JSMR', 'JSPT', 'JTPE',
    'KAEF', 'KAQI', 'KARW', 'KAYU', 'KBAG' ]


#  Main
def main():
    print("=" * 70)
    print("NEO BDM BROKER SUMMARY SCRAPER — MULTI-TICKER")
    print("=" * 70)

    username = os.getenv("NEOBDM_USERNAME") or input("Neo BDM username: ").strip()
    password = os.getenv("NEOBDM_PASSWORD") or input("Neo BDM password: ").strip()

    # ── Kumpulkan SEMUA parameter dulu sebelum buka browser ───
    print("\n" + "─" * 50)
    print("  PARAMETER SCRAPING")
    print("─" * 50)

    # Scope ticker
    print("\nScope ticker:")
    print("  [1] Satu ticker saja")
    print("  [2] Beberapa ticker (pisahkan koma, contoh: BBCA,BBRI,BMRI)")
    print(f"  [3] Semua ticker IDX ({len(ALL_TICKERS)} saham)")
    while True:
        scope = input("Pilih scope (1/2/3): ").strip()
        if scope in ("1", "2", "3"):
            break
        print("  ✗ Masukkan 1, 2, atau 3")

    if scope == "1":
        ticker_input = input("Ticker (contoh BBCA): ").strip().upper()
        if not ticker_input:
            print("✗ Ticker tidak boleh kosong")
            return
        tickers = [ticker_input]
    elif scope == "2":
        raw = input("Ticker (pisahkan koma, contoh BBCA,BBRI,BMRI): ").strip().upper()
        tickers = [t.strip() for t in raw.split(",") if t.strip()]
        if not tickers:
            print("✗ Tidak ada ticker valid.")
            return
        print(f"  → {len(tickers)} ticker: {tickers}")
    else:
        tickers = ALL_TICKERS
        print(f"  → Semua {len(tickers)} ticker IDX")

    mode       = (input("\nMode (Net/Val, default Net): ").strip() or "Net")
    filter_val = (input("Filter (All/F/D, default All): ").strip() or "All")
    start_str  = input("Start date (DD-MM-YYYY, contoh 07-03-2025): ").strip()
    end_str    = input("End date   (DD-MM-YYYY, contoh 07-03-2025): ").strip()

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

    # Mode scraping
    print("\nMode scraping:")
    print("  [1] Turbo API  — paralel requests (sangat direkomendasikan)")
    print("  [2] Selenium UI — interaksi browser (lambat, tapi lebih aman)")
    while True:
        mode_choice = input("Pilih mode (1/2, default 1): ").strip() or "1"
        if mode_choice in ("1", "2"):
            break
        print("  ✗ Masukkan 1 atau 2")
    use_api = (mode_choice == "1")

    max_workers = 1  # sequential — server tidak support concurrent requests

    start_label = start_str.replace("-", "")
    end_label   = end_str.replace("-", "")

    # ── Konfirmasi sebelum mulai ───────────────────────────────
    print("\n" + "─" * 50)
    print("  KONFIRMASI")
    print("─" * 50)
    print(f"  Ticker  : {tickers[0] if len(tickers)==1 else f'{len(tickers)} ticker'}")
    print(f"  Mode    : {mode} | Filter: {filter_val}")
    print(f"  Tanggal : {start_str} s/d {end_str}")
    print(f"  Scraping: {'Turbo API' if use_api else 'Selenium UI'}" +
          (f" ({max_workers} threads)" if use_api and multi else ""))
    confirm = input("\nLanjutkan? (y/n, default y): ").strip().lower()
    if confirm == "n":
        print("Dibatalkan.")
        return

    # ── Buka browser & login ───────────────────────────────────
    scraper = NeoBDMBrokerScraper(username, password, headless=use_api)

    try:
        if not scraper.login():
            print("\nLogin otomatis gagal.")
            if input("Login manual? (y/n): ").strip().lower() == "y":
                scraper.manual_login_assist()
            else:
                return

        # Opsional: sniff request sebelum scraping massal
        if use_api:
            do_sniff = input("\nJalankan sniffer dulu untuk cek format request? (y/n, default n): ").strip().lower()
            if do_sniff == "y":
                scraper.sniff_real_request("BBCA")
                confirm = input("Lanjut scraping? (y/n): ").strip().lower()
                if confirm != "y":
                    return

        # ── Jalankan scraping ──────────────────────────────────
        if not multi:
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

