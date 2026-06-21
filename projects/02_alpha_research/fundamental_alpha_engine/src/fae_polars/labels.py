from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import polars as pl

from .io import read_table, write_table
from .ohlcv import load_ohlcv
from .sectors import load_sector_mapping


def _future_min(arr: np.ndarray, horizon: int) -> np.ndarray:
    """Minimum close in the next `horizon` observations, excluding current row."""
    s = pd.Series(arr, dtype="float64").shift(-1)
    return s.iloc[::-1].rolling(window=int(horizon), min_periods=1).min().iloc[::-1].to_numpy()


def _future_max(arr: np.ndarray, horizon: int) -> np.ndarray:
    """Maximum close in the next `horizon` observations, excluding current row."""
    s = pd.Series(arr, dtype="float64").shift(-1)
    return s.iloc[::-1].rolling(window=int(horizon), min_periods=1).max().iloc[::-1].to_numpy()


def _add_path_targets_for_ticker(g: pl.DataFrame, horizons: list[int], tp: float, stop: float) -> pl.DataFrame:
    g = g.sort("date")
    close = g["close"].to_numpy().astype(float)
    n = close.shape[0]
    cols: dict[str, np.ndarray] = {}
    for h in horizons:
        h = int(h)
        fwd_close = np.full(n, np.nan, dtype=float)
        if n > h:
            fwd_close[:-h] = close[h:]
        fwd_ret = fwd_close / close - 1.0
        fut_min = _future_min(close, h)
        fut_max = _future_max(close, h)
        fwd_dd = fut_min / close - 1.0
        fwd_runup = fut_max / close - 1.0
        cols[f"fwd_return_{h}d"] = fwd_ret
        cols[f"fwd_max_drawdown_{h}d"] = fwd_dd
        cols[f"fwd_max_runup_{h}d"] = fwd_runup
        cols[f"label_bad_drawdown_{h}d"] = np.where(np.isfinite(fwd_dd), (fwd_dd <= -abs(stop)).astype(np.int8), np.nan)
        # Path-quality proxy: future runup reaches take-profit and observed future minimum does not breach stop.
        # It is intentionally not named "before_stop" because exact event ordering is handled in later execution backtests.
        cols[f"label_hit_tp_without_stop_{h}d"] = np.where(
            np.isfinite(fwd_runup) & np.isfinite(fwd_dd),
            ((fwd_runup >= abs(tp)) & (fwd_dd > -abs(stop))).astype(np.int8),
            np.nan,
        )
    return g.with_columns([pl.Series(k, v) for k, v in cols.items()])


def build_forward_labels(
    ohlcv_path: str | Path,
    output_path: str | Path,
    horizons: list[int],
    threshold: float = 0.05,
    sector_path: str | Path | None = None,
    bad_drawdown_threshold: float = 0.15,
    takeprofit_threshold: float = 0.20,
) -> pl.DataFrame:
    """Build rank-first, risk-aware forward labels.

    New v5 labels include:
    - raw forward return
    - market excess return
    - sector excess return
    - path-dependent future max drawdown proxy
    - bad drawdown label
    - takeprofit-without-stop proxy
    - market/sector outperformance labels
    """
    ohlcv = load_ohlcv(ohlcv_path)
    if ohlcv.is_empty():
        out = pl.DataFrame(); write_table(out, output_path, csv_copy=True); return out
    df = ohlcv.sort(["ticker", "date"])
    # Path targets require forward min/max over each ticker time series.
    df = df.group_by("ticker", maintain_order=True).map_groups(
        lambda g: _add_path_targets_for_ticker(g, horizons, tp=takeprofit_threshold, stop=bad_drawdown_threshold)
    )
    df = df.rename({"date": "as_of_date"})

    sec = load_sector_mapping(sector_path)
    if not sec.is_empty():
        df = df.join(sec.select(["ticker", "sector", "subsector"]), on="ticker", how="left")
    else:
        df = df.with_columns([pl.lit(None).alias("sector"), pl.lit(None).alias("subsector")])

    for h in horizons:
        h = int(h)
        ret_col = f"fwd_return_{h}d"
        market = df.group_by("as_of_date").agg(pl.col(ret_col).mean().alias(f"fwd_market_return_{h}d"))
        df = df.join(market, on="as_of_date", how="left")
        df = df.with_columns([
            (pl.col(ret_col) - pl.col(f"fwd_market_return_{h}d")).alias(f"fwd_excess_market_{h}d"),
            (pl.col(ret_col) > pl.col(f"fwd_market_return_{h}d") + float(threshold)).cast(pl.Int8).alias(f"label_outperform_market_{h}d"),
            (pl.col(ret_col) > 0).cast(pl.Int8).alias(f"label_positive_return_{h}d"),
        ])
        sector_ret = df.group_by(["as_of_date", "sector"]).agg(pl.col(ret_col).mean().alias(f"fwd_sector_return_{h}d"))
        df = df.join(sector_ret, on=["as_of_date", "sector"], how="left")
        df = df.with_columns([
            (pl.col(ret_col) - pl.col(f"fwd_sector_return_{h}d")).alias(f"fwd_excess_sector_{h}d"),
            (pl.col(ret_col) > pl.col(f"fwd_sector_return_{h}d") + float(threshold)).cast(pl.Int8).alias(f"label_outperform_sector_{h}d"),
        ])
        # Risk-adjusted return target: reward sector excess, penalize large future drawdown.
        df = df.with_columns([
            (pl.col(f"fwd_excess_sector_{h}d") + 0.50 * pl.col(f"fwd_max_drawdown_{h}d")).alias(f"fwd_risk_adjusted_excess_sector_{h}d")
        ])

    keep = ["ticker", "as_of_date", "close", "sector", "subsector"]
    for h in horizons:
        h = int(h)
        keep += [
            f"fwd_return_{h}d", f"fwd_max_drawdown_{h}d", f"fwd_max_runup_{h}d",
            f"fwd_market_return_{h}d", f"fwd_excess_market_{h}d", f"label_outperform_market_{h}d",
            f"fwd_sector_return_{h}d", f"fwd_excess_sector_{h}d", f"fwd_risk_adjusted_excess_sector_{h}d", f"label_outperform_sector_{h}d",
            f"label_positive_return_{h}d", f"label_bad_drawdown_{h}d", f"label_hit_tp_without_stop_{h}d",
        ]
    out = df.select([c for c in keep if c in df.columns]).sort(["ticker", "as_of_date"])
    write_table(out, output_path, csv_copy=True)
    return out


def build_training_panel(panel_path: str | Path, labels_path: str | Path, output_path: str | Path) -> pl.DataFrame:
    panel = read_table(panel_path)
    labels = read_table(labels_path)
    if panel.is_empty() or labels.is_empty():
        out = pl.DataFrame(); write_table(out, output_path, csv_copy=True); return out
    drop = [c for c in labels.columns if c in panel.columns and c not in ["ticker", "as_of_date"]]
    lab = labels.drop(drop) if drop else labels
    out = panel.join(lab, on=["ticker", "as_of_date"], how="left")
    write_table(out, output_path, csv_copy=True)
    return out
