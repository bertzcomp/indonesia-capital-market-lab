import pandas as pd
import numpy as np
import random
from datetime import timedelta

# Konfigurasi Random Seed untuk Reproducibility
np.random.seed(42)

def generate_synthetic_market_data(n_days=252, n_tickers=50, n_brokers=30):
    """
    Menghasilkan data transaksi broker sintetis yang meniru pola mikrostruktur IDX.
    
    Parameter:
    - n_days: Jumlah hari perdagangan (default 252 hari kerja / 1 tahun)
    - n_tickers: Jumlah saham emiten
    - n_brokers: Jumlah partisipan broker aktif
    
    Output:
    - DataFrame pandas dengan kolom: date, ticker, broker_id, volume_buy, volume_sell, value_buy, value_sell, type
    """
    
    # 1. Inisialisasi Dimensi Data
    dates = pd.date_range(start='2023-01-01', periods=n_days, freq='B')
    tickers =
    brokers =
    
    # Menetapkan Status Broker: Asing (F) atau Domestik (D)
    # Asumsi: 20% broker adalah broker asing institusional
    broker_types = {b: ('F' if i < n_brokers * 0.2 else 'D') for i, b in enumerate(brokers)}
    
    # Menetapkan "Bandar" Brokers: Broker yang memiliki kapasitas volume besar
    # Biasanya kode broker tertentu seperti YP, CC, PD sering diasosiasikan dengan ritel,
    # sementara broker seperti KZ, CS, AK diasosiasikan dengan institusi.
    bandar_brokers = brokers[:5] # 5 Broker pertama adalah Big Players
    
    data_list =
    
    print("Memulai simulasi data mikrostruktur pasar...")
    
    for date in dates:
        # Faktor Pasar Harian: Sentimen global yang mempengaruhi seluruh saham
        market_sentiment = np.random.normal(0, 1)
        
        for ticker in tickers:
            # Setiap saham memiliki 'hidden state' akumulasi/distribusi
            # State 1: Akumulasi, State -1: Distribusi, State 0: Netral
            stock_state = np.random.choice([1, -1, 0], p=[0.2, 0.2, 0.6])
            
            # Harga dasar saham (untuk perhitungan value)
            base_price = np.random.randint(500, 5000)
            
            for broker in brokers:
                is_bandar = broker in bandar_brokers
                is_foreign = broker_types[broker] == 'F'
                
                # Logika Volume Dasar: Distribusi Log-Normal (Fat-tail)
                base_vol = int(np.random.lognormal(mean=5, sigma=1.5)) * 100
                
                # Logika Bandarmology:
                # Jika fase Akumulasi (State 1), Bandar Beli Banyak, Jual Sedikit
                if stock_state == 1 and is_bandar:
                    vol_buy = base_vol * np.random.uniform(5, 10) # Beli agresif
                    vol_sell = base_vol * np.random.uniform(0.1, 0.5)
                # Jika fase Distribusi (State -1), Bandar Jual Banyak, Beli Sedikit
                elif stock_state == -1 and is_bandar:
                    vol_buy = base_vol * np.random.uniform(0.1, 0.5)
                    vol_sell = base_vol * np.random.uniform(5, 10) # Jual agresif
                else:
                    # Fase Netral atau Broker Ritel: Volume acak seimbang
                    vol_buy = base_vol * np.random.uniform(0.5, 1.5)
                    vol_sell = base_vol * np.random.uniform(0.5, 1.5)
                
                # Tambahkan noise pada harga transaksi
                avg_price = base_price + np.random.randint(-10, 10)
                
                data_list.append({
                    'date': date,
                    'ticker': ticker,
                    'broker_id': broker,
                    'volume_buy': int(vol_buy),
                    'volume_sell': int(vol_sell),
                    'value_buy': vol_buy * avg_price,
                    'value_sell': vol_sell * avg_price,
                    'broker_type': broker_types[broker]
                })
                
    df_raw = pd.DataFrame(data_list)
    print(f"Data berhasil dibangkitkan. Total baris: {len(df_raw)}")
    return df_raw

# Eksekusi Pembangkitan Data
df_broker_summary = generate_synthetic_market_data(n_days=100, n_tickers=20, n_brokers=15)

# Menampilkan sampel data
print("\nSampel Data Broker Summary Sintetis:")
print(df_broker_summary.head(10).to_markdown(index=False))