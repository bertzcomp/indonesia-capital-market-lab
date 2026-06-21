from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import pandas as pd


TICKER_RE = re.compile(r"\b[A-Z]{4}\b")
WS_RE = re.compile(r"\s+")

CAPITAL_STOPWORDS = {
    "PADA", "DARI", "IHSG", "RUPS", "BUMN", "ESDM", "APBN", "APBD", "RUPST",
    "POJK", "OJK", "IDX", "BEI", "KSEI", "YANG", "DENGAN", "UNTUK", "DALAM",
    "ATAU", "JUGA", "AKAN", "SUDAH", "OLEH", "ATAS", "AGAR", "BAGI", "SAAT",
    "SAJA", "HARGA", "TAHUN", "BULAN", "PASAR", "MODAL", "SAHAM", "EMITEN",
    "DIREKSI", "KOMISARIS", "RUPIAH", "DIVIDEN", "BURSA", "BANK", "DANA",
    "BELI", "JUAL", "NAIK", "TURUN", "LABA", "RUGI", "KURS", "NILAI", "RATA",
    "TOTAL", "HASIL", "CHINA", "IRAN", "USDI", "AI", "CASA"
}

BUY_TERMS = [
    "borong", "diborong", "akumulasi", "mengakumulasi", "menambah", "membeli",
    "pembelian", "net buy", "nilai beli", "diakumulasi", "masuk kembali",
]
SELL_TERMS = [
    "dilepas", "melepas", "distribusi", "jual", "penjualan", "net sell",
    "nilai jual", "aksi jual", "foreign outflow", "outflow",
]
NEGATIVE_TERMS = [
    "delisting", "pailit", "bangkrut", "suspensi", "uma", "gagal bayar", "rugi",
    "melemah", "merosot", "anjlok", "turun", "tekanan", "sanksi", "perkara", "gugatan",
]
POSITIVE_TERMS = [
    "dividen", "laba", "tumbuh", "meningkat", "kontrak", "ekspansi", "buyback",
    "kinerja positif", "fundamental kuat", "sinyal beli", "akuisisi", "rekomendasi beli",
]
UNCERTAINTY_TERMS = [
    "ketidakpastian", "volatil", "volatilitas", "risiko", "ancaman", "potensi", "belum jelas",
    "konflik", "geopolitik", "selat hormuz", "iran", "perang", "krisis", "tekanan global",
]

EVENT_PATTERNS: list[tuple[str, list[str]]] = [
    ("delisting_bankruptcy", ["delisting", "pailit", "bangkrut", "dicoret", "penghapusan pencatatan"]),
    ("suspension_uma", ["suspensi", "uma", "unusual market activity"]),
    ("dividend", ["dividen", "cum dividen", "ex dividen", "pembayaran dividen"]),
    ("insider_accumulation", ["president director", "direktur", "komisaris", "pengendali", "menambah kepemilikan", "mengakumulasi saham"]),
    ("retail_flow", ["investor ritel", "ritel", "broker xl", "stockbit sekuritas"]),
    ("foreign_flow", ["asing", "foreign", "net foreign", "foreign outflow", "aksi jual asing"]),
    ("earnings", ["laba bersih", "pendapatan", "kinerja", "laporan keuangan", "margin bersih"]),
    ("analyst_view", ["analis", "proyeksi", "rekomendasi", "target harga", "riset"]),
    ("corporate_action", ["rights issue", "private placement", "stock split", "waran", "rups", "akuisisi", "merger"]),
    ("currency_shock", ["rupiah", "dolar", "usd/idr", "kurs", "mata uang"]),
    ("rate_policy", ["bi rate", "suku bunga", "the fed", "fed rate", "yield"]),
    ("commodity_shock", ["batu bara", "batubara", "coal", "nikel", "emas", "cpo", "minyak", "brent", "harga plastik", "petrokimia"]),
    ("geopolitical_risk", ["konflik", "timur tengah", "iran", "selat hormuz", "geopolitik", "perang"]),
    ("market_index", ["ihsg", "indeks", "bursa", "ftse", "msci", "pasar saham"]),
    ("macro_policy", ["pemerintah", "ojk", "bei", "apbn", "kebijakan", "regulasi", "adb", "bank dunia"]),
]


@dataclass(frozen=True)
class BuildConfig:
    root: Path
    news_paths: list[Path]
    emiten_path: Path | None = None
    ohlcv_path: Path | None = None
    output_dir: Path | None = None
    entry_rule: str = "next_trading_day"
    horizons: tuple[int, ...] = (1, 3, 5, 10)
    alpha_threshold: float = 0.01
    vol_shock_threshold: float = 1.50


def _clean_text(x: Any) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return ""
    return WS_RE.sub(" ", str(x).replace("\u00a0", " ")).strip()


def _read_json_any(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    first = text.lstrip()[:1]
    if first == "[" or first == "{":
        return json.loads(text)
    return [json.loads(line) for line in text.splitlines() if line.strip()]


def load_news(paths: Iterable[Path]) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for p in paths:
        obj = _read_json_any(p)
        if isinstance(obj, dict) and "data" in obj:
            obj = obj["data"]
        if not isinstance(obj, list):
            raise ValueError(f"News JSON must be a list or dict with data: {p}")
        df = pd.DataFrame(obj)
        if df.empty:
            continue
        df["__source_file"] = str(p)
        frames.append(df)
    if not frames:
        return pd.DataFrame(columns=["title", "date", "source", "full_content", "summary"])
    df = pd.concat(frames, ignore_index=True)
    for c in ["title", "source", "full_content", "summary"]:
        if c not in df.columns:
            df[c] = ""
        df[c] = df[c].map(_clean_text)
    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
    df = df.dropna(subset=["date"]).copy()
    df["text"] = (df["title"] + ". " + df["summary"] + ". " + df["full_content"]).map(_clean_text)
    df["article_id"] = [
        hashlib.sha1(f"{d}|{s}|{t}".encode("utf-8")).hexdigest()[:16]
        for d, s, t in zip(df["date"], df["source"], df["title"])
    ]
    # Deduplicate exact repeated articles across exports.
    df = df.drop_duplicates(subset=["article_id"]).sort_values(["date", "source", "title"]).reset_index(drop=True)
    return df


def load_emiten_metadata(path: Path | None) -> pd.DataFrame:
    if path is None:
        return pd.DataFrame(columns=["ticker", "company_name", "sector", "subsector", "industry", "listing_board", "listing_date"])
    obj = _read_json_any(path)
    if isinstance(obj, dict) and "data" in obj:
        obj = obj["data"]
    df = pd.DataFrame(obj)
    rename = {
        "KodeEmiten": "ticker",
        "NamaEmiten": "company_name",
        "Sektor": "sector",
        "SubSektor": "subsector",
        "Industri": "industry",
        "PapanPencatatan": "listing_board",
        "TanggalPencatatan": "listing_date",
    }
    df = df.rename(columns={k: v for k, v in rename.items() if k in df.columns})
    for c in ["ticker", "company_name", "sector", "subsector", "industry", "listing_board"]:
        if c not in df.columns:
            df[c] = ""
        df[c] = df[c].map(_clean_text)
    if "listing_date" in df.columns:
        df["listing_date"] = pd.to_datetime(df["listing_date"], errors="coerce").dt.date
    else:
        df["listing_date"] = pd.NaT
    df["ticker"] = df["ticker"].str.upper().str.strip()
    return df.drop_duplicates("ticker").reset_index(drop=True)


def _window_around(text: str, token: str, width: int = 320) -> str:
    idx = text.find(token)
    if idx < 0:
        idx = text.upper().find(token.upper())
    if idx < 0:
        return text[:width]
    return text[max(0, idx - width): idx + len(token) + width]


def _contains_any(text: str, terms: list[str]) -> bool:
    low = text.lower()
    return any(term in low for term in terms)


def _term_present(text: str, term: str) -> bool:
    low = text.lower()
    if term.isalnum() and len(term) <= 4:
        return re.search(rf"(?<![a-z0-9]){re.escape(term.lower())}(?![a-z0-9])", low) is not None
    return term.lower() in low


def _has_ticker_context(text: str, ticker: str) -> bool:
    idxs = [m.start() for m in re.finditer(rf"(?<![A-Z]){re.escape(ticker)}(?![A-Z])", text)]
    if not idxs:
        return False
    low = text.lower()
    context_terms = ["saham", "emiten", "pt ", " tbk", "kode", "harga", "dividen", "akumulasi", "diborong", "dilepas", "beli", "jual"]
    for idx in idxs:
        w = low[max(0, idx-80): idx+len(ticker)+80]
        if any(term in w for term in context_terms):
            return True
    return False


def _count_terms(text: str, terms: list[str]) -> int:
    low = text.lower()
    return sum(low.count(term) for term in terms)


def extract_tickers(text: str, title: str, valid_tickers: set[str]) -> list[str]:
    candidates = []
    for t in TICKER_RE.findall(title or ""):
        if t not in CAPITAL_STOPWORDS and t in valid_tickers and t not in candidates:
            candidates.append(t)
    for t in TICKER_RE.findall(text or ""):
        if t in CAPITAL_STOPWORDS or t not in valid_tickers or t in candidates:
            continue
        if _has_ticker_context(text, t):
            candidates.append(t)
    return candidates


def classify_event_for_row(title: str, text: str, ticker: str | None, sector: str | None) -> dict[str, Any]:
    full_low = f"{title}. {text}".lower()
    context = _window_around(text, ticker, 420) if ticker else f"{title}. {text[:900]}"
    ctx_low = context.lower()

    event_type = "other_market_news"
    for name, terms in EVENT_PATTERNS:
        if any(_term_present(ctx_low, term) for term in terms) or any(_term_present(full_low, term) for term in terms):
            event_type = name
            break

    buy_score = _count_terms(context, BUY_TERMS)
    sell_score = _count_terms(context, SELL_TERMS)
    pos_score = _count_terms(context, POSITIVE_TERMS)
    neg_score = _count_terms(context, NEGATIVE_TERMS)
    uncertainty_score = _count_terms(context + " " + title, UNCERTAINTY_TERMS)

    event_side = "neutral"
    impact_channel = "informational"

    if event_type == "retail_flow":
        if buy_score > sell_score:
            event_side = "bullish_flow"
            impact_channel = "retail_flow_accumulation"
        elif sell_score > buy_score:
            event_side = "bearish_flow"
            impact_channel = "retail_flow_distribution"
        else:
            event_side = "mixed_flow"
            impact_channel = "retail_flow_mixed"
    elif event_type == "foreign_flow":
        if sell_score > buy_score or "outflow" in ctx_low:
            event_side = "bearish_flow"
        elif buy_score > sell_score:
            event_side = "bullish_flow"
        else:
            event_side = "mixed_flow"
        impact_channel = "foreign_flow"
    elif event_type == "insider_accumulation":
        event_side = "bullish_flow" if buy_score >= sell_score else "mixed_flow"
        impact_channel = "insider_ownership_change"
    elif event_type in {"delisting_bankruptcy", "suspension_uma"}:
        event_side = "bearish_risk"
        impact_channel = "tradability_distress"
    elif event_type == "dividend":
        event_side = "mixed_to_bullish"
        impact_channel = "cash_distribution"
    elif event_type == "earnings":
        event_side = "bullish_fundamental" if pos_score >= neg_score else "bearish_fundamental"
        impact_channel = "fundamental"
    elif event_type == "analyst_view":
        event_side = "bullish_view" if (pos_score + buy_score) >= (neg_score + sell_score) else "bearish_view"
        impact_channel = "analyst_narrative"
    elif event_type == "currency_shock":
        # Context-aware: USD/Rupiah strength is usually broad IDX/EM risk-off unless export/commodity hedge.
        if any(x in full_low for x in ["dolar menguat", "rupiah melemah", "usd/idr naik", "kurs melemah"]):
            event_side = "bearish_macro"
        elif any(x in full_low for x in ["rupiah menguat", "dolar melemah"]):
            event_side = "bullish_macro"
        else:
            event_side = "mixed_macro"
        impact_channel = "currency_risk"
    elif event_type in {"geopolitical_risk", "rate_policy", "macro_policy", "market_index"}:
        event_side = "risk_event" if uncertainty_score or neg_score > pos_score else "mixed_macro"
        impact_channel = "macro_regime"
    elif event_type == "commodity_shock":
        s = (sector or "").lower()
        energy = any(x in s for x in ["energi", "batu bara", "minyak", "gas"])
        if any(x in full_low for x in ["naik", "melonjak", "menguat", "kenaikan"]):
            event_side = "bullish_sector" if energy else "cost_pressure"
        elif any(x in full_low for x in ["turun", "melemah", "penurunan"]):
            event_side = "bearish_sector" if energy else "cost_relief"
        else:
            event_side = "mixed_sector"
        impact_channel = "commodity_input_output"
    else:
        if pos_score > neg_score:
            event_side = "bullish_textual"
        elif neg_score > pos_score:
            event_side = "bearish_textual"

    materiality_score = 0
    if event_type in {"delisting_bankruptcy", "suspension_uma", "currency_shock", "geopolitical_risk"}:
        materiality_score += 2
    if event_type in {"dividend", "insider_accumulation", "earnings", "retail_flow", "foreign_flow", "commodity_shock"}:
        materiality_score += 1
    if any(x in ctx_low for x in ["triliun", "miliar", "persen", "%", "yoy", "year on year"]):
        materiality_score += 1
    if ticker:
        materiality_score += 1

    materiality = "high" if materiality_score >= 3 else ("medium" if materiality_score >= 1 else "low")
    uncertainty = "high" if uncertainty_score >= 2 else ("medium" if uncertainty_score == 1 else "low")

    return {
        "event_type": event_type,
        "event_side": event_side,
        "impact_channel": impact_channel,
        "materiality": materiality,
        "uncertainty": uncertainty,
        "context_text": _clean_text(context)[:700],
    }


def build_event_store(news_df: pd.DataFrame, emiten_df: pd.DataFrame) -> pd.DataFrame:
    valid_tickers = set(emiten_df["ticker"].dropna().astype(str).str.upper()) if not emiten_df.empty else set()
    meta = emiten_df.set_index("ticker").to_dict("index") if not emiten_df.empty else {}
    rows: list[dict[str, Any]] = []

    for _, row in news_df.iterrows():
        title = row.get("title", "")
        text = row.get("text", "")
        tickers = extract_tickers(text, title, valid_tickers) if valid_tickers else []
        if not tickers:
            # Keep macro/market-wide news even without explicit ticker.
            tickers = [None]

        for ticker in tickers:
            m = meta.get(ticker, {}) if ticker else {}
            cls = classify_event_for_row(title, text, ticker, m.get("sector"))
            scope = "ticker" if ticker else "market"
            if cls["event_type"] in {"currency_shock", "rate_policy", "geopolitical_risk", "macro_policy", "market_index"}:
                scope = "market" if ticker is None else "ticker_via_macro"
            elif cls["event_type"] == "commodity_shock" and ticker is None:
                scope = "sector"
            rows.append({
                "article_id": row["article_id"],
                "news_date": row["date"],
                "source": row.get("source", ""),
                "title": title,
                "summary": row.get("summary", ""),
                "ticker": ticker,
                "company_name": m.get("company_name"),
                "sector": m.get("sector"),
                "subsector": m.get("subsector"),
                "industry": m.get("industry"),
                "listing_board": m.get("listing_board"),
                "listing_date": m.get("listing_date"),
                "event_scope": scope,
                **cls,
            })
    return pd.DataFrame(rows)


def _read_table(path: Path) -> pd.DataFrame:
    suf = path.suffix.lower()
    if suf == ".parquet":
        return pd.read_parquet(path)
    if suf == ".csv":
        return pd.read_csv(path)
    if suf in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    raise ValueError(f"Unsupported table format: {path}")


def _normalize_ohlcv(ohlcv: pd.DataFrame, emiten_df: pd.DataFrame | None = None) -> pd.DataFrame:
    rename = {c: c.lower() for c in ohlcv.columns}
    ohlcv = ohlcv.rename(columns=rename).copy()
    required = ["date", "ticker", "open", "high", "low", "close", "volume"]
    missing = [c for c in required if c not in ohlcv.columns]
    if missing:
        raise ValueError(f"OHLCV missing required columns: {missing}")
    ohlcv["date"] = pd.to_datetime(ohlcv["date"], errors="coerce").dt.date
    ohlcv["ticker"] = ohlcv["ticker"].astype(str).str.upper().str.strip()
    for c in ["open", "high", "low", "close", "volume"]:
        ohlcv[c] = pd.to_numeric(ohlcv[c], errors="coerce")
    before = len(ohlcv)
    ohlcv = ohlcv.dropna(subset=["date", "ticker", "close"]).copy()
    ohlcv = ohlcv.sort_values(["ticker", "date"]).drop_duplicates(["ticker", "date"], keep="last")

    if emiten_df is not None and not emiten_df.empty and "listing_date" in emiten_df.columns:
        lmap = emiten_df[["ticker", "listing_date"]].dropna().drop_duplicates("ticker")
        ohlcv = ohlcv.merge(lmap, on="ticker", how="left")
        mask = ohlcv["listing_date"].isna() | (ohlcv["date"] >= ohlcv["listing_date"])
        ohlcv = ohlcv.loc[mask].drop(columns=["listing_date"])

    ohlcv["is_zero_volume"] = ohlcv["volume"].fillna(0).eq(0)
    ohlcv["ret_1d"] = ohlcv.groupby("ticker")["close"].pct_change()
    ohlcv["pre_vol_20d"] = ohlcv.groupby("ticker")["ret_1d"].transform(lambda s: s.rolling(20, min_periods=5).std())
    ohlcv.attrs["dropped_rows"] = before - len(ohlcv)
    return ohlcv


def _add_forward_outcomes(ohlcv: pd.DataFrame, horizons: tuple[int, ...], emiten_df: pd.DataFrame) -> pd.DataFrame:
    df = ohlcv.sort_values(["ticker", "date"]).copy()
    for h in horizons:
        df[f"fwd_ret_{h}d"] = df.groupby("ticker")["close"].shift(-h) / df["close"] - 1.0
    for h in [x for x in horizons if x <= 10]:
        df[f"fwd_low_{h}d"] = df.groupby("ticker")["low"].transform(lambda s: s.shift(-1).rolling(h, min_periods=1).min())
        df[f"fwd_high_{h}d"] = df.groupby("ticker")["high"].transform(lambda s: s.shift(-1).rolling(h, min_periods=1).max())
        df[f"mae_{h}d"] = df[f"fwd_low_{h}d"] / df["close"] - 1.0
        df[f"mfe_{h}d"] = df[f"fwd_high_{h}d"] / df["close"] - 1.0
    if 5 in horizons:
        df["realized_vol_5d"] = df.groupby("ticker")["ret_1d"].transform(lambda s: s.shift(-1).rolling(5, min_periods=2).std())
        df["volatility_shock_5d"] = df["realized_vol_5d"] / df["pre_vol_20d"].replace(0, np.nan)

    # Market and sector alpha benchmarks. Prefer IHSG if present, otherwise equal-weight median market return.
    benchmark_cols = []
    if "IHSG" in set(df["ticker"]):
        ihsg = df.loc[df["ticker"].eq("IHSG"), ["date"] + [f"fwd_ret_{h}d" for h in horizons]].copy()
        ihsg = ihsg.rename(columns={f"fwd_ret_{h}d": f"ihsg_fwd_ret_{h}d" for h in horizons})
        df = df.merge(ihsg, on="date", how="left")
    else:
        for h in horizons:
            b = df.groupby("date")[f"fwd_ret_{h}d"].median().rename(f"market_fwd_ret_{h}d").reset_index()
            df = df.merge(b, on="date", how="left")
            benchmark_cols.append(f"market_fwd_ret_{h}d")

    if not emiten_df.empty:
        sec = emiten_df[["ticker", "sector"]].drop_duplicates("ticker")
        df = df.merge(sec, on="ticker", how="left", suffixes=("", "_meta"))
        for h in horizons:
            sector_ret = df.groupby(["date", "sector"])[f"fwd_ret_{h}d"].median().rename(f"sector_fwd_ret_{h}d").reset_index()
            df = df.merge(sector_ret, on=["date", "sector"], how="left")

    for h in horizons:
        mcol = f"ihsg_fwd_ret_{h}d" if f"ihsg_fwd_ret_{h}d" in df.columns else f"market_fwd_ret_{h}d"
        if mcol in df.columns:
            df[f"market_alpha_{h}d"] = df[f"fwd_ret_{h}d"] - df[mcol]
        if f"sector_fwd_ret_{h}d" in df.columns:
            df[f"sector_alpha_{h}d"] = df[f"fwd_ret_{h}d"] - df[f"sector_fwd_ret_{h}d"]
    return df


def _next_trading_date_map(calendar: list[Any], dates: Iterable[Any]) -> dict[Any, Any]:
    cal = pd.Index(pd.to_datetime(calendar).date)
    out = {}
    for d in set(dates):
        ts = pd.Timestamp(d).date()
        pos = cal.searchsorted(ts, side="right")  # strictly after news date: conservative without publish time
        out[d] = cal[pos] if pos < len(cal) else pd.NaT
    return out


def attach_market_outcomes(
    events: pd.DataFrame,
    ohlcv_path: Path,
    emiten_df: pd.DataFrame,
    horizons: tuple[int, ...],
    alpha_threshold: float,
    vol_shock_threshold: float,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    raw = _read_table(ohlcv_path)
    ohlcv = _normalize_ohlcv(raw, emiten_df)
    outcome = _add_forward_outcomes(ohlcv, horizons, emiten_df)
    calendar = sorted(outcome["date"].dropna().unique())
    date_map = _next_trading_date_map(calendar, events["news_date"])
    events = events.copy()
    events["entry_date"] = events["news_date"].map(date_map)

    join_cols = ["ticker", "date", "open", "high", "low", "close", "volume", "is_zero_volume", "pre_vol_20d"]
    for h in horizons:
        join_cols += [c for c in [
            f"fwd_ret_{h}d", f"market_alpha_{h}d", f"sector_alpha_{h}d", f"market_fwd_ret_{h}d",
            f"ihsg_fwd_ret_{h}d", f"sector_fwd_ret_{h}d"
        ] if c in outcome.columns]
    for c in ["realized_vol_5d", "volatility_shock_5d", "mae_5d", "mfe_5d"]:
        if c in outcome.columns:
            join_cols.append(c)
    join_cols = list(dict.fromkeys(join_cols))
    right = outcome[join_cols].rename(columns={"date": "entry_date", "close": "entry_close"})
    events = events.merge(right, on=["ticker", "entry_date"], how="left")

    alpha_col = "sector_alpha_5d" if "sector_alpha_5d" in events.columns else "market_alpha_5d"
    if alpha_col in events.columns:
        events["directional_label_5d"] = np.select(
            [events[alpha_col] > alpha_threshold, events[alpha_col] < -alpha_threshold],
            ["bullish", "bearish"],
            default="neutral_or_ambiguous",
        )
    if "volatility_shock_5d" in events.columns:
        events["volatility_label_5d"] = np.where(events["volatility_shock_5d"] > vol_shock_threshold, "volatility_shock", "normal_volatility")
    if "mae_5d" in events.columns:
        events["risk_label_5d"] = np.where(events["mae_5d"] < -0.03, "high_downside_risk", "normal_downside_risk")

    meta = {
        "ohlcv_rows_raw": int(len(raw)),
        "ohlcv_rows_clean": int(len(ohlcv)),
        "ohlcv_dropped_or_filtered_rows": int(raw.shape[0] - ohlcv.shape[0]),
        "ohlcv_min_date": str(ohlcv["date"].min()) if len(ohlcv) else None,
        "ohlcv_max_date": str(ohlcv["date"].max()) if len(ohlcv) else None,
        "events_with_entry": int(events["entry_date"].notna().sum()),
        "events_with_5d_outcome": int(events.get("fwd_ret_5d", pd.Series(dtype=float)).notna().sum()) if "fwd_ret_5d" in events.columns else 0,
    }
    return events, meta


def build_news_event_impact_dataset(config: BuildConfig) -> dict[str, Any]:
    out = config.output_dir or (config.root / "data" / "news" / "event_impact")
    out.mkdir(parents=True, exist_ok=True)

    news = load_news(config.news_paths)
    emiten = load_emiten_metadata(config.emiten_path)
    events = build_event_store(news, emiten)
    meta: dict[str, Any] = {
        "news_files": [str(p) for p in config.news_paths],
        "n_articles": int(len(news)),
        "n_event_rows_before_outcomes": int(len(events)),
        "n_unique_tickers": int(events["ticker"].dropna().nunique()) if len(events) else 0,
        "event_type_counts": events["event_type"].value_counts(dropna=False).to_dict() if len(events) else {},
    }

    if config.ohlcv_path is not None:
        events, outcome_meta = attach_market_outcomes(
            events, config.ohlcv_path, emiten, config.horizons, config.alpha_threshold, config.vol_shock_threshold
        )
        meta.update(outcome_meta)
    else:
        events["entry_date"] = pd.NaT
        meta["warning"] = "No OHLCV path was provided; event rows were built but future-return/volatility outcomes were not attached."

    # Stable column order for downstream workflows.
    preferred = [
        "article_id", "news_date", "entry_date", "source", "ticker", "company_name", "sector", "subsector",
        "event_scope", "event_type", "event_side", "impact_channel", "materiality", "uncertainty",
        "directional_label_5d", "volatility_label_5d", "risk_label_5d",
        "fwd_ret_1d", "fwd_ret_3d", "fwd_ret_5d", "fwd_ret_10d", "market_alpha_5d", "sector_alpha_5d",
        "realized_vol_5d", "volatility_shock_5d", "mae_5d", "mfe_5d",
        "title", "summary", "context_text",
    ]
    cols = [c for c in preferred if c in events.columns] + [c for c in events.columns if c not in preferred]
    events = events[cols]

    parquet_path = out / "news_event_impact_dataset.parquet"
    csv_path = out / "news_event_impact_dataset.csv"
    sample_path = out / "sample_5.csv"
    meta_path = out / "build_meta.json"

    parquet_written = True
    try:
        events.to_parquet(parquet_path, index=False)
    except ImportError as exc:
        # Keep the workflow usable in minimal environments; production Alpha Research
        # normally has pyarrow installed, but CSV is still written as a fallback.
        parquet_written = False
        meta["parquet_warning"] = f"Parquet was not written because pyarrow/fastparquet is unavailable: {exc}"
    events.to_csv(csv_path, index=False)
    events.head(5).to_csv(sample_path, index=False)
    meta.update({
        "output_parquet": str(parquet_path) if parquet_written else None,
        "output_csv": str(csv_path),
        "sample_csv": str(sample_path),
        "n_event_rows_final": int(len(events)),
    })
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    return meta
