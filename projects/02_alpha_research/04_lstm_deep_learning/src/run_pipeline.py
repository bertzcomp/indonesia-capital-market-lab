import pandas as pd
from train import build_dataset, train_rf
from backtest import backtest

news = pd.read_json("data/news.json")
stock = pd.read_csv("data/stock_ohlcv.csv")
ihsg = pd.read_csv("data/ihsg_ohlcv.csv")

X,y = build_dataset(news, stock, ihsg)
model = train_rf(X,y)

probs = model.predict_proba(X)[:,1]
signals = pd.DataFrame({"date":news.date,"prob":probs})

pnl = backtest(signals, stock.set_index("date"))
print("Final PnL:", pnl.iloc[-1])
