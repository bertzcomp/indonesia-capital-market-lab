# main.py
import pandas as pd
from data_loader import load_data
from features import add_technical_indicators, add_accumulation_features
from model import walk_forward_training
from backtest import compute_portfolio_returns

panel = load_data('/mnt/data/29_jan_2026.zip')
technical = add_technical_indicators(panel)
technical['FutureClose'] = technical.groupby('Ticker')['Close'].shift(-5)
technical['Return5d'] = technical['FutureClose'] / technical['Close'] - 1.0
threshold = 0.03
technical['Label'] = (technical['Return5d'] > threshold).astype(int)
features = technical[['MA20','RSI14','Volatility20','OBV','CMF20']]
labels = technical['Label']
results = walk_forward_training(features, labels, initial_train_period=100, test_period=20)
all_preds = []
for test_dates, probas, auc in results:
    df_preds = pd.DataFrame({'Date': test_dates, 'Ticker': features.loc[test_dates].index.get_level_values('Ticker'),
                             'probability': probas})
    all_preds.append(df_preds)
signals = pd.concat(all_preds).set_index(['Date','Ticker'])
metrics = compute_portfolio_returns(signals, panel[['Close']], top_n=10)
print(f"Sharpe: {metrics['Sharpe']:.2f}, PF: {metrics['ProfitFactor']:.2f}, MaxDD: {metrics['MaxDrawdown']:.2%}")
signals.reset_index().to_csv('daily_signals.csv', index=False)
metrics_df = pd.DataFrame({
    'Sharpe': [metrics['Sharpe']],
    'ProfitFactor': [metrics['ProfitFactor']],
    'MaxDrawdown': [metrics['MaxDrawdown']]
})
metrics_df.to_csv('backtest_metrics.csv', index=False)
metrics['equity_curve'].plot(title="Portfolio Equity Curve")
