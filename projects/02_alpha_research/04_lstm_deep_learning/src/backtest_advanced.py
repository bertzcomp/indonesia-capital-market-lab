import numpy as np

def backtest_pnl(
    probs, returns, threshold=0.6, cost=0.002
):
    equity = 1.0
    curve = []

    for p, r in zip(probs, returns):
        if p > threshold:
            equity *= (1 + r/100 - cost)
        curve.append(equity)

    return np.array(curve)
