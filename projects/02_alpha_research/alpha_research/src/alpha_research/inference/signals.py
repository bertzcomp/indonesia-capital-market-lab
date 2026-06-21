from __future__ import annotations
from pathlib import Path
import polars as pl
from alpha_research.core.io import write_json


def _latest_base_score(root):
    files = sorted((Path(root) / "signals/live").glob("base_scores_*.parquet"))
    if not files:
        raise FileNotFoundError("No base score parquet")
    return files[-1]


def _date_folder(target_date):
    import datetime as dt
    d = dt.date.fromisoformat(str(target_date))
    return f"signal_{d.day:02d}_{d.strftime('%b').lower()}_{d.year}"


def _ensure_score_cols(df: pl.DataFrame) -> pl.DataFrame:
    score_cols = [
        "score_sm", "score_ara", "score_scalp", "score_swing", "score_position",
        "score_mm_silent", "score_mm_big",
        "score_momentum_5d", "score_momentum_10d", "score_momentum_20d",
    ]
    for c in score_cols:
        if c not in df.columns:
            df = df.with_columns(pl.lit(0.0).alias(c))
    return df


def build_daily_signals(root, target_date, top_k_final=30, max_per_rank1_buyer=5):
    root = Path(root)
    p = _latest_base_score(root)
    df = pl.read_parquet(p)
    df = _ensure_score_cols(df)
    mm_score = pl.max_horizontal([pl.col("score_mm_silent"), pl.col("score_mm_big")])
    horizon_score = pl.max_horizontal([pl.col("score_scalp"), pl.col("score_swing"), pl.col("score_position")])
    momentum_score = pl.max_horizontal([pl.col("score_momentum_5d"), pl.col("score_momentum_10d"), pl.col("score_momentum_20d")])
    df = df.with_columns([
        mm_score.alias("score_mm"),
        horizon_score.alias("horizon_score"),
        momentum_score.alias("score_momentum"),
    ])
    df = df.with_columns(
        (0.38 * pl.col("score_sm") +
         0.12 * pl.col("score_ara") +
         0.15 * pl.col("score_mm") +
         0.20 * pl.col("horizon_score") +
         0.15 * pl.col("score_momentum")).alias("final_signal_score")
    )
    df = df.with_columns(
        pl.when((pl.col("score_swing") >= pl.col("score_scalp")) & (pl.col("score_swing") >= pl.col("score_position"))).then(pl.lit("swing"))
        .when(pl.col("score_position") >= pl.col("score_scalp")).then(pl.lit("position"))
        .otherwise(pl.lit("scalp")).alias("strategy_tag")
    )
    df = df.with_columns(
        pl.when(pl.col("strategy_tag") == "scalp").then(3)
        .when(pl.col("strategy_tag") == "swing").then(10)
        .otherwise(20).alias("suggested_hold_days")
    )
    df = df.with_columns(
        (pl.when(pl.col("score_sm") >= 0.60).then(pl.lit("SM_CONFIRMED|")).otherwise(pl.lit("")) +
         pl.when(pl.col("score_ara") >= 0.65).then(pl.lit("ARA_BOOST|")).otherwise(pl.lit("")) +
         pl.when(pl.col("score_mm") >= 0.60).then(pl.lit("MM_WATCH|")).otherwise(pl.lit("")) +
         pl.when(pl.col("score_momentum") >= 0.65).then(pl.lit("MOMENTUM_BOOST|")).otherwise(pl.lit(""))).alias("reason_codes")
    )
    df = df.with_columns(
        pl.when(pl.col("traded_value_proxy").fill_null(0) < 1_000_000_000).then(pl.lit("LOWER_LIQUIDITY")).otherwise(pl.lit("OK")).alias("risk_flags")
    )

    ranked = df.sort("final_signal_score", descending=True)
    rows, counts = [], {}
    for r in ranked.iter_rows(named=True):
        b = r.get("rank1_buyer") or "UNKNOWN"
        if counts.get(b, 0) >= max_per_rank1_buyer:
            continue
        rows.append(r)
        counts[b] = counts.get(b, 0) + 1
        if len(rows) >= top_k_final:
            break
    main = pl.DataFrame(rows) if rows else ranked.head(top_k_final)

    outdir = root / "signals/daily" / _date_folder(target_date)
    outdir.mkdir(parents=True, exist_ok=True)
    all_scores = df.sort("final_signal_score", descending=True)
    all_scores.write_csv(outdir / "all_scores.csv")
    main.write_csv(outdir / "signals_main.csv")
    main.filter((pl.col("risk_flags") == "OK") & (pl.col("score_sm") >= 0.75) & (pl.col("final_signal_score") >= 0.55)).write_csv(outdir / "execution_shortlist.csv")
    df.sort("score_sm", descending=True).head(50).write_csv(outdir / "sm_tracker_signal.csv")
    df.sort("score_ara", descending=True).head(50).write_csv(outdir / "ara_predict_signal.csv")
    df.sort("score_mm", descending=True).head(50).write_csv(outdir / "market_maker_signal.csv")
    df.sort("horizon_score", descending=True).head(50).write_csv(outdir / "multi_strategy_time_signal.csv")
    df.sort("score_momentum", descending=True).head(50).write_csv(outdir / "momentum_ranker_signal.csv")
    diag = {
        "target_date": target_date,
        "input_base_scores": str(p),
        "all_scores_rows": df.height,
        "signals_main_rows": main.height,
        "rank1_buyer_counts": main.group_by("rank1_buyer").len().sort("len", descending=True).to_dicts() if "rank1_buyer" in main.columns else [],
        "score_columns": [c for c in df.columns if c.startswith("score_")],
    }
    write_json(outdir / "diagnostics.json", diag)
    (outdir / "report.md").write_text(f"# Daily Signal Report\n\nTarget date: {target_date}\n\nRows: {main.height}\n", encoding="utf-8")
    return {"output_dir": str(outdir), **diag}
