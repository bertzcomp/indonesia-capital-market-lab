# Install dependency (hanya requests, tidak perlu playwright)
pip install requests

# Scrape semua pengumuman volatilitas transaksi
python idx_scraper_api.py --keyword volati --date-from 20260101 --delay 1.0

# Scrape + download PDF sekaligus
python idx_scraper_api.py --keyword volati --download-pdf --max-pdf 20

# Hanya dokumen utama (bukan lampiran), ambil 100 record
python idx_scraper_api.py --keyword volati --download-pdf --only-main --max-records 100

# Scrape semua jenis pengumuman (tanpa keyword)
python idx_scraper_api.py --date-from 20260401 --date-to 20260430