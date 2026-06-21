#!/usr/bin/env python3
"""
Validate whether the News Risk Gate improves Alpha Research daily signals.

It joins signal files with news_scores_all_live.parquet by signal_date + ticker,
then reports coverage, bucket distribution, action distribution, and outcome by
risk bucket/gate action.

This script can use outcomes already present in the signal file or proxy outcomes
from the news score file when available.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable, List, Optional

import pandas as pd

MONTH_MAP = {
    "jan": 1, "january": 1, "januari": 1,
    "feb": 2, "february": 2, "februari": 2,
    "mar": 3, "march": 3, "maret": 3,
    "apr": 4, "april": 4,
    "may": 5, "mei": 5,
    "jun": 6, "june": 6, "juni": 6,
    "jul": 7, "july": 7, "juli": 7,
    "aug": 8, "august": 8, "agustus": 8,
    "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "okt": 10, "october": 10, "oktober": 10,
    "nov": 11, "november": 11,
    "dec": 12, "des": 12, "december": 12, "desember": 12,
}


def read_frame(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() in [".parquet", ".pq"]:
        return pd.read_parquet(path)
    raise ValueError(f"Unsupported file type: {path}")


def infer_date_from_path(path: Path) -> Optional[pd.Timestamp]:
    text = str(path).lower()
    # signal_18_may_2026 or signal_01_june_2026
    m = re.search(r"signal[_-](\d{1,2})[_-]([a-z]+)[_-](\d{4})", text)
    if m:
        d = int(m.group(1)); mon = MONTH_MAP.get(m.group(2)); y = int(m.group(3))
        if mon:
            return pd.Timestamp(year=y, month=mon, day=d)
    # 2026-05-18 or 20260518
    m = re.search(r"(20\d{2})[-_]?([01]\d)[-_]?([0-3]\d)", text)
    if m:
        return pd.Timestamp(year=int(m.group(1)), month=int(m.group(2)), day=int(m.group(3)))
    return None


def normalize_ticker(s: pd.Series) -> pd.Series:
    return s.astype("string").str.upper().str.replace(".JK", "", regex=False).str.strip()


def load_signals(paths: Iterable[Path]) -> pd.DataFrame:
    frames = []
    for p in paths:
        if not p.exists():
            print("missing:", p)
            continue
        try:
            df = read_frame(p)
        except Exception as e:
            print("failed to read", p, e)
            continue
        df["source_file"] = str(p)
        if "signal_date" not in df.columns:
            if "date" in df.columns:
                df["signal_date"] = df["date"]
            else:
                inferred = infer_date_from_path(p)
                if inferred is None:
                    raise SystemExit(f"Cannot infer signal date from {p}; add signal_date/date column.")
                df["signal_date"] = inferred
        if "ticker" not in df.columns:
            for cand in ["symbol", "kode", "Kode", "emiten", "Ticker"]:
                if cand in df.columns:
                    df["ticker"] = df[cand]
                    break
        if "ticker" not in df.columns:
            raise SystemExit(f"No ticker/symbol column in {p}")
        frames.append(df)
    if not frames:
        raise SystemExit("No signal files loaded.")
    out = pd.concat(frames, ignore_index=True)
    out["signal_date"] = pd.to_datetime(out["signal_date"]).dt.normalize()
    out["ticker"] = normalize_ticker(out["ticker"])
    return out


def find_signal_files(root: Path, pattern: str) -> List[Path]:
    return sorted(root.glob(pattern))


def gate_action(bucket: str) -> str:
    if bucket == "EXTREME":
        return "SKIP_OR_WATCHLIST"
    if bucket == "HIGH":
        return "WAIT_CONFIRMATION_OR_REDUCE_SIZE"
    if bucket == "MEDIUM":
        return "NORMAL_CAUTION"
    if bucket == "LOW":
        return "KEEP_BASE_SIGNAL"
    return "NO_NEWS"


def summarize_by(df: pd.DataFrame, by: str, outcome_cols: List[str]) -> pd.DataFrame:
    rows = []
    for key, g in df.groupby(by, dropna=False):
        row = {by: key, "n": len(g)}
        for c in outcome_cols:
            if c in g.columns:
                row[f"avg_{c}"] = pd.to_numeric(g[c], errors="coerce").mean()
                row[f"median_{c}"] = pd.to_numeric(g[c], errors="coerce").median()
        if "target_downside_risk_5d" in g.columns:
            row["downside_risk_rate_5d"] = pd.to_numeric(g["target_downside_risk_5d"], errors="coerce").mean()
        if "sector_alpha_5d_w" in g.columns:
            s = pd.to_numeric(g["sector_alpha_5d_w"], errors="coerce")
            row["hit_sector_alpha_gt_0"] = (s > 0).mean()
            row["hit_sector_alpha_gt_1pct"] = (s > 0.01).mean()
        rows.append(row)
    return pd.DataFrame(rows).sort_values("n", ascending=False)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--signal-glob", default="signals/daily/signal_*/continual_model/all_scores.parquet")
    ap.add_argument("--news-scores", default="data/news/event_intelligence/modeling/models/news_scores_all_live.parquet")
    ap.add_argument("--output-dir", default="data/news/event_intelligence/modeling/signal_gate_validation")
    ap.add_argument("--date-lag", type=int, default=0, help="Join signal_date to news_date + lag. Use 0 for same EOD, -1/1 only if your workflow requires it.")
    args = ap.parse_args()

    root = Path(args.root)
    signal_paths = find_signal_files(root, args.signal_glob)
    if not signal_paths:
        raise SystemExit(f"No files matched: {args.signal_glob}")

    signals = load_signals(signal_paths)
    news = read_frame(root / args.news_scores)
    news["news_date"] = pd.to_datetime(news["news_date"]).dt.normalize()
    news["ticker"] = normalize_ticker(news["ticker"])
    if args.date_lag != 0:
        news["join_date"] = news["news_date"] + pd.to_timedelta(args.date_lag, unit="D")
    else:
        news["join_date"] = news["news_date"]

    # Deduplicate ticker-date news scores by highest risk score.
    news = news.sort_values("news_risk_score", ascending=False).drop_duplicates(["join_date", "ticker"], keep="first")

    keep_news = [
        "join_date", "news_date", "ticker", "sector",
        "dominant_event_type", "dominant_event_side", "dominant_impact_channel",
        "n_articles", "n_event_clusters", "n_event_types",
        "news_alpha_score", "news_risk_score", "news_risk_pct_rank", "news_risk_bucket_pct",
        "sector_alpha_5d_w", "market_alpha_5d_w", "fwd_ret_5d_w", "mae_5d_w", "mfe_5d_w",
        "target_downside_risk_5d", "target_alpha_pos_5d",
    ]
    keep_news = [c for c in keep_news if c in news.columns]

    joined = signals.merge(
        news[keep_news],
        left_on=["signal_date", "ticker"],
        right_on=["join_date", "ticker"],
        how="left",
        suffixes=("", "_news"),
    )

    joined["has_news_score"] = joined["news_risk_score"].notna()
    joined["news_risk_bucket_pct"] = joined["news_risk_bucket_pct"].fillna("NO_NEWS")
    joined["news_gate_action"] = joined["news_risk_bucket_pct"].apply(gate_action)

    out_dir = root / args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    joined.to_csv(out_dir / "signal_news_risk_joined.csv", index=False)
    joined.to_parquet(out_dir / "signal_news_risk_joined.parquet", index=False)

    outcome_cols = [c for c in ["sector_alpha_5d_w", "market_alpha_5d_w", "fwd_ret_5d_w", "mae_5d_w", "mfe_5d_w"] if c in joined.columns]
    coverage = pd.DataFrame({
        "metric": ["signal_rows", "matched_news_rows", "coverage_rate", "unique_signal_dates", "unique_tickers"],
        "value": [
            len(joined),
            int(joined["has_news_score"].sum()),
            float(joined["has_news_score"].mean()),
            int(joined["signal_date"].nunique()),
            int(joined["ticker"].nunique()),
        ],
    })
    coverage.to_csv(out_dir / "coverage_summary.csv", index=False)
    joined["news_risk_bucket_pct"].value_counts(dropna=False).rename_axis("bucket").reset_index(name="n").to_csv(out_dir / "bucket_distribution.csv", index=False)
    joined["news_gate_action"].value_counts(dropna=False).rename_axis("action").reset_index(name="n").to_csv(out_dir / "gate_action_distribution.csv", index=False)

    summarize_by(joined, "news_risk_bucket_pct", outcome_cols).to_csv(out_dir / "outcome_by_risk_bucket.csv", index=False)
    summarize_by(joined, "news_gate_action", outcome_cols).to_csv(out_dir / "outcome_by_gate_action.csv", index=False)
    if "dominant_event_type" in joined.columns:
        summarize_by(joined[joined["has_news_score"]], "dominant_event_type", outcome_cols).to_csv(out_dir / "outcome_by_dominant_event_type.csv", index=False)

    print("Saved validation to:", out_dir)
    print("Coverage:")
    print(coverage)
    print("\nBucket distribution:")
    print(joined["news_risk_bucket_pct"].value_counts(dropna=False))
    print("\nGate action distribution:")
    print(joined["news_gate_action"].value_counts(dropna=False))
    if outcome_cols:
        print("\nOutcome by risk bucket:")
        print(summarize_by(joined, "news_risk_bucket_pct", outcome_cols))
    else:
        print("\nNo proxy outcome columns found. Joined file was still saved for inspection.")


if __name__ == "__main__":
    main()
