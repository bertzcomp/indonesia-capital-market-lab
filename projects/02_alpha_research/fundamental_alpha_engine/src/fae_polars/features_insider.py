from __future__ import annotations

from pathlib import Path

import polars as pl

from .io import read_table, write_table


def _window_agg(events: pl.DataFrame, base: pl.DataFrame, window_days: int) -> pl.DataFrame:
    ev = events.rename({"available_date": "event_available_date", "date": "event_date"})
    joined = base.join(ev, on="ticker", how="left").filter(
        (pl.col("event_available_date").is_not_null())
        & (pl.col("event_available_date") <= pl.col("as_of_date"))
        & (pl.col("event_available_date") >= (pl.col("as_of_date") - pl.duration(days=window_days)))
    )
    if joined.is_empty():
        return base.select(["ticker", "as_of_date"]).with_columns([
            pl.lit(0).alias(f"insider_buy_count_{window_days}d"),
            pl.lit(0).alias(f"insider_sell_count_{window_days}d"),
            pl.lit(0.0).alias(f"insider_net_trade_value_{window_days}d"),
            pl.lit(0.0).alias(f"insider_net_shares_changed_{window_days}d"),
            pl.lit(0.0).alias(f"insider_net_shares_changed_pct_{window_days}d"),
            pl.lit(0).alias(f"insider_unique_buyers_{window_days}d"),
            pl.lit(0).alias(f"insider_unique_sellers_{window_days}d"),
        ])
    return joined.group_by(["ticker", "as_of_date"]).agg([
        (pl.col("action_type") == "BUY").sum().alias(f"insider_buy_count_{window_days}d"),
        (pl.col("action_type") == "SELL").sum().alias(f"insider_sell_count_{window_days}d"),
        (pl.col("action_type") == "TRANSFER").sum().alias(f"insider_transfer_count_{window_days}d"),
        (pl.col("action_type") == "CROSS").sum().alias(f"insider_cross_count_{window_days}d"),
        pl.col("signed_trade_value").sum().alias(f"insider_net_trade_value_{window_days}d"),
        pl.col("trade_value").filter(pl.col("action_type") == "BUY").sum().alias(f"insider_gross_buy_value_{window_days}d"),
        pl.col("trade_value").filter(pl.col("action_type") == "SELL").sum().alias(f"insider_gross_sell_value_{window_days}d"),
        pl.col("signed_shares_changed").sum().alias(f"insider_net_shares_changed_{window_days}d"),
        pl.col("signed_shares_changed_pct").sum().alias(f"insider_net_shares_changed_pct_{window_days}d"),
        pl.col("insider_name").filter(pl.col("action_type") == "BUY").n_unique().alias(f"insider_unique_buyers_{window_days}d"),
        pl.col("insider_name").filter(pl.col("action_type") == "SELL").n_unique().alias(f"insider_unique_sellers_{window_days}d"),
        pl.col("signed_trade_value").filter(pl.col("nationality") == "FOREIGN").sum().alias(f"insider_foreign_net_value_{window_days}d"),
        pl.col("signed_trade_value").filter(pl.col("nationality") == "LOCAL").sum().alias(f"insider_local_net_value_{window_days}d"),
    ])


def build_insider_features(input_path: str | Path, output_path: str | Path, windows: list[int], as_of_date: str | None = None) -> pl.DataFrame:
    events = read_table(input_path)
    if events.is_empty():
        out = pl.DataFrame(); write_table(out, output_path, csv_copy=True); return out
    events = events.filter(pl.col("ticker").is_not_null() & pl.col("available_date").is_not_null()).sort(["ticker", "available_date"])
    if as_of_date:
        target_expr = pl.lit(as_of_date).str.strptime(pl.Date, format="%Y-%m-%d", strict=False)
        base = events.select("ticker").unique().with_columns(target_expr.alias("as_of_date"))
    else:
        base = events.select(["ticker", pl.col("available_date").alias("as_of_date")]).unique().sort(["ticker", "as_of_date"])
    out = base
    for w in windows:
        feat = _window_agg(events, base, int(w))
        out = out.join(feat, on=["ticker", "as_of_date"], how="left")
    # Fill null numeric windows with zero.
    out = out.with_columns([pl.col(c).fill_null(0) for c in out.columns if c not in ["ticker", "as_of_date"]]).sort(["ticker", "as_of_date"])
    write_table(out, output_path, csv_copy=True)
    return out
