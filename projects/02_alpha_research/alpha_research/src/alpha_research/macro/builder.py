from __future__ import annotations

"""Macro canonical builder.

This module is intentionally self-contained and does NOT depend on notebook/Colab code.
It implements the user's original macro approach as a first-class production builder:

- Frankfurter API for IDR -> USD (`idr_usd`) and derived `usd_idr`
- yfinance for WTI (`CL=F`), Brent (`BZ=F`), Coal proxy (`KOL`), and optional IHSG (`^JKSE`)
- BI rate from local file when available, otherwise hardcoded historical events
- Coal proxy post-KOL-gap filling using correlation to Brent by default
- Macro feature engineering with leakage-safe 1-day lag applied later in feature join by date

Output contracts:
- data/raw_canonical/macro.parquet: normalized macro raw/unified daily data
- data/features/macro/macro_features.parquet: engineered macro features

If external scraping fails, the builder falls back to market-derived macro from canonical OHLCV,
but this fallback is explicitly flagged with `macro_missing_flag = 1`.
"""

from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Optional
import json
import warnings

import numpy as np
import pandas as pd
import polars as pl


REAL_MACRO_COLS = {"idr_usd", "usd_idr", "wti", "brent", "coal_proxy", "bi_rate", "ihsg"}


@dataclass
class MacroConfig:
    start_date: str = "2015-01-01"
    end_date: Optional[str] = None
    mode: str = "auto"  # auto | local | scrape | fallback
    force: bool = False
    coal_fill_method: str = "correlation"
    bi_rate_path: Optional[str] = None


def _date_str(x: object) -> str:
    return pd.to_datetime(x).date().isoformat()


def _safe_read(path: Path) -> Optional[pd.DataFrame]:
    if not path.exists() or path.stat().st_size == 0:
        return None
    try:
        suf = path.suffix.lower()
        if suf == ".parquet":
            return pd.read_parquet(path)
        if suf in {".csv", ".txt"}:
            return pd.read_csv(path)
        if suf in {".xlsx", ".xls"}:
            return pd.read_excel(path)
    except Exception:
        return None
    return None


def _normalize_macro_frame(df: Optional[pd.DataFrame]) -> pd.DataFrame:
    if df is None or len(df) == 0:
        return pd.DataFrame(columns=["date"])
    df = df.copy()
    rename: Dict[Any, str] = {}
    for c in df.columns:
        lc = str(c).strip().lower().replace(" ", "_")
        if lc in {"date", "tanggal", "time", "datetime"}:
            rename[c] = "date"
        elif lc in {"idr_usd", "idr/usd", "idr_to_usd", "idrusd"}:
            rename[c] = "idr_usd"
        elif lc in {"usd_idr", "usd/idr", "usd_to_idr", "usdidr", "uidrtousd"}:
            # Some older naming was misleading. If values are around 15k, treat as USD/IDR.
            rename[c] = "usd_idr"
        elif lc in {"wti", "cl=f", "oil_wti", "wti_crude"}:
            rename[c] = "wti"
        elif lc in {"brent", "bz=f", "oil_brent", "brent_crude"}:
            rename[c] = "brent"
        elif lc in {"coal", "coal_proxy", "kol", "coal_index"}:
            rename[c] = "coal_proxy"
        elif lc in {"bi_rate", "policy_rate", "rate", "bi_7drr", "bi_7day_rr"}:
            rename[c] = "bi_rate"
        elif lc in {"ihsg", "jkse", "^jkse", "composite_index"}:
            rename[c] = "ihsg"
    if rename:
        df = df.rename(columns=rename)
    if "date" not in df.columns:
        return pd.DataFrame(columns=["date"])

    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
    df = df[df["date"].notna()].copy()

    for c in REAL_MACRO_COLS:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    if "usd_idr" not in df.columns and "idr_usd" in df.columns:
        df["usd_idr"] = 1.0 / df["idr_usd"].replace(0, np.nan)
    if "idr_usd" not in df.columns and "usd_idr" in df.columns:
        df["idr_usd"] = 1.0 / df["usd_idr"].replace(0, np.nan)

    # Prevent OHLCV/trading-summary from being accepted as macro by accident.
    macro_cols = [c for c in df.columns if c in REAL_MACRO_COLS]
    keep_cols = ["date"] + macro_cols + [c for c in ["macro_missing_flag"] if c in df.columns]
    out = df[keep_cols].sort_values("date").drop_duplicates("date", keep="last").reset_index(drop=True)
    return out


def _load_local_macro(root: Path) -> Optional[pd.DataFrame]:
    candidates = [
        root / "data/raw/macro/macro.parquet",
        root / "data/raw/macro/macro.csv",
        root / "data/raw/macro/macro_features.parquet",
        root / "data/processed/macro_features.parquet",
        root / "data/features/macro/macro_features.parquet",
        root / "data/raw_canonical/macro.parquet",
    ]
    for path in candidates:
        df = _safe_read(path)
        if df is None:
            continue
        macro = _normalize_macro_frame(df)
        if len(macro) and (set(macro.columns) & REAL_MACRO_COLS):
            return macro
    return None


def _download_yf_close(ticker: str, col: str, start: str, end: Optional[str]) -> pd.DataFrame:
    import yfinance as yf
    yf_end = (pd.to_datetime(end).date() + timedelta(days=1)).isoformat() if end else None
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message=".*Timestamp.utcnow.*")
        df = yf.download(ticker, start=start, end=yf_end, progress=False, auto_adjust=True)
    if df is None or len(df) == 0:
        return pd.DataFrame(columns=["date", col])
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    if "Close" not in df.columns:
        return pd.DataFrame(columns=["date", col])
    out = df[["Close"]].rename(columns={"Close": col}).reset_index()
    out = out.rename(columns={"Date": "date", "index": "date"})
    out["date"] = pd.to_datetime(out["date"], errors="coerce").dt.tz_localize(None).dt.date
    out[col] = pd.to_numeric(out[col], errors="coerce")
    return out[["date", col]].dropna(subset=["date"])


def _get_fx_frankfurter(start: str, end: Optional[str]) -> pd.DataFrame:
    import requests
    end_str = end or date.today().isoformat()
    url = f"https://api.frankfurter.app/{start}..{end_str}"
    last_err = None
    for i in range(3):
        try:
            r = requests.get(url, params={"from": "IDR", "to": "USD"}, timeout=30)
            r.raise_for_status()
            data = r.json()
            rows = [{"date": d, "idr_usd": v.get("USD")} for d, v in data.get("rates", {}).items()]
            df = pd.DataFrame(rows)
            if len(df) == 0:
                return pd.DataFrame(columns=["date", "idr_usd", "usd_idr"])
            df["date"] = pd.to_datetime(df["date"]).dt.date
            df["idr_usd"] = pd.to_numeric(df["idr_usd"], errors="coerce")
            df["usd_idr"] = 1.0 / df["idr_usd"].replace(0, np.nan)
            return df.sort_values("date")
        except Exception as e:
            last_err = e
    raise RuntimeError(f"Frankfurter FX failed: {last_err}")



def _parse_bps_bi_rate_json_file(path: Path) -> pd.DataFrame:
    """Parse one BPS WebAPI BI Rate JSON file.

    BPS datacontent keys are concatenations of:
        vervar + var + turvar + tahun + turtahun
    For BI Rate var 379, this yields keys such as 137901251 for Jan 2025,
    1379012510 for Oct 2025, etc.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return pd.DataFrame(columns=["date", "bi_rate"])
    if data.get("status") not in {"OK", "ok", "Ok"}:
        return pd.DataFrame(columns=["date", "bi_rate"])
    try:
        var = str(data.get("var", [{}])[0].get("val", "379"))
        vervar = str(data.get("vervar", [{}])[0].get("val", "1"))
        turvar = str(data.get("turvar", [{}])[0].get("val", "0"))
        tahun_code = str(data.get("tahun", [{}])[0].get("val"))
        year_label = str(data.get("tahun", [{}])[0].get("label"))
        year = int(year_label)
        contents = data.get("datacontent", {}) or {}
    except Exception:
        return pd.DataFrame(columns=["date", "bi_rate"])

    rows = []
    for tt in data.get("turtahun", []) or []:
        try:
            month = int(tt.get("val"))
        except Exception:
            continue
        if month < 1 or month > 12:
            continue
        key = f"{vervar}{var}{turvar}{tahun_code}{month}"
        val = contents.get(key)
        if val is None:
            # Fallback: some BPS payloads can stringify or omit part variations.
            candidates = [k for k in contents.keys() if str(k).endswith(f"{tahun_code}{month}")]
            val = contents.get(candidates[0]) if candidates else None
        try:
            rate = float(val)
        except Exception:
            continue
        rows.append({"date": pd.Timestamp(year=year, month=month, day=1).date(), "bi_rate": rate})
    return pd.DataFrame(rows)


def _load_bps_bi_rate_dir(root: Path, path: Optional[str] = None) -> pd.DataFrame:
    paths = []
    if path:
        p = Path(path)
        if p.is_dir():
            paths.extend(sorted(p.glob("*.json")))
        elif p.exists():
            paths.append(p)
    default_dir = root / "data/raw/bps_bi_rate"
    if default_dir.exists():
        paths.extend(sorted(default_dir.glob("bi_rate_*.json")))
    seen = set(); unique_paths = []
    for p in paths:
        if p not in seen:
            unique_paths.append(p); seen.add(p)
    frames = [_parse_bps_bi_rate_json_file(p) for p in unique_paths]
    frames = [f for f in frames if f is not None and len(f)]
    if not frames:
        return pd.DataFrame(columns=["date", "bi_rate"])
    out = pd.concat(frames, ignore_index=True)
    out["date"] = pd.to_datetime(out["date"], errors="coerce").dt.date
    out["bi_rate"] = pd.to_numeric(out["bi_rate"], errors="coerce")
    out = out.dropna(subset=["date", "bi_rate"]).sort_values("date").drop_duplicates("date", keep="last")
    return out[["date", "bi_rate"]]


def _download_bps_bi_rate(root: Path, api_key: str, years: list[int] | None = None, max_retry: int = 3) -> pd.DataFrame:
    """Download BI Rate yearly JSON from BPS WebAPI into data/raw/bps_bi_rate.

    This is intentionally conservative: sequential request, retry, and resume by file.
    """
    import random, time, requests
    if not api_key:
        return pd.DataFrame(columns=["date", "bi_rate"])
    if years is None:
        years = list(range(2015, date.today().year + 1))
    out_dir = root / "data/raw/bps_bi_rate"
    out_dir.mkdir(parents=True, exist_ok=True)
    # BPS `th` code mapping observed from user's reference: 2015 -> 115, 2026 -> 126.
    base_url = "https://webapi.bps.go.id/v1/api/list/model/data/lang/eng/domain/0000/var/379/th/{th}/key/{key}"
    for year in years:
        th = year - 1900
        fp = out_dir / f"bi_rate_{year}.json"
        if fp.exists() and fp.stat().st_size > 0:
            continue
        last_err = None
        for attempt in range(1, max_retry + 1):
            try:
                r = requests.get(base_url.format(th=th, key=api_key), timeout=30)
                if r.status_code == 200:
                    data = r.json()
                    if data.get("status") == "OK":
                        with open(fp, "w", encoding="utf-8") as f:
                            json.dump(data, f, ensure_ascii=False, indent=2)
                        break
                    last_err = RuntimeError(f"BPS status not OK for {year}: {data.get('status')}")
                else:
                    last_err = RuntimeError(f"HTTP {r.status_code} for {year}")
            except Exception as e:
                last_err = e
            time.sleep((2 ** attempt) + random.random())
        # Do not fail entire macro build for a single BPS year; local fallback/hardcoded can fill.
    return _load_bps_bi_rate_dir(root, str(out_dir))


def _get_bi_rate(root: Path, path: Optional[str] = None, bps_api_key: Optional[str] = None, download_bps: bool = False) -> pd.DataFrame:
    # 1) Explicit local file/directory or default data/raw/bps_bi_rate JSON cache.
    bps_local = _load_bps_bi_rate_dir(root, path)
    if len(bps_local):
        return bps_local

    # 2) Optional BPS download. Keep this explicit because it requires API key and network.
    if download_bps and bps_api_key:
        bps_downloaded = _download_bps_bi_rate(root, bps_api_key)
        if len(bps_downloaded):
            return bps_downloaded

    # 3) Generic local macro file containing bi_rate.
    if path:
        df = _safe_read(Path(path))
        norm = _normalize_macro_frame(df)
        if "bi_rate" in norm.columns and len(norm):
            return norm[["date", "bi_rate"]]

    # 4) Historical fallback events. Values are event-date levels; daily frame will ffill.
    events = pd.DataFrame({
        "date": pd.to_datetime([
            "2015-01-01", "2016-01-14", "2016-03-17", "2016-06-16", "2016-09-22",
            "2017-08-22", "2018-05-17", "2018-06-29", "2018-07-19", "2018-09-27",
            "2019-07-18", "2019-08-22", "2019-09-19", "2019-10-24", "2020-02-20",
            "2020-03-19", "2020-04-14", "2020-06-18", "2020-07-16", "2020-11-19",
            "2021-02-18", "2022-08-23", "2022-09-22", "2022-10-20", "2022-11-03",
            "2022-12-22", "2023-01-19", "2024-01-17", "2024-09-18", "2025-01-15",
            "2025-05-21",
        ]).date,
        "bi_rate": [
            7.75, 7.25, 6.75, 6.50, 5.00,
            4.25, 4.75, 5.25, 5.50, 5.75,
            5.75, 5.50, 5.25, 5.00, 4.75,
            4.50, 4.50, 4.25, 4.00, 3.75,
            3.50, 3.75, 4.25, 4.75, 5.25,
            5.50, 5.75, 6.00, 6.00, 5.75,
            5.50,
        ],
    })
    return events


def _scrape_macro(root: Path, start: str, end: Optional[str], coal_fill_method: str, bi_rate_path: Optional[str], bps_api_key: Optional[str] = None, download_bps: bool = False) -> pd.DataFrame:
    frames = []
    frames.append(_get_fx_frankfurter(start, end))
    frames.append(_download_yf_close("CL=F", "wti", start, end))
    frames.append(_download_yf_close("BZ=F", "brent", start, end))
    frames.append(_download_yf_close("KOL", "coal_proxy", start, end))
    frames.append(_download_yf_close("^JKSE", "ihsg", start, end))
    frames.append(_get_bi_rate(root, bi_rate_path, bps_api_key=bps_api_key, download_bps=download_bps))

    df = frames[0]
    for f in frames[1:]:
        if f is not None and len(f):
            df = df.merge(f, on="date", how="outer")
    df = _normalize_macro_frame(df)
    if len(df) == 0:
        raise RuntimeError("Macro scrape produced no rows.")
    df = _unify_daily(df, start, end, coal_fill_method=coal_fill_method)
    df["macro_missing_flag"] = 0
    return df


def _unify_daily(df: pd.DataFrame, start: str, end: Optional[str], coal_fill_method: str = "correlation") -> pd.DataFrame:
    s = pd.to_datetime(start).date()
    e = pd.to_datetime(end).date() if end else date.today()
    df = _normalize_macro_frame(df)
    if len(df) == 0:
        return pd.DataFrame({"date": pd.date_range(s, e, freq="D").date})
    df = df[(df["date"] >= s) & (df["date"] <= e)].copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").set_index("date").asfreq("D")

    for c in ["idr_usd", "usd_idr", "wti", "brent", "bi_rate", "ihsg"]:
        if c in df.columns:
            df[c] = df[c].ffill().bfill()

    if "coal_proxy" in df.columns:
        if coal_fill_method == "correlation" and "brent" in df.columns:
            has = df["coal_proxy"].notna() & df["brent"].notna()
            gap = df["coal_proxy"].isna() & df["brent"].notna()
            if has.sum() >= 100 and gap.sum() > 0:
                x = df.loc[has, "brent"].astype(float).values
                y = df.loc[has, "coal_proxy"].astype(float).values
                try:
                    b, a = np.polyfit(x, y, deg=1)
                    df.loc[gap, "coal_proxy"] = np.clip(a + b * df.loc[gap, "brent"].astype(float).values, 0, np.inf)
                    df["coal_gap_flag"] = gap.astype(int)
                except Exception:
                    df["coal_proxy"] = df["coal_proxy"].ffill()
                    df["coal_gap_flag"] = df["coal_proxy"].isna().astype(int)
            else:
                df["coal_gap_flag"] = df["coal_proxy"].isna().astype(int)
                df["coal_proxy"] = df["coal_proxy"].ffill().bfill()
        else:
            df["coal_gap_flag"] = df["coal_proxy"].isna().astype(int)
            df["coal_proxy"] = df["coal_proxy"].ffill().bfill()
    else:
        df["coal_proxy"] = np.nan
        df["coal_gap_flag"] = 1

    if "idr_usd" not in df.columns and "usd_idr" in df.columns:
        df["idr_usd"] = 1.0 / df["usd_idr"].replace(0, np.nan)
    if "usd_idr" not in df.columns and "idr_usd" in df.columns:
        df["usd_idr"] = 1.0 / df["idr_usd"].replace(0, np.nan)

    # derived raw macro returns
    if "wti" in df.columns and "brent" in df.columns:
        df["oil_avg"] = (df["wti"] + df["brent"]) / 2.0
    for c, ret in [("wti", "wti_return"), ("brent", "brent_return"), ("idr_usd", "fx_return"), ("coal_proxy", "coal_proxy_return")]:
        df[ret] = df[c].pct_change() if c in df.columns else np.nan
    df["bi_rate_change"] = df["bi_rate"].diff() if "bi_rate" in df.columns else np.nan
    out = df.reset_index().rename(columns={"index": "date"})
    out["date"] = pd.to_datetime(out["date"]).dt.date
    return out


def _fallback_market_macro(root: Path, start: str, end: Optional[str]) -> pd.DataFrame:
    ohlcv = root / "data/raw_canonical/ohlcv.parquet"
    s = pd.to_datetime(start).date()
    e = pd.to_datetime(end).date() if end else date.today()
    if not ohlcv.exists():
        return pd.DataFrame({"date": pd.date_range(s, e, freq="D").date, "macro_missing_flag": 1})
    df = pl.read_parquet(ohlcv).with_columns(pl.col("date").cast(pl.Date))
    df = df.filter((pl.col("date") >= pl.lit(s)) & (pl.col("date") <= pl.lit(e))).sort(["ticker", "date"])
    if df.is_empty():
        return pd.DataFrame({"date": pd.date_range(s, e, freq="D").date, "macro_missing_flag": 1})
    df = df.with_columns(pl.col("close").pct_change().over("ticker").alias("_stock_ret_1d"))
    val_expr = (pl.col("value").sum().alias("market_traded_value_proxy") if "value" in df.columns else (pl.col("close") * pl.col("volume")).sum().alias("market_traded_value_proxy"))
    m = df.group_by("date").agg([
        pl.col("_stock_ret_1d").mean().alias("market_ret_1d"),
        (pl.col("_stock_ret_1d") > 0).mean().alias("market_breadth_up"),
        pl.col("ticker").n_unique().alias("market_breadth_n"),
        val_expr,
    ]).sort("date")
    pdf = m.to_pandas()
    pdf["date"] = pd.to_datetime(pdf["date"]).dt.date
    pdf["macro_missing_flag"] = 1
    return pdf


def _engineer_macro(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy().sort_values("date").reset_index(drop=True)
    if len(df) == 0:
        return df
    if "macro_missing_flag" not in df.columns:
        df["macro_missing_flag"] = 0

    for c in ["idr_usd", "usd_idr", "wti", "brent", "coal_proxy", "bi_rate", "ihsg", "oil_avg", "market_ret_1d"]:
        if c not in df.columns:
            df[c] = np.nan
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Feature set aligned with old MacroFeatureEngineer but robust to missing sources.
    windows = [5, 10, 20, 60]
    if "fx_return" not in df.columns:
        df["fx_return"] = df["idr_usd"].pct_change()
    if "brent_return" not in df.columns:
        df["brent_return"] = df["brent"].pct_change()
    if "wti_return" not in df.columns:
        df["wti_return"] = df["wti"].pct_change()
    if "coal_proxy_return" not in df.columns:
        df["coal_proxy_return"] = df["coal_proxy"].pct_change()
    if "bi_rate_change" not in df.columns:
        df["bi_rate_change"] = df["bi_rate"].diff()

    for w in windows:
        df[f"idr_usd_ret_{w}d"] = df["idr_usd"].pct_change(w)
        df[f"idr_usd_vol_{w}d"] = df["fx_return"].rolling(w, min_periods=max(3, w // 4)).std()
        df[f"brent_ret_{w}d"] = df["brent"].pct_change(w)
        df[f"wti_ret_{w}d"] = df["wti"].pct_change(w)
        df[f"oil_avg_ret_{w}d"] = df["oil_avg"].pct_change(w)
        df[f"brent_vol_{w}d"] = df["brent_return"].rolling(w, min_periods=max(3, w // 4)).std()
        df[f"coal_ret_{w}d"] = df["coal_proxy"].pct_change(w)
        df[f"coal_vol_{w}d"] = df["coal_proxy_return"].rolling(w, min_periods=max(3, w // 4)).std()
        df[f"ihsg_ret_{w}d"] = df["ihsg"].pct_change(w)

    roll60_mean = df["usd_idr"].rolling(60, min_periods=20).mean()
    roll60_std = df["usd_idr"].rolling(60, min_periods=20).std()
    df["usd_idr_zscore"] = (df["usd_idr"] - roll60_mean) / (roll60_std + 1e-9)
    df["idr_weak_flag"] = (df["usd_idr_zscore"] > 1.5).astype("int8")
    df["idr_strong_flag"] = (df["usd_idr_zscore"] < -1.5).astype("int8")

    for c in ["brent", "coal_proxy", "ihsg"]:
        mean = df[c].rolling(60, min_periods=20).mean()
        std = df[c].rolling(60, min_periods=20).std()
        df[f"{c}_zscore"] = (df[c] - mean) / (std + 1e-9)

    df["oil_crash_flag"] = (df["brent_ret_20d"] < -0.15).astype("int8")
    df["oil_rally_flag"] = (df["brent_ret_20d"] > 0.15).astype("int8")
    df["wti_brent_spread"] = df["wti"] - df["brent"]
    df["coal_rally_flag"] = (df["coal_proxy_zscore"] > 1.0).astype("int8")
    df["coal_slump_flag"] = (df["coal_proxy_zscore"] < -1.0).astype("int8")
    df["bi_rate_change"] = df["bi_rate_change"].fillna(0)
    df["bi_rate_cut_flag"] = (df["bi_rate_change"] < 0).astype("int8")
    df["bi_rate_hike_flag"] = (df["bi_rate_change"] > 0).astype("int8")

    if df["market_ret_1d"].isna().all():
        df["market_ret_1d"] = df["ihsg"].pct_change()
    df["market_ret_5d"] = df["market_ret_1d"].rolling(5, min_periods=2).sum()
    df["market_ret_20d"] = df["market_ret_1d"].rolling(20, min_periods=5).sum()
    df["market_volatility_20d"] = df["market_ret_1d"].rolling(20, min_periods=5).std()

    df["oil_idr_divergence"] = df["brent_ret_20d"].fillna(0) + df["idr_usd_ret_20d"].fillna(0)
    df["coal_oil_spread_ret"] = df["coal_ret_20d"].fillna(0) - df["brent_ret_20d"].fillna(0)

    bi_fill = df["bi_rate"].median() if df["bi_rate"].notna().any() else 6.0
    df["macro_risk_score"] = (
        -df["usd_idr_zscore"].fillna(0) * 0.30
        -df["brent_vol_20d"].fillna(0) * 100.0 * 0.20
        +df["brent_ret_20d"].fillna(0) * 0.20
        -df["bi_rate"].fillna(bi_fill) / 10.0 * 0.30
        +df["market_ret_20d"].fillna(0) * 0.20
    )
    mn = df["macro_risk_score"].expanding(min_periods=60).mean()
    sd = df["macro_risk_score"].expanding(min_periods=60).std()
    df["macro_risk_zscore"] = ((df["macro_risk_score"] - mn) / (sd + 1e-9)).clip(-3, 3) / 3.0
    df["market_regime"] = pd.cut(df["macro_risk_zscore"], [-np.inf, -0.33, 0.33, np.inf], labels=["risk_off", "neutral", "risk_on"]).astype(str)

    num = df.select_dtypes(include=[np.number]).columns
    df[num] = df[num].replace([np.inf, -np.inf], np.nan)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df.sort_values("date").drop_duplicates("date", keep="last").reset_index(drop=True)


def build_macro_features(root: str | Path, start_date: str, end_date: Optional[str] = None,
                         mode: str = "auto", force: bool = False,
                         bi_rate_path: Optional[str] = None,
                         coal_fill_method: str = "correlation",
                         bps_api_key: Optional[str] = None,
                         download_bps: bool = False) -> Dict[str, Any]:
    root = Path(root)
    raw_dir = root / "data/raw_canonical"
    raw_dir.mkdir(parents=True, exist_ok=True)
    feat_dir = root / "data/features/macro"
    feat_dir.mkdir(parents=True, exist_ok=True)
    out_raw = raw_dir / "macro.parquet"
    out_feat = feat_dir / "macro_features.parquet"

    if out_feat.exists() and out_raw.exists() and not force:
        try:
            existing = pl.read_parquet(out_feat)
            if not existing.is_empty():
                return {"table": "macro", "source": "existing", "rows": existing.height, "cols": existing.width,
                        "min_date": str(existing.select(pl.col("date").min()).item()),
                        "max_date": str(existing.select(pl.col("date").max()).item()), "path": str(out_raw), "features_path": str(out_feat)}
        except Exception:
            pass

    source = None
    macro: Optional[pd.DataFrame] = None
    mode = (mode or "auto").lower()

    if mode in {"auto", "local"}:
        macro = _load_local_macro(root)
        if macro is not None and len(macro) and (set(macro.columns) & REAL_MACRO_COLS):
            source = "local"
        elif mode == "local":
            raise RuntimeError("No valid local macro source found in data/raw/macro or data/processed.")

    if macro is None and mode in {"auto", "scrape"}:
        try:
            macro = _scrape_macro(root, start_date, end_date, coal_fill_method=coal_fill_method, bi_rate_path=bi_rate_path)
            source = "scraped"
        except Exception as e:
            if mode == "scrape":
                raise
            warnings.warn(f"Real macro scrape failed; falling back to market-derived macro. Reason: {e}")

    if macro is None:
        macro = _fallback_market_macro(root, start_date, end_date)
        source = "fallback_market"

    if source != "fallback_market":
        macro = _unify_daily(macro, start_date, end_date, coal_fill_method=coal_fill_method)
        if "macro_missing_flag" not in macro.columns:
            macro["macro_missing_flag"] = 0

    features = _engineer_macro(macro)
    raw_pl = pl.from_pandas(macro).with_columns(pl.col("date").cast(pl.Date, strict=False))
    feat_pl = pl.from_pandas(features).with_columns(pl.col("date").cast(pl.Date, strict=False))
    raw_pl.write_parquet(out_raw)
    feat_pl.write_parquet(out_feat)
    meta = {"table": "macro", "source": source, "rows": feat_pl.height, "cols": feat_pl.width,
            "min_date": str(feat_pl.select(pl.col("date").min()).item()) if feat_pl.height else None,
            "max_date": str(feat_pl.select(pl.col("date").max()).item()) if feat_pl.height else None,
            "path": str(out_raw), "features_path": str(out_feat),
            "macro_missing_rows": int(feat_pl.select(pl.col("macro_missing_flag").fill_null(0).sum()).item()) if "macro_missing_flag" in feat_pl.columns and feat_pl.height else None}
    (feat_dir / "macro_manifest.json").write_text(json.dumps(meta, indent=2, default=str))
    return meta


# Backward compatible wrapper used by existing feature-store code.
def build_macro(root, start_date, end_date=None, scrape=False, force=False, **kwargs):
    mode = "scrape" if scrape else kwargs.pop("mode", "auto")
    return build_macro_features(root, start_date, end_date, mode=mode, force=force, **kwargs)
