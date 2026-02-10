import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import json
from datetime import datetime
import traceback
import os
from dotenv import load_dotenv

load_dotenv()

class NeoBDMScraper:
    def __init__(self, username, password, headless=False):
        """Inisialisasi scraper dengan kredensial login"""
        self.username = username
        self.password = password
        self.driver = None
        self.wait = None
        self.output_dir = "/Users/albert/Documents/Finances/data/raw/market_data/bandarmology/09_feb_2026"
        self.setup_driver(headless)
        
    def setup_driver(self, headless=False):
        """Setup Chrome driver"""
        chrome_options = Options()
        
        # Opsi untuk menghindari deteksi sebagai bot
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Opsi tambahan
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        # Mode headless 
        if headless:
            chrome_options.add_argument("--headless=new")
        
        # Disable images 
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        
        self.driver = webdriver.Chrome(options=chrome_options)
        
        # Execute JavaScript for hide automation
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        self.wait = WebDriverWait(self.driver, 20)
        print("Browser initialized successfully")
        
    def save_screenshot(self, filename):
        """Save as screenshot for debugging"""
        try:
            self.driver.save_screenshot(filename)
            print(f"Screenshot saved: {filename}")
        except:
            pass
        
    def login(self):
        """Login Neo BDM"""
        print("="*60)
        print("LOGIN PROCESS")
        print("="*60)
        
        try:
            # login
            login_url = "https://neobdm.tech/accounts/login/"
            print(f"Navigating to login page: {login_url}")
            self.driver.get(login_url)
            
            # load
            time.sleep(3)
            
            # Cari elemen login form
            print("Looking for login form elements...")
            
            # Tunggu sampai form login muncul
            try:
                self.wait.until(EC.presence_of_element_located((By.ID, "id_login")))
                print("✓ Found login form")
            except:
                # Coba selector alternatif
                try:
                    self.wait.until(EC.presence_of_element_located((By.NAME, "login")))
                    print("✓ Found login form (alternate selector)")
                except:
                    print("✗ Could not find login form")
                    return False
            
            # Isi username
            username_field = self.driver.find_element(By.ID, "id_login")
            username_field.clear()
            username_field.send_keys(self.username)
            print("✓ Username filled")
            
            # Isi password
            password_field = self.driver.find_element(By.ID, "id_password")
            password_field.clear()
            password_field.send_keys(self.password)
            print("✓ Password filled")
            
            # Cari dan klik tombol login
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button.primaryAction")
            login_button.click()
            print("✓ Login button clicked")
            
            # Tunggu proses login
            print("Waiting for login to complete...")
            time.sleep(5)
            
            # Cek apakah login berhasil
            current_url = self.driver.current_url
            
            # List kondisi sukses login
            success_conditions = [
                "/dashboard/" in current_url,
                "/screener/" in current_url,
                "login" not in current_url and "signin" not in current_url
            ]
            
            if any(success_conditions):
                print("✓ Login successful!")
                time.sleep(3)
                return True
            else:
                print("✗ Login may have failed - still on login page")
                return False
                
        except Exception as e:
            print(f"✗ Login error: {str(e)}")
            return False
    
    def navigate_to_screener(self):
        """Navigasi ke halaman screener"""
        print("\n" + "="*60)
        print("NAVIGATING TO SCREENER")
        print("="*60)
        
        max_attempts = 2
        for attempt in range(max_attempts):
            try:
                print(f"Attempt {attempt + 1}/{max_attempts}...")
                
                # Coba URL screener
                screener_url = "https://neobdm.tech/dashboard/screener/"
                print(f"Trying URL: {screener_url}")
                self.driver.get(screener_url)
                time.sleep(4)
                
                # Cek apakah kita berhasil mengakses halaman
                try:
                    # Tunggu dropdown preset muncul
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, "preset-dropdown-custom"))
                    )
                    print(f"✓ Successfully loaded screener page")
                    return True
                except:
                    print("  Screener elements not found")
                    continue
                    
            except Exception as e:
                print(f"Error in navigation attempt {attempt + 1}: {e}")
                time.sleep(2)
        
        print("✗ Failed to navigate to screener page after all attempts")
        return False
    
    def get_preset_options(self):
        """Ambil semua opsi preset yang tersedia"""
        try:
            dropdown = self.driver.find_element(By.ID, "preset-dropdown-custom")
            select = Select(dropdown)
            
            options = []
            for option in select.options:
                if option.get_attribute("disabled") is None and option.get_attribute("value"):
                    options.append({
                        "value": option.get_attribute("value"),
                        "text": option.text.strip()
                    })
            
            return options
            
        except Exception as e:
            print(f"Error getting preset options: {e}")
            return []
    
    def select_preset(self, preset_value):
        """Pilih preset berdasarkan value"""
        try:
            dropdown = self.driver.find_element(By.ID, "preset-dropdown-custom")
            select = Select(dropdown)
            
            # Pilih preset
            select.select_by_value(preset_value)
            
            # Tunggu data dimuat
            time.sleep(3)
            
            print(f"✓ Selected preset: {preset_value}")
            return True
                
        except Exception as e:
            print(f"Error selecting preset {preset_value}: {e}")
            return False
    
    def extract_table_data(self):
        """Ekstrak data dari tabel Tabulator"""
        data = []
        
        try:
            # Tunggu baris tabel muncul
            time.sleep(2)
            
            # Dapatkan semua baris
            rows = self.driver.find_elements(By.CSS_SELECTOR, "#table-custom .tabulator-row")
            
            if not rows:
                print("  No rows found in table")
                return data
            
            for i, row in enumerate(rows):
                try:
                    # Ekstrak data dari setiap kolom
                    tick_element = row.find_element(By.CSS_SELECTOR, '[tabulator-field="tick"] a')
                    tick = tick_element.text.strip()
                    
                    price_element = row.find_element(By.CSS_SELECTOR, '[tabulator-field="price"]')
                    price = price_element.text.strip().replace('.', '')
                    
                    chg_element = row.find_element(By.CSS_SELECTOR, '[tabulator-field="chg"] span')
                    chg = chg_element.text.strip()
                    
                    # Data history dari SVG
                    history_element = row.find_element(By.CSS_SELECTOR, '[tabulator-field="history"] .bar')
                    history_data = history_element.get_attribute("textContent")
                    
                    tx_element = row.find_element(By.CSS_SELECTOR, '[tabulator-field="tx"] span')
                    tx = tx_element.text.strip()
                    
                    # Tambahkan ke data
                    data.append({
                        "no": i + 1,
                        "tick": tick,
                        "price": price,
                        "chg": chg,
                        "history": history_data,
                        "tx": tx
                    })
                    
                except NoSuchElementException:
                    continue
                except Exception:
                    continue
            
            return data
            
        except Exception as e:
            print(f"Error extracting table data: {e}")
            return data
    
    def scrape_all_pages_dynamic(self, preset_value):
        """
        Scrape semua halaman hingga tombol Next dinonaktifkan
        """
        print(f"\nScraping data for preset: {preset_value}")
        
        # Pilih preset terlebih dahulu
        if not self.select_preset(preset_value):
            return []
        
        all_data = []
        current_page = 1
        
        try:
            while current_page <= 50:  # Safety limit
                print(f"\n--- Page {current_page} ---")
                
                # Ekstrak data dari halaman saat ini
                page_data = self.extract_table_data()
                
                if page_data:
                    all_data.extend(page_data)
                    print(f"✓ Extracted {len(page_data)} rows")
                    
                    # Cek tombol Next
                    try:
                        next_button = self.driver.find_element(
                            By.CSS_SELECTOR, 
                            '#table-custom-pagination .tabulator-page[data-page="next"]'
                        )
                        
                        # Cek apakah tombol Next dinonaktifkan
                        is_disabled = next_button.get_attribute("disabled") is not None or \
                                     "disabled" in next_button.get_attribute("class")
                        
                        if is_disabled:
                            print("✓ Reached last page (Next button disabled)")
                            break
                        else:
                            # Klik tombol Next
                            try:
                                next_button.click()
                                print("✓ Clicked Next button")
                                current_page += 1
                                time.sleep(3)
                            except:
                                # Coba dengan JavaScript click
                                self.driver.execute_script("arguments[0].click();", next_button)
                                print("✓ Clicked Next button (via JavaScript)")
                                current_page += 1
                                time.sleep(3)
                                
                    except NoSuchElementException:
                        print("✗ Next button not found, assuming last page")
                        break
                    except Exception as e:
                        print(f"✗ Error with Next button: {e}")
                        break
                else:
                    print("✗ No data on current page, stopping...")
                    break
            
            print(f"\n✓ Total scraped: {len(all_data)} rows from {current_page} pages")
            return all_data
            
        except Exception as e:
            print(f"✗ Error in dynamic scraping: {e}")
            return all_data
    
    def create_output_dir(self):
        """Buat directory untuk output jika belum ada"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            print(f"Created output directory: {self.output_dir}")
    
    def save_to_csv(self, data, filename):
        """Simpan data ke CSV di output directory"""
        self.create_output_dir()
        
        # Full path untuk file
        filepath = os.path.join(self.output_dir, filename)
        
        try:
            df = pd.DataFrame(data)
            df.to_csv(filepath, index=False, encoding='utf-8')
            print(f"✓ Data saved to: {filepath}")
            return True
        except Exception as e:
            print(f"✗ Error saving to CSV: {e}")
            return False
    
    def save_to_excel(self, data_dict, filename):
        """Simpan semua data ke satu file Excel dengan sheet berbeda"""
        self.create_output_dir()
        
        # Full path untuk file
        filepath = os.path.join(self.output_dir, filename)
        
        try:
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                for preset_name, data in data_dict.items():
                    if data:  # Hanya simpan jika ada data
                        df = pd.DataFrame(data)
                        # Buat sheet name yang valid (max 31 karakter, tidak ada karakter khusus)
                        sheet_name = preset_name[:31].replace('/', '_').replace('\\', '_').replace('*', '_').replace('?', '_').replace(':', '_').replace('[', '_').replace(']', '_')
                        df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            print(f"✓ All data saved to Excel: {filepath}")
            return True
        except Exception as e:
            print(f"✗ Error saving to Excel: {e}")
            return False
    
    def scrape_single_preset(self, preset_value, preset_name):
        """Scrape satu preset saja dan simpan ke CSV"""
        print(f"\n{'='*60}")
        print(f"Processing: {preset_name} ({preset_value})")
        print(f"{'='*60}")
        
        # Scrape data dengan pagination dinamis
        preset_data = self.scrape_all_pages_dynamic(preset_value)
        
        if preset_data:
            # Simpan ke CSV
            csv_filename = f"{preset_value}.csv"
            self.save_to_csv(preset_data, csv_filename)
            return preset_data
        else:
            print(f"✗ No data scraped for {preset_name}")
            return []
    
    def scrape_all_presets(self):
        """Scrape data dari semua preset dan simpan ke satu file Excel"""
        print("\n" + "="*60)
        print("STARTING FULL SCRAPING PROCESS")
        print("="*60)
        
        # Pastikan sudah di halaman screener
        if not self.navigate_to_screener():
            print("✗ Cannot proceed without screener access")
            return {}
        
        # Dapatkan semua opsi preset
        presets = self.get_preset_options()
        
        if not presets:
            print("✗ No presets found!")
            return {}
        
        print(f"\nFound {len(presets)} preset options:")
        for i, preset in enumerate(presets, 1):
            print(f"  {i}. {preset['text']} ({preset['value']})")
        
        all_data = {}
        
        # Scrape setiap preset
        for preset in presets:
            preset_value = preset['value']
            preset_name = preset['text']
            
            if preset_value:
                preset_data = self.scrape_single_preset(preset_value, preset_name)
                if preset_data:
                    all_data[preset_name] = preset_data
                
                # Tunggu sebelum preset berikutnya (jika bukan yang terakhir)
                if preset != presets[-1]:
                    print("\nWaiting 3 seconds before next preset...")
                    time.sleep(3)
        
        # Simpan semua data ke satu file Excel
        if all_data:
            excel_filename = "neobdm_all_data.xlsx"
            self.save_to_excel(all_data, excel_filename)
        
        return all_data
    
    def close(self):
        """Tutup browser dengan aman"""
        if self.driver:
            try:
                self.driver.quit()
                print("\n✓ Browser closed successfully")
            except:
                print("\n✗ Error closing browser")


# FUNGSI UTAMA
def main():
    """Fungsi utama untuk menjalankan scraper"""
    print("="*70)
    print("NEO BDM SCREENER SCRAPER")
    print("="*70)
    
    # Konfigurasi
    USERNAME = os.getenv(USERNAME)
    PASSWORD = os.getenv(PASSWORD)
    
    # Inisialisasi scraper
    print("\n" + "="*60)
    print("INITIALIZING SCRAPER...")
    scraper = NeoBDMScraper(USERNAME, PASSWORD)
    
    try:
        # Step 1: Login
        login_success = scraper.login()
        
        if not login_success:
            print("\n✗ Login failed. Exiting...")
            return
        
        # Step 2: Navigasi ke screener
        print("\n" + "="*60)
        print("ACCESSING SCREENER PAGE...")
        
        if not scraper.navigate_to_screener():
            print("\n✗ Failed to access screener page")
            return
        
        # Step 3: Pilih mode scraping
        print("\nScraping options:")
        print("1. Scrape ALL presets (save to one Excel file)")
        print("2. Scrape ONE specific preset (save to CSV)")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "1":
            # Scrape semua preset
            results = scraper.scrape_all_presets()
            
            if results:
                print("\n" + "="*60)
                print("SCRAPING COMPLETED SUCCESSFULLY!")
                print("="*60)
                print(f"✓ All data saved in 'neobdm_data' folder")
                print(f"✓ Main file: neobdm_all_data.xlsx")
                print(f"✓ Individual CSV files for each preset")
                print(f"✓ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print("\n✗ No data was scraped")
                
        elif choice == "2":
            # Pilih preset tertentu
            presets = scraper.get_preset_options()
            
            if not presets:
                print("✗ No presets available")
                return
            
            print("\nAvailable presets:")
            for i, preset in enumerate(presets, 1):
                print(f"{i}. {preset['text']} ({preset['value']})")
            
            try:
                preset_choice = int(input("\nSelect preset number: ").strip())
                if 1 <= preset_choice <= len(presets):
                    selected_preset = presets[preset_choice - 1]
                    print(f"\nSelected: {selected_preset['text']}")
                    
                    # Scrape hanya preset ini
                    preset_data = scraper.scrape_single_preset(
                        selected_preset['value'], 
                        selected_preset['text']
                    )
                    
                    if preset_data:
                        print("\n" + "="*60)
                        print("SCRAPING COMPLETED SUCCESSFULLY!")
                        print("="*60)
                        print(f"✓ Data saved in 'neobdm_data' folder")
                        print(f"✓ File: {selected_preset['value']}.csv")
                        print(f"✓ Total rows: {len(preset_data)}")
                        print(f"✓ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    else:
                        print(f"✗ No data scraped for {selected_preset['text']}")
                else:
                    print("✗ Invalid choice")
            except ValueError:
                print("✗ Please enter a valid number")
        else:
            print("✗ Invalid choice")
        
        print("\n" + "="*60)
        print("PROCESS COMPLETED")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Process interrupted by user")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        traceback.print_exc()
    finally:
        # Step 5: Tutup browser
        keep_open = input("\nKeep browser open? (y/n, default=n): ").strip().lower()
        if keep_open != 'y':
            scraper.close()


if __name__ == "__main__":
    main()