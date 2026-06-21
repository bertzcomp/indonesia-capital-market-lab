from __future__ import annotations

import re
from typing import Any

import polars as pl


def normalize_ticker_expr(col: str = "ticker") -> pl.Expr:
    s = pl.col(col).cast(pl.Utf8, strict=False).str.strip_chars().str.to_uppercase()
    return pl.when(
        s.is_not_null()
        & (s != "")
        & (~s.str.contains(r"^\.+$"))
        & s.str.contains(r"^[A-Z0-9]{1,12}$")
    ).then(s).otherwise(None)


def slugify_expr(col: str) -> pl.Expr:
    s = pl.col(col).cast(pl.Utf8, strict=False).fill_null("")
    return (
        s.str.replace_all(r"&nbsp", " ")
        .str.replace_all(r"<[^>]+>", " ")
        .str.replace_all(r"\.\.\.", "")
        .str.to_lowercase()
        .str.strip_chars()
        .str.replace_all(r"[^a-z0-9]+", "_")
        .str.replace_all(r"_+", "_")
        .str.strip_chars("_")
    )


def parse_number_expr(col: str) -> pl.Expr:
    s0 = pl.col(col).cast(pl.Utf8, strict=False).str.strip_chars()
    empty = s0.is_null() | s0.is_in(["", "-", "--", "nan", "NaN", "None", "null", "NULL"])
    neg = s0.str.starts_with("(") & s0.str.ends_with(")")
    s = (
        s0.str.replace_all(r"^\((.*)\)$", r"${1}")
        .str.replace_all(r"IDR|USD|Rp|\$", "")
        .str.strip_chars()
    )
    pct = s.str.ends_with("%")
    s_no_pct = s.str.replace_all(r"%$", "").str.strip_chars()
    unit = s_no_pct.str.extract(r"(?i)\b([KMBT])\b$", 1).str.to_uppercase()
    mult = (
        pl.when(unit == "K").then(1_000.0)
        .when(unit == "M").then(1_000_000.0)
        .when(unit == "B").then(1_000_000_000.0)
        .when(unit == "T").then(1_000_000_000_000.0)
        .otherwise(1.0)
    )
    s_num = s_no_pct.str.replace_all(r"(?i)\b[KMBT]\b$", "").str.replace_all(r"\s+", "")
    # For suffixed values such as "3,206 B", comma is decimal separator.
    s_decimal = pl.when(unit.is_not_null() & s_num.str.contains(",") & (~s_num.str.contains(r"\."))).then(
        s_num.str.replace_all(",", ".")
    ).otherwise(s_num.str.replace_all(",", ""))
    val = s_decimal.cast(pl.Float64, strict=False) * mult
    val = pl.when(pct).then(val / 100.0).otherwise(val)
    val = pl.when(neg).then(-val).otherwise(val)
    return pl.when(empty).then(None).otherwise(val)


def parse_percent_points_expr(col: str) -> pl.Expr:
    # Converts strings like "1.55%" to 1.55 and keeps source values like 1.55 as 1.55.
    raw = pl.col(col).cast(pl.Utf8, strict=False).str.strip_chars()
    parsed = parse_number_expr(col)
    return pl.when(raw.str.ends_with("%") & parsed.is_not_null()).then(parsed * 100.0).otherwise(parsed)


def _month_name_to_int_expr(mon: pl.Expr) -> pl.Expr:
    m = mon.str.to_lowercase().str.slice(0, 3)
    return (
        pl.when(m == "jan").then(1)
        .when(m == "feb").then(2)
        .when(m == "mar").then(3)
        .when(m == "apr").then(4)
        .when(m == "may").then(5)
        .when(m == "jun").then(6)
        .when(m == "jul").then(7)
        .when(m == "aug").then(8)
        .when(m == "sep").then(9)
        .when(m == "oct").then(10)
        .when(m == "nov").then(11)
        .when(m == "dec").then(12)
        .otherwise(None)
    )


def parse_date_expr(col: str, dayfirst: bool = True) -> pl.Expr:
    s = pl.col(col).cast(pl.Utf8, strict=False).str.strip_chars()

    # Manual parser for English month names such as "05 Jun 26" and "31 Dec 2025".
    # This avoids chrono parser edge-case panics observed on some Polars builds.
    day_m = s.str.extract(r"^(\d{1,2})\s+([A-Za-z]{3,9})\s+(\d{2}|\d{4})$", 1).cast(pl.Int32, strict=False)
    mon_m = _month_name_to_int_expr(s.str.extract(r"^(\d{1,2})\s+([A-Za-z]{3,9})\s+(\d{2}|\d{4})$", 2))
    yy_raw = s.str.extract(r"^(\d{1,2})\s+([A-Za-z]{3,9})\s+(\d{2}|\d{4})$", 3).cast(pl.Int32, strict=False)
    year_m = pl.when(yy_raw < 100).then(pl.when(yy_raw < 80).then(2000 + yy_raw).otherwise(1900 + yy_raw)).otherwise(yy_raw)
    month_name_date = pl.date(year_m, mon_m, day_m)

    exprs = [
        s.str.strptime(pl.Datetime, format="%Y-%m-%dT%H:%M:%S", strict=False).dt.date(),
        s.str.strptime(pl.Date, format="%Y-%m-%d", strict=False),
        month_name_date,
    ]
    if dayfirst:
        exprs.extend([
            s.str.strptime(pl.Date, format="%d/%m/%Y", strict=False),
            s.str.strptime(pl.Date, format="%d-%m-%Y", strict=False),
        ])
    else:
        exprs.extend([
            s.str.strptime(pl.Date, format="%m/%d/%Y", strict=False),
            s.str.strptime(pl.Date, format="%m-%d-%Y", strict=False),
        ])
    return pl.coalesce(exprs)

def _last_day_expr(year: pl.Expr, month: pl.Expr) -> pl.Expr:
    leap = ((year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)))
    return (
        pl.when(month.is_in([1, 3, 5, 7, 8, 10, 12])).then(31)
        .when(month.is_in([4, 6, 9, 11])).then(30)
        .when((month == 2) & leap).then(29)
        .when(month == 2).then(28)
        .otherwise(None)
    )


def parse_period_end_expr(label_col: str = "period_label", display_col: str = "period_display") -> pl.Expr:
    label = pl.col(label_col).cast(pl.Utf8, strict=False).str.strip_chars().str.to_uppercase()
    q = label.str.extract(r"^Q([1-4])(\d{2})$", 1).cast(pl.Int32, strict=False)
    q_yy = label.str.extract(r"^Q[1-4](\d{2})$", 1).cast(pl.Int32, strict=False)
    q_year = pl.when(q_yy < 80).then(2000 + q_yy).otherwise(1900 + q_yy)
    q_month = q * 3
    q_day = _last_day_expr(q_year, q_month)
    q_date = pl.date(q_year, q_month, q_day)

    m = label.str.extract(r"^(\d{1,2})M(\d{2})$", 1).cast(pl.Int32, strict=False)
    m_yy = label.str.extract(r"^\d{1,2}M(\d{2})$", 1).cast(pl.Int32, strict=False)
    m_year = pl.when(m_yy < 80).then(2000 + m_yy).otherwise(1900 + m_yy)
    m_month = pl.when(m < 1).then(1).when(m > 12).then(12).otherwise(m)
    m_day = _last_day_expr(m_year, m_month)
    m_date = pl.date(m_year, m_month, m_day)

    disp = pl.col(display_col).cast(pl.Utf8, strict=False).str.strip_chars().str.to_uppercase()
    dq = disp.str.extract(r"Q([1-4])\s*(20\d{2}|19\d{2})", 1).cast(pl.Int32, strict=False)
    dq_year = disp.str.extract(r"Q[1-4]\s*(20\d{2}|19\d{2})", 1).cast(pl.Int32, strict=False)
    dq_month = dq * 3
    dq_day = _last_day_expr(dq_year, dq_month)
    dq_date = pl.date(dq_year, dq_month, dq_day)
    return pl.coalesce([q_date, m_date, dq_date])


def available_date_expr(period_col: str, statement_col: str, lag_map: dict[str, int]) -> pl.Expr:
    st = pl.col(statement_col).cast(pl.Utf8, strict=False)
    default_lag = int(lag_map.get("Quarterly", 60))
    expr = pl.col(period_col) + pl.duration(days=default_lag)
    for key, lag in lag_map.items():
        expr = pl.when(st == key).then(pl.col(period_col) + pl.duration(days=int(lag))).otherwise(expr)
    return expr.cast(pl.Date)


def normalize_colname(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return re.sub(r"_+", "_", s).strip("_")
