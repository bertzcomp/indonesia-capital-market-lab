from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

WINDOWS_DEFAULT = (1, 3, 5, 7, 14, 30)
RAW_MACRO_REL = Path("data/raw/news/macro-news/macro_news_2020-2026.json")
RAW_MARKET_REL = Path("data/raw/news/market_news/market_news_2020-2026.json")
# Backward-compatible read paths. Some Alpha Research branches used macro_news
# while newer branches use macro-news. We write to the primary paths above,
# but read from both so historical raw files are not accidentally ignored.
RAW_MACRO_READ_RELS = [
    RAW_MACRO_REL,
    Path("data/raw/news/macro_news/macro_news_2020-2026.json"),
]
RAW_MARKET_READ_RELS = [
    RAW_MARKET_REL,
    Path("data/raw/news/market_news/market_news_2020-2026.json"),
]
OUTPUT_REL = Path("data/news/event_intelligence/news_event_intelligence_dataset.parquet")

TICKER_RE = re.compile(r"(?<![A-Z0-9])([A-Z]{4})(?![A-Z0-9])")
MONEY_RE = re.compile(r"(?:Rp|IDR|USD|US\$|\$)\s?[0-9][0-9.,]*(?:\s?(?:triliun|miliar|juta|billion|million))?", re.I)
PCT_RE = re.compile(r"[+-]?[0-9]+(?:[,.][0-9]+)?\s?%|[0-9]+(?:[,.][0-9]+)?\s?persen", re.I)

CAPITAL_STOPWORDS = {
    "PADA", "DARI", "IHSG", "RUPS", "BUMN", "ESDM", "APBN", "APBD", "RUPST", "POJK",
    "OJK", "IDX", "BEI", "KSEI", "YANG", "DENGAN", "UNTUK", "DALAM", "ATAU", "JUGA",
    "AKAN", "SUDAH", "OLEH", "ATAS", "AGAR", "BAGI", "SAAT", "SAJA", "HARGA", "TAHUN",
    "BULAN", "PASAR", "MODAL", "SAHAM", "EMITEN", "DIREKSI", "KOMISARIS", "RUPIAH",
    "DIVIDEN", "BURSA", "BANK", "DANA", "BELI", "JUAL", "NAIK", "TURUN", "LABA",
    "RUGI", "KURS", "NILAI", "RATA", "TOTAL", "HASIL", "INDO", "DATA", "INFO",
}

BEARISH_WORDS = [
    "delisting", "pailit", "bangkrut", "suspensi", "gagal bayar", "default", "rugi",
    "kerugian", "turun", "melemah", "anjlok", "ambrol", "tertekan", "jual asing",
    "net sell", "outflow", "dilepas", "distribusi", "pemantauan khusus", "sanksi",
]
BULLISH_WORDS = [
    "akumulasi", "borong", "diborong", "membeli", "net buy", "inflow", "laba naik",
    "laba bersih", "tumbuh", "dividen", "buyback", "kontrak", "proyek", "ekspansi",
    "kinerja positif", "menguat", "rebound", "target harga", "upgrade",
]
UNCERTAINTY_WORDS = [
    "potensi", "berpotensi", "diperkirakan", "proyeksi", "belum jelas", "ancaman", "risiko",
    "ketidakpastian", "volatil", "gejolak", "konflik", "tekanan", "menunggu", "rumor",
]
HIGH_MATERIALITY_EVENTS = {
    "delisting_bankruptcy", "suspension_uma", "rights_issue_private_placement", "macro_rate",
    "macro_currency", "geopolitical_risk", "index_rebalancing", "earnings_negative",
    "earnings_positive", "foreign_flow", "insider_accumulation",
}

@dataclass
class BuildResult:
    dataset_path: Optional[Path]
    csv_path: Path
    sample_path: Path
    meta_path: Path
    rows: int
    articles: int
    tickers: int


def _sha1_text(*parts: Any) -> str:
    text = "||".join("" if p is None else str(p) for p in parts)
    return hashlib.sha1(text.encode("utf-8", errors="ignore")).hexdigest()[:20]


def _read_json_any(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        first = f.read(1)
        f.seek(0)
        if first == "[" or first == "{":
            return json.load(f)
        return [json.loads(line) for line in f if line.strip()]


def _flatten_records(obj: Any) -> List[Dict[str, Any]]:
    if isinstance(obj, list):
        return [x for x in obj if isinstance(x, dict)]
    if isinstance(obj, dict):
        for key in ("data", "results", "items", "records"):
            if isinstance(obj.get(key), list):
                return [x for x in obj[key] if isinstance(x, dict)]
        return [obj]
    return []


def _infer_source_category(path: Path, rec: Optional[Dict[str, Any]] = None) -> Tuple[str, str]:
    p = str(path).lower()
    source = "unknown"
    if rec and rec.get("source"):
        s = str(rec.get("source"))
        if "idx" in s.lower():
            source = "IDX Channel"
        elif "kabar" in s.lower() or "kb" == s.lower():
            source = "Kabar Bursa"
        else:
            source = s
    elif "idx" in p or "idxchannel" in p:
        source = "IDX Channel"
    elif "kabar" in p or "/kb/" in p or "_kb" in p:
        source = "Kabar Bursa"

    category = "market"
    if rec and rec.get("news_category"):
        category = str(rec.get("news_category")).lower().replace(" ", "_")
    elif "macro" in p:
        category = "macro"
    elif "market" in p:
        category = "market"
    return source, category


def _coalesce(rec: Dict[str, Any], keys: Sequence[str], default: Any = "") -> Any:
    for k in keys:
        if k in rec and rec[k] not in (None, ""):
            return rec[k]
    return default


def _normalize_news_record(rec: Dict[str, Any], path: Path) -> Dict[str, Any]:
    source, category = _infer_source_category(path, rec)
    title = str(_coalesce(rec, ["title", "headline", "judul"], "")).strip()
    summary = str(_coalesce(rec, ["summary", "description", "ringkasan"], "")).strip()
    content = str(_coalesce(rec, ["full_content", "content", "body", "text", "article"], "")).strip()
    date_raw = _coalesce(rec, ["published_at", "datetime", "date", "tanggal", "created_at"], "")
    date = pd.to_datetime(date_raw, errors="coerce")
    url = str(_coalesce(rec, ["url", "link"], "")).strip()
    text = " ".join([title, summary, content]).strip()
    article_id = _sha1_text(source, category, title, str(date.date()) if pd.notna(date) else "", text[:1000], url)
    return {
        "article_id": article_id,
        "source": source,
        "news_category": category,
        "news_date": date.normalize() if pd.notna(date) else pd.NaT,
        "published_at": date if pd.notna(date) else pd.NaT,
        "title": title,
        "summary": summary,
        "full_content": content,
        "url": url,
        "raw_file": str(path),
        "text": text,
    }


def discover_pure_raw_news_files(root: str | Path) -> List[Path]:
    root = Path(root)
    base = root / "data/pure_raw/news"
    if not base.exists():
        return []
    return sorted([p for p in base.rglob("*.json") if p.is_file()])


def _load_existing_raw_news_for_merge(root: str | Path) -> pd.DataFrame:
    """Load existing canonical raw news from all backward-compatible raw paths.

    This is used by refresh_raw_news_from_pure_raw(..., merge_existing_raw=True)
    so a daily EOD refresh appends new pure_raw files to historical raw instead
    of overwriting the historical 2020-2026 canonical store.
    """
    root = Path(root)
    rows: List[Dict[str, Any]] = []
    seen_paths = set()
    for rel in RAW_MACRO_READ_RELS + RAW_MARKET_READ_RELS:
        path = root / rel
        if not path.exists() or str(path.resolve()) in seen_paths:
            continue
        seen_paths.add(str(path.resolve()))
        try:
            obj = _read_json_any(path)
            rows.extend(_normalize_news_record(r, path) for r in _flatten_records(obj))
        except Exception:
            # Existing raw files should not break daily ingestion; malformed raw is
            # simply ignored here and pure_raw can still be processed.
            continue
    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows)


def refresh_raw_news_from_pure_raw(root: str | Path, merge_existing_raw: bool = False) -> Dict[str, Any]:
    root = Path(root)
    files = discover_pure_raw_news_files(root)
    rows: List[Dict[str, Any]] = []
    for path in files:
        try:
            obj = _read_json_any(path)
            recs = _flatten_records(obj)
            rows.extend(_normalize_news_record(r, path) for r in recs)
        except Exception as exc:
            rows.append({
                "article_id": _sha1_text(str(path), "ERROR"),
                "source": "error",
                "news_category": "error",
                "news_date": pd.NaT,
                "published_at": pd.NaT,
                "title": "",
                "summary": "",
                "full_content": "",
                "url": "",
                "raw_file": str(path),
                "text": "",
                "ingest_error": repr(exc),
            })
    pure_df = pd.DataFrame(rows)
    existing_df = _load_existing_raw_news_for_merge(root) if merge_existing_raw else pd.DataFrame()

    frames = [f for f in [existing_df, pure_df] if not f.empty]
    if frames:
        df = pd.concat(frames, ignore_index=True, sort=False)
    else:
        df = pd.DataFrame(columns=["article_id", "source", "news_category", "news_date", "published_at", "title", "summary", "full_content", "url", "raw_file", "text"])

    if not df.empty:
        df = df.dropna(subset=["news_date"]).copy()
        df = df[df["title"].astype(str).str.len().gt(0) | df["full_content"].astype(str).str.len().gt(0)]
        # article_id is stable because it is derived from source/category/date/title/text/url.
        # keep last lets pure_raw daily dumps supersede older normalized raw duplicates.
        sort_cols = [c for c in ["news_date", "source", "title", "raw_file"] if c in df.columns]
        df = df.sort_values(sort_cols).drop_duplicates("article_id", keep="last")

    macro = df[df["news_category"].astype(str).str.contains("macro", case=False, na=False)].copy()
    market = df[~df.index.isin(macro.index)].copy()
    outputs = []
    for rel, frame in [(RAW_MACRO_REL, macro), (RAW_MARKET_REL, market)]:
        out = root / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        payload = frame.drop(columns=["text"], errors="ignore").copy()
        for c in ("news_date", "published_at"):
            if c in payload.columns:
                payload[c] = pd.to_datetime(payload[c], errors="coerce").dt.strftime("%Y-%m-%d")
        payload.to_json(out, orient="records", force_ascii=False, indent=2)
        outputs.append(str(out))
    return {
        "pure_raw_files": len(files),
        "pure_raw_articles": int(len(pure_df)) if not pure_df.empty else 0,
        "existing_raw_articles": int(len(existing_df)) if not existing_df.empty else 0,
        "merge_existing_raw": bool(merge_existing_raw),
        "total_articles": int(len(df)),
        "macro_articles": int(len(macro)),
        "market_articles": int(len(market)),
        "outputs": outputs,
    }


def load_raw_news(root: str | Path) -> pd.DataFrame:
    root = Path(root)
    rels = RAW_MACRO_READ_RELS + RAW_MARKET_READ_RELS
    rows = []
    seen_paths = set()
    for rel in rels:
        path = root / rel
        if not path.exists() or str(path.resolve()) in seen_paths:
            continue
        seen_paths.add(str(path.resolve()))
        obj = _read_json_any(path)
        for rec in _flatten_records(obj):
            rows.append(_normalize_news_record(rec, path))
    df = pd.DataFrame(rows)
    if df.empty:
        return pd.DataFrame(columns=["article_id", "source", "news_category", "news_date", "published_at", "title", "summary", "full_content", "text"])
    df = df.dropna(subset=["news_date"]).copy()
    df = df.sort_values(["news_date", "source", "title"]).drop_duplicates("article_id", keep="last")
    return df.reset_index(drop=True)


def load_news_paths(paths: Sequence[str | Path]) -> pd.DataFrame:
    rows: List[Dict[str, Any]] = []
    for p in paths:
        path = Path(p)
        obj = _read_json_any(path)
        rows.extend(_normalize_news_record(r, path) for r in _flatten_records(obj))
    df = pd.DataFrame(rows)
    if df.empty:
        return pd.DataFrame(columns=["article_id", "source", "news_category", "news_date", "published_at", "title", "summary", "full_content", "text"])
    return df.dropna(subset=["news_date"]).sort_values(["news_date", "source", "title"]).drop_duplicates("article_id", keep="last").reset_index(drop=True)


def load_emiten_metadata(path: Optional[str | Path]) -> pd.DataFrame:
    if not path:
        return pd.DataFrame(columns=["ticker", "company_name", "sector", "subsector", "industry", "listing_board", "listing_date"])
    path = Path(path)
    if not path.exists():
        return pd.DataFrame(columns=["ticker", "company_name", "sector", "subsector", "industry", "listing_board", "listing_date"])
    obj = _read_json_any(path)
    recs = _flatten_records(obj)
    if not recs:
        return pd.DataFrame(columns=["ticker", "company_name", "sector", "subsector", "industry", "listing_board", "listing_date"])
    df = pd.DataFrame(recs)
    def find(options: Sequence[str]) -> Optional[str]:
        lower = {c.lower(): c for c in df.columns}
        for o in options:
            if o.lower() in lower:
                return lower[o.lower()]
        return None
    mapping = {
        "ticker": find(["KodeEmiten", "ticker", "kode", "symbol"]),
        "company_name": find(["NamaEmiten", "name", "company_name", "emiten"]),
        "sector": find(["Sektor", "sector"]),
        "subsector": find(["SubSektor", "subsector", "sub_sector"]),
        "industry": find(["Industri", "industry"]),
        "subindustry": find(["SubIndustri", "subindustry"]),
        "listing_board": find(["PapanPencatatan", "board", "listing_board"]),
        "listing_date": find(["TanggalPencatatan", "listing_date", "listed_date"]),
    }
    out = pd.DataFrame()
    for k, c in mapping.items():
        if c:
            out[k] = df[c]
        else:
            out[k] = np.nan
    out["ticker"] = out["ticker"].astype(str).str.upper().str.strip()
    out = out[out["ticker"].str.len().eq(4)].drop_duplicates("ticker", keep="last")
    out["listing_date"] = pd.to_datetime(out["listing_date"], errors="coerce")
    return out.reset_index(drop=True)


def _normalize_company_name(name: Any) -> str:
    s = str(name or "").lower()
    s = re.sub(r"\bpt\b|\btbk\b|\bpersero\b|\bterbuka\b", " ", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _context_around(text: str, ticker: str, window: int = 260) -> str:
    if not ticker:
        return text[: min(len(text), window * 2)]
    idx = text.find(ticker)
    if idx < 0:
        idx = text.lower().find(ticker.lower())
    if idx < 0:
        return text[: min(len(text), window * 2)]
    return text[max(0, idx - window): idx + len(ticker) + window]


def extract_tickers(text: str, emiten: pd.DataFrame) -> List[str]:
    valid = set(emiten["ticker"].dropna().astype(str).str.upper()) if not emiten.empty else set()
    cands = []
    for m in TICKER_RE.findall(text or ""):
        if m in CAPITAL_STOPWORDS:
            continue
        if valid and m not in valid:
            continue
        cands.append(m)
    # company-name alias fallback for top-level exact phrase matching
    text_norm = _normalize_company_name(text)
    if not emiten.empty and len(text_norm) > 0:
        for _, row in emiten.iterrows():
            t = str(row.get("ticker", ""))
            cname = _normalize_company_name(row.get("company_name", ""))
            if len(cname) >= 8 and cname in text_norm:
                cands.append(t)
    return sorted(set(cands))


def classify_event(text: str, context: Optional[str] = None, news_category: str = "market") -> Dict[str, Any]:
    full = (context or text or "").lower()
    all_text = (text or "").lower()
    def has(*words: str) -> bool:
        return any(w in full for w in words)
    def has_all_scope(*words: str) -> bool:
        return any(w in all_text for w in words)

    event_type = "generic_market_news"
    side = "neutral_or_unclear"
    channel = "information_flow"
    scope = "ticker"

    if has("delisting", "pailit", "bangkrut", "gagal bayar"):
        event_type, side, channel = "delisting_bankruptcy", "bearish_risk", "tradability_distress"
    elif has("suspensi", "uma", "unusual market activity"):
        event_type, side, channel = "suspension_uma", "bearish_risk", "tradability_distress"
    elif has("rights issue", "private placement", "waran", "hmtd"):
        event_type, side, channel = "rights_issue_private_placement", "bearish_to_mixed", "dilution_financing"
    elif has("buyback", "beli kembali saham"):
        event_type, side, channel = "buyback", "bullish", "capital_return_support"
    elif has("dividen", "cum dividen", "ex dividen"):
        event_type, side, channel = "dividend", "mixed_to_bullish", "cash_distribution"
    elif has("akumulasi", "borong", "diborong", "membeli", "pembelian") and has("direktur", "komisaris", "pengendali", "insider", "ceo", "president director"):
        event_type, side, channel = "insider_accumulation", "bullish", "insider_positioning"
    elif has("net buy", "asing beli", "investor asing masuk", "foreign buy"):
        event_type, side, channel = "foreign_flow", "bullish_flow", "foreign_flow"
    elif has("net sell", "asing jual", "outflow", "aksi jual asing", "dilepas asing"):
        event_type, side, channel = "foreign_flow", "bearish_flow", "foreign_flow"
    elif has("diborong ritel", "borong ritel", "akumulasi ritel", "banyak diborong"):
        event_type, side, channel = "retail_accumulation", "bullish_flow", "retail_positioning"
    elif has("dilepas ritel", "distribusi ritel", "saham yang dilepas", "sasaran distribusi"):
        event_type, side, channel = "retail_distribution", "bearish_flow", "retail_positioning"
    elif has("laba bersih") and has("tumbuh", "naik", "meningkat", "rekor"):
        event_type, side, channel = "earnings_positive", "bullish", "fundamental_earnings"
    elif has("rugi", "laba turun", "penurunan laba", "merosot"):
        event_type, side, channel = "earnings_negative", "bearish", "fundamental_earnings"
    elif has("kontrak", "proyek", "kerja sama", "gandeng", "joint venture"):
        event_type, side, channel = "contract_project", "mixed_to_bullish", "business_expansion"
    elif has("msci", "ftse", "rebalancing", "free float", "index provider"):
        event_type, side, channel, scope = "index_rebalancing", "mixed_flow", "index_flow", "market_or_ticker"
    elif has_all_scope("rupiah", "usd/idr", "dolar", "dollar", "kurs") and has_all_scope("melemah", "menguat", "tertekan", "jatuh"):
        event_type, side, channel, scope = "macro_currency", "bearish_for_idx", "currency_risk", "market"
    elif has_all_scope("bi rate", "suku bunga", "fed", "yield", "inflasi"):
        event_type, side, channel, scope = "macro_rate", "mixed_macro", "rate_inflation", "market"
    elif has_all_scope("brent", "minyak", "crude", "batu bara", "coal", "cpo", "nikel", "emas", "komoditas"):
        event_type, side, channel, scope = "commodity_shock", "sector_dependent", "commodity_input_output", "sector"
    elif has_all_scope("geopolitik", "timur tengah", "iran", "perang", "konflik", "selat hormuz"):
        event_type, side, channel, scope = "geopolitical_risk", "bearish_risk", "external_shock", "market"
    elif str(news_category).lower().startswith("macro"):
        event_type, side, channel, scope = "macro_general", "mixed_macro", "macro_narrative", "market"

    uncertainty_hits = sum(1 for w in UNCERTAINTY_WORDS if w in all_text)
    bullish_hits = sum(1 for w in BULLISH_WORDS if w in full)
    bearish_hits = sum(1 for w in BEARISH_WORDS if w in full)
    pct_hits = len(PCT_RE.findall(all_text))
    money_hits = len(MONEY_RE.findall(all_text))
    intensity = min(1.0, 0.10 * pct_hits + 0.10 * money_hits + 0.08 * (bullish_hits + bearish_hits) + (0.15 if event_type in HIGH_MATERIALITY_EVENTS else 0.0))
    uncertainty = min(1.0, 0.18 * uncertainty_hits + (0.25 if event_type in {"geopolitical_risk", "macro_currency", "macro_rate"} else 0.0))
    materiality = 0.75 if event_type in HIGH_MATERIALITY_EVENTS else 0.55 if event_type != "generic_market_news" else 0.30
    if money_hits >= 2 or pct_hits >= 3:
        materiality = min(1.0, materiality + 0.10)
    return {
        "event_scope": scope,
        "event_type": event_type,
        "event_side": side,
        "impact_channel": channel,
        "news_intensity_score": round(float(intensity), 4),
        "uncertainty_score": round(float(uncertainty), 4),
        "materiality_score": round(float(materiality), 4),
        "bullish_keyword_hits": bullish_hits,
        "bearish_keyword_hits": bearish_hits,
    }


def build_event_rows(news_df: pd.DataFrame, emiten: pd.DataFrame) -> pd.DataFrame:
    meta = emiten.set_index("ticker").to_dict("index") if not emiten.empty else {}
    rows: List[Dict[str, Any]] = []
    for _, rec in news_df.iterrows():
        text = str(rec.get("text", "") or "")
        title = str(rec.get("title", "") or "")
        category = str(rec.get("news_category", "market") or "market")
        tickers = extract_tickers(text, emiten)
        if not tickers:
            cls = classify_event(text, text[:600], category)
            rows.append({
                **{k: rec.get(k) for k in ["article_id", "source", "news_category", "news_date", "published_at", "title", "summary", "full_content", "url"] if k in rec},
                "ticker": None,
                "company_name": None,
                "sector": "MARKET",
                "subsector": None,
                "industry": None,
                "listing_board": None,
                "listing_date": pd.NaT,
                "entity_match_type": "market_scope_no_ticker",
                **cls,
                "event_row_id": _sha1_text(rec.get("article_id"), "MARKET", cls["event_type"]),
            })
            continue
        for ticker in tickers:
            ctx = _context_around(text, ticker)
            cls = classify_event(text, ctx, category)
            m = meta.get(ticker, {})
            rows.append({
                **{k: rec.get(k) for k in ["article_id", "source", "news_category", "news_date", "published_at", "title", "summary", "full_content", "url"] if k in rec},
                "ticker": ticker,
                "company_name": m.get("company_name"),
                "sector": m.get("sector"),
                "subsector": m.get("subsector"),
                "industry": m.get("industry"),
                "subindustry": m.get("subindustry"),
                "listing_board": m.get("listing_board"),
                "listing_date": m.get("listing_date"),
                "entity_match_type": "ticker_or_company_alias",
                "ticker_context": ctx,
                **cls,
                "event_row_id": _sha1_text(rec.get("article_id"), ticker, cls["event_type"], ctx[:200]),
            })
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["news_date"] = pd.to_datetime(df["news_date"], errors="coerce")
    df = df.sort_values(["news_date", "article_id", "ticker"], na_position="last").drop_duplicates("event_row_id", keep="last")
    df = add_novelty_features(df)
    return df.reset_index(drop=True)


def add_novelty_features(df: pd.DataFrame, lookback_days: int = 30) -> pd.DataFrame:
    df = df.copy().sort_values(["ticker", "event_type", "news_date"], na_position="last")
    counts = []
    for _, g in df.groupby(["ticker", "event_type"], dropna=False, sort=False):
        dates = pd.to_datetime(g["news_date"], errors="coerce").tolist()
        idxs = list(g.index)
        for i, d in enumerate(dates):
            if pd.isna(d):
                counts.append((idxs[i], 0))
            else:
                c = sum(1 for prev in dates[:i] if pd.notna(prev) and 0 < (d - prev).days <= lookback_days)
                counts.append((idxs[i], c))
    s = pd.Series({idx: c for idx, c in counts})
    df["recent_same_event_count_30d"] = df.index.map(s).fillna(0).astype(int)
    df["novelty_score"] = (1.0 / (1.0 + df["recent_same_event_count_30d"])).round(4)
    return df


def _read_table(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    suf = path.suffix.lower()
    if suf == ".parquet":
        return pd.read_parquet(path)
    if suf in (".csv", ".txt"):
        return pd.read_csv(path)
    if suf in (".json", ".jsonl"):
        obj = _read_json_any(path)
        return pd.DataFrame(_flatten_records(obj))
    raise ValueError(f"Unsupported file type: {path}")


def load_ohlcv(path: str | Path, emiten: Optional[pd.DataFrame] = None) -> pd.DataFrame:
    df = _read_table(path)
    cols = {c.lower().strip(): c for c in df.columns}
    def c(name: str) -> Optional[str]:
        return cols.get(name.lower())
    required = ["date", "ticker", "open", "high", "low", "close", "volume"]
    rename = {c(k): k for k in required if c(k)}
    df = df.rename(columns=rename)
    missing = [k for k in required if k not in df.columns]
    if missing:
        raise ValueError(f"OHLCV missing columns: {missing}; available={list(df.columns)}")
    df = df[required].copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["ticker"] = df["ticker"].astype(str).str.upper().str.strip()
    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["date", "ticker", "close"]).copy()
    df = df[df["ticker"].str.len().eq(4)]
    df = df.sort_values(["ticker", "date"]).drop_duplicates(["ticker", "date"], keep="last")
    if emiten is not None and not emiten.empty and "listing_date" in emiten.columns:
        listing = emiten.set_index("ticker")["listing_date"].to_dict()
        ld = df["ticker"].map(listing)
        mask = pd.isna(ld) | (df["date"] >= pd.to_datetime(ld, errors="coerce"))
        df = df[mask].copy()
    df["is_zero_volume"] = df["volume"].fillna(0).le(0)
    return df.reset_index(drop=True)


def enrich_ohlcv_features(ohlcv: pd.DataFrame, emiten: pd.DataFrame, windows: Sequence[int]) -> pd.DataFrame:
    df = ohlcv.copy().sort_values(["ticker", "date"]).reset_index(drop=True)
    if not emiten.empty:
        df = df.merge(emiten[["ticker", "sector"]].drop_duplicates("ticker"), on="ticker", how="left", suffixes=("", "_meta"))
    if "sector" not in df.columns:
        df["sector"] = np.nan
    grp = df.groupby("ticker", sort=False)
    df["daily_ret"] = grp["close"].pct_change()
    df["avg_volume_20d"] = grp["volume"].transform(lambda x: x.rolling(20, min_periods=5).mean())
    df["volume_ratio"] = df["volume"] / df["avg_volume_20d"].replace(0, np.nan)
    df["bwd_volatility_20d"] = grp["daily_ret"].transform(lambda x: x.rolling(20, min_periods=5).std())
    df["drawdown_20d"] = grp["close"].transform(lambda x: x / x.rolling(20, min_periods=5).max() - 1)
    for h in windows:
        df[f"fwd_ret_{h}d"] = grp["close"].transform(lambda x, h=h: x.shift(-h) / x - 1)
        df[f"bwd_ret_{h}d"] = grp["close"].transform(lambda x, h=h: x / x.shift(h) - 1)
        df[f"bwd_volume_ratio_{h}d"] = grp["volume"].transform(lambda x, h=h: x.rolling(h, min_periods=1).mean()) / df["avg_volume_20d"].replace(0, np.nan)
        # forward volatility, volume spike, MAE/MFE from the day after anchor date
        df[f"fwd_realized_vol_{h}d"] = grp["daily_ret"].transform(lambda x, h=h: x.shift(-1).iloc[::-1].rolling(h, min_periods=1).std(ddof=0).iloc[::-1])
        df[f"fwd_max_volume_ratio_{h}d"] = grp["volume_ratio"].transform(lambda x, h=h: x.shift(-1).iloc[::-1].rolling(h, min_periods=1).max().iloc[::-1])
        fwd_low = grp["low"].transform(lambda x, h=h: x.shift(-1).iloc[::-1].rolling(h, min_periods=1).min().iloc[::-1])
        fwd_high = grp["high"].transform(lambda x, h=h: x.shift(-1).iloc[::-1].rolling(h, min_periods=1).max().iloc[::-1])
        df[f"mae_{h}d"] = fwd_low / df["close"] - 1
        df[f"mfe_{h}d"] = fwd_high / df["close"] - 1
    # market and sector alpha, anchored by row date
    market = None
    if (df["ticker"] == "IHSG").any():
        market = df[df["ticker"] == "IHSG"][["date"] + [f"fwd_ret_{h}d" for h in windows]].rename(columns={f"fwd_ret_{h}d": f"market_fwd_ret_{h}d" for h in windows})
    else:
        market = df.groupby("date", as_index=False)[[f"fwd_ret_{h}d" for h in windows]].median().rename(columns={f"fwd_ret_{h}d": f"market_fwd_ret_{h}d" for h in windows})
    df = df.merge(market, on="date", how="left")
    sector_frames = []
    if "sector" in df.columns:
        for h in windows:
            tmp = df.groupby(["date", "sector"], as_index=False)[f"fwd_ret_{h}d"].median().rename(columns={f"fwd_ret_{h}d": f"sector_fwd_ret_{h}d"})
            sector_frames.append(tmp)
        if sector_frames:
            sector = sector_frames[0]
            for tmp in sector_frames[1:]:
                sector = sector.merge(tmp, on=["date", "sector"], how="outer")
            df = df.merge(sector, on=["date", "sector"], how="left")
    for h in windows:
        df[f"market_alpha_{h}d"] = df[f"fwd_ret_{h}d"] - df.get(f"market_fwd_ret_{h}d")
        if f"sector_fwd_ret_{h}d" in df.columns:
            df[f"sector_alpha_{h}d"] = df[f"fwd_ret_{h}d"] - df[f"sector_fwd_ret_{h}d"]
        else:
            df[f"sector_alpha_{h}d"] = df[f"market_alpha_{h}d"]
        df[f"volatility_shock_{h}d"] = df[f"fwd_realized_vol_{h}d"] / df["bwd_volatility_20d"].replace(0, np.nan)
    return df


def _trading_day_maps(ohlcv: pd.DataFrame) -> Tuple[List[pd.Timestamp], Dict[pd.Timestamp, pd.Timestamp], Dict[pd.Timestamp, pd.Timestamp]]:
    dates = sorted(pd.to_datetime(ohlcv["date"].dropna().unique()))
    next_map: Dict[pd.Timestamp, pd.Timestamp] = {}
    prev_map: Dict[pd.Timestamp, pd.Timestamp] = {}
    if not dates:
        return [], next_map, prev_map
    # Map any normalized news date in overall range to next strictly greater trading day and previous <= day.
    start, end = pd.Timestamp(dates[0]).normalize() - pd.Timedelta(days=5), pd.Timestamp(dates[-1]).normalize() + pd.Timedelta(days=5)
    all_days = pd.date_range(start, end, freq="D")
    arr = pd.Index([pd.Timestamp(d).normalize() for d in dates])
    for d in all_days:
        gt = arr[arr > d]
        le = arr[arr <= d]
        if len(gt):
            next_map[d] = pd.Timestamp(gt[0])
        if len(le):
            prev_map[d] = pd.Timestamp(le[-1])
    return dates, next_map, prev_map


def attach_market_outcomes(events: pd.DataFrame, ohlcv: pd.DataFrame, emiten: pd.DataFrame, windows: Sequence[int]) -> pd.DataFrame:
    if events.empty:
        return events
    features = enrich_ohlcv_features(ohlcv, emiten, windows)
    dates, next_map, prev_map = _trading_day_maps(features)
    out = events.copy()
    news_norm = pd.to_datetime(out["news_date"], errors="coerce").dt.normalize()
    out["entry_date"] = news_norm.map(next_map)
    out["anchor_date"] = news_norm.map(prev_map)  # last available EOD before execution
    # Ticker-scoped rows attach ticker outcomes. Market-scoped rows use IHSG if present, otherwise no ticker-level outcome.
    out["outcome_ticker"] = out["ticker"].fillna("IHSG")
    attach_cols = [
        "ticker", "date", "close", "volume", "volume_ratio", "is_zero_volume", "bwd_volatility_20d", "drawdown_20d",
    ]
    for h in windows:
        attach_cols += [
            f"fwd_ret_{h}d", f"bwd_ret_{h}d", f"bwd_volume_ratio_{h}d", f"market_fwd_ret_{h}d", f"sector_fwd_ret_{h}d",
            f"market_alpha_{h}d", f"sector_alpha_{h}d", f"fwd_realized_vol_{h}d", f"volatility_shock_{h}d",
            f"fwd_max_volume_ratio_{h}d", f"mae_{h}d", f"mfe_{h}d",
        ]
    attach_cols = [c for c in attach_cols if c in features.columns]
    feat = features[attach_cols].copy().rename(columns={"ticker": "outcome_ticker", "date": "entry_date", "close": "entry_close", "volume": "entry_volume"})
    out = out.merge(feat, on=["outcome_ticker", "entry_date"], how="left")
    return add_reaction_labels(out)


def add_reaction_labels(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    alpha1 = out.get("sector_alpha_1d", pd.Series(index=out.index, dtype=float))
    alpha5 = out.get("sector_alpha_5d", pd.Series(index=out.index, dtype=float))
    fwd5 = out.get("fwd_ret_5d", pd.Series(index=out.index, dtype=float))
    bwd5 = out.get("bwd_ret_5d", pd.Series(index=out.index, dtype=float))
    volshock = out.get("volatility_shock_5d", pd.Series(index=out.index, dtype=float))
    mae5 = out.get("mae_5d", pd.Series(index=out.index, dtype=float))
    side = out.get("event_side", pd.Series("", index=out.index)).astype(str)

    out["directional_label_5d"] = np.select(
        [alpha5 > 0.01, alpha5 < -0.01], ["bullish_alpha", "bearish_alpha"], default="neutral_or_ambiguous"
    )
    out["volatility_label_5d"] = np.select(
        [volshock > 2.0, volshock > 1.5], ["extreme_volatility_expansion", "volatility_expansion"], default="normal_or_unknown"
    )
    out["risk_label_5d"] = np.select(
        [mae5 < -0.05, mae5 < -0.03], ["high_downside_risk", "moderate_downside_risk"], default="normal_or_unknown"
    )
    bullish_side = side.str.contains("bullish", case=False, na=False) | side.str.contains("mixed_to_bullish", case=False, na=False)
    bearish_side = side.str.contains("bearish", case=False, na=False)
    out["sentiment_trap_label_5d"] = np.where(bullish_side & (bwd5 > 0.05) & (alpha5 < -0.01), 1, 0)
    out["sell_the_news_label_5d"] = np.where((bwd5 > 0.05) & (alpha5 < 0), 1, 0)
    out["delayed_reaction_label_5d"] = np.where(alpha1.abs().le(0.005) & (alpha5 > 0.01), 1, 0)
    out["confirmed_positive_label_5d"] = np.where(bullish_side & (alpha5 > 0.01), 1, 0)
    out["confirmed_negative_label_5d"] = np.where(bearish_side & (alpha5 < -0.01), 1, 0)
    out["acceleration_trigger_label_5d"] = np.where((bwd5.abs() <= 0.03) & (alpha5 > 0.02), 1, 0)
    conditions = [
        out["sentiment_trap_label_5d"].eq(1),
        out["sell_the_news_label_5d"].eq(1),
        out["delayed_reaction_label_5d"].eq(1),
        out["acceleration_trigger_label_5d"].eq(1),
        out["confirmed_positive_label_5d"].eq(1),
        out["confirmed_negative_label_5d"].eq(1),
        out["volatility_label_5d"].ne("normal_or_unknown"),
    ]
    choices = [
        "sentiment_trap", "sell_the_news", "delayed_reaction", "acceleration_trigger",
        "confirmed_positive", "confirmed_negative", "volatility_event",
    ]
    out["reaction_label_5d"] = np.select(conditions, choices, default="neutral_or_unclassified")
    return out


def attach_simple_regime_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    # Conservative simple labels. Can be replaced later by Alpha Research's dedicated regime table.
    ma = out.get("market_fwd_ret_5d", pd.Series(index=out.index, dtype=float))
    vol = out.get("bwd_volatility_20d", pd.Series(index=out.index, dtype=float))
    out["market_regime_proxy"] = np.select([ma > 0.01, ma < -0.01], ["risk_on_forward", "risk_off_forward"], default="sideways_or_unknown")
    if vol.notna().any():
        q70 = vol.quantile(0.70)
        q30 = vol.quantile(0.30)
        out["volatility_regime_proxy"] = np.select([vol >= q70, vol <= q30], ["high_vol", "low_vol"], default="normal_vol")
    else:
        out["volatility_regime_proxy"] = "unknown"
    return out


def safe_write_dataset(df: pd.DataFrame, out_path: str | Path) -> Tuple[Optional[Path], Path]:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    parquet_path: Optional[Path] = None
    csv_path = out_path.with_suffix(".csv")
    # Avoid saving full content in CSV if huge? Keep it because this is a research dataset, but text can be large.
    df.to_csv(csv_path, index=False)
    try:
        df.to_parquet(out_path, index=False)
        parquet_path = out_path
    except Exception:
        parquet_path = None
    return parquet_path, csv_path


def build_news_event_intelligence_dataset(
    root: str | Path = ".",
    news_paths: Optional[Sequence[str | Path]] = None,
    news_source: str = "raw",
    refresh_raw_news: bool = False,
    merge_existing_raw_news: bool = False,
    emiten_path: Optional[str | Path] = None,
    ohlcv_path: Optional[str | Path] = None,
    output_path: str | Path | None = None,
    windows: Sequence[int] = WINDOWS_DEFAULT,
    no_ohlcv: bool = False,
) -> BuildResult:
    root = Path(root)
    refresh_meta = None
    if refresh_raw_news:
        refresh_meta = refresh_raw_news_from_pure_raw(root, merge_existing_raw=merge_existing_raw_news)
    if news_paths:
        news_df = load_news_paths(news_paths)
    elif news_source == "pure_raw":
        files = discover_pure_raw_news_files(root)
        news_df = load_news_paths(files)
    else:
        news_df = load_raw_news(root)
    if emiten_path is None:
        candidates = [
            root / "data/raw/listed_companies.json",
            root / "data/raw/emiten/listed_companies.json",
            root / "data/pure_raw/listed_companies.json",
            root / "data/raw/idx/listed_companies.json",
        ]
        emiten_path = next((p for p in candidates if p.exists()), None)
    emiten = load_emiten_metadata(emiten_path)
    events = build_event_rows(news_df, emiten)
    if not no_ohlcv and ohlcv_path:
        ohlcv = load_ohlcv(ohlcv_path, emiten)
        events = attach_market_outcomes(events, ohlcv, emiten, windows)
        events = attach_simple_regime_features(events)
    else:
        events["entry_date"] = pd.to_datetime(events.get("news_date"), errors="coerce") + pd.Timedelta(days=1)
        events["outcome_status"] = "no_ohlcv_attached"
    if output_path is None:
        output_path = root / OUTPUT_REL
    else:
        output_path = Path(output_path)
        if not output_path.is_absolute():
            output_path = root / output_path
    parquet_path, csv_path = safe_write_dataset(events, output_path)
    sample_path = output_path.parent / "sample_5.csv"
    events.head(5).to_csv(sample_path, index=False)
    meta = {
        "rows": int(len(events)),
        "articles": int(events["article_id"].nunique()) if "article_id" in events.columns else 0,
        "tickers": int(events["ticker"].nunique(dropna=True)) if "ticker" in events.columns else 0,
        "news_source": news_source,
        "refresh_raw_news": bool(refresh_raw_news),
        "merge_existing_raw_news": bool(merge_existing_raw_news),
        "refresh_meta": refresh_meta,
        "emiten_path": str(emiten_path) if emiten_path else None,
        "ohlcv_path": str(ohlcv_path) if ohlcv_path else None,
        "windows": list(windows),
        "output_parquet": str(parquet_path) if parquet_path else None,
        "output_csv": str(csv_path),
        "sample_path": str(sample_path),
    }
    meta_path = output_path.parent / "build_meta.json"
    meta_path.write_text(json.dumps(meta, indent=2, default=str), encoding="utf-8")
    return BuildResult(parquet_path, csv_path, sample_path, meta_path, int(len(events)), int(meta["articles"]), int(meta["tickers"]))
