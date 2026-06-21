from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
import polars as pl
from sklearn.base import clone
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import average_precision_score, mean_absolute_error, roc_auc_score, r2_score
from sklearn.pipeline import Pipeline

from .io import ensure_dir, read_table, write_table

DROP_PREFIXES = ("label_", "fwd_")
DROP_COLS = {
    "ticker", "as_of_date", "company_name", "sector", "subsector", "industry", "subindustry",
    "signal_family", "conviction", "reason_codes", "action", "risk_flags",
}
SCORE_COMPONENTS = [
    "quality_score", "growth_score", "valuation_score", "insider_score", "balance_sheet_score",
    "dividend_score", "liquidity_score", "risk_penalty", "fundamental_score",
]
KEYSTAT_FEATURE_HINTS = [
    "pe_ttm", "pbv", "ps_ttm", "ev_ebitda", "earnings_yield", "roe_ttm", "roa_ttm", "roic_ttm",
    "debt_to_equity", "dividend_yield", "payout_ratio", "altman_z_score", "piotroski_f_score",
    "relative_strength_rating", "current_ratio", "quick_ratio", "interest_coverage",
]


@dataclass
class ModelTargets:
    horizon: int = 60
    rank_target: str | None = None
    classifier_target: str | None = None
    risk_target: str | None = None

    def resolved(self) -> "ModelTargets":
        h = int(self.horizon)
        return ModelTargets(
            horizon=h,
            rank_target=self.rank_target or f"fwd_risk_adjusted_excess_sector_{h}d",
            classifier_target=self.classifier_target or f"label_outperform_sector_{h}d",
            risk_target=self.risk_target or f"label_bad_drawdown_{h}d",
        )


def _feature_columns(df: pl.DataFrame, targets: list[str] | str | None = None, min_coverage: float = 0.01) -> list[str]:
    target_set = set([targets] if isinstance(targets, str) else (targets or []))
    nulls = df.null_count().to_dicts()[0] if df.width else {}
    feats: list[str] = []
    for c, dt in df.schema.items():
        if c in target_set or c in DROP_COLS or any(c.startswith(p) for p in DROP_PREFIXES):
            continue
        if not dt.is_numeric():
            continue
        coverage = 1.0 - (nulls.get(c, 0) / max(df.height, 1))
        if coverage < min_coverage:
            continue
        feats.append(c)
    # Stable ordering: ordinary numeric features first, then explicit high-value meta/keystats if present.
    priority = [c for c in KEYSTAT_FEATURE_HINTS + SCORE_COMPONENTS if c in feats]
    rest = [c for c in feats if c not in set(priority)]
    return rest + priority


def _pipeline(model_type: str, random_state: int = 42) -> Pipeline:
    if model_type == "regressor":
        model = HistGradientBoostingRegressor(
            max_iter=120,
            learning_rate=0.045,
            max_leaf_nodes=31,
            l2_regularization=0.05,
            early_stopping=True,
            random_state=random_state,
        )
    elif model_type == "classifier":
        model = HistGradientBoostingClassifier(
            max_iter=120,
            learning_rate=0.045,
            max_leaf_nodes=31,
            l2_regularization=0.05,
            early_stopping=True,
            random_state=random_state,
        )
    else:
        raise ValueError(f"Unknown model_type={model_type}")
    return Pipeline([("imputer", SimpleImputer(strategy="median")), ("model", model)])


def _time_split(pdf: pd.DataFrame, valid_fraction: float = 0.20) -> tuple[pd.DataFrame, pd.DataFrame]:
    pdf = pdf.sort_values("as_of_date")
    split_idx = max(int(len(pdf) * (1.0 - valid_fraction)), 1)
    return pdf.iloc[:split_idx].copy(), pdf.iloc[split_idx:].copy()


def _rank_corr(y_true: np.ndarray, y_pred: np.ndarray) -> float | None:
    if len(y_true) < 3:
        return None
    a = pd.Series(y_true).rank(method="average").to_numpy()
    b = pd.Series(y_pred).rank(method="average").to_numpy()
    if np.nanstd(a) == 0 or np.nanstd(b) == 0:
        return None
    return float(np.corrcoef(a, b)[0, 1])


def _regression_metrics(y_true: np.ndarray, pred: np.ndarray) -> dict[str, float]:
    out: dict[str, float] = {}
    mask = np.isfinite(y_true) & np.isfinite(pred)
    if mask.sum() < 3:
        return out
    yt = y_true[mask]
    yp = pred[mask]
    out["mae"] = float(mean_absolute_error(yt, yp))
    try:
        out["r2"] = float(r2_score(yt, yp))
    except Exception:
        pass
    rc = _rank_corr(yt, yp)
    if rc is not None:
        out["rank_corr"] = rc
    return out


def _classification_metrics(y_true: np.ndarray, prob: np.ndarray) -> dict[str, float]:
    out: dict[str, float] = {}
    mask = np.isfinite(y_true) & np.isfinite(prob)
    if mask.sum() < 3:
        return out
    yt = y_true[mask].astype(int)
    pp = prob[mask]
    out["positive_rate"] = float(np.mean(yt))
    if len(set(yt.tolist())) > 1:
        out["roc_auc"] = float(roc_auc_score(yt, pp))
        out["avg_precision"] = float(average_precision_score(yt, pp))
    return out


def _train_one(pdf: pd.DataFrame, feats: list[str], target: str, model_type: str) -> tuple[Pipeline | None, dict[str, Any]]:
    d = pdf[pdf[target].notna()].copy()
    metrics: dict[str, Any] = {"target": target, "model_type": model_type, "rows": int(len(d))}
    if len(d) < 100:
        metrics["skipped"] = "not_enough_rows"
        return None, metrics
    train, valid = _time_split(d)
    if len(valid) < 20:
        metrics["skipped"] = "not_enough_validation_rows"
        return None, metrics
    pipe = _pipeline(model_type)
    X_train, X_valid = train[feats], valid[feats]
    y_train, y_valid = train[target], valid[target]
    if model_type == "classifier":
        y_train = y_train.astype(int)
        y_valid = y_valid.astype(int)
        if y_train.nunique() < 2:
            metrics["skipped"] = f"single_train_class:{dict(y_train.value_counts())}"
            return None, metrics
        pipe.fit(X_train, y_train)
        prob = pipe.predict_proba(X_valid)[:, 1]
        metrics.update({"train_rows": int(len(train)), "valid_rows": int(len(valid))})
        metrics.update({f"valid_{k}": v for k, v in _classification_metrics(y_valid.to_numpy(), prob).items()})
    else:
        pipe.fit(X_train, y_train.astype(float))
        pred = pipe.predict(X_valid)
        metrics.update({"train_rows": int(len(train)), "valid_rows": int(len(valid))})
        metrics.update({f"valid_{k}": v for k, v in _regression_metrics(y_valid.to_numpy(dtype=float), pred).items()})
    # Refit final on all labelled rows after holdout diagnostics.
    final_pipe = _pipeline(model_type)
    if model_type == "classifier":
        final_pipe.fit(d[feats], d[target].astype(int))
    else:
        final_pipe.fit(d[feats], d[target].astype(float))
    return final_pipe, metrics


def _walkforward_report(pdf: pd.DataFrame, feats: list[str], target: str, model_type: str, purge_days: int = 60, min_train_rows: int = 5000) -> list[dict[str, Any]]:
    d = pdf[pdf[target].notna()].copy()
    if d.empty:
        return []
    d["as_of_date"] = pd.to_datetime(d["as_of_date"])
    years = sorted(d["as_of_date"].dt.year.dropna().unique().tolist())
    reports: list[dict[str, Any]] = []
    for y in years[1:]:
        valid_start = pd.Timestamp(year=int(y), month=1, day=1)
        valid_end = pd.Timestamp(year=int(y) + 1, month=1, day=1)
        train_cutoff = valid_start - pd.Timedelta(days=int(purge_days))
        tr = d[d["as_of_date"] < train_cutoff]
        va = d[(d["as_of_date"] >= valid_start) & (d["as_of_date"] < valid_end)]
        if len(tr) < min_train_rows or len(va) < 100:
            continue
        pipe = _pipeline(model_type, random_state=100 + int(y))
        if model_type == "classifier":
            ytr = tr[target].astype(int)
            yva = va[target].astype(int)
            if ytr.nunique() < 2 or yva.nunique() < 2:
                continue
            pipe.fit(tr[feats], ytr)
            prob = pipe.predict_proba(va[feats])[:, 1]
            m = _classification_metrics(yva.to_numpy(), prob)
        else:
            pipe.fit(tr[feats], tr[target].astype(float))
            pred = pipe.predict(va[feats])
            m = _regression_metrics(va[target].to_numpy(dtype=float), pred)
        reports.append({"valid_year": int(y), "train_rows": int(len(tr)), "valid_rows": int(len(va)), **m})
    return reports


def train_model(training_panel_path: str | Path, model_dir: str | Path, target: str = "label_outperform_sector_60d") -> dict:
    """Backward-compatible single classifier entrypoint."""
    df = read_table(training_panel_path)
    if df.is_empty() or target not in df.columns:
        raise ValueError(f"Training panel is empty or target column not found: {target}")
    df = df.filter(pl.col(target).is_not_null()).sort("as_of_date")
    feats = _feature_columns(df, target)
    if not feats:
        raise ValueError("No numeric feature columns found.")
    pdf = df.select(["as_of_date", target, *feats]).to_pandas()
    model, metrics = _train_one(pdf, feats, target, "classifier")
    if model is None:
        raise ValueError(f"Model training skipped: {metrics}")
    outdir = ensure_dir(model_dir)
    joblib.dump(model, outdir / "model.joblib")
    metrics["features"] = feats
    with open(outdir / "metadata.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, default=str)
    return metrics


def train_redesigned_models(
    training_panel_path: str | Path,
    model_dir: str | Path,
    horizon: int = 60,
    rank_target: str | None = None,
    classifier_target: str | None = None,
    risk_target: str | None = None,
    walkforward: bool = False,
    purge_days: int = 60,
) -> dict[str, Any]:
    df = read_table(training_panel_path)
    targets = ModelTargets(horizon, rank_target, classifier_target, risk_target).resolved()
    required = [targets.rank_target, targets.classifier_target, targets.risk_target]
    missing = [c for c in required if c not in df.columns]
    if df.is_empty() or missing:
        raise ValueError(f"Training panel empty or missing target columns: {missing}")
    df = df.sort("as_of_date")
    feats = _feature_columns(df, required, min_coverage=0.01)
    if not feats:
        raise ValueError("No numeric feature columns found for redesigned training.")
    pdf = df.select(["as_of_date", *required, *feats]).to_pandas()

    specs = {
        "return_ranker": (targets.rank_target, "regressor"),
        "outperform_classifier": (targets.classifier_target, "classifier"),
        "downside_risk_classifier": (targets.risk_target, "classifier"),
    }
    outdir = ensure_dir(model_dir)
    models_meta: dict[str, Any] = {}
    for name, (target, model_type) in specs.items():
        model, metrics = _train_one(pdf, feats, target, model_type)
        if model is not None:
            joblib.dump(model, outdir / f"{name}.joblib")
        if walkforward:
            metrics["walkforward"] = _walkforward_report(pdf, feats, target, model_type, purge_days=purge_days)
        models_meta[name] = metrics
    metadata = {
        "version": "v5_model_redesign",
        "horizon": int(horizon),
        "rank_target": targets.rank_target,
        "classifier_target": targets.classifier_target,
        "risk_target": targets.risk_target,
        "features": feats,
        "feature_count": len(feats),
        "score_components_included": [c for c in SCORE_COMPONENTS if c in feats],
        "keystats_included": [c for c in KEYSTAT_FEATURE_HINTS if c in feats],
        "models": models_meta,
    }
    with open(outdir / "metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, default=str)
    return metadata


def _date_rank_expr(col: str, out: str, higher: bool = True) -> pl.Expr:
    rank = pl.col(col).rank(method="average").over("as_of_date")
    n = pl.len().over("as_of_date")
    pct = pl.when(n > 1).then((rank - 1) / (n - 1) * 100.0).otherwise(50.0)
    score = pct if higher else 100.0 - pct
    return pl.when(pl.col(col).is_null()).then(50.0).otherwise(score).alias(out)


def apply_model(panel_path: str | Path, model_dir: str | Path, output_path: str | Path) -> pl.DataFrame:
    """Backward-compatible single classifier application."""
    df = read_table(panel_path)
    if df.is_empty():
        write_table(df, output_path, csv_copy=True); return df
    outdir = Path(model_dir)
    pipe = joblib.load(outdir / "model.joblib")
    with open(outdir / "metadata.json", "r", encoding="utf-8") as f:
        meta = json.load(f)
    feats = [c for c in meta["features"] if c in df.columns]
    pdf = df.select(feats).to_pandas()
    score = pipe.predict_proba(pdf)[:, 1] * 100.0
    out = df.with_columns(pl.Series("ml_rank_score", score))
    write_table(out, output_path, csv_copy=True)
    return out


def apply_redesigned_models(panel_path: str | Path, model_dir: str | Path, output_path: str | Path) -> pl.DataFrame:
    df = read_table(panel_path)
    if df.is_empty():
        write_table(df, output_path, csv_copy=True); return df
    outdir = Path(model_dir)
    with open(outdir / "metadata.json", "r", encoding="utf-8") as f:
        meta = json.load(f)
    feats = [c for c in meta["features"] if c in df.columns]
    if not feats:
        raise ValueError("No trained feature columns found in scoring panel.")
    pdf = df.select(feats).to_pandas()
    cols: list[pl.Series] = []
    if (outdir / "return_ranker.joblib").exists():
        m = joblib.load(outdir / "return_ranker.joblib")
        cols.append(pl.Series("pred_excess_return", m.predict(pdf).astype(float)))
    if (outdir / "outperform_classifier.joblib").exists():
        m = joblib.load(outdir / "outperform_classifier.joblib")
        cols.append(pl.Series("prob_outperform", (m.predict_proba(pdf)[:, 1] * 100.0).astype(float)))
    if (outdir / "downside_risk_classifier.joblib").exists():
        m = joblib.load(outdir / "downside_risk_classifier.joblib")
        cols.append(pl.Series("prob_bad_drawdown", (m.predict_proba(pdf)[:, 1] * 100.0).astype(float)))
    out = df.with_columns(cols) if cols else df
    # Fallback columns keep formula robust if one model was skipped.
    for c in ["pred_excess_return", "prob_outperform", "prob_bad_drawdown", "fundamental_score", "insider_score", "valuation_score", "quality_score", "liquidity_score"]:
        if c not in out.columns:
            out = out.with_columns(pl.lit(None, dtype=pl.Float64).alias(c))
    out = out.with_columns([
        _date_rank_expr("pred_excess_return", "return_rank_score", higher=True),
        _date_rank_expr("prob_outperform", "prob_outperform_score", higher=True),
        pl.col("prob_bad_drawdown").fill_null(50.0).clip(0, 100).alias("downside_risk_score"),
        ((pl.col("valuation_score").fill_null(50.0) + pl.col("quality_score").fill_null(50.0)) / 2.0).alias("valuation_quality_score"),
    ]).with_columns([
        (
            0.35 * pl.col("return_rank_score")
            + 0.25 * pl.col("prob_outperform_score")
            + 0.15 * pl.col("fundamental_score").fill_null(50.0)
            + 0.10 * pl.col("insider_score").fill_null(50.0)
            + 0.10 * pl.col("valuation_quality_score").fill_null(50.0)
            + 0.05 * pl.col("liquidity_score").fill_null(50.0)
            - 0.25 * pl.col("downside_risk_score").fill_null(50.0)
        ).clip(0, 100).alias("ml_alpha_score")
    ]).with_columns([
        (
            0.35 * pl.col("fundamental_score").fill_null(50.0)
            + 0.25 * pl.col("return_rank_score")
            + 0.20 * pl.col("prob_outperform_score")
            + 0.10 * pl.col("insider_score").fill_null(50.0)
            + 0.05 * pl.col("valuation_quality_score").fill_null(50.0)
            + 0.05 * pl.col("liquidity_score").fill_null(50.0)
            - 0.20 * pl.col("downside_risk_score").fill_null(50.0)
        ).clip(0, 100).alias("final_alpha_score_v2")
    ])
    write_table(out, output_path, csv_copy=True)
    return out
