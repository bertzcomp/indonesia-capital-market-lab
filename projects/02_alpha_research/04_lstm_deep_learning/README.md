News2Price Pipeline (Indonesia)

Pipeline untuk memprediksi dampak berita terhadap harga saham Indonesia:
- IndoBERT embedding
- Abnormal return vs IHSG
- Hybrid model (text + price)
- Backtest dasar + cost-aware

Quickstart:
1. Masukkan data ke folder `data/`
2. Install dependencies:
   pip install -r requirements.txt
3. Jalankan pipeline:
   python3 src/run_pipeline.py \
     --news data/news.json \
     --stock data/stock_ohlcv.csv \
     --ihsg data/ihsg_ohlcv.csv \
     --out results/

Catatan:
- Model IndoBERT akan di-download otomatis saat pertama kali jalan
- Gunakan --no-emb jika ingin disable embedding (fallback lexicon)
