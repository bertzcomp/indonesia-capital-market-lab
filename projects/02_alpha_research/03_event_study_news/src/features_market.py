import numpy as np

def add_market_features(events, ohlcv):
    prior_vol = []
    volume_spike = []
    days_since_prev = []

    prev_date = None

    for _, row in events.iterrows():
        d = row["date"]

        idx = ohlcv.index.get_indexer([d], method="backfill")[0]
        idx = min(idx, len(ohlcv)-1)

        # prior volatility (20 days)
        start = max(0, idx-20)
        vol = ohlcv.iloc[start:idx]["ret"].std()
        prior_vol.append(0 if np.isnan(vol) else vol)

        # volume spike
        v = ohlcv.iloc[idx]["volume"]
        vavg = ohlcv.iloc[idx]["vol_20avg"]
        volume_spike.append(int(vavg > 0 and v / vavg > 2))

        # distance to previous news
        if prev_date is None:
            days_since_prev.append(0)
        else:
            days_since_prev.append((d - prev_date).days)

        prev_date = d

    events["prior_vol_20"] = prior_vol
    events["volume_spike_flag"] = volume_spike
    events["days_since_prev"] = days_since_prev
    events["weekday"] = events["date"].dt.weekday

    return events
