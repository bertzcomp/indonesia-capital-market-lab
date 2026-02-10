import pandas as pd

def backtest(signals, ohlcv, cost=0.001, horizon=3):
    pnl = []
    for i,r in signals.iterrows():
        if r.prob < 0.6: 
            pnl.append(0); continue
        idx = ohlcv.index.get_indexer([r.date], method="backfill")[0]
        buy = ohlcv.iloc[idx].open
        sell = ohlcv.iloc[min(idx+horizon,len(ohlcv)-1)].close
        pnl.append((sell/buy-1)-2*cost)
    return pd.Series(pnl).cumsum()
