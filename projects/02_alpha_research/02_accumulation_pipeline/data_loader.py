# data_loader.py
import pandas as pd
import yfinance as yf
from zipfile import ZipFile

def load_data(zip_path):
    with ZipFile(zip_path) as z:
        csv_files = [f for f in z.namelist() if f.endswith('.csv') and not f.startswith('__MACOSX')]
        list_df = []
        for file in csv_files:
            df = pd.read_csv(z.open(file))
            date_str = file.split('/')[0]
            date = pd.to_datetime(date_str, format='%d_%b_%Y')
            df['Date'] = date
            if 'Tick' in df.columns:
                df = df.rename(columns={'Tick':'Ticker'})
            list_df.append(df)
    accum_df = pd.concat(list_df, ignore_index=True)
    accum_df = accum_df.set_index(['Date','Ticker'])
    tickers = accum_df.index.get_level_values('Ticker').unique().tolist()
    dates = accum_df.index.get_level_values('Date')
    start_date, end_date = dates.min(), dates.max()
    price_data = yf.download(tickers, start=start_date, end=end_date)
    price_data = price_data.stack(level=1).rename_axis(['Date','Ticker']).reset_index()
    price_data = price_data.set_index(['Date','Ticker'])
    panel_df = price_data.join(accum_df, how='left').fillna(0)
    return panel_df
