import pandas as pd
import numpy as np

def add_price_features(df):
    df = df.copy()
    df["ret1"] = df["close"].pct_change()
    df["ret5"] = df["close"].pct_change(5)
    df["vol20"] = df["ret1"].rolling(20).std()
    df["vol_spike"] = df["volume"] / df["volume"].rolling(20).mean()
    return df

def price_features_at_event(df, event_date):
    idx = df.index.get_indexer([event_date], method="backfill")[0]
    r = df.iloc[idx]
    return np.array([
        r.ret1, r.ret5, r.vol20, r.vol_spike
    ])
