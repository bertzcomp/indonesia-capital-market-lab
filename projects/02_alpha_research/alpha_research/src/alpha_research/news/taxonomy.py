from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Iterable, Tuple


def _norm(s: object) -> str:
    return re.sub(r"\s+", " ", str(s or "").strip())


def _has(pattern: str, text: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE) is not None


@dataclass(frozen=True)
class EventDecision:
    event_scope: str
    event_type: str
    event_side: str
    impact_channel: str
    materiality_label: str
    materiality_score: float
    news_intensity_score: float
    uncertainty_score: float
    bullish_keyword_hits: int
    bearish_keyword_hits: int
    uncertainty_keyword_hits: int


BULLISH_WORDS = [
    r"\bnaik\b", r"\bmenguat\b", r"\brebound\b", r"\btumbuh\b", r"\bmelonjak\b",
    r"\bpositif\b", r"\bekspansi\b", r"\bakumulasi\b", r"\bborong\b", r"\bbeli\b",
    r"\blaba\b", r"\bdividen\b", r"\bbuyback\b", r"\bkontrak\b", r"\btarget\b",
]
BEARISH_WORDS = [
    r"\bturun\b", r"\bmelemah\b", r"\bkoreksi\b", r"\banjlok\b", r"\brugi\b",
    r"\bkerugian\b", r"\bdijual\b", r"\bdilepas\b", r"\bdistribusi\b", r"\bgagal\b",
    r"\bpailit\b", r"\bbangkrut\b", r"\bdelisting\b", r"\bsuspensi\b",
]
UNCERTAINTY_WORDS = [
    r"\brisiko\b", r"\bketidakpastian\b", r"\bvolatil\b", r"\bgejolak\b", r"\btekanan\b",
    r"\bpotensi\b", r"\bancaman\b", r"\bkonflik\b", r"\bkrisis\b", r"\bmenanti\b",
]


_PATTERNS: list[tuple[str, str, str, str, str, str, float]] = [
    # very specific / high priority corporate distress
    (r"\b(delisting|pailit|bangkrut|PKPU|insolven|dicoret dari bursa)\b", "ticker", "delisting_bankruptcy", "bearish_risk", "tradability_distress", "high", 0.95),
    (r"\b(suspensi|disuspensi|suspend|penghentian sementara|dihentikan sementara|\bUMA\b|unusual market activity)\b", "ticker", "suspension_uma", "bearish_risk", "tradability_distress", "high", 0.90),
    # corporate action
    (r"\b(rights issue|HMETD|private placement|waran|dilusi|konversi utang|obligasi konversi)\b", "ticker", "dilution_corporate_action", "mixed_to_bearish", "capital_structure", "high", 0.85),
    (r"\b(stock split|pemecahan saham|reverse stock)\b", "ticker", "stock_split", "mixed", "corporate_action", "medium", 0.65),
    (r"\b(dividen|cum dividen|ex dividen|pembagian dividen|tebar dividen)\b", "ticker", "dividend", "mixed_to_bullish", "cash_distribution", "medium", 0.70),
    (r"\b(buyback|pembelian kembali saham)\b", "ticker", "buyback", "bullish_support", "capital_action", "medium", 0.72),
    (r"\b(IPO|listing perdana|melantai di bursa|pencatatan saham perdana)\b", "ticker", "ipo_listing", "mixed", "listing_event", "medium", 0.62),
    (r"\b(obligasi|sukuk|senior notes|medium term notes|MTN|utang|pinjaman|fasilitas kredit)\b", "ticker", "debt_financing", "mixed", "financing", "medium", 0.62),
    (r"\b(PEFINDO|peringkat|rating|idA|idAA|idAAA|outlook)\b", "ticker", "credit_rating", "mixed", "credit_quality", "medium", 0.64),
    # fundamentals / analyst
    (r"\b(laba bersih|pendapatan|penjualan|kinerja|rugi bersih|kerugian|margin|EBITDA|laporan keuangan|kuartal|semester|tahun buku)\b", "ticker", "earnings_fundamental", "mixed", "fundamental", "medium", 0.68),
    (r"\b(rekomendasi|target harga|rating beli|buy call|hold|sell|analis|sekuritas)\b", "ticker", "analyst_view", "mixed", "analyst_expectation", "medium", 0.55),
    (r"\b(akuisisi|merger|joint venture|kerja sama|kemitraan|kontrak baru|proyek|ekspansi|pabrik baru|kapasitas produksi)\b", "ticker", "business_development", "mixed_to_bullish", "business_growth", "medium", 0.66),
    # flow
    (r"\b(akumulasi|memborong|diborong|net buy|beli bersih|insider beli|direktur membeli|pengendali membeli)\b", "ticker", "accumulation_flow", "bullish_flow", "positioning_flow", "medium", 0.70),
    (r"\b(distribusi|dilepas|net sell|jual bersih|asing jual|foreign sell|investor asing melepas)\b", "ticker", "distribution_flow", "bearish_flow", "positioning_flow", "medium", 0.70),
]

# macro patterns are evaluated after market commentary filter and are title/lead centric.
MACRO_CURRENCY = r"\b(rupiah|kurs|nilai tukar|USD/IDR|dolar AS|dollar index|DXY|rupiah ditutup|rupiah melemah|rupiah menguat)\b"
MACRO_RATE = r"\b(BI rate|suku bunga|The Fed|FOMC|yield|imbal hasil|inflasi|deflasi|hawkish|dovish)\b"
COMMODITY_TERM = r"\b(minyak|brent|WTI|batubara|batu bara|coal|nikel|timah|emas|CPO|sawit|tembaga|gas alam|komoditas)\b"
COMMODITY_ACTION = r"\b(harga|naik|turun|menguat|melemah|anjlok|rebound|rally|koreksi|lonjakan|tertekan)\b"
GEOPOLITICAL = r"\b(perang|konflik|geopolitik|Iran|Israel|Rusia|Ukraina|Timur Tengah|Selat Hormuz|sanksi|eskalasi)\b"
INDEX_REBAL = r"\b(MSCI|FTSE|rebalancing|index review|konstituen indeks|masuk indeks|keluar indeks|free float)\b"
MARKET_COMMENTARY = r"\b(IHSG|indeks harga saham gabungan|LQ45|IDX30|JII|bursa|pasar modal|top gainers|top losers|awal perdagangan|akhir perdagangan|sesi I|sesi II|ditutup|dibuka|jeda siang|zona hijau|zona merah)\b"


def classify_event(title: object, summary: object = "", full_content: object = "", news_category: object = "") -> EventDecision:
    title_s = _norm(title)
    summary_s = _norm(summary)
    body_s = _norm(full_content)
    category_s = str(news_category or "").lower()

    lead = f"{title_s} {summary_s}".strip()
    full = f"{lead} {body_s}".strip()
    lead_l = lead.lower()
    full_l = full.lower()

    bullish = sum(1 for p in BULLISH_WORDS if _has(p, full_l))
    bearish = sum(1 for p in BEARISH_WORDS if _has(p, full_l))
    uncert = sum(1 for p in UNCERTAINTY_WORDS if _has(p, full_l))

    # Market commentary must win before broad macro/commodity if title/lead is clearly recap/top movers.
    if _has(MARKET_COMMENTARY, lead):
        # But allow truly important macro if title itself is explicitly about FX/rates/geopolitics/index event.
        if _has(MACRO_CURRENCY, lead) and not _has(r"\b(USD\d|USD\s?\d|juta|miliar|triliun|laba|rugi|pendapatan|obligasi|notes|utang|pinjaman)\b", lead,):
            return _decision("market", "macro_currency", "sector_dependent", "currency_fx", "high", 0.82, bullish, bearish, uncert)
        if _has(INDEX_REBAL, lead) and _has(r"\b(rebalancing|MSCI|FTSE|index review|konstituen)\b", lead):
            return _decision("market", "index_rebalancing", "flow_pressure", "index_flow", "high", 0.86, bullish, bearish, uncert)
        return _decision("market", "market_commentary", "mixed", "market_breadth", "low", 0.35, bullish, bearish, uncert)

    # Macro title/lead centric.
    if _has(MACRO_CURRENCY, lead) and not _has(r"\b(USD\d|USD\s?\d|juta|miliar|triliun|laba|rugi|pendapatan|obligasi|notes|utang|pinjaman|investasi|nilai transaksi|berhadiah)\b", lead):
        return _decision("market", "macro_currency", "sector_dependent", "currency_fx", "high", 0.82, bullish, bearish, uncert)
    if _has(MACRO_RATE, lead):
        return _decision("market", "macro_rate", "sector_dependent", "rates_policy", "high", 0.80, bullish, bearish, uncert)
    if _has(GEOPOLITICAL, lead):
        return _decision("market", "geopolitical_risk", "risk_off", "external_shock", "high", 0.86, bullish, bearish, uncert)
    if _has(INDEX_REBAL, lead) and _has(r"\b(rebalancing|MSCI|FTSE|index review|konstituen|masuk indeks|keluar indeks)\b", lead):
        return _decision("market", "index_rebalancing", "flow_pressure", "index_flow", "high", 0.86, bullish, bearish, uncert)
    if _has(COMMODITY_TERM, lead) and _has(COMMODITY_ACTION, lead):
        return _decision("sector", "commodity_shock", "sector_dependent", "commodity_input_output", "medium", 0.74, bullish, bearish, uncert)

    # Ticker/corporate patterns. Use lead first, then full body only for high-specific corporate events.
    for pattern, scope, etype, side, channel, mat_label, intensity in _PATTERNS:
        search_text = full if etype in {"delisting_bankruptcy", "suspension_uma", "dilution_corporate_action"} else lead
        if _has(pattern, search_text):
            return _decision(scope, etype, side, channel, mat_label, intensity, bullish, bearish, uncert)

    if category_s == "macro":
        return _decision("market", "general_macro", "mixed", "macro_context", "low", 0.30, bullish, bearish, uncert)
    return _decision("ticker", "general_news", "mixed", "general_information", "low", 0.25, bullish, bearish, uncert)


def _decision(scope: str, etype: str, side: str, channel: str, mat_label: str, intensity: float, bullish: int, bearish: int, uncert: int) -> EventDecision:
    mat_score = {"low": 0.30, "medium": 0.60, "high": 0.90}.get(mat_label, 0.40)
    uncertainty_score = min(1.0, 0.15 + 0.12 * uncert + (0.12 if etype in {"geopolitical_risk", "macro_currency", "macro_rate", "suspension_uma", "delisting_bankruptcy"} else 0.0))
    return EventDecision(
        event_scope=scope,
        event_type=etype,
        event_side=side,
        impact_channel=channel,
        materiality_label=mat_label,
        materiality_score=float(mat_score),
        news_intensity_score=float(intensity),
        uncertainty_score=float(uncertainty_score),
        bullish_keyword_hits=int(bullish),
        bearish_keyword_hits=int(bearish),
        uncertainty_keyword_hits=int(uncert),
    )
