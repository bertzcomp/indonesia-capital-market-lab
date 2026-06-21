#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import polars as pl

from alpha_research.inference.policy_engine import build_policy_signals, collect_policy_score_cols, load_json


def _date_slug(d: str) -> str:
    dt = datetime.strptime(d[:10], "%Y-%m-%d")
    return dt.strftime("%d_%b_%Y").lower()


def _find_base_scores(root: Path, end_date: str, explicit: Optional[str] = None) -> Path:
    if explicit:
        p = Path(explicit)
        if not p.is_absolute():
            p = root / p
        if not p.exists():
            raise FileNotFoundError(p)
        return p
    exact = root / "signals" / "live" / f"base_scores_{end_date}.parquet"
    if exact.exists():
        return exact
    candidates = sorted((root / "signals" / "live").glob("base_scores_*.parquet"))
    if candidates:
        return candidates[-1]
    raise FileNotFoundError(f"No base score panel found under {root / 'signals/live'}")


def _run_base_scores(args: argparse.Namespace) -> None:
    cmd = [
        sys.executable,
        "workflows/build_live_base_scores.py",
        "--root", str(args.root),
        "--feature-scope", "live",
        "--registry", args.registry,
        "--from-date", args.from_date,
        "--end-date", args.end_date,
        "--price-min", str(args.price_min),
        "--price-max", str(args.price_max),
        "--min-traded-value", str(args.min_traded_value),
    ]
    if args.require_broksum:
        cmd.append("--require-broksum")
    subprocess.run(cmd, check=True)


def _write_df(df: pl.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if df.is_empty():
        # Write an empty CSV and parquet with no rows; Polars can write empty df if schema exists.
        df.write_parquet(path.with_suffix(".parquet"))
        df.write_csv(path.with_suffix(".csv"))
    else:
        df.write_parquet(path.with_suffix(".parquet"))
        df.write_csv(path.with_suffix(".csv"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--from-date", required=True)
    ap.add_argument("--end-date", required=True)
    ap.add_argument("--target-date", required=True)
    ap.add_argument("--holiday-dates", default="")
    ap.add_argument("--registry", default="configs/model_registry.json")
    ap.add_argument("--signal-policy", default="configs/signal_policy.json")
    ap.add_argument("--base-score-panel", default=None)
    ap.add_argument("--skip-base-scores", action="store_true")
    ap.add_argument("--price-min", type=float, default=0.0)
    ap.add_argument("--price-max", type=float, default=1e18)
    ap.add_argument("--min-traded-value", type=float, default=0.0)
    ap.add_argument("--require-broksum", action="store_true")
    ap.add_argument("--top-k-final", type=int, default=30)
    args = ap.parse_args()

    root = Path(args.root).resolve()
    args.root = root

    policy_path = Path(args.signal_policy)
    if not policy_path.is_absolute():
        policy_path = root / policy_path
    if not policy_path.exists():
        raise FileNotFoundError(f"Missing signal policy: {policy_path}")
    policy = load_json(policy_path)
    policy.setdefault("risk_controls", {})
    policy["risk_controls"].setdefault("max_total_final_signals", args.top_k_final)

    if not args.skip_base_scores:
        _run_base_scores(args)

    panel_path = _find_base_scores(root, args.end_date, args.base_score_panel)
    base = pl.read_parquet(panel_path)
    if base.is_empty():
        raise ValueError(f"Base score panel is empty: {panel_path}")

    needed = collect_policy_score_cols(policy)
    missing = [c for c in needed if c not in base.columns]
    if missing:
        raise ValueError(f"Signal policy requires score columns missing from base scores: {missing}")

    out = build_policy_signals(
        base,
        policy,
        price_min=args.price_min,
        price_max=args.price_max,
        default_min_traded_value=args.min_traded_value,
    )

    out_dir = root / "signals" / "daily" / f"signal_{_date_slug(args.target_date)}"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Always save all base scores for traceability.
    base.write_parquet(out_dir / "all_scores.parquet")
    base.write_csv(out_dir / "all_scores.csv")

    per_strategy = out["per_strategy"]
    assert isinstance(per_strategy, dict)
    for name, df in per_strategy.items():
        safe_name = str(name).replace(" ", "_").replace("/", "_").lower()
        _write_df(df, out_dir / safe_name)

    for key in ["all_strategy_watchlist", "all_strategy_candidates", "signals_main", "execution_shortlist"]:
        df = out[key]
        assert isinstance(df, pl.DataFrame)
        _write_df(df, out_dir / key)

    diagnostics = {
        "target_date": args.target_date,
        "from_date": args.from_date,
        "end_date": args.end_date,
        "base_score_panel": str(panel_path),
        "signal_policy": str(policy_path),
        "policy_score_cols": needed,
        "base_rows": base.height,
        "outputs": {
            "all_strategy_watchlist": out["all_strategy_watchlist"].height,
            "all_strategy_candidates": out["all_strategy_candidates"].height,
            "signals_main": out["signals_main"].height,
            "execution_shortlist": out["execution_shortlist"].height,
        },
        "per_strategy_watchlist_rows": {name: df.height for name, df in per_strategy.items()},
        "per_strategy_execution_rows": {name: df.height for name, df in out.get("per_strategy_execution", {}).items()},
        "warnings": [],
    }
    # ARA warning if execution is enabled.
    for name, df in per_strategy.items():
        if "ara" in name.lower() and not df.is_empty():
            diagnostics["warnings"].append("ARA strategy is active; monitor drawdown and treat as high-risk unless Monte Carlo accepted.")
    with open(out_dir / "diagnostics.json", "w", encoding="utf-8") as f:
        json.dump(diagnostics, f, indent=2, default=str)

    report = [
        f"# Daily Signal Report — {args.target_date}",
        "",
        f"Base score panel: `{panel_path}`",
        f"Policy: `{policy_path}`",
        "",
        "## Output counts",
        "",
        f"- All watchlist candidates: {diagnostics['outputs']['all_strategy_watchlist']}",
        f"- Execution candidates: {diagnostics['outputs']['all_strategy_candidates']}",
        f"- Signals main: {diagnostics['outputs']['signals_main']}",
        f"- Execution shortlist: {diagnostics['outputs']['execution_shortlist']}",
        "",
        "## Per strategy",
        "",
    ]
    for name, n in diagnostics["per_strategy_watchlist_rows"].items():
        exe_n = diagnostics.get("per_strategy_execution_rows", {}).get(name, 0)
        report.append(f"- {name}: watchlist={n}, execution_candidates={exe_n}")
    if diagnostics["warnings"]:
        report += ["", "## Warnings", ""] + [f"- {w}" for w in diagnostics["warnings"]]
    (out_dir / "report.md").write_text("\n".join(report), encoding="utf-8")

    print(json.dumps({
        "out_dir": str(out_dir),
        "base_score_panel": str(panel_path),
        "signals_main": diagnostics["outputs"]["signals_main"],
        "execution_shortlist": diagnostics["outputs"]["execution_shortlist"],
        "per_strategy_watchlist_rows": diagnostics["per_strategy_watchlist_rows"],
        "per_strategy_execution_rows": diagnostics["per_strategy_execution_rows"],
    }, indent=2))


if __name__ == "__main__":
    main()
