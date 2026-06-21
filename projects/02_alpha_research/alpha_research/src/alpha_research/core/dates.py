from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
import re
import pandas as pd

# Canonical month map for English + Indonesian month names/abbreviations.
# This module is intentionally permissive because source files come from IDX,
# broker exports, KSEI-style text dates, and manually downloaded spreadsheets.
_MONTHS = {
    # English
    "jan": 1, "january": 1,
    "feb": 2, "february": 2,
    "mar": 3, "march": 3,
    "apr": 4, "april": 4,
    "may": 5,
    "jun": 6, "june": 6,
    "jul": 7, "july": 7,
    "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10,
    "nov": 11, "november": 11,
    "dec": 12, "december": 12,

    # Indonesian official/common variants
    "januari": 1,
    "februari": 2, "pebruari": 2, "feb": 2, "peb": 2,
    "maret": 3,
    "mei": 5,
    "juni": 6,
    "juli": 7,
    "agu": 8, "agt": 8, "agst": 8, "agustus": 8,
    "okt": 10, "oktober": 10,
    "nop": 11, "nopember": 11,  # older Indonesian spelling sometimes appears in legacy data
    "des": 12, "desember": 12,
}

_NULL_STRINGS = {"", "nan", "nat", "none", "null", "-", "--"}


def _clean_month_token(token: str) -> str:
    return re.sub(r"[^a-z]", "", str(token).strip().lower())


def month_number(token: str) -> int | None:
    """Return month number for English/Indonesian month tokens.

    Never raises KeyError. Unknown tokens return None so callers can fall back
    to pandas parsing or mark the date as unparsed.
    """
    t = _clean_month_token(token)
    if not t:
        return None
    if t in _MONTHS:
        return _MONTHS[t]
    # Safe prefix fallback for long names, without assuming all prefixes exist.
    if len(t) >= 3 and t[:3] in _MONTHS:
        return _MONTHS[t[:3]]
    return None


def _coerce_year(y: str | int) -> int:
    yy = int(y)
    if yy < 70:
        return yy + 2000
    if yy < 100:
        return yy + 1900
    return yy


def parse_date_any(x) -> date | None:
    """Parse common project date formats into ``datetime.date``.

    Supported examples:
    - 2026-03-09
    - 20260309
    - 2026-03-09T00:00:00
    - 12 Oct 17
    - 01 Agt 2026
    - 04_may_2026
    - 04_mei_2026

    This function should never raise ``KeyError`` for unknown month tokens. If
    parsing fails it returns None, allowing the canonical layer to drop/report
    invalid rows explicitly instead of crashing in the middle of a build.
    """
    if x is None:
        return None
    if isinstance(x, date) and not isinstance(x, datetime):
        return x
    if isinstance(x, datetime):
        return x.date()

    s = str(x).strip()
    if s.lower() in _NULL_STRINGS:
        return None

    s2 = s.replace("/", "-").replace("_", " ").replace(".", " ")

    # ISO-like dates first. Never day-first for ISO.
    m = re.search(r"\b(20\d{2}|19\d{2})-(\d{1,2})-(\d{1,2})\b", s2)
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None

    # Compact YYYYMMDD.
    m = re.fullmatch(r"(20\d{2}|19\d{2})(\d{2})(\d{2})", s)
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None

    # dd month yyyy / dd month yy, English or Indonesian.
    m = re.search(r"\b(\d{1,2})\s+([A-Za-z]+)\s+(20\d{2}|19\d{2}|\d{2})\b", s2)
    if m:
        mm = month_number(m.group(2))
        if mm is not None:
            try:
                return date(_coerce_year(m.group(3)), mm, int(m.group(1)))
            except ValueError:
                return None

    # Last-resort mixed parser for odd spreadsheet values. Keep dayfirst=True
    # here because non-ISO local source dates are usually day-month-year.
    dt = pd.to_datetime(s, errors="coerce", format="mixed", dayfirst=True)
    if pd.isna(dt):
        return None
    return dt.date()


def date_str(x) -> str:
    d = parse_date_any(x)
    if d is None:
        raise ValueError(f"Cannot parse date: {x}")
    return d.isoformat()


def ensure_start_end(start, end):
    s = parse_date_any(start)
    e = parse_date_any(end)
    if s is None or e is None:
        raise ValueError(f"Invalid date range: {start} -> {end}")
    if s > e:
        raise ValueError(f"start_date > end_date after parsing: {s} > {e}")
    return s, e


def extract_date_from_name(path: str | Path) -> date | None:
    name = Path(path).name
    patterns = [
        r"(20\d{6})",
        r"(20\d{2}-\d{2}-\d{2})",
        r"(\d{1,2}_[A-Za-z]+_20\d{2})",
        r"(\d{1,2}\s+[A-Za-z]+\s+20\d{2})",
    ]
    for pat in patterns:
        m = re.search(pat, name)
        if m:
            d = parse_date_any(m.group(1))
            if d is not None:
                return d
    return parse_date_any(name)
