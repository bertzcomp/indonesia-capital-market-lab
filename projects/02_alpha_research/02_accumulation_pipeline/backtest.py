# backtest.py
import numpy as np

def compute_portfolio_returns(signals, price_data, top_n=10, cost=0.001):
    df = signals.reset_index().merge(
        price_data[['Close']], on=['Date','Ticker'], how='left')
    df = df.sort_values(['Date','Ticker'])
    df['rank'] = df.groupby('Date')['probability'].rank(ascending=False, method='first')
    picks = df[df['rank'] <= top_n]
    picks['FutureClose'] = picks.groupby('Ticker')['Close'].shift(-5)
    picks['Return5d'] = picks['FutureClose'] / picks['Close'] - 1.0
    picks['Return5d_net'] = picks['Return5d'] - 2*cost
    daily_return = picks.groupby('Date')['Return5d_net'].mean()
    equity = (1 + daily_return).cumprod()
    sharpe = np.mean(daily_return) / np.std(daily_return) * np.sqrt(252)
    wins = daily_return[daily_return > 0].sum()
    losses = -daily_return[daily_return < 0].sum()
    profit_factor = wins / losses if losses > 0 else np.inf
    peak = equity.cummax()
    drawdown = (peak - equity).max()
    return {
        'daily_return': daily_return,
        'equity_curve': equity,
        'Sharpe': sharpe,
        'ProfitFactor': profit_factor,
        'MaxDrawdown': drawdown
    }

