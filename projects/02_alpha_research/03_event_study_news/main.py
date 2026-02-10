import re
import json
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import warnings

# Mengabaikan pesan warning agar output bersih
warnings.filterwarnings('ignore')

def run_news_probability_analysis(news_file, price_file):
    print("Memuat data berita dan harga saham...")
    with open(news_file, 'r', encoding='utf-8') as f:
        news_data = json.load(f)

    news_df = pd.DataFrame(news_data)
    news_df['date'] = pd.to_datetime(news_df['date'])

    price_df = pd.read_csv(price_file)

    # Membersihkan nama kolom (menghapus tanda < >)
    price_df.columns = [col.replace('<', '').replace('>', '').lower() for col in price_df.columns]
    price_df['date'] = pd.to_datetime(price_df['date'])
    price_df = price_df.sort_values('date')

    # EKSTRAKSI SENTIMEN (NLP Lexicon Sederhana)
    print("2. Menghitung skor sentimen berita (NLP)...")
    
    # Kamus kata keuangan Bahasa Indonesia
    positive_words = ['akuisisi', 'laba', 'naik', 'beli', 'untung', 'tinggi', 'borong', 'target', 'potensi', 'penguatan', 'bullish', 'positif', 'masuk', 'dorong', 'rampungkan', 'optimis', 'akumulasi']
    negative_words = ['rugi', 'turun', 'jual', 'tekanan', 'lepas', 'gagal', 'anjlok', 'rendah', 'koreksi', 'bearish', 'negatif', 'keluar', 'beban', 'utang']

    def get_sentiment(text):
        text = text.lower()
        pos_count = sum(len(re.findall(r'\b' + word + r'\b', text)) for word in positive_words)
        neg_count = sum(len(re.findall(r'\b' + word + r'\b', text)) for word in negative_words)
        total = pos_count + neg_count
        if total == 0: return 0
        return (pos_count - neg_count) / total # Skala -1.0 sampai 1.0

    news_df['sentiment_score'] = news_df['full_content'].apply(get_sentiment)

    # FINANCIAL FEATURE ENGINEERING & LAG EFFECT
    print("3. Menghitung efek tertunda (Lag Effect) harga saham...")
    
    # Hitung Return Harian
    price_df['prev_close'] = price_df['close'].shift(1)
    
    # Melihat masa depan: Harga penutupan 1, 2, dan 3 hari ke depan
    price_df['future_close_1'] = price_df['close'].shift(-1)
    price_df['future_close_2'] = price_df['close'].shift(-2)
    price_df['future_close_3'] = price_df['close'].shift(-3)

    # Mencari harga TERTINGGI dalam 3 hari ke depan pasca berita rilis
    price_df['max_future_close'] = price_df[['future_close_1', 'future_close_2', 'future_close_3']].max(axis=1)
    
    # Menghitung potensi keuntungan maksimal (Max Future Return)
    price_df['max_future_return'] = (price_df['max_future_close'] - price_df['close']) / price_df['close']

    # TARGET VARIABEL (Y): 1 jika harga naik > 1% dalam 3 hari ke depan, 0 jika tidak.
    price_df['target_up'] = (price_df['max_future_return'] > 0.01).astype(int)

    # DATA ALIGNMENT (Penggabungan Data)
    print("4. Menggabungkan data (menyelaraskan berita akhir pekan dengan hari bursa)...")
    
    # Gabung berdasarkan tanggal. 
    merged_df = pd.merge(news_df, price_df, on='date', how='left')
    merged_df = merged_df.sort_values('date')
    
    # Jika berita muncul hari Sabtu/Minggu (NaN pada price_df), 
    # kita tarik data hari Senin (Backward Fill)
    merged_df['target_up'] = merged_df['target_up'].bfill()
    merged_df['volume'] = merged_df['volume'].bfill()
    merged_df['max_future_return'] = merged_df['max_future_return'].bfill()

    # Buang data yang tidak punya pasangan harga (ujung akhir dataset)
    train_df = merged_df.dropna(subset=['target_up', 'volume']).copy()

    # MACHINE LEARNING (Probabilistic Scoring)
    print("5. Melatih model Machine Learning (Random Forest)...")
    
    # Normalisasi Volume Transaksi
    scaler = MinMaxScaler()
    train_df['vol_norm'] = scaler.fit_transform(train_df[['volume']])

    # Fitur (X) dan Target (Y)
    X = train_df[['sentiment_score', 'vol_norm']]
    y = train_df['target_up']

    # Menggunakan Random Forest untuk mendapatkan Probabilitas
    clf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=4)
    clf.fit(X, y)

    # MENGHASILKAN SCORE PROBABILITAS
    # [:, 1] mengambil kolom probabilitas kelas "1" (Saham Naik)
    train_df['probabilitas'] = clf.predict_proba(X)[:, 1] 

    # FORMAT OUTPUT AKHIR
    print("6. Menyusun laporan akhir...\n")
    
    output_df = train_df[['date', 'title', 'sentiment_score', 'max_future_return', 'probabilitas']].copy()
    
    # Merapikan tampilan angka
    output_df['Probabilitas (%)'] = (output_df['probabilitas'] * 100).round(2)
    output_df['Skor Sentimen'] = output_df['sentiment_score'].round(2)
    output_df['Potensi Cuan (Lag 1-3 Hari) %'] = (output_df['max_future_return'] * 100).round(2)
    
    # Memilih kolom untuk ditampilkan
    final_table = output_df[['date', 'title', 'Skor Sentimen', 'Potensi Cuan (Lag 1-3 Hari) %', 'Probabilitas (%)']]
    final_table.columns = ['Tanggal', 'Judul Berita', 'Sentimen', 'Potensi Kenaikan Max (%)', 'Probability Score (%)']

    # Tampilkan di Terminal
    pd.set_option('display.max_colwidth', None)
    print(final_table.to_string(index=False))

    # Simpan ke CSV
    output_filename = 'data/output/Hasil_Analisis_Berita_BUMI.csv'
    final_table.to_csv(output_filename, index=False)
    print(f"\n✅ Selesai! Data berhasil disimpan ke dalam file: {output_filename}")

    return final_table


if __name__ == "__main__":
    FILE_BERITA = 'data/news/filtered_BUMI_oct_nov_2025.json'
    FILE_HARGA = 'data/ohlcv/BUMI_daily_oct_nov_2025_ohlcv.csv'
    
    try:
        hasil = run_news_probability_analysis(FILE_BERITA, FILE_HARGA)
    except FileNotFoundError as e:
        print(f"Error: File tidak ditemukan. Pastikan nama file sudah benar. Detail: {e}")