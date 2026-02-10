import numpy as np

def compute_impact_pct(event_date, ohlcv, window=3):
    idx = ohlcv.index.get_indexer([event_date], method="backfill")[0]
    idx = min(idx, len(ohlcv)-1)

    start_price = ohlcv.iloc[idx]["close"]
    end_idx = min(len(ohlcv)-1, idx + window)
    end_price = ohlcv.iloc[end_idx]["close"]

    return (end_price / start_price - 1) * 100


def add_impact_labels(events, ohlcv, window=3, threshold=5):
    impacts = []

    for d in events["date"]:
        impacts.append(compute_impact_pct(d, ohlcv, window))

    events["impact_return_pct"] = impacts
    events["label_positive"] = (events["impact_return_pct"] > threshold).astype(int)

    return events
