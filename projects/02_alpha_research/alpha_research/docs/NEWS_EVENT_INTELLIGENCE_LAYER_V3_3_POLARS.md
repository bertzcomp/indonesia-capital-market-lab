# Alpha Research — News Event Intelligence Layer v3.3 Polars Engine

This patch replaces the pandas prototype with a Polars-based production-oriented engine.

## Why Polars?

The news layer can reach 200k+ articles. The heavy operations are concat, dedup, explode ticker events, join OHLCV, group-by rolling windows, and report aggregation. Polars is more appropriate than pandas for this EOD production workflow.

## Data flow

```text
data/pure_raw/news/                  # daily immutable scraper dumps
  -> data/raw/news/                  # canonical merged + deduplicated raw news
  -> data/news/event_intelligence/   # derived event intelligence dataset + reports
```

## First build when historical raw already exists but pure_raw only contains latest EOD files

Use merge mode:

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

This reads existing canonical raw news plus pure_raw news, deduplicates, writes canonical raw parquet/json, then builds the event intelligence dataset.

## If pure_raw is already complete 2020-2026

```bash
python3 workflows/build_news_event_intelligence_dataset.py \
  --root . \
  --engine polars \
  --news-source raw \
  --refresh-raw-news \
  --ohlcv-path data/raw_canonical/ohlcv.parquet \
  --build-report
```

## If raw is already complete and you do not want to touch it

```bash
python3 workflows/build_news_event_intelligence_dataset.py \
  --root . \
  --engine polars \
  --news-source raw \
  --ohlcv-path data/raw_canonical/ohlcv.parquet \
  --build-report
```

## Output

Primary output is Parquet:

```text
data/news/event_intelligence/news_event_intelligence_dataset.parquet
```

CSV full dataset is optional because it can be very large:

```bash
--write-full-csv
```

A small sample is always written:

```text
data/news/event_intelligence/sample_5.csv
```

Report:

```text
data/news/event_intelligence/report/event_study_by_event_type.csv
```

## Important flags

- `--refresh-raw-news`: read `data/pure_raw/news` and rebuild canonical raw news.
- `--merge-existing-raw-news`: when refreshing, merge existing `data/raw/news` historical files with `pure_raw` EOD files.
- `--no-ohlcv`: build event rows without forward/backward OHLCV labels.
- `--write-full-csv`: write full CSV in addition to Parquet.
- `--no-canonical-json`: write canonical parquet only; skip canonical JSON copies.

## Notes

- `news_date -> entry_date` uses the next trading day after `news_date`, because most news files only contain a date and not exact `published_at` time.
- Forward columns and reaction labels are training/evaluation outcomes and must not be used as live features.
- The event taxonomy remains rule-based in v3.3. The purpose is to build a reliable event-intelligence dataset before training NLP models.
