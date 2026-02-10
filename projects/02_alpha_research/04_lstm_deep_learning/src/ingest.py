import pandas as pd
from pathlib import Path

def load_news(path):
    p = Path(path)
    df = pd.read_json(p) if p.suffix == ".json" else pd.read_csv(p)
    df["date"] = pd.to_datetime(df["date"]).dt.tz_localize(None)
    if "summary" not in df.columns:
        df["summary"] = df["title"]
    return df.sort_values("date").reset_index(drop=True)

def load_ohlcv(path):
    df = pd.read_csv(path)
    for c in df.columns:
        if c.lower() in ["date", "<date>"]:
            df.rename(columns={c: "date"}, inplace=True)
    df["date"] = pd.to_datetime(df["date"]).dt.tz_localize(None)
    df.columns = [c.lower().replace("<", "").replace(">", "") for c in df.columns]
    return df.sort_values("date").reset_index(drop=True)
