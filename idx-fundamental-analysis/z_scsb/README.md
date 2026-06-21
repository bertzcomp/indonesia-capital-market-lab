to get the data, you should to activate the venv (virtual environment) using this command:

```py
source .venv/bin/activate
```

if you not do this, that will throw the error becoz the program designed for ts. So stay calm twin and adapt with the rule gng 

and if you done on it, you should end the venv with this
```py
deactivate
```


### for filter_rt.py

```py
python3 runing_trade_filtered.py --price-from 1 --price-to 10 --min-lot 100 --max-scroll 250 --debug
```

### for running-trade.py

```py
python3 main.py
```

# broker_summary.py

Scrape EOD Broker Summary for ALL stocks listed on IDX (Bursa Efek Indonesia)
using Stockbit's /marketdetectors/{ticker} API.

Output CSV schema matches Stockbit web UI table exactly:
    stock_code | date | from | to | rank | BY | BY_type | B.val | B.lot | B.freq | B.avg
                                         | SL | SL_type | S.val | S.lot | S.freq | S.avg

Each row = one rank position (buy[i] paired with sell[i]).

### Scrape all IDX stocks for a single date (EOD today)
    python broker_summary.py --date 2026-03-17

### Scrape specific date range:
    python broker_summary.py --date-from 2026-03-16 --date-to 2026-03-17

### Use local ticker list (faster, no Selenium):
    python broker_summary.py --date 2026-03-17 --ticker-file tickers.txt

### Scrape only specific tickers:
    python broker_summary.py --date 2026-03-17 --tickers BBRI BKSL TLKM ASII

### Full options:
    python broker_summary.py \
        --date-from 2026-03-16 \
        --date-to 2026-03-17 \
        --transaction-type TRANSACTION_TYPE_NET \
        --market-board MARKET_BOARD_REGULER \
        --investor-type INVESTOR_TYPE_ALL \
        --limit 25 \
        --delay 0.5 \
        --output-dir output/broker_summary \
        --debug