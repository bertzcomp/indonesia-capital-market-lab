from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

import polars as pl

from alpha_research.news.taxonomy import classify_event


DEFAULT_WINDOWS = [1, 3, 5, 7, 14, 30]
TICKER_RE = re.compile(r"\b([A-Z]{4})\b")
CAPITAL_STOPWORDS = {
    "PADA","DARI","IHSG","RUPS","BUMN","ESDM","APBN","APBD","RUPST","POJK","OJK","IDX","BEI","KSEI",
    "YANG","DENGAN","UNTUK","DALAM","ATAU","JUGA","AKAN","SUDAH","OLEH","ATAS","AGAR","BAGI","SAAT","SAJA",
    "HARGA","TAHUN","BULAN","PASAR","MODAL","SAHAM","EMITEN","DIREKSI","KOMISARIS","RUPIAH","DIVIDEN","BURSA",
    "BANK","DANA","BELI","JUAL","NAIK","TURUN","LABA","RUGI","KURS","NILAI","RATA","TOTAL","HASIL","EURO","NATO",
}


@dataclass
class BuildResult:
    engine: str
    rows: int
    articles: int
    tickers: int
    news_source: str
    refresh_raw_news: bool
    merge_existing_raw_news: bool
    emiten_path: str
    ohlcv_path: Optional[str]
    windows: list[int]
    output_parquet: str
    sample_path: str
    output_csv: Optional[str] = None


def _read_json_records(path: Path) -> list[dict]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="ignore").strip()
    if not text:
        return []
    try:
        obj = json.loads(text)
        if isinstance(obj, list):
            return [x for x in obj if isinstance(x, dict)]
        if isinstance(obj, dict):
            if "data" in obj and isinstance(obj["data"], list):
                return [x for x in obj["data"] if isinstance(x, dict)]
            return [obj]
    except json.JSONDecodeError:
        rows = []
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                x = json.loads(line)
                if isinstance(x, dict):
                    rows.append(x)
            except Exception:
                continue
        return rows
    return []


def _infer_source(path: Path, obj: dict) -> str:
    src = str(obj.get("source") or obj.get("Source") or "").strip()
    if src and src.lower() not in {"nan", "none", "null", "unknown"}:
        if "idx" in src.lower():
            return "IDX Channel"
        if "kabar" in src.lower() or src.lower() in {"kb", "kabarbursa"}:
            return "Kabar Bursa"
        return src
    p = str(path).lower()
    if "idxchannel" in p or "/idx/" in p or "\\idx\\" in p:
        return "IDX Channel"
    if "kabarbursa" in p or "/kb/" in p or "\\kb\\" in p:
        return "Kabar Bursa"
    return "unknown"


def _infer_category(path: Path, obj: dict) -> str:
    cat = str(obj.get("news_category") or obj.get("category") or obj.get("channel") or obj.get("type") or "").lower()
    p = str(path).lower()
    if "macro" in cat or "macro" in p:
        return "macro"
    if "market" in cat or "market" in p:
        return "market"
    return "unknown"


def _date_col(obj: dict) -> str:
    for k in ["date", "published_at", "publish_date", "created_at", "datetime"]:
        if obj.get(k):
            return str(obj.get(k))
    return ""


def _text(obj: dict, *keys: str) -> str:
    for k in keys:
        v = obj.get(k)
        if v is not None and str(v).strip():
            return str(v)
    return ""


def _article_id(source: str, category: str, date: str, title: str, content: str) -> str:
    key = f"{source}|{category}|{date[:10]}|{title.strip().lower()}|{content[:200].strip().lower()}"
    return hashlib.md5(key.encode("utf-8", errors="ignore")).hexdigest()


def load_news_files(paths: Iterable[Path]) -> pl.DataFrame:
    rows = []
    for path in paths:
        for obj in _read_json_records(path):
            source = _infer_source(path, obj)
            category = _infer_category(path, obj)
            date = _date_col(obj)
            title = _text(obj, "title", "judul")
            summary = _text(obj, "summary", "ringkasan", "description")
            content = _text(obj, "full_content", "content", "body", "text", "article")
            url = _text(obj, "url", "link")
            if not (title or summary or content):
                continue
            aid = _article_id(source, category, date, title, content)
            rows.append({
                "article_id": aid,
                "source": source,
                "news_category": category,
                "news_date_raw": date,
                "title": title,
                "summary": summary,
                "full_content": content,
                "url": url,
            })
    if not rows:
        return pl.DataFrame(schema={
            "article_id": pl.Utf8, "source": pl.Utf8, "news_category": pl.Utf8, "news_date_raw": pl.Utf8,
            "title": pl.Utf8, "summary": pl.Utf8, "full_content": pl.Utf8, "url": pl.Utf8,
        })
    df = pl.DataFrame(rows)
    return (
        df.with_columns([
            pl.col("news_date_raw").cast(pl.Utf8).str.slice(0, 10).str.strptime(pl.Date, format="%Y-%m-%d", strict=False).alias("news_date"),
            pl.col("title").cast(pl.Utf8),
            pl.col("summary").cast(pl.Utf8),
            pl.col("full_content").cast(pl.Utf8),
        ])
        .filter(pl.col("news_date").is_not_null())
        .unique("article_id", keep="last")
    )


def pure_raw_paths(root: Path) -> list[Path]:
    base = root / "data" / "pure_raw" / "news"
    return sorted(base.rglob("*.json")) if base.exists() else []


def raw_news_paths(root: Path) -> list[Path]:
    base = root / "data" / "raw" / "news"
    if not base.exists():
        return []
    return sorted([p for p in base.rglob("*.json") if p.is_file()])


def canonical_paths(root: Path) -> tuple[Path, Path]:
    macro = root / "data" / "raw" / "news" / "macro-news" / "macro_news_2020-2026.parquet"
    market = root / "data" / "raw" / "news" / "market_news" / "market_news_2020-2026.parquet"
    return macro, market


def refresh_canonical_raw_news(root: Path, merge_existing: bool = True, write_json: bool = False) -> pl.DataFrame:
    frames = []
    if merge_existing:
        macro_pq, market_pq = canonical_paths(root)
        for p in [macro_pq, market_pq]:
            if p.exists():
                frames.append(pl.read_parquet(p))
        # Also include old JSON canonical if Parquet does not exist yet.
        json_paths = raw_news_paths(root)
        if json_paths:
            frames.append(load_news_files(json_paths))
    pure_paths = pure_raw_paths(root)
    if pure_paths:
        frames.append(load_news_files(pure_paths))
    if not frames:
        return load_news_files([])
    df = pl.concat(frames, how="diagonal_relaxed").unique("article_id", keep="last")
    macro = df.filter(pl.col("news_category") == "macro")
    market = df.filter(pl.col("news_category") != "macro")
    macro_path, market_path = canonical_paths(root)
    macro_path.parent.mkdir(parents=True, exist_ok=True)
    market_path.parent.mkdir(parents=True, exist_ok=True)
    macro.write_parquet(macro_path)
    market.write_parquet(market_path)
    if write_json:
        (macro_path.with_suffix(".json")).write_text(json.dumps(macro.to_dicts(), ensure_ascii=False), encoding="utf-8")
        (market_path.with_suffix(".json")).write_text(json.dumps(market.to_dicts(), ensure_ascii=False), encoding="utf-8")
    return df


def load_canonical_raw_news(root: Path) -> pl.DataFrame:
    macro_path, market_path = canonical_paths(root)
    frames = []
    for p in [macro_path, market_path]:
        if p.exists():
            frames.append(pl.read_parquet(p))
    if frames:
        return pl.concat(frames, how="diagonal_relaxed").unique("article_id", keep="last")
    return load_news_files(raw_news_paths(root))


def load_emiten(path: Path) -> pl.DataFrame:
    records = _read_json_records(path)
    if not records:
        return pl.DataFrame(schema={"ticker": pl.Utf8})
    df = pl.DataFrame(records)
    rename = {}
    opts = {
        "ticker": ["KodeEmiten", "ticker", "kode", "symbol"],
        "company_name": ["NamaEmiten", "company_name", "nama", "name"],
        "sector": ["Sektor", "sector", "sektor"],
        "subsector": ["SubSektor", "subsector", "sub_sektor"],
        "industry": ["Industri", "industry"],
        "subindustry": ["SubIndustri", "subindustry"],
        "listing_board": ["PapanPencatatan", "listing_board"],
        "listing_date": ["TanggalPencatatan", "listing_date"],
    }
    for target, candidates in opts.items():
        for c in candidates:
            if c in df.columns:
                rename[c] = target
                break
    df = df.rename(rename)
    for c in opts:
        if c not in df.columns:
            df = df.with_columns(pl.lit(None).cast(pl.Utf8).alias(c))
    return (
        df.with_columns([
            pl.col("ticker").cast(pl.Utf8).str.to_uppercase(),
            pl.col("listing_date").cast(pl.Utf8).str.strip_chars().str.slice(0, 10).str.strptime(pl.Date, format="%Y-%m-%d", strict=False).alias("listing_date"),
        ])
        .select(["ticker", "company_name", "sector", "subsector", "industry", "subindustry", "listing_board", "listing_date"])
        .filter(pl.col("ticker").is_not_null())
        .unique("ticker", keep="last")
    )


def _extract_tickers(title: str, text: str, valid: set[str]) -> list[tuple[str, str]]:
    combined = f"{title or ''} {text or ''}"
    seen = set()
    out = []
    title_cands = TICKER_RE.findall(title or "")
    content_cands = TICKER_RE.findall(combined or "")
    for c in title_cands + content_cands:
        c = c.upper()
        if c in seen or c in CAPITAL_STOPWORDS or c not in valid:
            continue
        seen.add(c)
        match_type = "title" if c in title_cands else "content"
        out.append((c, match_type))
    return out


def build_article_event_rows(news: pl.DataFrame, emiten: pl.DataFrame) -> pl.DataFrame:
    valid = set(emiten.get_column("ticker").drop_nulls().to_list()) if "ticker" in emiten.columns else set()
    rows = []
    for r in news.iter_rows(named=True):
        dec = classify_event(r.get("title"), r.get("summary"), r.get("full_content"), r.get("news_category"))
        text = f"{r.get('summary') or ''} {r.get('full_content') or ''}"
        tickers = _extract_tickers(r.get("title") or "", text, valid)
        # Keep market/macro articles without ticker as __MARKET__ for market-day regime only.
        if not tickers and dec.event_scope == "market":
            tickers = [("__MARKET__", "market_scope")]
        for ticker, match_type in tickers:
            eid_key = f"{r.get('article_id')}|{ticker}|{dec.event_type}|{dec.event_side}"
            rows.append({
                "event_row_id": hashlib.md5(eid_key.encode()).hexdigest(),
                "article_id": r.get("article_id"),
                "source": r.get("source"),
                "news_category": r.get("news_category"),
                "news_date": r.get("news_date"),
                "title": r.get("title"),
                "summary": r.get("summary"),
                "full_content": r.get("full_content"),
                "url": r.get("url"),
                "ticker": ticker,
                "entity_match_type": match_type,
                "event_scope": dec.event_scope,
                "event_type": dec.event_type,
                "event_side": dec.event_side,
                "impact_channel": dec.impact_channel,
                "materiality_label": dec.materiality_label,
                "materiality_score": dec.materiality_score,
                "news_intensity_score": dec.news_intensity_score,
                "uncertainty_score": dec.uncertainty_score,
                "bullish_keyword_hits": dec.bullish_keyword_hits,
                "bearish_keyword_hits": dec.bearish_keyword_hits,
                "uncertainty_keyword_hits": dec.uncertainty_keyword_hits,
            })
    if not rows:
        return pl.DataFrame()
    events = pl.DataFrame(rows)
    events = events.join(emiten, on="ticker", how="left")
    events = events.sort(["ticker", "event_type", "news_date"])
    events = events.with_columns([
        pl.cum_count("event_row_id").over(["ticker", "event_type"]).alias("same_event_seen_so_far"),
    ])
    events = events.with_columns([
        (1.0 / (1.0 + pl.col("same_event_seen_so_far").cast(pl.Float64).log1p())).clip(0.05, 1.0).alias("novelty_score")
    ])
    return events.unique("event_row_id", keep="last")


def load_ohlcv(path: Path) -> pl.DataFrame:
    if not path or not path.exists():
        return pl.DataFrame()
    if path.suffix.lower() == ".parquet":
        df = pl.read_parquet(path)
    else:
        df = pl.read_csv(path, infer_schema_length=10000)
    # normalize lower-case-ish columns
    ren = {c: c.strip() for c in df.columns}
    df = df.rename(ren)
    lower = {c.lower(): c for c in df.columns}
    mapping = {}
    for target in ["date", "ticker", "open", "high", "low", "close", "volume", "value", "frequency", "foreign_buy", "foreign_sell"]:
        if target in lower and lower[target] != target:
            mapping[lower[target]] = target
    df = df.rename(mapping)
    for c in ["open", "high", "low", "close", "volume", "value", "frequency", "foreign_buy", "foreign_sell"]:
        if c not in df.columns:
            df = df.with_columns(pl.lit(None).cast(pl.Float64).alias(c))
    if "value" in df.columns:
        pass
    df = df.with_columns([
        pl.col("date").cast(pl.Utf8).str.slice(0, 10).str.strptime(pl.Date, format="%Y-%m-%d", strict=False).alias("date"),
        pl.col("ticker").cast(pl.Utf8).str.to_uppercase(),
        *[pl.col(c).cast(pl.Float64, strict=False).alias(c) for c in ["open", "high", "low", "close", "volume", "value", "frequency", "foreign_buy", "foreign_sell"]]
    ]).filter(pl.col("date").is_not_null() & pl.col("ticker").is_not_null())
    if df["value"].null_count() == df.height:
        df = df.with_columns((pl.col("close") * pl.col("volume")).alias("value"))
    return df.unique(["date", "ticker"], keep="last").sort(["ticker", "date"])


def enrich_ohlcv_features(ohlcv: pl.DataFrame, emiten: pl.DataFrame, windows: list[int]) -> pl.DataFrame:
    if ohlcv.is_empty():
        return ohlcv
    df = ohlcv.join(emiten.select(["ticker", "sector", "listing_date"]), on="ticker", how="left")
    df = df.filter(pl.col("listing_date").is_null() | (pl.col("date") >= pl.col("listing_date")))
    df = df.sort(["ticker", "date"])
    df = df.with_columns([
        (pl.col("close") / pl.col("close").shift(1).over("ticker") - 1).alias("daily_ret"),
        (pl.col("volume").fill_null(0) <= 0).alias("is_zero_volume"),
        pl.col("volume").rolling_mean(20, min_samples=1).over("ticker").alias("avg_volume_20d"),
    ])
    df = df.with_columns([
        (pl.col("volume") / pl.col("avg_volume_20d").replace(0, None)).alias("volume_ratio"),
        pl.col("daily_ret").rolling_std(20, min_samples=5).over("ticker").alias("bwd_volatility_20d"),
        (pl.col("close") / pl.col("close").rolling_max(20, min_samples=1).over("ticker") - 1).alias("drawdown_20d"),
    ])
    for h in windows:
        df = df.with_columns([
            (pl.col("close") / pl.col("close").shift(h).over("ticker") - 1).alias(f"bwd_ret_{h}d"),
            (pl.col("close").shift(-h).over("ticker") / pl.col("close") - 1).alias(f"fwd_ret_{h}d"),
            (pl.col("volume") / pl.col("volume").shift(h).over("ticker").replace(0, None)).alias(f"bwd_volume_ratio_{h}d"),
        ])
    # Forward vol/MAE/MFE via per-ticker map_groups for correctness.
    def add_forward(g: pl.DataFrame) -> pl.DataFrame:
        g = g.sort("date")
        close = g.get_column("close")
        lows = g.get_column("low")
        highs = g.get_column("high")
        ret = g.get_column("daily_ret")
        cols = []
        for h in windows:
            fwd_vol = ret.shift(-1).reverse().rolling_std(window_size=h, min_samples=1).reverse().fill_null(0.0).alias(f"fwd_realized_vol_{h}d")
            fwd_low = lows.shift(-1).reverse().rolling_min(window_size=h, min_samples=1).reverse()
            fwd_high = highs.shift(-1).reverse().rolling_max(window_size=h, min_samples=1).reverse()
            mae = (fwd_low / close - 1).alias(f"mae_{h}d")
            mfe = (fwd_high / close - 1).alias(f"mfe_{h}d")
            cols += [fwd_vol, mae, mfe]
        return g.with_columns(cols)
    df = df.group_by("ticker", maintain_order=True).map_groups(add_forward)

    # IHSG forward returns or market median fallback.
    ihsg = df.filter(pl.col("ticker") == "IHSG").select(["date"] + [f"fwd_ret_{h}d" for h in windows])
    if ihsg.height == 0:
        ihsg = df.group_by("date").agg([pl.col(f"fwd_ret_{h}d").median().alias(f"ihsg_fwd_ret_{h}d") for h in windows])
    else:
        ihsg = ihsg.rename({f"fwd_ret_{h}d": f"ihsg_fwd_ret_{h}d" for h in windows})
    df = df.join(ihsg, on="date", how="left")
    sector_ret = df.group_by(["date", "sector"]).agg([pl.col(f"fwd_ret_{h}d").median().alias(f"sector_fwd_ret_{h}d") for h in windows])
    df = df.join(sector_ret, on=["date", "sector"], how="left")
    for h in windows:
        df = df.with_columns([
            (pl.col(f"fwd_ret_{h}d") - pl.col(f"ihsg_fwd_ret_{h}d")).alias(f"market_alpha_{h}d"),
            (pl.col(f"fwd_ret_{h}d") - pl.col(f"sector_fwd_ret_{h}d")).alias(f"sector_alpha_{h}d"),
            (pl.col(f"fwd_realized_vol_{h}d") / pl.col("bwd_volatility_20d").replace(0, None)).alias(f"volatility_shock_{h}d"),
        ])
    return df


def attach_market_outcomes(events: pl.DataFrame, ohlcv: pl.DataFrame, emiten: pl.DataFrame, windows: list[int]) -> pl.DataFrame:
    if events.is_empty() or ohlcv.is_empty():
        return events.with_columns(pl.lit("no_ohlcv_attached").alias("outcome_status"))
    feats = enrich_ohlcv_features(ohlcv, emiten, windows)
    feats = feats.rename({"date": "entry_date"})
    events2 = events.with_columns((pl.col("news_date") + pl.duration(days=1)).alias("entry_lookup_date"))
    left = events2.filter(pl.col("ticker") != "__MARKET__").sort(["ticker", "entry_lookup_date"])
    right = feats.sort(["ticker", "entry_date"])
    attached = left.join_asof(
        right,
        left_on="entry_lookup_date",
        right_on="entry_date",
        by="ticker",
        strategy="forward",
    ).drop("entry_lookup_date")
    market_rows = events2.filter(pl.col("ticker") == "__MARKET__").drop("entry_lookup_date")
    if market_rows.height:
        attached = pl.concat([attached, market_rows], how="diagonal_relaxed")
    attached = add_reaction_labels(attached)
    return attached


def add_reaction_labels(df: pl.DataFrame) -> pl.DataFrame:
    if "sector_alpha_5d" not in df.columns:
        return df
    return df.with_columns([
        pl.when(pl.col("sector_alpha_5d") > 0.01).then(pl.lit("positive_alpha"))
          .when(pl.col("sector_alpha_5d") < -0.01).then(pl.lit("negative_alpha"))
          .otherwise(pl.lit("neutral_alpha")).alias("directional_label_5d"),
        (pl.col("volatility_shock_5d") > 1.5).cast(pl.Int8).alias("volatility_label_5d"),
        (pl.col("mae_5d") < -0.03).cast(pl.Int8).alias("risk_label_5d"),
        ((pl.col("event_side").str.contains("bullish|positive", literal=False)) & (pl.col("bwd_ret_5d") > 0.05) & (pl.col("sector_alpha_5d") < -0.01)).cast(pl.Int8).alias("sentiment_trap_label_5d"),
        ((pl.col("bwd_ret_5d") > 0.05) & (pl.col("sector_alpha_5d") < -0.01)).cast(pl.Int8).alias("sell_the_news_label_5d"),
        ((pl.col("fwd_ret_1d").abs() < 0.005) & (pl.col("sector_alpha_5d") > 0.01)).cast(pl.Int8).alias("delayed_reaction_label_5d"),
        ((pl.col("bwd_ret_5d").abs() < 0.03) & (pl.col("sector_alpha_5d") > 0.02)).cast(pl.Int8).alias("acceleration_trigger_label_5d"),
        (pl.col("sector_alpha_5d") > 0.01).cast(pl.Int8).alias("confirmed_positive_label_5d"),
        (pl.col("sector_alpha_5d") < -0.01).cast(pl.Int8).alias("confirmed_negative_label_5d"),
    ]).with_columns([
        pl.when(pl.col("sentiment_trap_label_5d") == 1).then(pl.lit("sentiment_trap"))
          .when(pl.col("sell_the_news_label_5d") == 1).then(pl.lit("sell_the_news"))
          .when(pl.col("delayed_reaction_label_5d") == 1).then(pl.lit("delayed_reaction"))
          .when(pl.col("acceleration_trigger_label_5d") == 1).then(pl.lit("acceleration_trigger"))
          .when(pl.col("confirmed_positive_label_5d") == 1).then(pl.lit("confirmed_positive"))
          .when(pl.col("confirmed_negative_label_5d") == 1).then(pl.lit("confirmed_negative"))
          .otherwise(pl.lit("neutral_or_noise")).alias("reaction_label_5d")
    ])


def build_news_event_intelligence_dataset(
    root: str | Path,
    news_source: str = "raw",
    refresh_raw_news: bool = False,
    merge_existing_raw_news: bool = True,
    emiten_path: str = "data/raw/emiten/listed_companies.json",
    ohlcv_path: Optional[str] = None,
    windows: list[int] | None = None,
    output_dir: str = "data/news/event_intelligence",
    build_report: bool = False,
    write_full_csv: bool = False,
) -> BuildResult:
    root = Path(root)
    windows = windows or DEFAULT_WINDOWS
    if refresh_raw_news:
        news = refresh_canonical_raw_news(root, merge_existing=merge_existing_raw_news)
    elif news_source == "pure_raw":
        news = load_news_files(pure_raw_paths(root))
    else:
        news = load_canonical_raw_news(root)
    emiten = load_emiten(root / emiten_path)
    events = build_article_event_rows(news, emiten)
    ohlcv = load_ohlcv(root / ohlcv_path) if ohlcv_path else pl.DataFrame()
    events = attach_market_outcomes(events, ohlcv, emiten, windows)

    out = root / output_dir
    out.mkdir(parents=True, exist_ok=True)
    output_parquet = out / "news_event_intelligence_dataset.parquet"
    sample_path = out / "sample_5.csv"
    events.write_parquet(output_parquet)
    events.head(5).write_csv(sample_path)
    output_csv = None
    if write_full_csv:
        output_csv = out / "news_event_intelligence_dataset.csv"
        events.write_csv(output_csv)
    meta = {
        "engine": "polars",
        "rows": events.height,
        "articles": events.get_column("article_id").n_unique() if "article_id" in events.columns and events.height else 0,
        "tickers": events.get_column("ticker").n_unique() if "ticker" in events.columns and events.height else 0,
        "news_source": news_source,
        "refresh_raw_news": refresh_raw_news,
        "merge_existing_raw_news": merge_existing_raw_news,
        "emiten_path": emiten_path,
        "ohlcv_path": ohlcv_path,
        "windows": windows,
        "output_parquet": str(output_parquet.relative_to(root)),
        "output_csv": str(output_csv.relative_to(root)) if output_csv else None,
        "sample_path": str(sample_path.relative_to(root)),
    }
    (out / "build_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    if build_report:
        from alpha_research.news.event_study_polars import build_basic_event_study
        build_basic_event_study(events, out / "report")
    return BuildResult(**meta)
