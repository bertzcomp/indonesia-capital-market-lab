from __future__ import annotations

from pathlib import Path

import polars as pl

from .io import read_table
from .parsing import normalize_ticker_expr


def load_sector_mapping(path: str | Path | None) -> pl.DataFrame:
    if not path:
        return pl.DataFrame()
    df = read_table(path)
    if df.is_empty():
        return df
    rename = {
        "KodeEmiten": "ticker",
        "NamaEmiten": "company_name",
        "Sektor": "sector",
        "SubSektor": "subsector",
        "Industri": "industry",
        "SubIndustri": "subindustry",
        "PapanPencatatan": "listing_board",
        "TanggalPencatatan": "listing_date",
    }
    existing = {k: v for k, v in rename.items() if k in df.columns}
    df = df.rename(existing)
    if "ticker" not in df.columns:
        return pl.DataFrame()
    keep = ["ticker", "company_name", "sector", "subsector", "industry", "subindustry", "listing_board", "listing_date"]
    for c in keep:
        if c not in df.columns:
            df = df.with_columns(pl.lit(None).alias(c))
    return df.with_columns(normalize_ticker_expr("ticker").alias("ticker")).filter(pl.col("ticker").is_not_null()).select(keep).unique("ticker", keep="last")
