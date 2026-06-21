"""
=============================================================================
FILE 1: DATA LOADER, CLEANER & PREPROCESSOR
=============================================================================
BEI/IDX Quantitative Trading System
Handles all raw data ingestion, cleaning, and adjusted price computation.

Usage:
    from data_loader import BEIDataLoader
    loader = BEIDataLoader(base_path="/content/drive/MyDrive/BEI_Data")
    master_df = loader.build_master_dataset()
=============================================================================
"""

import os
import re
import json
import glob
import warnings
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("BEIDataLoader")


# CONSTANTS
BROKER_COMMISSION_RATE = 0.0015   # 0.15% buy commission (typical BEI)
SELL_TAX_RATE = 0.0025             # 0.25% sell (commission + final tax)
IDX_TRADE_DAYS_PER_YEAR = 245      # approximate trading days/year on BEI

CA_TYPE_SPLIT  = "Stock Split"
CA_TYPE_DIV    = "Dividen Tunai"
CA_TYPE_WARRANT = "Waran"


# HELPER UTILITIES
def parse_flexible_date(date_str: str) -> Optional[pd.Timestamp]:
    """Try multiple date formats common in BEI datasets."""
    formats = [
        "%Y-%m-%d", "%d %b %Y", "%d/%m/%Y",
        "%d-%m-%Y", "%b %d, %Y", "%d %B %Y",
    ]
    for fmt in formats:
        try:
            return pd.Timestamp(datetime.strptime(str(date_str).strip(), fmt))
        except ValueError:
            continue
    try:
        return pd.Timestamp(date_str)
    except Exception:
        return None


def safe_numeric(series: pd.Series) -> pd.Series:
    """Convert series to numeric, replacing errors with NaN."""
    return pd.to_numeric(series, errors="coerce")


# MODULE 1A: OHLCV LOADER
class OHLCVLoader:
    """
    Loads all OHLCV files (saham + IHSG) from a directory.
    Handles: 1.95M+ rows, multiple yearly CSVs, zero-open anomalies.
    """

    def __init__(self, ohlcv_dir: str, ihsg_path: str):
        self.ohlcv_dir = Path(ohlcv_dir)
        self.ihsg_path = Path(ihsg_path)

    def _clean_ohlcv(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date", "ticker"])
        df["ticker"] = df["ticker"].str.strip().str.upper()

        for col in ["open", "high", "low", "close", "volume"]:
            if col in df.columns:
                df[col] = safe_numeric(df[col])

        # Replace zero opens with close (common BEI data issue – no pre-market)
        df.loc[df["open"] == 0, "open"] = df.loc[df["open"] == 0, "close"]

        # Sanity: drop rows where close <= 0
        df = df[df["close"] > 0]
        return df

    def load_stocks(self) -> pd.DataFrame:
        """Load all yearly OHLCV CSVs from ohlcv_dir."""
        all_files = sorted(glob.glob(str(self.ohlcv_dir / "*.csv")))
        if not all_files:
            raise FileNotFoundError(f"No CSV files found in {self.ohlcv_dir}")

        frames = []
        for fp in all_files:
            try:
                df = pd.read_csv(fp, low_memory=False)
                df = self._clean_ohlcv(df)
                frames.append(df)
                logger.info(f"  Loaded {len(df):,} rows from {Path(fp).name}")
            except Exception as e:
                logger.warning(f"  Skipped {fp}: {e}")

        combined = pd.concat(frames, ignore_index=True)
        # Deduplicate: keep last entry per (date, ticker)
        combined = combined.sort_values("date")
        combined = combined.drop_duplicates(subset=["date", "ticker"], keep="last")
        logger.info(f"OHLCV total: {len(combined):,} rows, {combined['ticker'].nunique()} tickers")
        return combined

    def load_ihsg(self) -> pd.DataFrame:
        """Load IHSG index data."""
        df = pd.read_csv(self.ihsg_path, low_memory=False)
        df = self._clean_ohlcv(df)
        df["ticker"] = "IHSG"
        logger.info(f"IHSG loaded: {len(df):,} rows")
        return df


# MODULE 1B: CORPORATE ACTIONS LOADER
class CorporateActionsLoader:
    """
    Loads and parses Corporate Actions (CA) file.
    Supports: Stock Split, Dividen Tunai, Waran.
    """

    def __init__(self, ca_path: str):
        self.ca_path = Path(ca_path)

    def load(self) -> pd.DataFrame:
        df = pd.read_csv(self.ca_path, low_memory=False)

        # Normalize columns
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

        # Expected: Date, Emiten Code, Type of Corporate Action, Amount, Total Amount
        rename_map = {}
        for col in df.columns:
            if "date" in col:
                rename_map[col] = "ca_date"
            elif "emiten" in col or "code" in col:
                rename_map[col] = "ticker"
            elif "type" in col:
                rename_map[col] = "ca_type"
            elif "amount" in col and "total" not in col:
                rename_map[col] = "ca_amount"
            elif "total" in col:
                rename_map[col] = "ca_total"
        df = df.rename(columns=rename_map)

        df["ca_date"] = df["ca_date"].apply(parse_flexible_date)
        df = df.dropna(subset=["ca_date", "ticker"])
        df["ticker"] = df["ticker"].str.strip().str.upper()
        df["ca_amount"] = safe_numeric(df.get("ca_amount", pd.Series(dtype=float)))
        df = df.sort_values("ca_date")

        logger.info(f"Corporate Actions loaded: {len(df):,} rows")
        return df


# MODULE 1C: ADJUSTED PRICE CALCULATOR
class AdjustedPriceCalculator:
    """
    Computes Adjusted Close Price retroactively using Corporate Actions.

    Rules (applied from most-recent event backwards):
      - Stock Split: Adjusted = Close / Split_Ratio  (retroactive to all prior dates)
      - Cash Dividend: Adjusted = Close - Dividend_Amount (on ex-date and prior)

    No look-ahead: adjustments are computed once at load time, not in the event loop.
    """

    def compute(self, ohlcv_df: pd.DataFrame, ca_df: pd.DataFrame) -> pd.DataFrame:
        """
        Returns ohlcv_df with a new column `adj_close`.
        """
        ohlcv = ohlcv_df.copy()
        ohlcv = ohlcv.sort_values(["ticker", "date"])
        ohlcv["adj_close"] = ohlcv["close"].astype(float)

        tickers_with_ca = ca_df["ticker"].unique()

        for ticker in tickers_with_ca:
            ticker_ca = ca_df[ca_df["ticker"] == ticker].sort_values("ca_date")
            mask = ohlcv["ticker"] == ticker
            if not mask.any():
                continue

            # Walk events from latest to earliest (retroactive adjustment)
            cumulative_split_ratio = 1.0

            for _, event in ticker_ca.sort_values("ca_date", ascending=False).iterrows():
                ca_date = event["ca_date"]
                ca_type = str(event.get("ca_type", "")).strip()
                ca_amount = float(event.get("ca_amount", 1) or 1)

                prior_mask = mask & (ohlcv["date"] < ca_date)

                if CA_TYPE_SPLIT.lower() in ca_type.lower():
                    # e.g., split 1:5 means ca_amount = 5.0
                    ratio = ca_amount if ca_amount > 0 else 1.0
                    cumulative_split_ratio *= ratio
                    ohlcv.loc[prior_mask, "adj_close"] = (
                        ohlcv.loc[prior_mask, "adj_close"] / ratio
                    )
                    logger.debug(
                        f"  {ticker} Split x{ratio} on {ca_date.date()}: "
                        f"{prior_mask.sum()} rows adjusted"
                    )

                elif CA_TYPE_DIV.lower() in ca_type.lower():
                    # Subtract dividend from all prices prior to ex-date
                    div_amount = ca_amount if ca_amount > 0 else 0.0
                    # Adjust by ratio to preserve relative changes
                    # Standard: factor = (close_pre - div) / close_pre
                    # For simplicity, subtract nominal amount
                    ohlcv.loc[prior_mask, "adj_close"] = (
                        ohlcv.loc[prior_mask, "adj_close"] - div_amount
                    ).clip(lower=0.01)

        logger.info("Adjusted Close Price computation complete.")
        return ohlcv


# MODULE 1D: SECTOR & EMITEN MAPPER
class SectorMapper:
    """
    Loads sector / sub-sector mapping from stocksectors.json or allCompanies.json.
    Returns a dict: ticker -> {Sektor, SubSektor, Industri, SubIndustri}
    """

    def __init__(self, sectors_path: str):
        self.sectors_path = Path(sectors_path)

    def load(self) -> pd.DataFrame:
        with open(self.sectors_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        df = pd.DataFrame(data)

        # Normalize column names
        col_map = {}
        for col in df.columns:
            c = col.strip()
            if c in ("KodeEmiten", "kode_emiten"):
                col_map[col] = "ticker"
            else:
                col_map[col] = c
        df = df.rename(columns=col_map)
        df["ticker"] = df["ticker"].str.strip().str.upper()
        logger.info(f"Sector mapping: {len(df):,} emitens")
        return df


# MODULE 1E: MARKET CAP LOADER
class MarketCapLoader:
    """
    Loads all market cap CSV files and returns a tidy DataFrame.
    """

    def __init__(self, market_cap_dir: str):
        self.dir = Path(market_cap_dir)

    def load(self) -> pd.DataFrame:
        all_files = sorted(glob.glob(str(self.dir / "*.csv")))
        frames = []
        for fp in all_files:
            try:
                df = pd.read_csv(fp, low_memory=False)
                frames.append(df)
            except Exception as e:
                logger.warning(f"  Skipped market cap file {fp}: {e}")

        if not frames:
            logger.warning("No market cap files found.")
            return pd.DataFrame()

        df = pd.concat(frames, ignore_index=True)
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["ticker"] = df["ticker"].str.strip().str.upper()
        df["market_cap"] = safe_numeric(df.get("market_cap", pd.Series(dtype=float)))
        df["listed_shares"] = safe_numeric(df.get("listed_shares", pd.Series(dtype=float)))
        df = df.dropna(subset=["date", "ticker"])
        df = df.drop_duplicates(subset=["date", "ticker"], keep="last")
        logger.info(f"Market Cap loaded: {len(df):,} rows")
        return df


# MODULE 1F: MACROECONOMICS LOADER
class MacroLoader:
    """
    Loads: USD/IDR, Brent Oil, Coal Newcastle, BI 7-Day Repo Rate.
    Returns a single merged daily DataFrame with forward-filled values.
    """

    def __init__(
        self,
        usdidr_path: str,
        brent_path: str,
        coal_path: str,
        bi_rate_path: str,
    ):
        self.usdidr_path = Path(usdidr_path)
        self.brent_path = Path(brent_path)
        self.coal_path = Path(coal_path)
        self.bi_rate_path = Path(bi_rate_path)

    def _load_usdidr(self) -> pd.DataFrame:
        df = pd.read_csv(self.usdidr_path)
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])
        df = df.rename(columns={"close": "usdidr"})
        df["usdidr"] = safe_numeric(df["usdidr"])
        return df[["date", "usdidr"]].dropna()

    def _load_brent(self) -> pd.DataFrame:
        df = pd.read_csv(self.brent_path)
        df.columns = [c.strip() for c in df.columns]
        date_col = [c for c in df.columns if "date" in c.lower() or "observation" in c.lower()][0]
        val_col  = [c for c in df.columns if c != date_col][0]
        df = df.rename(columns={date_col: "date", val_col: "brent_usd"})
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["brent_usd"] = safe_numeric(df["brent_usd"])
        return df[["date", "brent_usd"]].dropna()

    def _load_coal(self) -> pd.DataFrame:
        df = pd.read_csv(self.coal_path)
        df.columns = [c.strip() for c in df.columns]
        date_col = [c for c in df.columns if "date" in c.lower() or "observation" in c.lower()][0]
        val_col  = [c for c in df.columns if c != date_col][0]
        df = df.rename(columns={date_col: "date", val_col: "coal_usd"})
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["coal_usd"] = safe_numeric(df["coal_usd"])
        return df[["date", "coal_usd"]].dropna()

    def _load_bi_rate(self) -> pd.DataFrame:
        df = pd.read_csv(self.bi_rate_path)
        df.columns = [c.strip() for c in df.columns]
        date_col = df.columns[0]
        rate_col = df.columns[1]
        df = df.rename(columns={date_col: "date", rate_col: "bi_rate_pct"})
        df["date"] = df["date"].apply(parse_flexible_date)
        # Handle "4,75%" format
        df["bi_rate_pct"] = (
            df["bi_rate_pct"]
            .astype(str)
            .str.replace("%", "", regex=False)
            .str.replace(",", ".", regex=False)
            .pipe(safe_numeric)
        )
        return df[["date", "bi_rate_pct"]].dropna().sort_values("date")

    def load(self) -> pd.DataFrame:
        """
        Returns a daily macro DataFrame, forward-filled to cover all trading days.
        Monthly Brent/Coal and irregular BI rate are upsampled.
        """
        usdidr = self._load_usdidr()
        brent  = self._load_brent()
        coal   = self._load_coal()
        bi     = self._load_bi_rate()

        # Create a daily date range
        min_date = pd.Timestamp("2015-01-01")
        max_date = pd.Timestamp("2026-12-31")
        daily_idx = pd.date_range(min_date, max_date, freq="D")
        macro = pd.DataFrame({"date": daily_idx})

        for df, name in [(usdidr, "usdidr"), (brent, "brent_usd"), (coal, "coal_usd"), (bi, "bi_rate_pct")]:
            df = df.drop_duplicates("date").set_index("date")
            df = df.reindex(daily_idx)
            macro[name] = df[df.columns[0]].values

        # Forward fill (no future data leakage – ffill is correct here)
        macro = macro = macro.ffill().bfill()
        logger.info(f"Macro data assembled: {len(macro):,} daily rows")
        return macro


# MODULE 1G: BANDARMOLOGI LOADER
class BandarmologiLoader:
    """
    Loads 120 broker summary files (CSV or JSON).
    Extracts: date range, ticker, net_foreign_buy_sell, net_nonfin_buy_sell.
    """

    def __init__(self, bdm_dir: str):
        self.dir = Path(bdm_dir)

    def _parse_file(self, fp: str) -> Optional[pd.DataFrame]:
        fp = Path(fp)
        try:
            if fp.suffix.lower() == ".csv":
                df = pd.read_csv(fp, low_memory=False)
            elif fp.suffix.lower() == ".json":
                with open(fp, "r", encoding="utf-8") as f:
                    data = json.load(f)
                df = pd.DataFrame(data) if isinstance(data, list) else pd.DataFrame([data])
            else:
                return None

            df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

            # Try to identify key columns
            ticker_cols   = [c for c in df.columns if "ticker" in c or "kode" in c or "emiten" in c]
            date_cols     = [c for c in df.columns if "date" in c or "tanggal" in c]
            foreign_cols  = [c for c in df.columns if "foreign" in c or "asing" in c]
            nonret_cols   = [c for c in df.columns if "non_ret" in c or "institusi" in c or "nonritel" in c]

            if not ticker_cols:
                return None

            df = df.rename(columns={ticker_cols[0]: "ticker"})
            df["ticker"] = df["ticker"].astype(str).str.strip().str.upper()

            if date_cols:
                df["date"] = pd.to_datetime(df[date_cols[0]], errors="coerce")
            else:
                # Extract date from filename: e.g., bdm_2024_01.csv
                date_match = re.search(r"(\d{4})[_\-](\d{2})", fp.stem)
                if date_match:
                    yr, mo = date_match.group(1), date_match.group(2)
                    df["date"] = pd.Timestamp(f"{yr}-{mo}-01")
                else:
                    df["date"] = pd.NaT

            # Net foreign flow (positive = net buy, negative = net sell)
            if foreign_cols:
                df["net_foreign"] = safe_numeric(df[foreign_cols[0]])
            else:
                df["net_foreign"] = np.nan

            if nonret_cols:
                df["net_nonfin"] = safe_numeric(df[nonret_cols[0]])
            else:
                df["net_nonfin"] = np.nan

            return df[["date", "ticker", "net_foreign", "net_nonfin"]].dropna(subset=["date", "ticker"])

        except Exception as e:
            logger.warning(f"  BDM parse error {fp.name}: {e}")
            return None

    def load(self) -> pd.DataFrame:
        all_files = (
            list(glob.glob(str(self.dir / "*.csv"))) +
            list(glob.glob(str(self.dir / "*.json")))
        )
        frames = [self._parse_file(f) for f in all_files]
        frames = [f for f in frames if f is not None and len(f) > 0]

        if not frames:
            logger.warning("No bandarmologi files loaded.")
            return pd.DataFrame(columns=["date", "ticker", "net_foreign", "net_nonfin"])

        df = pd.concat(frames, ignore_index=True)
        df = df.drop_duplicates(subset=["date", "ticker"], keep="last")
        logger.info(f"Bandarmologi loaded: {len(df):,} rows")
        return df


# MASTER DATA BUILDER
class BEIDataLoader:
    """
    Orchestrates all data loading and returns a single master DataFrame
    joined on (date, ticker).

    Master DataFrame columns (non-exhaustive):
        date, ticker, open, high, low, close, volume,
        adj_close, market_cap, listed_shares,
        Sektor, SubSektor, Industri, SubIndustri,
        usdidr, brent_usd, coal_usd, bi_rate_pct,
        net_foreign, net_nonfin
    """

    def __init__(self, base_path: str):
        self.base = Path(base_path)

        # FIXED PATH CONFIGURATION

        # OHLCV folder
        self.ohlcv_dir = self.base / "ohlcv"

        # IHSG file (langsung di root)
        self.ihsg_path = self.base / "ihsg.csv"

        # Corporate Actions (langsung di root)
        self.ca_path = self.base / "corporate_actions.csv"

        # Sector mapping (langsung di root)
        self.sectors_path = self.base / "stocks_sectors.json"

        # Market cap (kalau belum ada, biarkan kosong)
        self.mcap_dir = self.base / "listed_shares"

        # Macro
        self.usdidr_path = self.base / "macro" / "usdidr.csv"
        self.brent_path  = self.base / "macro" / "brent.csv"
        self.coal_path   = self.base / "macro" / "coal.csv"
        self.bi_rate_path = self.base / "macro" / "bi_rate.csv"

        # Bandarmologi
        self.bdm_dir = self.base / "bandarmologi"

    def build_master_dataset(
        self,
        start_date: str = "2015-01-01",
        end_date: str   = "2026-03-08",
    ) -> pd.DataFrame:

        logger.info("=" * 60)
        logger.info("Starting BEI Master Dataset Build")
        logger.info("=" * 60)

        # 1. OHLCV
        ohlcv_loader  = OHLCVLoader(self.ohlcv_dir, self.ihsg_path)
        stocks_df     = ohlcv_loader.load_stocks()
        ihsg_df       = ohlcv_loader.load_ihsg()
        ohlcv_df      = pd.concat([stocks_df, ihsg_df], ignore_index=True)

        # 2. Corporate Actions → Adjusted Close
        ca_loader     = CorporateActionsLoader(self.ca_path)
        ca_df         = ca_loader.load()
        adj_calc      = AdjustedPriceCalculator()
        ohlcv_df      = adj_calc.compute(ohlcv_df, ca_df)

        # 3. Sector Mapping
        sector_mapper = SectorMapper(self.sectors_path)
        sector_df     = sector_mapper.load()
        ohlcv_df      = ohlcv_df.merge(sector_df, on="ticker", how="left")

        # 4. Market Cap
        mcap_loader   = MarketCapLoader(self.mcap_dir)
        mcap_df       = mcap_loader.load()
        if not mcap_df.empty:
            ohlcv_df  = ohlcv_df.merge(
                mcap_df[["date", "ticker", "market_cap", "listed_shares"]],
                on=["date", "ticker"], how="left"
            )

        # 5. Macro
        macro_loader  = MacroLoader(
            self.usdidr_path, self.brent_path, self.coal_path, self.bi_rate_path
        )
        macro_df      = macro_loader.load()
        ohlcv_df      = ohlcv_df.merge(macro_df, on="date", how="left")

        # 6. Bandarmologi (monthly summary → merge on nearest date)
        bdm_loader    = BandarmologiLoader(self.bdm_dir)
        bdm_df        = bdm_loader.load()
        if not bdm_df.empty:
            ohlcv_df  = pd.merge_asof(
                ohlcv_df.sort_values("date"),
                bdm_df.sort_values("date"),
                on="date",
                by="ticker",
                direction="backward",
                tolerance=pd.Timedelta("35 days"),
            )

        # 7. Date filter
        ohlcv_df["date"] = pd.to_datetime(ohlcv_df["date"])
        ohlcv_df = ohlcv_df[
            (ohlcv_df["date"] >= start_date) &
            (ohlcv_df["date"] <= end_date)
        ]

        # 8. Final sort and reset
        ohlcv_df = ohlcv_df.sort_values(["date", "ticker"]).reset_index(drop=True)

        # 9. Derived columns
        ohlcv_df["daily_return"] = ohlcv_df.groupby("ticker")["adj_close"].pct_change()
        ohlcv_df["intraday_move"] = (ohlcv_df["close"] - ohlcv_df["open"]) / ohlcv_df["open"].replace(0, np.nan)

        logger.info(f"Master dataset ready: {len(ohlcv_df):,} rows × {ohlcv_df.shape[1]} columns")
        logger.info(f"  Tickers  : {ohlcv_df['ticker'].nunique()}")
        logger.info(f"  Date range: {ohlcv_df['date'].min().date()} → {ohlcv_df['date'].max().date()}")
        logger.info("=" * 60)

        return ohlcv_df


# ENTRY POINT (for standalone testing)
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="BEI Data Loader")
    parser.add_argument("--base", type=str, default="/content/drive/MyDrive/Finance/filter_news/claude/data/",
                        help="Base path to data directory")
    parser.add_argument("--start", type=str, default="2015-01-01")
    parser.add_argument("--end",   type=str, default="2026-03-08")
    parser.add_argument("--output", type=str, default="master_dataset.parquet",
                        help="Output file path (.parquet or .csv)")
    args = parser.parse_args()

    loader = BEIDataLoader(base_path=args.base)
    master = loader.build_master_dataset(start_date=args.start, end_date=args.end)

    if args.output.endswith(".parquet"):
        master.to_parquet(args.output, index=False)
    else:
        master.to_csv(args.output, index=False)

    print(f"\nSaved to: {args.output}")
    print(master.head(5).to_string())