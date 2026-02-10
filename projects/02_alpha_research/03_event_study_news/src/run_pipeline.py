import pandas as pd

from features_text import text_features
from features_market import add_market_features
from impact_label import add_impact_labels
from model import train_model

# CONFIG
NEWS_PATH = "../data/news/filtered_BUMI_oct_nov_2025.json"
OHLCV_PATH = "../data/ohlcv/BUMI_daily_oct_nov_2025_ohlcv.csv"
OUTPUT_PATH = "../data/output/news_impact_probability.csv"
IMPACT_WINDOW = 3        # H0–H+3
IMPACT_THRESHOLD = 5.0  # % naik

# LOAD DATA
news = pd.read_json(NEWS_PATH)
news["date"] = pd.to_datetime(news["date"])

ohlcv = pd.read_csv(OHLCV_PATH)
ohlcv.columns = [c.lower().replace("<","").replace(">","") for c in ohlcv.columns]
ohlcv["date"] = pd.to_datetime(ohlcv["date"])
ohlcv = ohlcv.sort_values("date").set_index("date")

ohlcv["ret"] = ohlcv["close"].pct_change()
ohlcv["vol_20avg"] = ohlcv["volume"].rolling(20).mean()

events = news.sort_values("date").reset_index(drop=True)

# TEXT FEATURES
text_df = events["title"].apply(text_features).apply(pd.Series)
events = pd.concat([events, text_df], axis=1)

# MARKET FEATURES
events = add_market_features(events, ohlcv)

# IMPACT LABEL
events = add_impact_labels(
    events,
    ohlcv,
    window=IMPACT_WINDOW,
    threshold=IMPACT_THRESHOLD
)

# MODEL
FEATURES = [
    "sent_score","pos_count","neg_count","title_len",
    "prior_vol_20","volume_spike_flag","days_since_prev","weekday"
]

X = events[FEATURES].fillna(0)
y = events["label_positive"]

model, scaler = train_model(X, y)

# PREDICT PROBABILITY
events["probability"] = model.predict_proba(
    scaler.transform(X)
)[:,1] * 100

# SAVE
out = events[[
    "date","title","impact_return_pct","probability"
]].sort_values("date")

out.to_csv(OUTPUT_PATH, index=False)
print("Saved:", OUTPUT_PATH)
