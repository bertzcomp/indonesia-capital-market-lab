#!/usr/bin/env python3
"""
Validate News Risk Gate against Alpha Research daily signals (v2.1).

Fixes vs v2:
- robust parquet serialization: casts outcome/score columns to numeric and categorical columns to string
- computes OHLCV realized outcome for all signal rows, including NO_NEWS rows
- adds market-day news risk overlay
- supports CSV/parquet signal files via glob
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable, Optional

import numpy as np
import pandas as pd

MONTH_MAP = {
    "jan": 1, "january": 1,
    "feb": 2, "february": 2,
    "mar": 3, "march": 3,
    "apr": 4, "april": 4,
    "may": 5, "mei": 5,
    "jun": 6, "june": 6, "juni": 6,
    "jul": 7, "july": 7, "juli": 7,
    "aug": 8, "august": 8, "agu": 8, "agustus": 8,
    "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "okt": 10, "october": 10, "oktober": 10,
    "nov": 11, "november": 11,
    "dec": 12, "des": 12, "december": 12, "desember": 12,
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=".")
    p.add_argument("--signal-glob", required=True)
    p.add_argument("--news-scores", required=True)
    p.add_argument("--ohlcv", required=True)
    p.add_argument("--output-dir", required=True)
    p.add_argument("--horizon", type=int, default=5)
    p.add_argument("--date-lag", type=int, default=0, help="Join signal_date + date_lag days to news_date")
    p.add_argument("--signal-date-col", default=None)
    p.add_argument("--ticker-col", default="ticker")
    p.add_argument("--write-parquet", action="store_true", default=True)
    p.add_argument("--no-write-parquet", action="store_false", dest="write_parquet")
    return p.parse_args()


def read_table(path: Path) -> pd.DataFrame:
    if path.suffix.lower() in [".parquet", ".pq"]:
        return pd.read_parquet(path)
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    raise ValueError(f"Unsupported file type: {path}")


def parse_signal_date_from_path(path: Path) -> Optional[pd.Timestamp]:
    # signal_20_may_2026 or signal_01_june_2026
    text = str(path)
    m = re.search(r"signal_(\d{1,2})_([A-Za-z]+)_(\d{4})", text)
    if not m:
        return None
    day = int(m.group(1))
    mon_raw = m.group(2).lower()
    year = int(m.group(3))
    mon = MONTH_MAP.get(mon_raw)
    if not mon:
        return None
    return pd.Timestamp(year=year, month=mon, day=day)


def normalize_ticker(s: pd.Series) -> pd.Series:
    return s.astype("string").str.upper().str.replace(".JK", "", regex=False).str.strip()


def load_signals(root: Path, pattern: str, date_col: Optional[str], ticker_col: str) -> pd.DataFrame:
    paths = sorted(root.glob(pattern))
    if not paths:
        raise FileNotFoundError(f"No signal files found for glob: {pattern}")

    frames = []
    for p in paths:
        df = read_table(p)
        df["source_file"] = str(p)

        if ticker_col not in df.columns:
            # fallback common names
            for cand in ["Ticker", "symbol", "stock", "kode", "KodeEmiten"]:
                if cand in df.columns:
                    df[ticker_col] = df[cand]
                    break
        if ticker_col not in df.columns:
            raise ValueError(f"Ticker column not found in {p}. Available columns: {df.columns.tolist()}")

        if date_col and date_col in df.columns:
            df["signal_date"] = pd.to_datetime(df[date_col], errors="coerce")
        elif "signal_date" in df.columns:
            df["signal_date"] = pd.to_datetime(df["signal_date"], errors="coerce")
        elif "date" in df.columns:
            df["signal_date"] = pd.to_datetime(df["date"], errors="coerce")
        else:
            inferred = parse_signal_date_from_path(p)
            if inferred is None:
                raise ValueError(f"Could not infer signal_date for {p}. Pass --signal-date-col.")
            df["signal_date"] = inferred

        df["ticker"] = normalize_ticker(df[ticker_col])
        frames.append(df)

    out = pd.concat(frames, ignore_index=True)
    out["signal_date"] = pd.to_datetime(out["signal_date"], errors="coerce").dt.normalize()
    out = out.dropna(subset=["signal_date", "ticker"])
    return out


def load_news_scores(path: Path) -> pd.DataFrame:
    news = read_table(path)
    if "news_date" not in news.columns:
        if "date" in news.columns:
            news["news_date"] = news["date"]
        else:
            raise ValueError("news scores must contain news_date/date")
    news["news_date"] = pd.to_datetime(news["news_date"], errors="coerce").dt.normalize()
    news["ticker"] = normalize_ticker(news["ticker"])

    required_defaults = {
        "news_risk_score": 0.0,
        "news_alpha_score": np.nan,
        "news_risk_pct_rank": np.nan,
        "news_risk_bucket_pct": "NO_NEWS",
        "dominant_event_type": "NO_NEWS",
        "dominant_event_side": "UNKNOWN",
        "dominant_impact_channel": "UNKNOWN",
    }
    for c, val in required_defaults.items():
        if c not in news.columns:
            news[c] = val
    return news


def load_ohlcv_with_outcomes(path: Path, horizon: int) -> pd.DataFrame:
    px = read_table(path)
    rename = {c: c.lower() for c in px.columns}
    px = px.rename(columns=rename)
    if "ticker" not in px.columns or "date" not in px.columns:
        raise ValueError(f"OHLCV must contain ticker/date. Columns: {px.columns.tolist()}")

    px["ticker"] = normalize_ticker(px["ticker"])
    px["date"] = pd.to_datetime(px["date"], errors="coerce").dt.normalize()
    for c in ["open", "high", "low", "close", "volume"]:
        if c in px.columns:
            px[c] = pd.to_numeric(px[c], errors="coerce")
    px = px.dropna(subset=["ticker", "date", "close"]).sort_values(["ticker", "date"])

    # Forward close after N trading rows per ticker
    g = px.groupby("ticker", group_keys=False)
    px[f"future_close_{horizon}d"] = g["close"].shift(-horizon)

    # Forward window high/low over next 1..horizon trading rows, excluding current day
    px_rev = px.sort_values(["ticker", "date"], ascending=[True, False]).copy()
    gr = px_rev.groupby("ticker", group_keys=False)
    # In reversed order, previous rows correspond to future in normal order.
    px_rev[f"future_low_{horizon}d"] = gr["low"].apply(lambda s: s.shift(1).rolling(horizon, min_periods=1).min()) if "low" in px_rev.columns else np.nan
    px_rev[f"future_high_{horizon}d"] = gr["high"].apply(lambda s: s.shift(1).rolling(horizon, min_periods=1).max()) if "high" in px_rev.columns else np.nan
    px = px.merge(
        px_rev[["ticker", "date", f"future_low_{horizon}d", f"future_high_{horizon}d"]],
        on=["ticker", "date"], how="left"
    )

    px[f"signal_fwd_ret_{horizon}d"] = (px[f"future_close_{horizon}d"] / px["close"]) - 1.0
    px[f"signal_mae_{horizon}d"] = (px[f"future_low_{horizon}d"] / px["close"]) - 1.0
    px[f"signal_mfe_{horizon}d"] = (px[f"future_high_{horizon}d"] / px["close"]) - 1.0

    keep = ["ticker", "date", "close", f"signal_fwd_ret_{horizon}d", f"signal_mae_{horizon}d", f"signal_mfe_{horizon}d"]
    keep = [c for c in keep if c in px.columns]
    out = px[keep].copy()
    out = out.rename(columns={"date": "signal_date", "close": "signal_close"})
    return out


def build_market_overlay(news: pd.DataFrame) -> pd.DataFrame:
    n = news.copy()
    n["is_high_extreme"] = n["news_risk_bucket_pct"].isin(["HIGH", "EXTREME"]).astype(int)
    n["is_extreme"] = (n["news_risk_bucket_pct"] == "EXTREME").astype(int)
    for c in ["news_risk_score", "news_risk_pct_rank"]:
        n[c] = pd.to_numeric(n[c], errors="coerce")

    grp = n.groupby("news_date", dropna=False).agg(
        market_news_rows=("ticker", "size"),
        market_unique_tickers=("ticker", "nunique"),
        market_avg_news_risk_score=("news_risk_score", "mean"),
        market_p90_news_risk_score=("news_risk_score", lambda x: x.quantile(0.90)),
        market_p95_news_risk_score=("news_risk_score", lambda x: x.quantile(0.95)),
        market_high_extreme_count=("is_high_extreme", "sum"),
        market_extreme_count=("is_extreme", "sum"),
    ).reset_index()
    grp["market_high_extreme_ratio"] = grp["market_high_extreme_count"] / grp["market_news_rows"].replace(0, np.nan)

    def regime(row):
        if row["market_news_rows"] < 10:
            return "MARKET_RISK_LOW"
        if row["market_p95_news_risk_score"] >= 0.96 or row["market_high_extreme_ratio"] >= 0.20:
            return "MARKET_RISK_EXTREME"
        if row["market_p90_news_risk_score"] >= 0.90 or row["market_high_extreme_ratio"] >= 0.10:
            return "MARKET_RISK_HIGH"
        if row["market_avg_news_risk_score"] >= 0.65:
            return "MARKET_RISK_MEDIUM"
        return "MARKET_RISK_LOW"

    grp["market_news_risk_regime"] = grp.apply(regime, axis=1)
    return grp.rename(columns={"news_date": "signal_date"})


def gate_action(row) -> str:
    market = row.get("market_news_risk_regime", "MARKET_RISK_LOW")
    bucket = row.get("news_risk_bucket_pct", "NO_NEWS")
    if market == "MARKET_RISK_EXTREME":
        return "MARKET_WIDE_WATCHLIST_ONLY"
    if market == "MARKET_RISK_HIGH":
        if bucket in ["EXTREME", "HIGH"]:
            return "SKIP_OR_WATCHLIST"
        return "WAIT_CONFIRMATION_MARKET_RISK"
    if bucket == "EXTREME":
        return "SKIP_OR_WATCHLIST"
    if bucket == "HIGH":
        return "WAIT_CONFIRMATION_OR_REDUCE_SIZE"
    if bucket == "MEDIUM":
        return "NORMAL_CAUTION"
    if bucket == "LOW":
        return "KEEP_BASE_SIGNAL"
    return "NO_NEWS"


def summarize_outcome(df: pd.DataFrame, group_col: str, horizon: int) -> pd.DataFrame:
    ret_col = f"signal_fwd_ret_{horizon}d"
    mae_col = f"signal_mae_{horizon}d"
    mfe_col = f"signal_mfe_{horizon}d"

    tmp = df.copy()
    for c in [ret_col, mae_col, mfe_col, "news_risk_score"]:
        if c in tmp.columns:
            tmp[c] = pd.to_numeric(tmp[c], errors="coerce")
    tmp["hit_ret_gt_0"] = (tmp[ret_col] > 0).astype(float) if ret_col in tmp.columns else np.nan
    tmp["downside_mae_lt_3pct"] = (tmp[mae_col] < -0.03).astype(float) if mae_col in tmp.columns else np.nan
    tmp["downside_mae_lt_7pct"] = (tmp[mae_col] < -0.07).astype(float) if mae_col in tmp.columns else np.nan

    agg = tmp.groupby(group_col, dropna=False).agg(
        n_rows=("ticker", "size"),
        n_tickers=("ticker", "nunique"),
        matched_news_rows=("has_news_match", "sum"),
        avg_news_risk_score=("news_risk_score", "mean"),
        avg_fwd_ret_5d=(ret_col, "mean"),
        median_fwd_ret_5d=(ret_col, "median"),
        hit_ret_gt_0=("hit_ret_gt_0", "mean"),
        avg_mae_5d=(mae_col, "mean"),
        median_mae_5d=(mae_col, "median"),
        avg_mfe_5d=(mfe_col, "mean"),
        downside_mae_lt_3pct=("downside_mae_lt_3pct", "mean"),
        downside_mae_lt_7pct=("downside_mae_lt_7pct", "mean"),
    ).reset_index()
    return agg


def sanitize_for_parquet(df: pd.DataFrame, horizon: int) -> pd.DataFrame:
    out = df.copy()
    numeric_cols = [
        "news_risk_score", "news_alpha_score", "news_risk_pct_rank",
        "market_avg_news_risk_score", "market_p90_news_risk_score", "market_p95_news_risk_score",
        "market_high_extreme_ratio", "market_news_rows", "market_unique_tickers",
        "market_high_extreme_count", "market_extreme_count", "signal_close",
        f"signal_fwd_ret_{horizon}d", f"signal_mae_{horizon}d", f"signal_mfe_{horizon}d",
    ]
    for c in numeric_cols:
        if c in out.columns:
            out[c] = pd.to_numeric(out[c], errors="coerce")

    bool_cols = ["has_news_match"]
    for c in bool_cols:
        if c in out.columns:
            out[c] = out[c].fillna(False).astype(bool)

    # Convert mixed object columns to string if they are not obviously numeric.
    for c in out.columns:
        if out[c].dtype == "object":
            # try numeric for outcome-like object columns, otherwise string
            if any(tok in c.lower() for tok in ["ret", "mae", "mfe", "score", "ratio", "count", "rows"]):
                converted = pd.to_numeric(out[c], errors="coerce")
                # keep numeric if it produces any non-null or original was mostly null
                if converted.notna().sum() > 0:
                    out[c] = converted
                    continue
            out[c] = out[c].astype("string")
    return out


def safe_write_outputs(df: pd.DataFrame, out_path: Path, horizon: int, parquet_name: str, csv_name: str, write_parquet: bool = True):
    out_path.mkdir(parents=True, exist_ok=True)
    clean = sanitize_for_parquet(df, horizon)
    clean.to_csv(out_path / csv_name, index=False)
    if write_parquet:
        try:
            clean.to_parquet(out_path / parquet_name, index=False)
        except Exception as e:
            (out_path / f"{parquet_name}.ERROR.txt").write_text(str(e))
            print(f"WARNING: failed writing parquet {parquet_name}; CSV was saved. Error: {e}")
    return clean


def main():
    args = parse_args()
    root = Path(args.root)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    h = args.horizon

    signals = load_signals(root, args.signal_glob, args.signal_date_col, args.ticker_col)
    news = load_news_scores(root / args.news_scores if not Path(args.news_scores).is_absolute() else Path(args.news_scores))
    ohlcv_out = load_ohlcv_with_outcomes(root / args.ohlcv if not Path(args.ohlcv).is_absolute() else Path(args.ohlcv), h)

    # Join news score. date_lag: signal_date + lag = news_date
    signals["news_join_date"] = signals["signal_date"] + pd.to_timedelta(args.date_lag, unit="D")

    news_keep = [
        "news_date", "ticker", "dominant_event_type", "dominant_event_side", "dominant_impact_channel",
        "news_risk_score", "news_alpha_score", "news_risk_pct_rank", "news_risk_bucket_pct",
    ]
    news_keep = [c for c in news_keep if c in news.columns]
    joined = signals.merge(
        news[news_keep],
        left_on=["news_join_date", "ticker"],
        right_on=["news_date", "ticker"],
        how="left",
    )
    joined["has_news_match"] = joined["news_date"].notna()
    joined["news_risk_score"] = pd.to_numeric(joined.get("news_risk_score", 0.0), errors="coerce").fillna(0.0)
    joined["news_alpha_score"] = pd.to_numeric(joined.get("news_alpha_score", np.nan), errors="coerce")
    joined["news_risk_pct_rank"] = pd.to_numeric(joined.get("news_risk_pct_rank", np.nan), errors="coerce")
    joined["news_risk_bucket_pct"] = joined.get("news_risk_bucket_pct", "NO_NEWS").fillna("NO_NEWS").astype("string")
    for c in ["dominant_event_type", "dominant_event_side", "dominant_impact_channel"]:
        if c not in joined.columns:
            joined[c] = "NO_NEWS"
        joined[c] = joined[c].fillna("NO_NEWS").astype("string")

    # Join OHLCV outcomes for every signal row
    joined = joined.merge(ohlcv_out, on=["signal_date", "ticker"], how="left")

    # Market overlay by date from news scores
    overlay = build_market_overlay(news)
    joined = joined.merge(overlay, on="signal_date", how="left")
    joined["market_news_risk_regime"] = joined["market_news_risk_regime"].fillna("MARKET_RISK_LOW").astype("string")
    joined["news_gate_action"] = joined.apply(gate_action, axis=1)

    # Save full joined robustly
    joined = safe_write_outputs(joined, out, h, "signal_news_risk_joined_v2.parquet", "signal_news_risk_joined_v2.csv", args.write_parquet)

    ret_col = f"signal_fwd_ret_{h}d"
    coverage = pd.DataFrame({
        "metric": [
            "signal_rows", "matched_news_rows", "coverage_rate", "rows_with_ohlcv_outcome",
            "outcome_coverage_rate", "unique_signal_dates", "unique_tickers",
        ],
        "value": [
            len(joined), int(joined["has_news_match"].sum()), float(joined["has_news_match"].mean()),
            int(joined[ret_col].notna().sum()) if ret_col in joined.columns else 0,
            float(joined[ret_col].notna().mean()) if ret_col in joined.columns else 0.0,
            int(joined["signal_date"].nunique()), int(joined["ticker"].nunique()),
        ]
    })
    coverage.to_csv(out / "coverage_summary_v2.csv", index=False)

    joined["news_risk_bucket_pct"].value_counts(dropna=False).rename_axis("news_risk_bucket_pct").reset_index(name="count").to_csv(out / "bucket_distribution_v2.csv", index=False)
    joined["news_gate_action"].value_counts(dropna=False).rename_axis("news_gate_action").reset_index(name="count").to_csv(out / "gate_action_distribution_v2.csv", index=False)
    joined["market_news_risk_regime"].value_counts(dropna=False).rename_axis("market_news_risk_regime").reset_index(name="count").to_csv(out / "market_regime_distribution_v2.csv", index=False)
    overlay.to_csv(out / "market_day_news_risk_overlay_v2.csv", index=False)

    summarize_outcome(joined, "news_risk_bucket_pct", h).to_csv(out / "outcome_by_risk_bucket_v2.csv", index=False)
    summarize_outcome(joined, "news_gate_action", h).to_csv(out / "outcome_by_gate_action_v2.csv", index=False)
    summarize_outcome(joined, "market_news_risk_regime", h).to_csv(out / "outcome_by_market_regime_v2.csv", index=False)
    summarize_outcome(joined, "dominant_event_type", h).to_csv(out / "outcome_by_dominant_event_type_v2.csv", index=False)

    meta = {
        "signal_rows": int(len(joined)),
        "matched_news_rows": int(joined["has_news_match"].sum()),
        "coverage_rate": float(joined["has_news_match"].mean()),
        "rows_with_ohlcv_outcome": int(joined[ret_col].notna().sum()) if ret_col in joined.columns else 0,
        "outcome_coverage_rate": float(joined[ret_col].notna().mean()) if ret_col in joined.columns else 0.0,
        "horizon": h,
        "date_lag": args.date_lag,
    }
    (out / "validation_meta_v2.json").write_text(json.dumps(meta, indent=2))

    print(coverage.to_string(index=False))
    print("Saved:", out)


if __name__ == "__main__":
    main()
