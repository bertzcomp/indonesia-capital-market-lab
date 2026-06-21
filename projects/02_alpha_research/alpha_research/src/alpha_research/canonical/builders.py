from __future__ import annotations
from pathlib import Path
import re
import polars as pl
from alpha_research.core.dates import parse_date_any, ensure_start_end, extract_date_from_name
from alpha_research.core.io import read_table, safe_write_parquet, write_json
from alpha_research.core.contracts import assert_unique

NUMERIC_REPLACE = [",", "%", "-"]


def _norm_col_name(c: str) -> str:
    """Normalize source column names for tolerant schema matching."""
    return re.sub(r"[^a-z0-9]+", "", str(c).lower().strip())


def _clean_num_expr(c: str):
    return (pl.col(c).cast(pl.Utf8, strict=False)
        .str.replace_all(",", "")
        .str.replace_all("%", "")
        .str.replace_all(r"^-$", "")
        .cast(pl.Float64, strict=False))

def _standardize_date_series(df: pl.DataFrame, col="date") -> pl.DataFrame:
    """Normalize a date column to pl.Date without throwing opaque parser errors.

    Date parsing has historically been one of the main failure points in this
    project because IDX/KSEI/third-party files mix ISO, compact YYYYMMDD,
    English month names, and Indonesian month abbreviations such as ``Agt``.
    The parser returns None for unparseable values; those rows are later
    removed by date filtering or explicit ``drop_nulls`` in each canonical
    builder.
    """
    if col not in df.columns:
        return df
    vals = [parse_date_any(x) for x in df[col].to_list()]
    return df.with_columns(pl.Series(col, vals).cast(pl.Date).alias(col))

def _standardize_ticker(df: pl.DataFrame, col="ticker") -> pl.DataFrame:
    if col in df.columns:
        return df.with_columns(pl.col(col).cast(pl.Utf8, strict=False).str.to_uppercase().str.strip_chars().alias(col))
    return df

def _filter_date(df: pl.DataFrame, start, end) -> pl.DataFrame:
    s,e=ensure_start_end(start,end)
    if "date" not in df.columns: return df
    return df.filter((pl.col("date")>=pl.lit(s)) & (pl.col("date")<=pl.lit(e)))

def build_ohlcv(root, start, end):
    root = Path(root)
    out = root / "data/raw_canonical/ohlcv.parquet"
    diag_dir = root / "data/raw_canonical/_diagnostics"
    diag_dir.mkdir(parents=True, exist_ok=True)

    frames = []
    diagnostics = []

    # Historical canonical/raw OHLCV files + daily IDX trading summary.
    # IMPORTANT:
    # - data/raw/ohlcv may contain long historical vendor files.
    # - data/pure_raw/trading_summary contains daily RingkasanSaham-YYYYMMDD.xlsx.
    # - pure_raw gets higher priority so recent official IDX files override stale historical rows.
    for base in [root / "data/raw/ohlcv", root / "data/pure_raw/trading_summary"]:
        if not base.exists():
            diagnostics.append({"base": str(base), "status": "missing_base_dir"})
            continue

        files = sorted(
            list(base.glob("*.csv"))
            + list(base.glob("*.parquet"))
            + list(base.glob("*.xlsx"))
            + list(base.glob("*.xls"))
        )

        for p in files:
            file_diag = {
                "path": str(p),
                "source_kind": "pure_raw_trading_summary" if "pure_raw" in str(p) else "raw_ohlcv",
                "status": "started",
            }
            try:
                df = read_table(p)
                file_diag["raw_rows"] = df.height
                file_diag["raw_cols"] = df.width
                file_diag["columns"] = list(df.columns)

                cols = {_norm_col_name(c): c for c in df.columns}

                # More tolerant mapping. The old version matched lower/strip only,
                # which is fragile for Stock Code, Open Price, snake_case variants,
                # and future IDX spelling changes.
                mapping = {
                    "date": "date",
                    "tanggal": "date",
                    "tradedate": "date",

                    "stockcode": "ticker",
                    "stock": "ticker",
                    "ticker": "ticker",
                    "kode": "ticker",
                    "kodeemiten": "ticker",
                    "emiten": "ticker",
                    "code": "ticker",

                    "openprice": "open",
                    "open": "open",
                    "firsttrade": "first_trade",
                    "high": "high",
                    "highprice": "high",
                    "low": "low",
                    "lowprice": "low",
                    "close": "close",
                    "closeprice": "close",

                    "volume": "volume",
                    "value": "value",
                    "frequency": "frequency",
                    "freq": "frequency",
                    "foreignbuy": "foreign_buy",
                    "foreignsell": "foreign_sell",
                    "nonregularvolume": "non_regular_volume",
                    "nonregularvalue": "non_regular_value",
                    "nonregularfrequency": "non_regular_frequency",
                }
                ren = {orig: mapping[k] for k, orig in cols.items() if k in mapping}

                # Date can also be inferred from filename, e.g. RingkasanSaham-20260602.xlsx.
                file_date = extract_date_from_name(p.name)
                required_no_date = {"ticker", "open", "high", "low", "close", "volume"}
                present_targets = set(ren.values())

                if not required_no_date.issubset(present_targets):
                    file_diag.update({
                        "status": "skipped_missing_required_columns",
                        "present_targets": sorted(present_targets),
                        "required": sorted(required_no_date),
                    })
                    diagnostics.append(file_diag)
                    continue

                if "date" not in present_targets and file_date is None:
                    file_diag.update({
                        "status": "skipped_missing_date",
                        "present_targets": sorted(present_targets),
                        "note": "No date column and no YYYYMMDD date in filename.",
                    })
                    diagnostics.append(file_diag)
                    continue

                df = df.rename(ren)

                if "date" not in df.columns:
                    df = df.with_columns(pl.lit(file_date).cast(pl.Date).alias("date"))
                    if file_date is not None:
                        file_diag["date_source"] = "filename"
                else:
                    # IDX daily trading summary files are single-day files and the
                    # filename date is more reliable than mixed parser heuristics.
                    #
                    # Example bug caught in production:
                    #   RingkasanSaham-20260602.xlsx has Date = 2026-06-02T00:00:00
                    #   but the generic parse_date_any path interpreted it as 2026-02-06.
                    #
                    # Therefore for data/pure_raw/trading_summary/RingkasanSaham-YYYYMMDD.*
                    # we force date from filename and record the raw parsed date in diagnostics.
                    if file_date is not None and "pure_raw" in str(p) and "trading_summary" in str(p):
                        raw_date_sample = df["date"].head(3).to_list() if "date" in df.columns else []
                        parsed_tmp = _standardize_date_series(df.select(["date"]), "date")
                        parsed_min = parsed_tmp["date"].min() if parsed_tmp.height else None
                        parsed_max = parsed_tmp["date"].max() if parsed_tmp.height else None
                        df = df.with_columns(pl.lit(file_date).cast(pl.Date).alias("date"))
                        file_diag["date_source"] = "filename_forced"
                        file_diag["filename_date"] = file_date
                        file_diag["raw_date_sample"] = [str(x) for x in raw_date_sample]
                        file_diag["generic_parsed_min_date_before_override"] = parsed_min
                        file_diag["generic_parsed_max_date_before_override"] = parsed_max
                        if parsed_min != file_date or parsed_max != file_date:
                            file_diag["date_override_reason"] = "generic parser disagreed with RingkasanSaham filename date"
                    else:
                        df = _standardize_date_series(df, "date")
                        if file_date is not None:
                            df = df.with_columns(pl.col("date").fill_null(pl.lit(file_date).cast(pl.Date)).alias("date"))
                            file_diag["date_source"] = "date_column_with_filename_null_fallback"
                        else:
                            file_diag["date_source"] = "date_column"

                # Prefer OpenPrice; if it is missing/null but FirstTrade is present, use FirstTrade.
                if "open" not in df.columns and "first_trade" in df.columns:
                    df = df.rename({"first_trade": "open"})
                elif "first_trade" in df.columns:
                    df = df.with_columns(pl.when(pl.col("open").is_null()).then(pl.col("first_trade")).otherwise(pl.col("open")).alias("open"))

                keep = [
                    "date", "ticker", "open", "high", "low", "close", "volume",
                    "value", "frequency", "foreign_buy", "foreign_sell"
                ]
                for c in keep:
                    if c not in df.columns:
                        df = df.with_columns(pl.lit(None).alias(c))
                df = df.select(keep)

                df = _standardize_ticker(df, "ticker")
                before_drop = df.height
                df = df.drop_nulls(["date", "ticker"])
                file_diag["rows_after_date_ticker_drop"] = df.height
                file_diag["dropped_date_ticker_nulls"] = before_drop - df.height

                if df.is_empty():
                    file_diag.update({"status": "skipped_empty_after_date_ticker_cleaning"})
                    diagnostics.append(file_diag)
                    continue

                for c in ["open", "high", "low", "close", "volume", "value", "frequency", "foreign_buy", "foreign_sell"]:
                    df = df.with_columns(_clean_num_expr(c).alias(c))

                # Drop rows with no usable price/volume identity.
                before_required_numeric = df.height
                df = df.drop_nulls(["open", "high", "low", "close", "volume"])
                file_diag["rows_after_required_numeric_drop"] = df.height
                file_diag["dropped_required_numeric_nulls"] = before_required_numeric - df.height

                if df.is_empty():
                    file_diag.update({"status": "skipped_empty_after_numeric_cleaning"})
                    diagnostics.append(file_diag)
                    continue

                # source priority: pure_raw trading summary > raw historical
                prio = 2 if "pure_raw" in str(p) else 1
                df = df.with_columns(
                    pl.lit(str(p)).alias("source_file"),
                    pl.lit(prio).alias("source_priority"),
                )

                file_diag.update({
                    "status": "loaded",
                    "min_date": df["date"].min(),
                    "max_date": df["date"].max(),
                    "rows_loaded": df.height,
                    "source_priority": prio,
                })
                diagnostics.append(file_diag)
                frames.append(df)

            except Exception as e:
                file_diag.update({"status": "error", "error": repr(e)})
                diagnostics.append(file_diag)
                continue

    if not frames:
        df = pl.DataFrame(schema={
            "date": pl.Date,
            "ticker": pl.Utf8,
            "open": pl.Float64,
            "high": pl.Float64,
            "low": pl.Float64,
            "close": pl.Float64,
            "volume": pl.Float64,
            "value": pl.Float64,
            "frequency": pl.Float64,
            "foreign_buy": pl.Float64,
            "foreign_sell": pl.Float64,
        })
    else:
        df = pl.concat(frames, how="diagonal_relaxed")
        df = _filter_date(df, start, end)

        # Keep highest source priority and latest source file deterministically.
        df = (
            df.sort(["date", "ticker", "source_priority", "source_file"])
              .unique(subset=["date", "ticker"], keep="last")
              .sort(["date", "ticker"])
        )

        df = df.select([
            "date", "ticker", "open", "high", "low", "close", "volume",
            "value", "frequency", "foreign_buy", "foreign_sell"
        ])
        assert_unique(df, ["date", "ticker"], "ohlcv_canonical")

    # Persist source diagnostics so future silent-skip issues are traceable.
    write_json(diag_dir / "ohlcv_sources.json", {
        "table": "ohlcv",
        "start": str(ensure_start_end(start, end)[0]),
        "end": str(ensure_start_end(start, end)[1]),
        "canonical_rows": df.height,
        "canonical_min_date": df["date"].min() if df.height else None,
        "canonical_max_date": df["date"].max() if df.height else None,
        "sources": diagnostics,
    })

    safe_write_parquet(df, out)
    return {
        "table": "ohlcv",
        "rows": df.height,
        "cols": df.width,
        "min_date": df["date"].min() if df.height else None,
        "max_date": df["date"].max() if df.height else None,
        "path": str(out),
        "diagnostics_path": str(diag_dir / "ohlcv_sources.json"),
    }

def build_broker_summary(root, start, end):
    root=Path(root); out=root/"data/raw_canonical/broker_summary.parquet"
    frames=[]
    for base in [root/"data/raw/broker_summary", root/"data/raw/broksum", root/"data/pure_raw/broker_summary"]:
        if not base.exists(): continue
        for p in sorted(base.glob("*.csv")):
            try: df=pl.read_csv(p, infer_schema_length=10000, ignore_errors=True)
            except Exception: continue
            cols={c.lower().strip():c for c in df.columns}
            def get(*names):
                for n in names:
                    if n in cols: return cols[n]
                return None
            stock=get("stock_code","ticker","kode","code")
            datec=get("date","tanggal")
            rankc=get("rank")
            if not (stock and datec and rankc): continue
            ren={stock:"ticker", datec:"date", rankc:"rank"}
            for raw,new in [("by","buy_broker"),("by_type","buy_type"),("b.val","buy_val"),("b.lot","buy_lot"),("b.freq","buy_freq"),("b.avg","buy_avg"),("sl","sell_broker"),("sl_type","sell_type"),("s.val","sell_val"),("s.lot","sell_lot"),("s.freq","sell_freq"),("s.avg","sell_avg")]:
                if raw in cols: ren[cols[raw]]=new
            df=df.rename(ren)
            keep=["date","ticker","rank","buy_broker","buy_type","buy_val","buy_lot","buy_freq","buy_avg","sell_broker","sell_type","sell_val","sell_lot","sell_freq","sell_avg"]
            for c in keep:
                if c not in df.columns: df=df.with_columns(pl.lit(None).alias(c))
            df=df.select(keep)
            df=_standardize_date_series(df,"date"); df=_standardize_ticker(df,"ticker")
            df=df.drop_nulls(["date", "ticker"])
            df=df.with_columns(pl.col("rank").cast(pl.Int32, strict=False))
            for c in ["buy_val","buy_lot","buy_freq","buy_avg","sell_val","sell_lot","sell_freq","sell_avg"]:
                df=df.with_columns(_clean_num_expr(c).alias(c))
            for c in ["buy_broker","buy_type","sell_broker","sell_type"]:
                df=df.with_columns(pl.col(c).cast(pl.Utf8, strict=False).str.to_uppercase().str.strip_chars())
            df=df.with_columns(pl.lit(str(p)).alias("source_file"))
            frames.append(df)
    if not frames:
        df=pl.DataFrame(schema={"date":pl.Date,"ticker":pl.Utf8,"rank":pl.Int32})
    else:
        df=pl.concat(frames, how="diagonal_relaxed")
        df=_filter_date(df,start,end)
        df=df.unique(subset=["date","ticker","rank","buy_broker","sell_broker","buy_val","sell_val"], keep="last")
        # if same date/ticker/rank still duplicate, keep first deterministically
        df=df.sort(["date","ticker","rank"]).unique(subset=["date","ticker","rank"], keep="first")
    safe_write_parquet(df,out)
    return {"table":"broker_summary","rows":df.height,"cols":df.width,"min_date":df["date"].min() if df.height and "date" in df.columns else None,"max_date":df["date"].max() if df.height and "date" in df.columns else None,"path":str(out)}

def build_insider_activity(root, start, end):
    root = Path(root)
    out = root / "data/raw_canonical/insider_activity.parquet"
    diag_dir = root / "data/raw_canonical/_diagnostics"
    diag_dir.mkdir(parents=True, exist_ok=True)

    frames = []
    diagnostics = []

    for base in [root / "data/raw/insider_activity", root / "data/pure_raw/insider_activity"]:
        if not base.exists():
            diagnostics.append({"base": str(base), "status": "missing_base_dir"})
            continue

        for p in sorted(base.glob("*.csv")):
            file_diag = {
                "path": str(p),
                "source_kind": "pure_raw_insider_activity" if "pure_raw" in str(p) else "raw_insider_activity",
                "status": "started",
            }
            try:
                df = pl.read_csv(p, infer_schema_length=10000, ignore_errors=True, try_parse_dates=False)
                file_diag["raw_rows"] = df.height
                file_diag["raw_cols"] = df.width
                file_diag["columns"] = list(df.columns)

                cols = {_norm_col_name(c): c for c in df.columns}

                def pick(*names):
                    for n in names:
                        key = _norm_col_name(n)
                        if key in cols:
                            return cols[key]
                    return None

                datec = pick("date", "tanggal", "transaction_date", "trade_date", "report_date", "recording_date")
                tickc = pick("ticker", "stock_code", "stockcode", "kode", "kode_emiten", "emiten_code", "emiten code", "code")
                if not datec or not tickc:
                    file_diag.update({
                        "status": "skipped_missing_date_or_ticker",
                        "date_col": datec,
                        "ticker_col": tickc,
                    })
                    diagnostics.append(file_diag)
                    continue

                ren = {datec: "date", tickc: "ticker"}

                aliases = [
                    (["action_type", "action", "transaction_type", "type", "jenis_transaksi"], "action_type"),
                    (["shares_changed", "share_changed", "shares", "jumlah_saham", "jumlah"], "shares_changed"),
                    (["shares_changed_pct", "share_changed_pct", "pct", "percentage", "persen"], "shares_changed_pct"),
                    (["nationality", "kewarganegaraan"], "nationality"),
                    (["broker_group", "broker", "group"], "broker_group"),
                    (["insider_name", "name", "nama", "nama_pemegang_saham"], "insider_name"),
                ]
                for keys, target in aliases:
                    c = pick(*keys)
                    if c:
                        ren[c] = target

                df = df.rename(ren)
                keep = [
                    "date", "ticker", "action_type", "shares_changed", "shares_changed_pct",
                    "nationality", "broker_group", "insider_name"
                ]
                for c in keep:
                    if c not in df.columns:
                        df = df.with_columns(pl.lit(None).alias(c))
                df = df.select(keep)

                df = _standardize_date_series(df, "date")
                df = _standardize_ticker(df, "ticker")

                before_drop = df.height
                df = df.drop_nulls(["date", "ticker"])
                file_diag["rows_after_date_ticker_drop"] = df.height
                file_diag["dropped_date_ticker_nulls"] = before_drop - df.height

                if df.is_empty():
                    file_diag.update({"status": "skipped_empty_after_date_ticker_cleaning"})
                    diagnostics.append(file_diag)
                    continue

                df = df.with_columns(
                    _clean_num_expr("shares_changed").alias("shares_changed"),
                    _clean_num_expr("shares_changed_pct").alias("shares_changed_pct"),
                )
                for c in ["action_type", "nationality", "broker_group", "insider_name"]:
                    df = df.with_columns(pl.col(c).cast(pl.Utf8, strict=False).str.to_uppercase().str.strip_chars().alias(c))

                df = df.with_columns(pl.lit(str(p)).alias("source_file"))
                file_diag.update({
                    "status": "loaded",
                    "min_date": df["date"].min(),
                    "max_date": df["date"].max(),
                    "rows_loaded": df.height,
                })
                diagnostics.append(file_diag)
                frames.append(df)

            except Exception as e:
                file_diag.update({"status": "error", "error": repr(e)})
                diagnostics.append(file_diag)
                continue

    if frames:
        df = pl.concat(frames, how="diagonal_relaxed")
        df = _filter_date(df, start, end)
        # Deduplicate deterministic source overlap while preserving distinct insider/action rows.
        subset = [
            c for c in ["date", "ticker", "action_type", "shares_changed", "shares_changed_pct", "nationality", "broker_group", "insider_name"]
            if c in df.columns
        ]
        df = df.sort(["date", "ticker", "source_file"]).unique(subset=subset, keep="last")
        if "source_file" in df.columns:
            df = df.drop("source_file")
    else:
        df = pl.DataFrame(schema={"date": pl.Date, "ticker": pl.Utf8})

    write_json(diag_dir / "insider_activity_sources.json", {
        "table": "insider_activity",
        "start": str(ensure_start_end(start, end)[0]),
        "end": str(ensure_start_end(start, end)[1]),
        "canonical_rows": df.height,
        "canonical_min_date": df["date"].min() if df.height and "date" in df.columns else None,
        "canonical_max_date": df["date"].max() if df.height and "date" in df.columns else None,
        "sources": diagnostics,
    })

    safe_write_parquet(df, out)
    return {
        "table": "insider_activity",
        "rows": df.height,
        "cols": df.width,
        "min_date": df["date"].min() if df.height and "date" in df.columns else None,
        "max_date": df["date"].max() if df.height and "date" in df.columns else None,
        "path": str(out),
        "diagnostics_path": str(diag_dir / "insider_activity_sources.json"),
    }

def build_corporate_action(root, start, end):
    root=Path(root); out=root/"data/raw_canonical/corporate_action.parquet"
    frames=[]
    for base in [root/"data/raw/corporate_action", root/"data/pure_raw/corporate_action", root/"data/raw"]:
        if not base.exists(): continue
        for p in sorted(list(base.glob("corporate*.csv"))+list(base.glob("corporate*.xlsx"))):
            try: df=read_table(p)
            except Exception: continue
            cols={c.lower().strip():c for c in df.columns}
            datec=cols.get("date"); tickc=cols.get("emiten code") or cols.get("ticker") or cols.get("stock_code")
            typec=cols.get("type of corporate action") or cols.get("type")
            if not datec or not tickc: continue
            ren={datec:"date", tickc:"ticker"}
            if typec: ren[typec]="ca_type"
            df=df.rename(ren)
            keep=["date","ticker","ca_type"]
            for c in keep:
                if c not in df.columns: df=df.with_columns(pl.lit(None).alias(c))
            df=df.select(keep)
            df=_standardize_date_series(df,"date"); df=_standardize_ticker(df,"ticker")
            df=df.drop_nulls(["date", "ticker"])
            df=df.with_columns(pl.col("ca_type").cast(pl.Utf8, strict=False).str.to_uppercase())
            frames.append(df)
    df=pl.concat(frames, how="diagonal_relaxed") if frames else pl.DataFrame(schema={"date":pl.Date,"ticker":pl.Utf8,"ca_type":pl.Utf8})
    if not df.is_empty(): df=_filter_date(df,start,end).unique(subset=["date","ticker","ca_type"])
    safe_write_parquet(df,out)
    return {"table":"corporate_action","rows":df.height,"cols":df.width,"min_date":df["date"].min() if df.height else None,"max_date":df["date"].max() if df.height else None,"path":str(out)}

def _bdm_group_window_from_name(name: str):
    s=name.lower()
    group="foreign" if "-f-" in s else "market_maker" if "-m-" in s else "non_retail" if "-nr-" in s else "unknown"
    window="week" if "-w" in s else "day" if "-d" in s else "unknown"
    return group, window

def build_neo_bdm(root, start, end):
    root=Path(root); out=root/"data/raw_canonical/neo_bdm.parquet"
    frames=[]
    for base in [root/"data/raw/neo_bdm", root/"data/raw/bdm_neo", root/"data/pure_raw/neo_bdm"]:
        if not base.exists(): continue
        files=list(base.rglob("*.csv"))
        for p in sorted(files):
            d=extract_date_from_name(p.parent.name) or extract_date_from_name(p.name)
            if d is None: continue
            group,window=_bdm_group_window_from_name(p.name)
            try: df=pl.read_csv(p, infer_schema_length=10000, ignore_errors=True)
            except Exception: continue
            cols={c.lower().strip():c for c in df.columns}
            tick=cols.get("tick") or cols.get("ticker") or cols.get("stock_code")
            if not tick: continue
            ren={tick:"ticker"}
            for raw,new in [("price","price"),("chg","chg"),("tx","tx"),("history","history")]:
                if raw in cols: ren[cols[raw]]=new
            df=df.rename(ren)
            for c in ["ticker","price","chg","tx","history"]:
                if c not in df.columns: df=df.with_columns(pl.lit(None).alias(c))
            df=df.select(["ticker","price","chg","tx","history"])
            df=_standardize_ticker(df,"ticker")
            df=df.with_columns(pl.lit(d).cast(pl.Date).alias("date"), pl.lit(group).alias("group"), pl.lit(window).alias("window"), pl.lit(str(p)).alias("source_file"))
            for c in ["price","chg","tx"]:
                df=df.with_columns(_clean_num_expr(c).alias(c))
            # history fields
            parts=[]
            for row in df["history"].to_list():
                vals=[]
                if row is not None:
                    for x in str(row).split(',')[:5]:
                        try: vals.append(float(x.replace(',','')))
                        except Exception: vals.append(None)
                vals = vals + [None]*(5-len(vals))
                parts.append(vals)
            if parts:
                hist_df=pl.DataFrame({f"hist{i+1}":[r[i] for r in parts] for i in range(5)})
                df=pl.concat([df.drop("history"), hist_df], how="horizontal")
            frames.append(df)
    df=pl.concat(frames, how="diagonal_relaxed") if frames else pl.DataFrame(schema={"date":pl.Date,"ticker":pl.Utf8,"group":pl.Utf8,"window":pl.Utf8})
    if not df.is_empty():
        df=_filter_date(df,start,end).unique(subset=["date","ticker","group","window"], keep="last")
    safe_write_parquet(df,out)
    return {"table":"neo_bdm","rows":df.height,"cols":df.width,"min_date":df["date"].min() if df.height else None,"max_date":df["date"].max() if df.height else None,"path":str(out)}

def build_tradebook_orderbook(root, start, end):
    root=Path(root); outdir=root/"data/raw_canonical"; outdir.mkdir(parents=True, exist_ok=True)
    summaries=[]
    patterns={"orderbook_snapshot":"orderbook_snapshot_*.csv","orderbook_levels":"orderbook_levels_*.csv","tradebook_price":"tradebook_price_*.csv","tradebook_time":"tradebook_time_*.csv"}
    for name,pat in patterns.items():
        frames=[]
        for base in [root/"data/raw/tradebook", root/"data/raw/orderbook", root/"data/pure_raw/tradebook"]:
            if not base.exists(): continue
            for p in sorted(base.glob(pat)):
                d=extract_date_from_name(p.name)
                try: df=pl.read_csv(p, infer_schema_length=10000, ignore_errors=True)
                except Exception: continue
                cols={c.lower().strip():c for c in df.columns}
                if "ticker" not in cols: continue
                if "date" in cols:
                    df=df.rename({cols["date"]:"date", cols["ticker"]:"ticker"})
                    df=_standardize_date_series(df,"date")
                else:
                    df=df.rename({cols["ticker"]:"ticker"}).with_columns(pl.lit(d).cast(pl.Date).alias("date"))
                df=_standardize_ticker(df,"ticker").with_columns(pl.lit(str(p)).alias("source_file"))
                frames.append(df)
        df=pl.concat(frames, how="diagonal_relaxed") if frames else pl.DataFrame(schema={"date":pl.Date,"ticker":pl.Utf8})
        if not df.is_empty(): df=_filter_date(df,start,end)
        safe_write_parquet(df,outdir/f"{name}.parquet")
        summaries.append({"table":name,"rows":df.height,"cols":df.width,"min_date":df["date"].min() if df.height else None,"max_date":df["date"].max() if df.height else None,"path":str(outdir/f'{name}.parquet')})
    return summaries

def build_macro_fallback(root, start, end):
    root=Path(root); out=root/"data/raw_canonical/macro.parquet"
    ohlcv_path=root/"data/raw_canonical/ohlcv.parquet"
    s,e=ensure_start_end(start,end)
    if ohlcv_path.exists():
        o=pl.read_parquet(ohlcv_path).filter((pl.col("date")>=pl.lit(s)) & (pl.col("date")<=pl.lit(e)))
        if not o.is_empty():
            m=(o.group_by("date").agg([
                pl.col("close").mean().alias("market_close_proxy"),
                pl.col("volume").sum().alias("market_volume"),
                pl.col("value").sum().alias("market_value"),
                pl.col("ticker").n_unique().alias("market_breadth_n")
            ]).sort("date"))
            m=m.with_columns([
                pl.col("market_close_proxy").pct_change().alias("market_ret_1d"),
                (pl.col("market_close_proxy")/pl.col("market_close_proxy").shift(5)-1).alias("market_ret_5d"),
                pl.col("market_ret_1d").rolling_std(20).alias("market_volatility_20d"),
                pl.lit(None).cast(pl.Float64).alias("usd_idr"),
                pl.lit(None).cast(pl.Float64).alias("brent"),
                pl.lit(None).cast(pl.Float64).alias("coal_proxy"),
                pl.lit(1).alias("macro_missing_flag")
            ])
            m=m.with_columns((pl.col("market_volatility_20d").fill_null(0)*10 - pl.col("market_ret_5d").fill_null(0)).alias("macro_risk_score"))
            m=m.with_columns(pl.when(pl.col("macro_risk_score")>0.05).then(pl.lit("RISK_OFF")).when(pl.col("market_ret_5d")>0.03).then(pl.lit("RISK_ON")).otherwise(pl.lit("NEUTRAL")).alias("market_regime"))
            safe_write_parquet(m,out)
            return {"table":"macro","rows":m.height,"cols":m.width,"min_date":m["date"].min(),"max_date":m["date"].max(),"path":str(out),"mode":"market_fallback"}
    dates=pl.date_range(s,e,interval="1d",eager=True).alias("date")
    m=pl.DataFrame({"date":dates}).with_columns([
        pl.lit(None).cast(pl.Float64).alias("market_close_proxy"), pl.lit(None).cast(pl.Float64).alias("market_ret_1d"), pl.lit(None).cast(pl.Float64).alias("market_ret_5d"), pl.lit(None).cast(pl.Float64).alias("market_volatility_20d"), pl.lit(None).cast(pl.Float64).alias("usd_idr"), pl.lit(None).cast(pl.Float64).alias("brent"), pl.lit(None).cast(pl.Float64).alias("coal_proxy"), pl.lit(1).alias("macro_missing_flag"), pl.lit(None).cast(pl.Float64).alias("macro_risk_score"), pl.lit("MISSING").alias("market_regime")
    ])
    safe_write_parquet(m,out)
    return {"table":"macro","rows":m.height,"cols":m.width,"min_date":s,"max_date":e,"path":str(out),"mode":"empty_fallback"}

def build_all_canonical(root, start, end, include_tradebook=True, build_macro=True):
    root=Path(root); (root/"data/raw_canonical").mkdir(parents=True, exist_ok=True)
    steps=[]
    steps.append(build_ohlcv(root,start,end))
    steps.append(build_broker_summary(root,start,end))
    steps.append(build_insider_activity(root,start,end))
    steps.append(build_corporate_action(root,start,end))
    steps.append(build_neo_bdm(root,start,end))
    if include_tradebook:
        steps.extend(build_tradebook_orderbook(root,start,end))
    if build_macro:
        steps.append(build_macro_fallback(root,start,end))
    manifest={"root":str(Path(root).resolve()),"start_date":str(ensure_start_end(start,end)[0]),"end_date":str(ensure_start_end(start,end)[1]),"steps":steps}
    write_json(root/"data/raw_canonical/canonical_manifest.json", manifest)
    return manifest
