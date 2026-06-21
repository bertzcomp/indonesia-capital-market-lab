from __future__ import annotations

import argparse
import html
import json
import re
import urllib.parse
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
import streamlit as st


# -------------------------
# Page config / constants
# -------------------------
st.set_page_config(
    page_title="Alpha Research Signal Board",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ARTIFACTS = {
    "numeric_csv": "numeric_trade_plan.csv",
    "numeric_json": "numeric_trade_plan.json",
    "numeric_report": "numeric_trading_report.md",
    "numeric_meta": "numeric_trade_report_meta.json",
    "narrative_csv": "narrative_signal_cards.csv",
    "narrative_json": "narrative_signal_cards.json",
    "narrative_report": "narrative_trading_report.md",
    "execution": "execution_shortlist.csv",
    "signals_main": "signals_main.csv",
    "watchlist": "all_strategy_watchlist.csv",
    "candidates": "all_strategy_candidates.csv",
    "all_scores": "all_scores.csv",
    "diagnostics": "diagnostics.json",
    "profile_meta": "profile_output_meta.json",
    "report": "report.md",
}


# -------------------------
# Utilities
# -------------------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--root", default=".")
    args, _ = parser.parse_known_args()
    return args


def qget(name: str, default: Optional[str] = None) -> Optional[str]:
    try:
        value = st.query_params.get(name, default)
        if isinstance(value, list):
            return value[0] if value else default
        return value
    except Exception:
        try:
            values = st.experimental_get_query_params().get(name, [default])
            return values[0] if values else default
        except Exception:
            return default


def esc(x: Any) -> str:
    if x is None:
        return ""
    if isinstance(x, float) and pd.isna(x):
        return ""
    return html.escape(str(x))


def is_missing(x: Any) -> bool:
    if x is None:
        return True
    if isinstance(x, float) and pd.isna(x):
        return True
    if isinstance(x, str) and x.strip().lower() in {"", "nan", "none", "null", "-"}:
        return True
    return False


def first_val(row: pd.Series | Dict[str, Any], names: List[str], default: Any = None) -> Any:
    for n in names:
        if n in row and not is_missing(row[n]):
            return row[n]
    return default


def fmt_num(x: Any, digits: int = 2, suffix: str = "") -> str:
    if is_missing(x):
        return "—"
    try:
        v = float(x)
        if abs(v) >= 1000:
            s = f"{v:,.0f}"
        elif v == int(v):
            s = f"{v:.0f}"
        else:
            s = f"{v:.{digits}f}"
        return f"{s}{suffix}"
    except Exception:
        return str(x)


def fmt_pct(x: Any, digits: int = 1) -> str:
    if is_missing(x):
        return "—"
    try:
        v = float(x)
        if abs(v) <= 1.5:
            v *= 100.0
        return f"{v:.{digits}f}%"
    except Exception:
        return str(x)


def fmt_rr(x: Any) -> str:
    if is_missing(x):
        return "—"
    try:
        return f"{float(x):.2f}R"
    except Exception:
        return str(x)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def read_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def discover_signal_folders(root: Path) -> Dict[str, Dict[str, Path]]:
    daily = root / "signals" / "daily"
    result: Dict[str, Dict[str, Path]] = {}
    if not daily.exists():
        return result
    for signal_dir in sorted([p for p in daily.glob("signal_*") if p.is_dir()]):
        profiles: Dict[str, Path] = {}
        child_profiles = [c for c in signal_dir.iterdir() if c.is_dir() and any((c / name).exists() for name in ARTIFACTS.values())]
        if child_profiles:
            for child in sorted(child_profiles):
                profiles[child.name] = child
        else:
            profiles["default"] = signal_dir
        result[signal_dir.name] = profiles
    return result


def route_url(signal: str, profile: str, page: str = "board", ticker: Optional[str] = None) -> str:
    q = {"signal": signal, "profile": profile, "page": page}
    if ticker:
        q["ticker"] = ticker
    return "?" + urllib.parse.urlencode(q)


def normalize_ticker(df: pd.DataFrame) -> pd.DataFrame:
    if not df.empty and "ticker" in df.columns:
        df = df.copy()
        df["ticker"] = df["ticker"].astype(str).str.upper().str.strip()
    return df


def load_bundle(signal_path: Path) -> Dict[str, Any]:
    num = normalize_ticker(read_csv(signal_path / ARTIFACTS["numeric_csv"]))
    nar = normalize_ticker(read_csv(signal_path / ARTIFACTS["narrative_csv"]))
    exec_df = normalize_ticker(read_csv(signal_path / ARTIFACTS["execution"]))
    main_df = normalize_ticker(read_csv(signal_path / ARTIFACTS["signals_main"]))
    watch = normalize_ticker(read_csv(signal_path / ARTIFACTS["watchlist"]))
    cand = normalize_ticker(read_csv(signal_path / ARTIFACTS["candidates"]))
    scores = normalize_ticker(read_csv(signal_path / ARTIFACTS["all_scores"]))

    merged = build_merged_cards(num, nar, exec_df, main_df, watch)

    return {
        "numeric": num,
        "narrative": nar,
        "execution": exec_df,
        "signals_main": main_df,
        "watchlist": watch,
        "candidates": cand,
        "scores": scores,
        "cards": merged,
        "numeric_report": read_text(signal_path / ARTIFACTS["numeric_report"]),
        "narrative_report": read_text(signal_path / ARTIFACTS["narrative_report"]),
        "legacy_report": read_text(signal_path / ARTIFACTS["report"]),
        "diagnostics": read_json(signal_path / ARTIFACTS["diagnostics"]),
        "profile_meta": read_json(signal_path / ARTIFACTS["profile_meta"]),
        "numeric_meta": read_json(signal_path / ARTIFACTS["numeric_meta"]),
        "path": signal_path,
    }


def build_merged_cards(num: pd.DataFrame, nar: pd.DataFrame, exec_df: pd.DataFrame, main_df: pd.DataFrame, watch: pd.DataFrame) -> pd.DataFrame:
    frames: List[pd.DataFrame] = []

    if not num.empty:
        n = num.copy()
        n["_has_numeric"] = True
        frames.append(n)
    elif not nar.empty:
        n = pd.DataFrame({"ticker": nar["ticker"].unique()})
        n["_has_numeric"] = False
        frames.append(n)
    elif not exec_df.empty:
        n = exec_df.copy()
        n["_has_numeric"] = False
        frames.append(n)
    elif not main_df.empty:
        n = main_df.copy()
        n["_has_numeric"] = False
        frames.append(n)
    elif not watch.empty:
        n = watch.copy()
        n["_has_numeric"] = False
        frames.append(n)

    if not frames:
        return pd.DataFrame()

    base = frames[0].copy()
    if "ticker" not in base.columns:
        return pd.DataFrame()
    base = normalize_ticker(base)

    if not nar.empty:
        ncols = [c for c in nar.columns if c != "ticker"]
        base = base.merge(nar[["ticker"] + ncols], on="ticker", how="left", suffixes=("", "_nar"))

    # Add membership/source flags.
    exec_t = set(exec_df["ticker"].astype(str)) if not exec_df.empty and "ticker" in exec_df.columns else set()
    main_t = set(main_df["ticker"].astype(str)) if not main_df.empty and "ticker" in main_df.columns else set()
    watch_t = set(watch["ticker"].astype(str)) if not watch.empty and "ticker" in watch.columns else set()

    def source_label(t: str) -> str:
        if t in exec_t:
            return "execution_shortlist.csv"
        if t in main_t:
            return "signals_main.csv"
        if t in watch_t:
            return "all_strategy_watchlist.csv"
        return "numeric_trade_plan.csv"

    base["signal_source"] = base["ticker"].apply(source_label)
    return base.drop_duplicates("ticker", keep="first")


# -------------------------
# CSS / UI helpers
# -------------------------
def inject_css(theme: str = "Dark") -> None:
    dark = theme.lower().startswith("dark")
    if dark:
        colors = {
            "bg": "#0b1020", "panel": "#111a2e", "panel2": "#162238", "text": "#edf3ff", "muted": "#9aa8bd",
            "border": "#263852", "soft": "#0f1729", "accent": "#2563eb", "green": "#16a34a", "yellow": "#f59e0b", "red": "#ef4444",
        }
    else:
        colors = {
            "bg": "#f6f8fc", "panel": "#ffffff", "panel2": "#f1f5fb", "text": "#172033", "muted": "#5b677a",
            "border": "#dbe3ef", "soft": "#eef3fa", "accent": "#2563eb", "green": "#16a34a", "yellow": "#d97706", "red": "#dc2626",
        }
    st.markdown(f"""
    <style>
    .stApp {{ background: {colors['bg']}; color: {colors['text']}; }}
    section[data-testid="stSidebar"] {{ background: {colors['soft']}; border-right: 1px solid {colors['border']}; }}
    .block-container {{ padding-top: 1.2rem; max-width: 1480px; }}
    h1, h2, h3, h4 {{ color: {colors['text']}; letter-spacing: -0.02em; }}
    .top-hero {{ background: {colors['panel']}; border: 1px solid {colors['border']}; border-radius: 24px; padding: 24px 28px; margin-bottom: 20px; box-shadow: 0 18px 45px rgba(0,0,0,.16); }}
    .top-hero h1 {{ margin:0; font-size: 34px; }}
    .top-hero p {{ color: {colors['muted']}; margin-top: 8px; margin-bottom:0; font-size: 15px; }}
    .signal-card {{ position: relative; min-height: 440px; background: {colors['panel']}; border: 1px solid {colors['border']}; border-radius: 28px; padding: 24px; margin-bottom: 18px; box-shadow: 0 16px 44px rgba(0,0,0,.16); overflow: hidden; }}
    .signal-card:before {{ content:""; position:absolute; top:0; left:0; right:0; height:4px; background: linear-gradient(90deg, #22c55e, #2563eb, #8b5cf6); }}
    .signal-head {{ display:flex; align-items:flex-start; justify-content:space-between; gap:16px; }}
    .ticker-row {{ display:flex; align-items:center; gap:14px; margin-top:12px; }}
    .flag-dot {{ width:52px; height:36px; border-radius:18px; background:rgba(255,255,255,.06); display:flex; align-items:center; justify-content:center; font-size:24px; border: 1px solid {colors['border']}; }}
    .ticker {{ font-size: 30px; line-height:1; font-weight: 900; letter-spacing: .02em; color:{colors['text']}; }}
    .strategy {{ color:{colors['muted']}; font-weight: 700; font-size: 14px; margin-top:6px; }}
    .badges {{ display:flex; flex-wrap:wrap; gap:8px; }}
    .badge {{ display:inline-flex; align-items:center; padding:7px 12px; border-radius:999px; font-size:12px; font-weight:900; letter-spacing:.11em; text-transform:uppercase; border:1px solid {colors['border']}; }}
    .badge.green {{ background: rgba(34,197,94,.16); color:#86efac; border-color:rgba(34,197,94,.44); }}
    .badge.blue {{ background: rgba(37,99,235,.18); color:#93c5fd; border-color:rgba(37,99,235,.46); }}
    .badge.yellow {{ background: rgba(245,158,11,.15); color:#fcd34d; border-color:rgba(245,158,11,.42); }}
    .badge.red {{ background: rgba(239,68,68,.15); color:#fecaca; border-color:rgba(239,68,68,.42); }}
    .badge.gray {{ background: rgba(148,163,184,.12); color:#cbd5e1; }}
    .score-box {{ min-width:92px; padding:13px 14px; border-radius:18px; background:{colors['panel2']}; border:1px solid {colors['border']}; text-align:center; }}
    .score-box .label {{ color:{colors['muted']}; font-size:10px; letter-spacing:.18em; font-weight:900; }}
    .score-box .value {{ color:{colors['text']}; font-size:24px; font-weight:900; margin-top:5px; }}
    .screening {{ margin-top:18px; display:flex; align-items:center; flex-wrap:wrap; gap:10px; color:{colors['muted']}; font-size:15px; }}
    .pill {{ padding:7px 12px; border-radius:999px; background:{colors['panel2']}; border:1px solid {colors['border']}; font-weight:800; color:{colors['text']}; }}
    .main-price {{ margin-top:18px; font-size:38px; color:{colors['text']}; font-weight:900; letter-spacing:-.03em; }}
    .metric-grid {{ display:grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap:10px; margin-top:16px; }}
    .mini {{ background:{colors['panel2']}; border:1px solid {colors['border']}; border-radius:16px; padding:11px 12px; min-height:74px; }}
    .mini .k {{ color:{colors['muted']}; font-size:10px; font-weight:900; letter-spacing:.16em; text-transform:uppercase; }}
    .mini .v {{ color:{colors['text']}; font-weight:900; font-size:18px; margin-top:6px; }}
    .today-box {{ margin-top:12px; background:{colors['panel2']}; border:1px solid {colors['border']}; border-radius:18px; padding:14px 16px; display:flex; justify-content:space-between; align-items:center; gap:10px; }}
    .today-box .label {{ color:{colors['muted']}; text-transform:uppercase; letter-spacing:.18em; font-size:11px; font-weight:900; }}
    .today-box .price {{ font-size:22px; font-weight:900; color:{colors['text']}; }}
    .gain {{ color:#86efac; background:rgba(34,197,94,.16); border:1px solid rgba(34,197,94,.36); padding:6px 10px; border-radius:999px; font-weight:900; }}
    .thesis {{ color:{colors['muted']}; margin-top:16px; font-size:15px; line-height:1.55; min-height:74px; }}
    .detail-btn {{ display:block; margin-top:18px; text-align:center; background:#2563eb; color:white !important; text-decoration:none !important; padding:13px 16px; border-radius:18px; font-weight:900; box-shadow: 0 12px 24px rgba(37,99,235,.25); }}
    .detail-btn:hover {{ background:#1d4ed8; }}
    .section-card {{ background:{colors['panel']}; border:1px solid {colors['border']}; border-radius:22px; padding:22px; margin-bottom:16px; }}
    .logic h4 {{ margin:0 0 8px 0; }}
    .logic ul {{ margin: 8px 0 0 18px; color:{colors['muted']}; line-height:1.65; }}
    .logic li {{ margin-bottom: 6px; }}
    .navbar-note {{ color:{colors['muted']}; font-size:14px; margin-bottom: 6px; }}
    div[data-testid="stDataFrame"] {{ border-radius: 18px; overflow:hidden; }}
    </style>
    """, unsafe_allow_html=True)


def badge(text: Any, color: str = "gray") -> str:
    if is_missing(text):
        return ""
    return f'<span class="badge {color}">{esc(text)}</span>'


def status_badge(row: pd.Series) -> str:
    quality = str(first_val(row, ["plan_quality"], "")).upper()
    source = str(first_val(row, ["signal_source", "source_file"], ""))
    if quality == "ACTIONABLE" or "execution" in source.lower():
        return badge("Actionable", "green")
    if "NO_TRADE" in quality:
        return badge("No-trade", "yellow")
    if "watch" in source.lower():
        return badge("Watchlist", "blue")
    return badge("Signal", "blue")


def risk_color(x: Any) -> str:
    s = str(x).lower()
    if "high" in s or "dominant" in s or "anomaly" in s:
        return "red"
    if "medium" in s or "watch" in s or "below" in s:
        return "yellow"
    if "ok" in s or "controlled" in s or "core" in s:
        return "green"
    return "gray"


def text_excerpt(x: Any, max_len: int = 170) -> str:
    if is_missing(x):
        return "No thesis text available. Open detail for raw signal fields."
    s = re.sub(r"\s+", " ", str(x)).strip()
    return s if len(s) <= max_len else s[: max_len - 3].rstrip() + "..."


def split_logic(text: Any) -> List[str]:
    if is_missing(text):
        return []
    s = re.sub(r"\s+", " ", str(text)).strip()
    if not s:
        return []
    # Split on sentence boundary but keep decimal numbers safe enough.
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", s)
    cleaned = [p.strip() for p in parts if p.strip()]
    if len(cleaned) == 1 and ";" in cleaned[0]:
        cleaned = [p.strip() for p in cleaned[0].split(";") if p.strip()]
    return cleaned[:8]


def logic_block(title: str, text: Any, icon: str = "•") -> None:
    bullets = split_logic(text)
    if not bullets:
        return
    items = "".join([f"<li>{esc(b)}</li>" for b in bullets])
    st.markdown(f"""
    <div class="section-card logic">
      <h4>{esc(icon)} {esc(title)}</h4>
      <ul>{items}</ul>
    </div>
    """, unsafe_allow_html=True)


def signal_card(row: pd.Series, signal: str, profile: str) -> str:
    ticker = first_val(row, ["ticker"], "-")
    strategy = first_val(row, ["strategy", "strategy_num", "strategy_nar"], "-")
    score = first_val(row, ["score", "score_num", "score_nar"], None)
    risk_flags = first_val(row, ["risk_flags", "risk_flags_num", "risk_flags_nar"], "OK")
    risk_profile = first_val(row, ["risk_profile", "risk_grade"], "-")
    plan_quality = first_val(row, ["plan_quality", "confidence"], "-")
    signal_date = first_val(row, ["signal_date"], "-")
    latest_close = first_val(row, ["latest_close", "close"], None)
    entry_trigger = first_val(row, ["entry_trigger", "trigger"], None)
    stop = first_val(row, ["stop_loss", "stop"], None)
    tp1 = first_val(row, ["target_1", "tp1"], None)
    risk_pct = first_val(row, ["risk_pct"], None)
    rr = first_val(row, ["recommended_rr", "rr_1", "rr"], None)
    hold = first_val(row, ["hold_days", "suggested_hold_days"], None)
    broker = first_val(row, ["rank1_buyer", "broker"], None)
    today = first_val(row, ["last_price", "today_price", "latest_quote", "latest_close"], latest_close)
    thesis = first_val(row, ["why_entry", "trade_thesis", "entry_plan"], None)
    url = route_url(signal, profile, page="detail", ticker=str(ticker))
    risk_badge = badge(risk_profile, risk_color(risk_profile))
    flags_badge = badge(risk_flags, risk_color(risk_flags))
    quality_badge = badge(plan_quality, "green" if str(plan_quality).upper() == "ACTIONABLE" else "yellow" if "NO" in str(plan_quality).upper() else "blue")

    return f"""
    <div class="signal-card">
      <div class="signal-head">
        <div class="badges">
          {status_badge(row)}{quality_badge}{risk_badge}{flags_badge}
        </div>
        <div class="score-box"><div class="label">Score</div><div class="value">{fmt_num(score,3)}</div></div>
      </div>
      <div class="ticker-row"><div class="flag-dot">🇮🇩</div><div><div class="ticker">{esc(ticker)}</div><div class="strategy">{esc(strategy)}</div></div></div>
      <div class="screening"><b>SCREENING:</b> <span>{esc(signal_date)}</span> <span class="pill">{esc(profile)}</span></div>
      <a class="detail-btn" href="{esc(url)}">Lihat Detail ↗</a>
      <div class="main-price">Rp{fmt_num(latest_close,0)}</div>
      <div class="today-box"><div><div class="label">Execution plan</div><div>Trigger <b>{fmt_num(entry_trigger,0)}</b> · Stop <b>{fmt_num(stop,0)}</b> · TP1 <b>{fmt_num(tp1,0)}</b></div></div><div class="gain">RR {fmt_rr(rr)}</div></div>
      <div class="metric-grid">
        <div class="mini"><div class="k">Risk</div><div class="v">{fmt_pct(risk_pct,1)}</div></div>
        <div class="mini"><div class="k">Hold</div><div class="v">{fmt_num(hold,0)}</div></div>
        <div class="mini"><div class="k">Broker</div><div class="v">{esc(broker) if not is_missing(broker) else '—'}</div></div>
        <div class="mini"><div class="k">Today</div><div class="v">Rp{fmt_num(today,0)}</div></div>
      </div>
      <div class="thesis">{esc(text_excerpt(thesis, 220))}</div>
    </div>
    """


def render_card_grid(df: pd.DataFrame, signal: str, profile: str, max_cards: int = 40) -> None:
    if df.empty:
        st.info("No signal cards available for this filter.")
        return
    rows = df.head(max_cards).to_dict("records")
    for i in range(0, len(rows), 2):
        cols = st.columns(2, gap="large")
        for j, c in enumerate(cols):
            if i + j < len(rows):
                with c:
                    st.markdown(signal_card(pd.Series(rows[i + j]), signal, profile), unsafe_allow_html=True)


def filter_cards(df: pd.DataFrame, key_prefix: str = "board") -> pd.DataFrame:
    if df.empty:
        return df
    c1, c2, c3, c4 = st.columns([1.2, 1, 1, 1])
    with c1:
        search = st.text_input("Search ticker", key=f"{key_prefix}_search")
    with c2:
        strategies = ["All"] + sorted([str(x) for x in df.get("strategy", pd.Series(dtype=str)).dropna().unique()])
        strat = st.selectbox("Strategy", strategies, key=f"{key_prefix}_strategy")
    with c3:
        qualities = ["All"] + sorted([str(x) for x in df.get("plan_quality", pd.Series(dtype=str)).dropna().unique()])
        quality = st.selectbox("Quality", qualities, key=f"{key_prefix}_quality")
    with c4:
        risks = ["All"] + sorted([str(x) for x in df.get("risk_profile", pd.Series(dtype=str)).dropna().unique()])
        risk = st.selectbox("Risk", risks, key=f"{key_prefix}_risk")
    out = df.copy()
    if search:
        out = out[out["ticker"].astype(str).str.contains(search, case=False, na=False)]
    if strat != "All" and "strategy" in out.columns:
        out = out[out["strategy"].astype(str) == strat]
    if quality != "All" and "plan_quality" in out.columns:
        out = out[out["plan_quality"].astype(str) == quality]
    if risk != "All" and "risk_profile" in out.columns:
        out = out[out["risk_profile"].astype(str) == risk]
    return out


# -------------------------
# Pages
# -------------------------
def render_hero(signal: str, profile: str, path: Path) -> None:
    st.markdown(f"""
    <div class="top-hero">
      <h1>🎯 Signal Board</h1>
      <p>{esc(signal)} · {esc(profile)} · {esc(path)}</p>
    </div>
    """, unsafe_allow_html=True)


def board_page(bundle: Dict[str, Any], signal: str, profile: str) -> None:
    st.subheader("Signal board")
    st.caption("Compact per-emiten cards. Click **Lihat Detail** to open the numeric + narrative trade report route.")
    df = filter_cards(bundle["cards"], "board")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Cards", len(df))
    m2.metric("Actionable", int((df.get("plan_quality", pd.Series(dtype=str)).astype(str).str.upper() == "ACTIONABLE").sum()) if not df.empty else 0)
    m3.metric("Execution", len(bundle["execution"]))
    m4.metric("Watchlist", len(bundle["watchlist"]))
    render_card_grid(df, signal, profile, max_cards=60)


def detail_page(bundle: Dict[str, Any], signal: str, profile: str, ticker: str) -> None:
    df = bundle["cards"]
    if df.empty or "ticker" not in df.columns:
        st.warning("No card data available.")
        return
    row_df = df[df["ticker"].astype(str).str.upper() == ticker.upper()]
    if row_df.empty:
        st.warning(f"Ticker {ticker} not found in selected signal/profile.")
        st.markdown(f"[← Back to board]({route_url(signal, profile, 'board')})")
        return
    row = row_df.iloc[0]
    st.markdown(f"[← Back to board]({route_url(signal, profile, 'board')})")
    st.markdown(f"""
    <div class="top-hero">
      <h1>🇮🇩 {esc(first_val(row, ['ticker']))} · Trade Detail</h1>
      <p>{esc(first_val(row, ['strategy'], '-'))} · {esc(first_val(row, ['plan_quality'], '-'))} · {esc(first_val(row, ['risk_profile'], '-'))}</p>
    </div>
    """, unsafe_allow_html=True)

    # Numeric ticket
    st.subheader("Numeric execution ticket")
    c = st.columns(8)
    metrics = [
        ("Close", fmt_num(first_val(row, ["latest_close", "close"]),0)),
        ("Zone Low", fmt_num(first_val(row, ["entry_zone_low"]),0)),
        ("Zone High", fmt_num(first_val(row, ["entry_zone_high"]),0)),
        ("Trigger", fmt_num(first_val(row, ["entry_trigger"]),0)),
        ("Stop", fmt_num(first_val(row, ["stop_loss"]),0)),
        ("Risk", fmt_pct(first_val(row, ["risk_pct"]),1)),
        ("TP1", fmt_num(first_val(row, ["target_1"]),0)),
        ("RR", fmt_rr(first_val(row, ["recommended_rr", "rr_1"]))),
    ]
    for col, (label, val) in zip(c, metrics):
        col.metric(label, val)

    c2 = st.columns(6)
    more_metrics = [
        ("TP2", fmt_num(first_val(row, ["target_2"]),0)),
        ("TP3", fmt_num(first_val(row, ["target_3"]),0)),
        ("ATR14", fmt_num(first_val(row, ["atr14"]),2)),
        ("Volume Ratio", fmt_num(first_val(row, ["volume_ratio_20d"]),2)),
        ("Hold", fmt_num(first_val(row, ["hold_days"]),0)),
        ("Rank1 Buyer", first_val(row, ["rank1_buyer"], "—")),
    ]
    for col, (label, val) in zip(c2, more_metrics):
        col.metric(label, val)

    st.divider()
    st.subheader("Decision logic")
    logic_block("Why Entry / Trade Thesis", first_val(row, ["why_entry", "trade_thesis"]), "🎯")
    cols = st.columns(2)
    with cols[0]:
        logic_block("Entry Plan", first_val(row, ["entry_plan"]), "🟢")
        logic_block("Invalidation / Stop Logic", first_val(row, ["why_stop", "invalidation_plan"]), "🔴")
        logic_block("No-Trade Conditions", first_val(row, ["no_trade_reasons", "no_trade_condition"]), "⛔")
    with cols[1]:
        logic_block("Targets / Exit Logic", first_val(row, ["why_targets", "exit_plan"]), "🟡")
        logic_block("Portfolio / Risk Notes", first_val(row, ["risk_note"]), "🛡️")
        logic_block("Broker / Behaviour Context", first_val(row, ["broker_context"]), "🏦")
    logic_block("Liquidity Context", first_val(row, ["liquidity_context"]), "💧")
    logic_block("Price Structure", first_val(row, ["price_context"]), "📈")

    with st.expander("All numeric + narrative fields for this ticker"):
        st.dataframe(pd.DataFrame([row]), width="stretch", hide_index=True)

    if bundle.get("numeric_report"):
        with st.expander("Full numeric trading report"):
            st.markdown(bundle["numeric_report"])
    if bundle.get("narrative_report"):
        with st.expander("Full narrative trading report"):
            st.markdown(bundle["narrative_report"])


def execution_page(bundle: Dict[str, Any], signal: str, profile: str) -> None:
    st.subheader("Execution signals")
    exec_df = bundle["cards"]
    if not bundle["execution"].empty:
        tickers = set(bundle["execution"]["ticker"].astype(str).str.upper())
        exec_df = exec_df[exec_df["ticker"].astype(str).str.upper().isin(tickers)]
    filtered = filter_cards(exec_df, "execution")
    render_card_grid(filtered, signal, profile, max_cards=80)


def playbook_page(bundle: Dict[str, Any], signal: str, profile: str) -> None:
    st.subheader("Playbooks")
    st.caption("Every card opens a full numeric + narrative detail route.")
    filtered = filter_cards(bundle["cards"], "playbook")
    render_card_grid(filtered, signal, profile, max_cards=100)


def watchlist_page(bundle: Dict[str, Any], signal: str, profile: str) -> None:
    st.subheader("Watchlists")
    watch_df = bundle["cards"]
    if not bundle["watchlist"].empty:
        tickers = set(bundle["watchlist"]["ticker"].astype(str).str.upper())
        watch_df = watch_df[watch_df["ticker"].astype(str).str.upper().isin(tickers)]
    filtered = filter_cards(watch_df, "watchlist")
    render_card_grid(filtered, signal, profile, max_cards=100)


def compare_page(root: Path, signal: str) -> None:
    folders = discover_signal_folders(root).get(signal, {})
    if len(folders) < 2:
        st.info("Need at least two model profiles for comparison.")
        return
    cols = st.columns(len(folders))
    for col, (profile, path) in zip(cols, folders.items()):
        with col:
            b = load_bundle(path)
            st.markdown(f"### {profile}")
            st.metric("Cards", len(b["cards"]))
            st.metric("Execution", len(b["execution"]))
            st.metric("Watchlist", len(b["watchlist"]))
            if not b["cards"].empty:
                sample = b["cards"].sort_values("score", ascending=False, na_position="last").head(5) if "score" in b["cards"].columns else b["cards"].head(5)
                st.dataframe(sample[[c for c in ["ticker", "strategy", "plan_quality", "risk_profile", "score", "latest_close", "entry_trigger", "stop_loss", "target_1", "recommended_rr"] if c in sample.columns]], width="stretch", hide_index=True)


def risk_page(bundle: Dict[str, Any], signal: str, profile: str) -> None:
    st.subheader("Risk review")
    df = bundle["cards"]
    if df.empty:
        st.info("No data.")
        return
    c1, c2 = st.columns(2)
    with c1:
        if "risk_flags" in df.columns:
            vc = df["risk_flags"].fillna("OK").astype(str).value_counts().rename_axis("risk_flags").reset_index(name="count")
            st.markdown("#### Risk flags")
            st.dataframe(vc, width="stretch", hide_index=True)
    with c2:
        if "rank1_buyer" in df.columns:
            vc = df["rank1_buyer"].fillna("UNKNOWN").astype(str).value_counts().head(15).rename_axis("rank1_buyer").reset_index(name="count")
            st.markdown("#### Broker concentration")
            st.dataframe(vc, width="stretch", hide_index=True)
    caution = df[df.get("risk_flags", pd.Series(index=df.index, dtype=str)).fillna("OK").astype(str).str.upper() != "OK"] if "risk_flags" in df.columns else pd.DataFrame()
    if not caution.empty:
        st.markdown("#### Caution cards")
        render_card_grid(caution, signal, profile, max_cards=20)


def analytics_page(bundle: Dict[str, Any]) -> None:
    st.subheader("Analytics")
    df = bundle["cards"]
    if df.empty:
        return
    cols = [c for c in ["ticker", "strategy", "plan_quality", "risk_profile", "score", "latest_close", "risk_pct", "recommended_rr", "rank1_buyer", "risk_flags"] if c in df.columns]
    st.dataframe(df[cols], width="stretch", hide_index=True)


def health_page(bundle: Dict[str, Any]) -> None:
    st.subheader("Data health")
    st.write("Signal path:", str(bundle["path"]))
    c = st.columns(5)
    c[0].metric("Numeric plans", len(bundle["numeric"]))
    c[1].metric("Narrative cards", len(bundle["narrative"]))
    c[2].metric("Execution", len(bundle["execution"]))
    c[3].metric("Watchlist", len(bundle["watchlist"]))
    c[4].metric("All scores", len(bundle["scores"]))
    with st.expander("Diagnostics JSON"):
        st.json(bundle.get("diagnostics") or {})
    with st.expander("Profile meta"):
        st.json(bundle.get("profile_meta") or {})


def raw_page(bundle: Dict[str, Any]) -> None:
    st.subheader("Raw data")
    for name in ["numeric", "narrative", "execution", "signals_main", "watchlist", "candidates", "scores"]:
        df = bundle[name]
        with st.expander(f"{name} · {df.shape}"):
            if df.empty:
                st.info("Empty / missing")
            else:
                st.dataframe(df, width="stretch", hide_index=True)


# -------------------------
# Main app
# -------------------------
def main() -> None:
    args = parse_args()
    root = Path(args.root).resolve()
    folders = discover_signal_folders(root)
    theme = st.sidebar.radio("Theme", ["Dark", "Light"], index=0, horizontal=True)
    inject_css(theme)

    st.sidebar.title("Alpha Research")
    st.sidebar.caption("Signal Board")
    st.sidebar.text_input("Root", value=str(root), disabled=True)

    if not folders:
        st.error(f"No signal folders found under {root / 'signals/daily'}")
        return

    signals = sorted(folders.keys())
    q_signal = qget("signal", signals[-1])
    signal = st.sidebar.selectbox("Signal date", signals, index=signals.index(q_signal) if q_signal in signals else len(signals)-1)
    profiles = sorted(folders[signal].keys())
    q_profile = qget("profile", profiles[0])
    profile = st.sidebar.selectbox("Model profile", profiles, index=profiles.index(q_profile) if q_profile in profiles else 0)
    signal_path = folders[signal][profile]
    page_q = qget("page", "board")
    ticker_q = qget("ticker", None)

    st.sidebar.markdown("---")
    st.sidebar.markdown("Direct routes")
    for p in profiles:
        st.sidebar.markdown(f"[{p}]({route_url(signal, p, 'board')})")

    bundle = load_bundle(signal_path)

    if page_q == "detail" and ticker_q:
        detail_page(bundle, signal, profile, ticker_q)
        return

    render_hero(signal, profile, signal_path)
    tabs = st.tabs(["🎯 Board", "✅ Execution", "📘 Playbooks", "🧭 Watchlists", "📌 Brief", "⚖️ Compare", "⚠️ Risk", "📊 Analytics", "🩺 Health", "🗄️ Raw"])
    with tabs[0]:
        board_page(bundle, signal, profile)
    with tabs[1]:
        execution_page(bundle, signal, profile)
    with tabs[2]:
        playbook_page(bundle, signal, profile)
    with tabs[3]:
        watchlist_page(bundle, signal, profile)
    with tabs[4]:
        st.subheader("Brief")
        c = st.columns(4)
        c[0].metric("Cards", len(bundle["cards"]))
        c[1].metric("Execution", len(bundle["execution"]))
        c[2].metric("Watchlist", len(bundle["watchlist"]))
        c[3].metric("Numeric plans", len(bundle["numeric"]))
        if bundle.get("numeric_report"):
            with st.expander("Numeric report summary"):
                st.markdown(bundle["numeric_report"][:8000])
        if bundle.get("narrative_report"):
            with st.expander("Narrative report summary"):
                st.markdown(bundle["narrative_report"][:8000])
    with tabs[5]:
        compare_page(root, signal)
    with tabs[6]:
        risk_page(bundle, signal, profile)
    with tabs[7]:
        analytics_page(bundle)
    with tabs[8]:
        health_page(bundle)
    with tabs[9]:
        raw_page(bundle)


if __name__ == "__main__":
    main()
