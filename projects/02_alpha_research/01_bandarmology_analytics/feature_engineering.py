def calculate_hhi(series):
    """Fungsi bantuan untuk menghitung HHI dari series pangsa pasar"""
    return (series ** 2).sum()

def feature_engineering_bandarmology(df_raw):
    print("Memulai Feature Engineering Bandarmology...")
    
    # 1. Hitung Total Volume Harian per Ticker
    daily_totals = df_raw.groupby(['date', 'ticker'])[['volume_buy', 'volume_sell']].sum().reset_index()
    daily_totals.rename(columns={'volume_buy': 'total_vol_buy', 'volume_sell': 'total_vol_sell'}, inplace=True)
    
    # Merge kembali ke data level broker untuk menghitung market share
    df_merged = pd.merge(df_raw, daily_totals, on=['date', 'ticker'])
    
    # 2. Hitung Market Share setiap broker
    df_merged['share_buy'] = df_merged['volume_buy'] / df_merged['total_vol_buy']
    df_merged['share_sell'] = df_merged['volume_sell'] / df_merged['total_vol_sell']
    
    # 3. Hitung HHI per Ticker per Hari
    # Kita menggunakan groupby apply untuk HHI
    hhi_features = df_merged.groupby(['date', 'ticker']).apply(
        lambda x: pd.Series({
            'hhi_buy': calculate_hhi(x['share_buy']),
            'hhi_sell': calculate_hhi(x['share_sell']),
            'total_volume': x['volume_buy'].sum() # Total turnover volume
        })
    ).reset_index()
    
    # 4. Hitung Fitur Foreign Flow
    # Filter hanya broker asing
    df_foreign = df_merged[df_merged['broker_type'] == 'F'].copy()
    df_foreign['net_vol_foreign'] = df_foreign['volume_buy'] - df_foreign['volume_sell']
    
    foreign_features = df_foreign.groupby(['date', 'ticker'])['net_vol_foreign'].sum().reset_index()
    
    # 5. Gabungkan semua fitur
    df_features = pd.merge(hhi_features, foreign_features, on=['date', 'ticker'], how='left')
    df_features['net_vol_foreign'] = df_features['net_vol_foreign'].fillna(0)
    
    # Normalisasi Foreign Flow
    df_features['foreign_flow_ratio'] = df_features['net_vol_foreign'] / df_features['total_volume']
    
    # Fitur Derivatif: HHI Spread
    df_features['hhi_spread'] = df_features['hhi_buy'] - df_features['hhi_sell']
    
    # Harga Penutupan (Approximation using VWAP from raw data)
    # VWAP = Total Value / Total Volume
    daily_values = df_raw.groupby(['date', 'ticker'])[['value_buy', 'volume_buy']].sum().reset_index()
    daily_values['vwap'] = daily_values['value_buy'] / daily_values['volume_buy']
    
    df_features = pd.merge(df_features, daily_values[['date', 'ticker', 'vwap']], on=['date', 'ticker'])
    
    return df_features

# Eksekusi Feature Engineering
df_model_ready = feature_engineering_bandarmology(df_broker_summary)

print("\nFitur Bandarmology (5 Baris Pertama):")
print(df_model_ready[['date', 'ticker', 'hhi_buy', 'hhi_sell', 'hhi_spread', 'foreign_flow_ratio']].head().to_markdown())