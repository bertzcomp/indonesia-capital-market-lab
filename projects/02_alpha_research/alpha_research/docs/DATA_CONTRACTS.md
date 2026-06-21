# Data Contracts

## pure_raw

Untouched landing zone for scraped/downloaded files.

## raw

Optional normalized raw source cache.

## raw_canonical

Only canonical tables should feed feature builders.

## key contracts

- OHLCV canonical key: `(date, ticker)` unique.
- Broker summary canonical key: `(date, ticker, rank)` unique.
- Insider raw can have multiple events per `(date, ticker)` and is aggregated before feature join.
- Macro canonical key: `(date)` unique.
- BDM canonical key: `(date, ticker, group, window)` unique.

## Feature store contracts

- Historical and live feature stores must have identical schema.
- `date` must be `pl.Date`.
- `ticker` must be uppercase string.
- Final feature store key `(date, ticker)` must be unique.
- Broker ratios must never be infinite and `net_flow_ratio` must be clipped to `[-1, 1]`.
