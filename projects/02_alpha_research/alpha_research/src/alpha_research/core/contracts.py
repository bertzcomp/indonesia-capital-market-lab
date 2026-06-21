from __future__ import annotations
import polars as pl

PANEL_KEY = ["date", "ticker"]


def normalize_date_ticker(df: pl.DataFrame, ticker_col: str = "ticker") -> pl.DataFrame:
    exprs = []
    if "date" in df.columns:
        exprs.append(pl.col("date").cast(pl.Date, strict=False).alias("date"))
    if ticker_col in df.columns:
        exprs.append(
            pl.col(ticker_col)
            .cast(pl.Utf8, strict=False)
            .str.to_uppercase()
            .str.strip_chars()
            .alias(ticker_col)
        )
    return df.with_columns(exprs) if exprs else df


def assert_unique(df: pl.DataFrame, keys: list[str], name: str):
    if df is None or df.is_empty():
        return
    missing = [k for k in keys if k not in df.columns]
    if missing:
        raise KeyError(f"[{name}] missing key columns: {missing}. columns={df.columns}")
    dup = df.group_by(keys).len().filter(pl.col("len") > 1)
    if dup.height:
        raise ValueError(
            f"[{name}] not unique on {keys}. duplicate groups={dup.height}. sample={dup.head(10)}"
        )


def _normalize_join_keys(df: pl.DataFrame, keys: list[str]) -> pl.DataFrame:
    exprs = []
    if "date" in keys and "date" in df.columns:
        exprs.append(pl.col("date").cast(pl.Date, strict=False).alias("date"))
    if "ticker" in keys and "ticker" in df.columns:
        exprs.append(
            pl.col("ticker")
            .cast(pl.Utf8, strict=False)
            .str.to_uppercase()
            .str.strip_chars()
            .alias("ticker")
        )
    return df.with_columns(exprs) if exprs else df


def safe_left_join(
    left: pl.DataFrame,
    right: pl.DataFrame,
    keys: list[str],
    name: str,
    *,
    left_unique_keys: list[str] | None = None,
    assert_right_unique: bool = True,
) -> pl.DataFrame:
    """Safe many-to-one left join.

    Important semantics:
    - The *right* side must be unique on the join keys, otherwise a row explosion can occur.
    - The *left* side is allowed to be many-to-one for date-level joins, e.g.
      macro date table joined to ticker-date panel on ["date"].
    - Row count must stay unchanged.
    - If the left table is a ticker-date panel, output uniqueness on ["date", "ticker"]
      is asserted after the join.

    This fixes the historical bug where joining macro on ["date"] failed because
    the left ticker-date panel is naturally not unique on date.
    """
    if right is None or right.is_empty():
        return left

    l = _normalize_join_keys(left, keys)
    r = _normalize_join_keys(right, keys)

    if assert_right_unique:
        assert_unique(r, keys, f"right_{name}")

    if left_unique_keys is not None:
        l = _normalize_join_keys(l, left_unique_keys)
        assert_unique(l, left_unique_keys, f"left_before_{name}")

    before = left.height
    out = l.join(r, on=keys, how="left")

    if out.height != before:
        raise ValueError(f"[{name}] row count changed {before}->{out.height}; right side may not be unique on {keys}")

    if all(k in out.columns for k in PANEL_KEY):
        assert_unique(out, PANEL_KEY, f"after_{name}")

    return out
