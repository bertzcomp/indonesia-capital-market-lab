# Strategy Trading in IDX (Tape Reading)

## 1. Mengecek Daftar Antrian Order (Bid & Offer)

### Bid / Offer Anomaly Detection
- Perhatikan bid atau offer yang kopong / tipis.
- Jika ada 1 anomali di ask/offer misal 205, dimana lot yang diinginkan sangat besar dibanding order lain → indikasi manipulasi psikologis.
- Jika terdapat lebih dari 1 bid/offer, periksa apakah ada “ganjalan” yang sengaja dibuat untuk membuat bid terlihat ramai → tujuan: memancing ritel agar ikut beli.

#### Contoh Visual Anomali di Bid

| lot    | bid | offer | lot     |
|--------|-----|-------|---------|
| 57,000 | 86  | 87    | 25,000  ← bid besar (may be manipulated) |
| 7,000  | 87  | 88    | 1,500   |

- Jika ada 1 order 30,000 → bid asli = 57,000 - 30,000 = 27,000
- Sisanya → bisa jadi psikologi MM untuk menampilkan likuiditas palsu.

---

## 2. Mengecek Likuiditas

### Real Bid-Offer
- Perhatikan siapa yang mendominasi (misal 1 broker besar)
- Bisa jadi crossing internal, mereka menukar saham antar akun → terlihat aktif tapi bukan market driven.

#### Contoh
- Top Buy CC NV 1T → jika majority dia yang menempel di top sell offer, bisa jadi lempar-lempar barang untuk akumulasi/distribusi.

---

## 3. Analisis Bid

### Poin Penting
1. **Bid tebal belum tentu bagus**
    - Pastikan order list/antrian valid
    - Contoh: bid 86 dengan total 57,000 lot
        - Jika 1 order anomali 30,000 lot → bid asli = 27,000 lot
        - MM bisa membuat bid terlihat ramai → menipu ritel agar HAKA
2. **Cek bid lainnya**
    - Misal bid 87 = 12,000 lot
    - Ada 1 order 7,000 lot → ganjalan, bid palsu
    - Tujuan: buat terlihat likuid, ritel ikut beli → MM akumulasi

#### Visualisasi Bid Palsu

| lot    | bid | offer | lot     |
|--------|-----|-------|---------|
| 57,000 | 86  | 87    | 25,000  |
| 12,000 | 87  | 88    | 1,500   |
| 7,000  | 87  | 88    | 0 ← ganjalan / anomaly |

- **Kesimpulan:** MM manipulasi psikologi ritel

---

## 4. Analisis Offer

### Offer Tebal
- Bisa strategi psikologi MM untuk menahan harga → “belum izinkan naik”.
- Ciri:
    - 1 offer tebal (misal 108 = 98,000 lot)
    - Order lainnya tipis
    - Bid tipis / kecil (2–3x lebih kecil dari offer)
    - Meski tebal, tidak diguyur → tidak ada penjualan nyata

#### Visual Offer Tebal Palsu

| lot  | bid  | offer | lot      |
|------|------|-------|----------|
| 500  | 105  | 106   | 600      |
| 700  | 104  | 107   | 1,200    |
| 300  | 103  | 108   | 98,000 ← offer tebal, psikologi |
| 200  | 102  | 109   | 900      |

- Tujuan: mengintimidasi ritel agar tidak HAKA, sembari MM akumulasi di bawah.

---

## 5. Broker Summary (BROKSUM)

### Perhatikan Aktivitas Broker Major
- Contoh:
    - CP beli 24,000 → jual 22,800 → kemungkinan crossing internal
    - Periksa broker lain (YP, ZP) untuk melihat pola yang sama
    - Jika masih sama → hindari → indikasi pseudo-liquidity

#### Contoh Tabel Net Buy / Sell Broker

| NBY | NBLot  | NBVal   | # | NSL | NSLot  | NSVal  |
|-----|--------|---------|---|-----|--------|--------|
| II  | 60.5 M | 1461 B  | 1 | FS  | -21.4 M | -534 B |
| HP  | 4.1 M  | 95.7 B  | 2 | HD  | -16.2 M | -392 B |
| RO  | 8.5 M  | 8.5 B   | 3 | AN  | -13.4 M | -328 B |

- II terlihat akumulasi → tapi kemungkinan hanya tukeran barang antar broker
- Tujuan: tampak likuid padahal sebenarnya crossing.

---

## 6. Kesimpulan Tape Reading di IDX
1. Bid tebal belum tentu bagus → cek validitas order & anomalies
2. Offer tebal belum tentu jelek → bisa psikologi MM untuk menahan harga
3. Bid tipis + offer tebal → bisa jebakan psikologi untuk HAKA
4. Running trade & reaksi harga = indikator paling jujur
5. Perhatikan broker summary → indikasi crossing atau manipulasi

---

## Contoh Visual “Bid Tebal Palsu vs Offer Tebal Palsu”

### STEP 1 — Bid Tebal Palsu

| lot    | bid | offer | lot     |
|--------|-----|-------|---------|
| 57,000 | 86  | 87    | 25,000  |
| 12,000 | 87  | 88    | 1,500   |
| 7,000  | 87  | 88    | 0 ← anomaly / ganjalan |

### STEP 2 — Offer Tebal Palsu (Psikologi)

| lot  | bid  | offer | lot      |
|------|------|-------|----------|
| 500  | 105  | 106   | 600      |
| 700  | 104  | 107   | 1,200    |
| 300  | 103  | 108   | 98,000 ← MM nahan harga |
| 200  | 102  | 109   | 900      |

### STEP 3 — Running Trade & Reaksi Harga
- Bid mulai naik → harga bertahan → sinyal akumulasi valid
- Bid tetap tipis + offer tebal → jangan HAKA
