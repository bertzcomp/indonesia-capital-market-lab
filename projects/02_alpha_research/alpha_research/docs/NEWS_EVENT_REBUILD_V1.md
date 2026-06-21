# Alpha Research News Event Intelligence Rebuild v1

This patch rebuilds the news pipeline from scratch with a Polars-first design.

## Design goals

- Keep `data/pure_raw/news` as immutable daily scraper dump.
- Keep `data/raw/news` as canonical normalized raw layer.
- Build article-level event intelligence only as an extraction/audit layer.
- Aggregate article events into `event_cluster`, `ticker_day`, and `market_day` layers to avoid article-level label collapse.
- Use `ticker_day_news_features` as the main modeling grain.

## Main workflow

```bash
python3 workflows/build_news_event_intelligence_dataset.py \
  --root . \
  --engine polars \
  --news-source raw \
  --refresh-raw-news \
  --merge-existing-raw-news \
  --ohlcv-path data/raw_canonical/ohlcv.parquet \
  --build-report
```

Output:

```text
data/news/event_intelligence/news_event_intelligence_dataset.parquet
data/news/event_intelligence/sample_5.csv
data/news/event_intelligence/build_meta.json
data/news/event_intelligence/report/event_study_by_event_type.csv
```

## Aggregation workflow

```bash
python3 workflows/build_news_event_aggregates.py \
  --root . \
  --input data/news/event_intelligence/news_event_intelligence_dataset.parquet \
  --output-dir data/news/event_intelligence/aggregates
```

Output:

```text
data/news/event_intelligence/aggregates/news_event_cluster.parquet
data/news/event_intelligence/aggregates/ticker_day_news_features.parquet
data/news/event_intelligence/aggregates/market_day_news_regime.parquet
```

## Ticker-day event study

```bash
python3 workflows/build_news_ticker_day_event_study.py \
  --root . \
  --input data/news/event_intelligence/aggregates/ticker_day_news_features.parquet \
  --output-dir data/news/event_intelligence/aggregates/report \
  --min-rows 30
```

## Modeling views

```bash
python3 workflows/build_news_modeling_views.py \
  --root . \
  --input data/news/event_intelligence/aggregates/ticker_day_news_features.parquet \
  --output-dir data/news/event_intelligence/modeling
```

Output:

```text
data/news/event_intelligence/modeling/ticker_day_live_features.parquet
data/news/event_intelligence/modeling/ticker_day_training_labels.parquet
data/news/event_intelligence/modeling/ticker_day_modeling_full_with_flags.parquet
data/news/event_intelligence/modeling/ticker_day_modeling_eligible.parquet
data/news/event_intelligence/modeling/modeling_quality_summary.csv
```

## Notes

- Full CSV output is disabled by default. Use `--write-full-csv` only for debugging.
- If `pure_raw` is incomplete but `raw` contains historical data, always use `--merge-existing-raw-news` together with `--refresh-raw-news`.
- Article-level labels are not intended as final causal alpha labels. Use ticker-day aggregation for modeling.
