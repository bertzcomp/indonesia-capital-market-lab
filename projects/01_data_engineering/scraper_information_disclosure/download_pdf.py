# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()

#     page.goto("https://www.idx.co.id")
#     page.goto("https://www.idx.co.id/StaticData/NewsAndAnnouncement/ANNOUNCEMENTSTOCK/From_EREP/202602/76123c64df_f834484774.pdf")

#     page.wait_for_timeout(3000)

#     with open("pengumuman_idx.pdf", "wb") as f:
#         f.write(page.content().encode())

#     browser.close()




import os
import pandas as pd
from playwright.sync_api import sync_playwright
import time

def simple_downloader(csv_path, save_dir="pdf_idx", max_files=10, delay=1):
    """
    Downloader sederhana untuk testing
    """
    # Baca CSV
    df = pd.read_csv(csv_path)
    
    # Buat direktori
    os.makedirs(save_dir, exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        # Buka homepage
        print("🌐 Mendapatkan session...")
        page.goto("https://www.idx.co.id")
        time.sleep(2)
        
        success = 0
        fail = 0
        
        # Download file utama (maksimal max_files)
        for i in range(min(len(df), max_files)):
            row = df.iloc[i]
            url = row["LinkUtama"]
            
            if pd.isna(url):
                continue
            
            # Buat nama file
            kode = row["KodeEmiten"] if pd.notna(row["KodeEmiten"]) else f"file_{i}"
            tanggal = row["Tanggal"] if pd.notna(row["Tanggal"]) else ""
            filename = f"{kode}_{tanggal}_{i}.pdf"
            filepath = os.path.join(save_dir, filename)
            
            print(f"[{i+1}/{min(len(df), max_files)}] Download: {filename}")
            
            try:
                response = page.request.get(url, timeout=30000)
                
                if response.ok:
                    with open(filepath, "wb") as f:
                        f.write(response.body())
                    print(f"   ✅ OK")
                    success += 1
                else:
                    print(f"   ❌ HTTP {response.status}")
                    fail += 1
                    
            except Exception as e:
                print(f"   ❌ Error: {str(e)[:50]}")
                fail += 1
            
            # Delay
            if i < min(len(df), max_files) - 1:
                time.sleep(delay)
        
        browser.close()
        
        print(f"\n📊 Hasil: {success} berhasil, {fail} gagal")
        print(f"💾 File disimpan di: {os.path.abspath(save_dir)}")

# Jalankan untuk testing
if __name__ == "__main__":
    csv_path = "/Users/albert/Documents/Finances/projects/01_data_engineering/scraper_information_disclosure/data/idx_disclosures_20260210_231440.csv"
    simple_downloader(csv_path, max_files=5, delay=2)