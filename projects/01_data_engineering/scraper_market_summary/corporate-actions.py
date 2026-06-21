import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape_all_corporate_action(output_file="/Users/albert/Documents/Finances/data/raw/market_data/corporate_actions/all_corporate_action.csv", url=None):
    """
    Mengambil semua data corporate action dari halaman IDX tanpa filter.
    Hanya mengubah dropdown 'Rows' menjadi 'All' agar semua data tampil.
    """
    if url is None:
        url = "https://www.idx.co.id/en/listed-companies/corporate-actions/"

    # Inisialisasi driver Chrome (pastikan chromedriver tersedia di PATH)
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        print(f"Membuka halaman: {url}")
        driver.get(url)

        # Tunggu hingga tabel muncul
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.ID, "vgt-table")))
        print("Tabel ditemukan.")

        # Ubah dropdown "Rows" menjadi "All" (value="-1")
        try:
            rows_select = driver.find_element(By.CSS_SELECTOR, "select.footer__row-count__select")
            select = Select(rows_select)
            select.select_by_value("-1")  # Pilih opsi All
            print("Dropdown rows diubah ke 'All'.")
            time.sleep(3)  # Tunggu tabel refresh
        except Exception as e:
            print(f"Error saat mengubah dropdown: {e}")
            # Jika gagal, lanjutkan dengan jumlah baris default (misal 10)

        # Ambil HTML tabel
        table_element = driver.find_element(By.ID, "vgt-table")
        table_html = table_element.get_attribute("outerHTML")
        soup = BeautifulSoup(table_html, "html.parser")

        # Ekstrak data dari tbody
        all_data = []
        tbody = soup.find("tbody")
        if tbody:
            rows = tbody.find_all("tr", recursive=False)
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 5:
                    date = cols[0].get_text(strip=True)
                    emiten = cols[1].get_text(strip=True)
                    ca_type = cols[2].get_text(strip=True)
                    amount = cols[3].get_text(strip=True).replace(',', '')   # hapus koma jika ada
                    total = cols[4].get_text(strip=True).replace(',', '')
                    all_data.append([date, emiten, ca_type, amount, total])

        # Simpan ke CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Emiten Code", "Type of Corporate Action",
                             "Amount of Corporate Action", "Total Amount"])
            writer.writerows(all_data)

        print(f"\nScraping selesai! Total data: {len(all_data)} baris.")
        print(f"Data disimpan ke: {output_file}")

    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_all_corporate_action(output_file="/Users/albert/Documents/Finances/data/raw/market_data/corporate_actions/all_corporate_action_no_filter.csv")