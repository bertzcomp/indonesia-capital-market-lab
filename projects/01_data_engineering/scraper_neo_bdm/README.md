# Neo BDM Screener Data Scraper

Web scraper otomatis untuk mengumpulkan data dari Neo BDM Screener menggunakan Selenium dan Python. Scraper ini dapat login ke akun Neo BDM, menavigasi ke halaman screener, dan mengumpulkan data dari berbagai preset yang tersedia.

## Fitur Utama

- **Login Otomatis**: Masuk ke akun Neo BDM menggunakan kredensial yang diberikan.
- **Multi-Preset Support**: Mendukung semua 6 preset yang tersedia:
  - Top Akum Bandarmologi (Harian dan 5 Hari)
  - Top Akum NonRetail (Harian dan 5 Hari)
  - Top Akum Foreign (Harian dan 5 Hari)
- **Pagination Dinamis**: Scraper secara otomatis mendeteksi dan menavigasi melalui semua halaman hingga data habis.
- **Multi-Format Output**: Menyimpan data dalam format CSV dan Excel.
- **User-Friendly Interface**: Menu interaktif di konsol untuk memilih preset dan mode scraping.
- **Error Handling**: Dilengkapi dengan penanganan error dan mekanisme retry.
- **Screenshot Debugging**: Menyimpan screenshot untuk debugging jika terjadi error.


## Prasyarat
1. **Python 3.7 atau lebih baru**
2. **Google Chrome Browser** (versi terbaru disarankan)
3. **ChromeDriver** (akan diunduh otomatis oleh webdriver-manager)


## Instalasi
1. Clone repository ini atau salin kode ke direktori lokal Anda.
2. Buat virtual environment (opsional namun disarankan):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   venv\Scripts\activate     # Untuk Windows
   ```
3. Install dependencies:
    ```bash
    pip install selenium pandas openpyxl webdriver-manager
    ```

## Penggunaan
1. Jalankan script:
    ```bash
    python neobdm_scraper.py
    ```
2. Masukkan username dan password Neo BDM.
    ```bash
    # Konfigurasi
    USERNAME = ""
    PASSWORD = ""
    ```

2. Pilih mode scraping:
    - Mode 1: Scrape semua preset (akan menyimpan data ke file Excel dan CSV individual untuk setiap preset).
    - Mode 2: Scrape satu preset tertentu (hanya menyimpan data untuk preset yang dipilih dalam format CSV).

3. Hasil scraping akan disimpan dalam folder neobdm_data/.


## Struktur Output
Setelah proses scraping selesai, data akan disimpan dalam folder neobdm_data/ dengan struktur sebagai berikut:

```bash
neobdm_data/
├── neobdm_all_data.xlsx       # File Excel berisi semua preset (jika memilih Mode 1)
├── neobdm-m-d.csv             # Data untuk preset Top Akum Bandarmologi (Harian)
├── neobdm-nr-d.csv            # Data untuk preset Top Akum NonRetail (Harian)
├── neobdm-f-d.csv             # Data untuk preset Top Akum Foreign (Harian)
├── neobdm-m-w.csv             # Data untuk preset Top Akum Bandarmologi 5 Hari
├── neobdm-nr-w.csv            # Data untuk preset Top Akum NonRetail 5 Hari
└── neobdm-f-w.csv             # Data untuk preset Top Akum Foreign 5 Hari
```

Setiap file CSV/Excel berisi kolom berikut:
    - no: Nomor urut.
    - tick: Kode saham (ticker).
    - price: Harga saham.
    - chg: Persentase perubahan (5 hari).
    - history: Data historis dalam format string (dipisahkan koma).
    - tx: Persentase transaksi (5 hari).

## Konfigurasi
Anda dapat mengubah beberapa konfigurasi dengan mengedit kode langsung:
    - Headless Mode: Untuk menjalankan tanpa GUI, ubah parameter headless=False menjadi True saat inisialisasi scraper.
    - Waktu Tunggu: Jika halaman lambat, Anda dapat menambah waktu tunggu di berbagai tempat (parameter time.sleep()).

## Troubleshooting
#### 1. Login Gagal

    - Pastikan username dan password benar.
    - Cek koneksi internet.
    - Jika ada CAPTCHA, gunakan opsi login manual.

#### 2. ChromeDriver Error
    - Pastikan Google Chrome sudah terinstall dan up-to-date.
    - Script menggunakan webdriver-manager yang seharusnya dapat mengunduh driver yang sesuai. Jika masih error, unduh manual dari ChromeDriver dan letakkan di PATH.

#### 3. Element Tidak Ditemukan
    - Halaman Neo BDM mungkin telah diubah. Periksa screenshot yang disimpan (jika ada) dan sesuaikan selector di kode.

#### 4. Slow Performance
    - Nonaktifkan mode headless untuk debugging.
    - Tingkatkan waktu tunggu (timeout) di kode.

## Disclaimer!
Alat ini hanya untuk tujuan edukasi dan penelitian. Pengguna bertanggung jawab penuh atas penggunaan alat ini. Pastikan Anda mematuhi syarat dan ketentuan Neo BDM.