import numpy as np
import pandas as pd

def calc_rsi(series, window=14):
    delta = series.diff()
    gain = (delta.clip(lower=0)).ewm(alpha=1/window, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/window, adjust=False).mean()
    rs = gain / loss
    rsi = 100 - 100/(1+rs)
    return rsi

def add_technical_indicators(df):
    df = df.copy()
    df = df.sort_index()
    df['MA20'] = df.groupby('Ticker')['Close'].transform(lambda x: x.rolling(window=20).mean())
    df['RSI14'] = df.groupby('Ticker')['Close'].transform(lambda x: calc_rsi(x,14))
    df['Ret'] = df.groupby('Ticker')['Close'].transform(lambda x: x.pct_change())
    df['Volatility20'] = df.groupby('Ticker')['Ret'].transform(lambda x: x.rolling(window=20).std())
    def obv(group):
        obv_val = (group['Volume'] * np.sign(group['Close'].diff().fillna(0))).cumsum()
        return obv_val
    df['OBV'] = df.groupby('Ticker', group_keys=False).apply(obv).reset_index(level=0, drop=True)
    tp = (df['High'] + df['Low'] + df['Close'])/3
    mf = tp * df['Volume']
    mf_pos = mf.where(tp > tp.shift(1), 0).rolling(window=20).sum()
    mf_neg = mf.where(tp < tp.shift(1), 0).rolling(window=20).sum()
    df['CMF20'] = (mf_pos - mf_neg) / (mf_pos + mf_neg)
    return df

def add_accumulation_features(df, accum_df):
    df = df.reset_index().merge(accum_df.reset_index(), on=['Date','Ticker'], how='left')
    df = df.fillna(0)
    if 'Foreign' in df.columns and 'Local' in df.columns:
        df['Foreign_Local_diff'] = df['Foreign'] - df['Local']
    return df.set_index(['Date','Ticker'])

