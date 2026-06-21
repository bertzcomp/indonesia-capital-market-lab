from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import polars as pl

from fae_polars.io import ensure_dir, read_table, write_table
from fae_polars.modeling import apply_redesigned_models
from fae_polars.scorecard import score_panel
from fae_polars.signals import MODE_THRESHOLDS


def _mode_filter(df: pl.DataFrame, mode: str) -> pl.DataFrame:
    min_val = MODE_THRESHOLDS.get(mode, 0.0)
    if min_val > 0 and "avg_value_20d" in df.columns:
        return df.filter(pl.col("avg_value_20d").fill_null(0) >= min_val)
    return df


def _run_topk(df: pl.DataFrame, score_col: str, return_col: str, ks: list[int]) -> pl.DataFrame:
    if df.is_empty() or score_col not in df.columns or return_col not in df.columns:
        return pl.DataFrame()
    base = df.filter(pl.col(score_col).is_not_null() & pl.col(return_col).is_not_null())
    if base.is_empty():
        return pl.DataFrame()
    base = base.with_columns([
        pl.col("as_of_date").dt.year().alias("year") if base.schema.get("as_of_date") == pl.Date else pl.col("as_of_date").str.strptime(pl.Date, strict=False).dt.year().alias("year"),
        pl.col(score_col).rank(method="ordinal", descending=True).over("as_of_date").alias("rank_by_score"),
    ])
    rows = []
    for k in ks:
        top = base.filter(pl.col("rank_by_score") <= int(k))
        if top.is_empty():
            continue
        total = top.select([
            pl.lit("ALL").alias("bucket"),
            pl.lit(int(k)).alias("top_k"),
            pl.len().alias("rows"),
            pl.col("as_of_date").n_unique().alias("dates"),
            pl.col(return_col).mean().alias("mean_return"),
            pl.col(return_col).median().alias("median_return"),
            (pl.col(return_col) > 0).mean().alias("hit_rate_positive"),
            pl.col(return_col).quantile(0.10).alias("p10_return"),
            pl.col(return_col).quantile(0.90).alias("p90_return"),
            pl.col("avg_value_20d").median().alias("median_avg_value_20d") if "avg_value_20d" in top.columns else pl.lit(None).alias("median_avg_value_20d"),
        ])
        rows.append(total)
        by_year = top.group_by("year").agg([
            pl.lit(int(k)).alias("top_k"),
            pl.len().alias("rows"),
            pl.col("as_of_date").n_unique().alias("dates"),
            pl.col(return_col).mean().alias("mean_return"),
            pl.col(return_col).median().alias("median_return"),
            (pl.col(return_col) > 0).mean().alias("hit_rate_positive"),
            pl.col(return_col).quantile(0.10).alias("p10_return"),
            pl.col(return_col).quantile(0.90).alias("p90_return"),
            pl.col("avg_value_20d").median().alias("median_avg_value_20d") if "avg_value_20d" in top.columns else pl.lit(None).alias("median_avg_value_20d"),
        ]).rename({"year": "bucket"}).with_columns(pl.col("bucket").cast(pl.Utf8))
        rows.append(by_year)
    return pl.concat(rows, how="diagonal_relaxed") if rows else pl.DataFrame()


def main() -> None:
    ap = argparse.ArgumentParser(description="Top-k historical backtest for scorecard/model/hybrid scores.")
    ap.add_argument("--root", default=".")
    ap.add_argument("--model-dir", default=None, help="Optional redesigned model dir. If provided, historical training panel is model-scored before backtest.")
    ap.add_argument("--score-col", default="fundamental_score", help="Score column: fundamental_score, ml_alpha_score, final_alpha_score_v2, return_rank_score, etc.")
    ap.add_argument("--return-col", default="fwd_excess_sector_60d")
    ap.add_argument("--mode", choices=["research_all", "tradable", "liquid", "strict_liquid"], default="research_all")
    ap.add_argument("--top-k", nargs="+", type=int, default=[10, 20, 50])
    ap.add_argument("--output", default="reports/topk_backtest_report.csv")
    args = ap.parse_args()
    root = Path(args.root)
    print("[1/3] Ensuring historical scorecard panel exists...")
    scorecard_path = root / "data/features/fundamental_training_scorecard_panel.parquet"
    if not scorecard_path.exists():
        score_panel(root / "data/features/fundamental_training_panel.parquet", scorecard_path)
    panel = read_table(scorecard_path)
    if args.model_dir:
        print("[2/3] Applying redesigned model to historical panel...")
        model_scored_path = root / "data/features/fundamental_training_model_v2_scored_panel.parquet"
        apply_redesigned_models(scorecard_path, root / args.model_dir, model_scored_path)
        panel = read_table(model_scored_path)
    else:
        print("[2/3] No model dir provided; using scorecard panel only.")
    print("[3/3] Running top-k backtest...")
    panel = _mode_filter(panel, args.mode)
    report = _run_topk(panel, args.score_col, args.return_col, args.top_k)
    out = root / args.output
    write_table(report, out, csv_copy=False)
    json_out = out.with_suffix(".json")
    ensure_dir(json_out.parent)
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(report.to_dicts(), f, indent=2, default=str)
    print("Done. Output:", out)
    print("JSON:", json_out)
    if report.height:
        print(report)


if __name__ == "__main__":
    main()
