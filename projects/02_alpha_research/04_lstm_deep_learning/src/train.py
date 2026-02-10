import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from features_text import indobert_embedding, lexicon_features
from features_price import add_price_features, price_features_at_event
from impact_label import abnormal_returns

def build_dataset(news, stock, ihsg, use_emb=True):
    texts = news.summary.tolist()
    X_text = indobert_embedding(texts) if use_emb else lexicon_features(texts)
    stock = add_price_features(stock.set_index("date"))
    X_price = np.vstack([price_features_at_event(stock, d) for d in news.date])
    X = np.hstack([X_text, X_price])
    ar = abnormal_returns(stock, ihsg.set_index("date"), news.date)
    y = (np.array(ar[3]) > 5).astype(int)
    return X, y

def train_rf(X, y):
    clf = RandomForestClassifier(n_estimators=300, class_weight="balanced")
    clf.fit(X, y)
    return clf
