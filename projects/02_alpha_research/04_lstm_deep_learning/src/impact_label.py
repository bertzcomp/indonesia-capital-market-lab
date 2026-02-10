import numpy as np

def abnormal_returns(stock, ihsg, dates, horizons=(3,5,7)):
    out = {h:[] for h in horizons}
    for d in dates:
        s_idx = stock.index.get_indexer([d], method="backfill")[0]
        for h in horizons:
            e = min(len(stock)-1, s_idx+h)
            r_stock = stock.iloc[e].close / stock.iloc[s_idx].close - 1
            i_idx = ihsg.index.get_indexer([stock.index[s_idx]], method="backfill")[0]
            i_end = min(len(ihsg)-1, i_idx+h)
            r_mkt = ihsg.iloc[i_end].close / ihsg.iloc[i_idx].close - 1
            out[h].append((r_stock - r_mkt)*100)
    return out
