# model.py
import numpy as np
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score

def train_and_predict(X_train, y_train, X_valid, y_valid):
    model = XGBClassifier(
        n_estimators=100, max_depth=4, learning_rate=0.1,
        subsample=0.8, colsample_bytree=0.8, random_state=42)
    model.fit(X_train, y_train)
    probas = model.predict_proba(X_valid)[:,1]
    auc = roc_auc_score(y_valid, probas)
    return model, probas, auc

def walk_forward_training(features, labels, initial_train_period, test_period):
    dates = features.index.get_level_values('Date').unique().sort_values()
    results = []
    start_idx = 0
    while start_idx + initial_train_period + test_period <= len(dates):
        train_dates = dates[start_idx : start_idx + initial_train_period]
        test_dates = dates[start_idx + initial_train_period : start_idx + initial_train_period + test_period]
        X_train = features.loc[train_dates]
        y_train = labels.loc[train_dates]
        X_test = features.loc[test_dates]
        y_test = labels.loc[test_dates]
        model, probas, auc = train_and_predict(X_train, y_train, X_test, y_test)
        results.append((test_dates, probas, auc))
        start_idx += test_period
    return results

