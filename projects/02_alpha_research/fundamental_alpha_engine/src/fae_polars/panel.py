from __future__ import annotations

from pathlib import Path

import polars as pl

from .io import read_table, write_table
from .ohlcv import build_market_features
from .sectors import load_sector_mapping


def _parse_date_literal(value: str | None) -> pl.Expr:
    if not value:
        return pl.lit(None, dtype=pl.Date)
    return pl.lit(value).str.strptime(pl.Date, format="%Y-%m-%d", strict=False)


def _asof_join(base: pl.DataFrame, feat: pl.DataFrame, suffix: str = "") -> pl.DataFrame:
    if feat.is_empty() or "ticker" not in feat.columns or "as_of_date" not in feat.columns:
        return base
    # Polars may still warn that sortedness cannot be verified with `by`, but explicit
    # sorting keeps the point-in-time join deterministic.
    b = base.sort(["ticker", "as_of_date"])
    f = feat.sort(["ticker", "as_of_date"])
    return b.join_asof(f, on="as_of_date", by="ticker", strategy="backward", suffix=suffix)


def _overlay_current_keystats_for_inference(
    panel: pl.DataFrame,
    key: pl.DataFrame,
    inference_as_of_date: str | None,
) -> pl.DataFrame:
    """Overlay the latest keystats snapshot onto the latest market row for inference.

    Why this exists:
    - Backtests/training must use strict backward as-of joins.
    - Live inference often has a current keystats snapshot whose snapshot_date is newer
      than the latest OHLCV date in the local data bundle, e.g. keystats 2026-06-12
      and max OHLCV 2026-06-09.
    - Strict point-in-time join correctly leaves PE/PBV/ROE as null on 2026-06-09.
      For an inference run requested as of 2026-06-12, it is reasonable to overlay
      the latest keystats snapshot <= requested as_of_date onto the latest market row.

    This function only updates the latest panel date <= inference_as_of_date. It does
    not backfill historical rows, so it should not create large-scale look-ahead
    contamination in the training history. Still, for pure research/backtest runs,
    keep this option disabled unless you explicitly want current-snapshot inference.
    """
    if panel.is_empty() or key.is_empty() or not inference_as_of_date:
        return panel
    if "ticker" not in key.columns or "as_of_date" not in key.columns:
        return panel
    if "ticker" not in panel.columns or "as_of_date" not in panel.columns:
        return panel

    target_expr = _parse_date_literal(inference_as_of_date)
    latest_panel_date_df = panel.filter(pl.col("as_of_date") <= target_expr).select(pl.col("as_of_date").max().alias("latest_date"))
    if latest_panel_date_df.is_empty():
        return panel
    latest_panel_date = latest_panel_date_df.item()
    if latest_panel_date is None:
        return panel

    key_latest = (
        key.filter(pl.col("as_of_date") <= target_expr)
        .sort(["ticker", "as_of_date"])
        .group_by("ticker", maintain_order=True)
        .tail(1)
    )
    if key_latest.is_empty():
        return panel

    key_feature_cols = [c for c in key_latest.columns if c not in {"ticker", "as_of_date"}]
    if not key_feature_cols:
        return panel

    overlay = key_latest.rename({"as_of_date": "keystats_snapshot_date"})
    overlay = overlay.rename({c: f"__ks_overlay__{c}" for c in key_feature_cols})
    out = panel.join(overlay, on="ticker", how="left")

    latest_mask = pl.col("as_of_date") == pl.lit(latest_panel_date)
    updates: list[pl.Expr] = []
    for c in key_feature_cols:
        oc = f"__ks_overlay__{c}"
        if oc not in out.columns:
            continue
        if c in out.columns:
            updates.append(
                pl.when(latest_mask)
                .then(pl.coalesce([pl.col(c), pl.col(oc)]))
                .otherwise(pl.col(c))
                .alias(c)
            )
        else:
            updates.append(
                pl.when(latest_mask)
                .then(pl.col(oc))
                .otherwise(pl.lit(None))
                .alias(c)
            )
    if updates:
        out = out.with_columns(updates)

    # Keep a clear audit trail on the rows that were overlayed.
    out = out.with_columns(
        pl.when(latest_mask)
        .then(pl.col("keystats_snapshot_date"))
        .otherwise(pl.lit(None, dtype=pl.Date))
        .alias("keystats_snapshot_date")
    )
    drop_cols = [c for c in out.columns if c.startswith("__ks_overlay__")]
    if drop_cols:
        out = out.drop(drop_cols)
    return out


def build_signal_panel(
    financial_features_path: str | Path,
    keystats_features_path: str | Path,
    insider_features_path: str | Path,
    output_path: str | Path,
    ohlcv_path: str | Path | None = None,
    sector_path: str | Path | None = None,
    inference_as_of_date: str | None = None,
    current_keystats_overlay: bool = False,
) -> pl.DataFrame:
    fin = read_table(financial_features_path)
    key = read_table(keystats_features_path)
    ins = read_table(insider_features_path)
    market = build_market_features(ohlcv_path) if ohlcv_path else pl.DataFrame()

    if not market.is_empty():
        base = market.select(["ticker", "as_of_date", "close", "volume", "trading_value", "avg_value_20d", "return_1d", "return_20d", "return_60d", "volatility_20d"])
    else:
        bases = []
        for f in [fin, key, ins]:
            if not f.is_empty() and "ticker" in f.columns and "as_of_date" in f.columns:
                bases.append(f.select(["ticker", "as_of_date"]))
        base = pl.concat(bases, how="diagonal_relaxed").unique().sort(["ticker", "as_of_date"]) if bases else pl.DataFrame()
    if base.is_empty():
        write_table(base, output_path, csv_copy=True); return base

    out = _asof_join(base, fin, suffix="_fin")
    out = _asof_join(out, key, suffix="_key")
    if current_keystats_overlay:
        out = _overlay_current_keystats_for_inference(out, key, inference_as_of_date)
    out = _asof_join(out, ins, suffix="_ins")

    sec = load_sector_mapping(sector_path)
    if not sec.is_empty():
        out = out.join(sec, on="ticker", how="left")
    else:
        out = out.with_columns([
            pl.lit(None).alias("sector"), pl.lit(None).alias("subsector"), pl.lit(None).alias("industry"), pl.lit(None).alias("subindustry"),
        ])
    out = out.sort(["as_of_date", "ticker"])
    write_table(out, output_path, csv_copy=True)
    return out
