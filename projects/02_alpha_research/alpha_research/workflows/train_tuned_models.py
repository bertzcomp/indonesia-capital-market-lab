#!/usr/bin/env python3
from __future__ import annotations

import argparse
import inspect
import json
import os
import shutil
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from alpha_research.training.trainer import train_models


def _split_csv(x: str) -> list[str]:
    return [v.strip() for v in str(x).split(",") if v.strip()]


def _copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def _copytree_contents(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


def _backup_path(path: Path, tag: str) -> Path:
    return path.with_name(path.name + f".bak_{tag}")


def _read_json(path: Path) -> Any | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _fold_records(fold_dir: Path, fold_set: str) -> list[dict[str, Any]]:
    meta = _read_json(fold_dir / "fold_manifest.json") or _read_json(fold_dir / f"fold_meta_{fold_set}.json") or _read_json(fold_dir / "fold_meta.json")
    if isinstance(meta, dict) and isinstance(meta.get("folds"), list):
        return list(meta["folds"])

    records: list[dict[str, Any]] = []
    for train_path in sorted(fold_dir.glob("*train*.parquet")):
        name = train_path.name
        val_name = name.replace("_train.parquet", "_val.parquet").replace("train", "val", 1)
        val_path = fold_dir / val_name
        if val_path.exists():
            records.append({"fold": len(records) + 1, "train_path": str(train_path), "val_path": str(val_path), "fold_id": train_path.stem.replace("_train", "")})
    return records


def _materialize_fold_aliases(src_fold_dir: Path, dst_fold_dir: Path, fold_set: str) -> dict[str, Any]:
    """Copy folds and create common legacy filename aliases.

    Different trainer revisions in this project have expected different fold layouts.
    To avoid n_records=0 caused by path-pattern mismatch, we expose the same folds as:
      data/datasets/folds/*
      data/datasets/folds/<fold_set>/*
      data/training/folds/*
      data/training/folds/<fold_set>/*
    and create aliases like fold_01_train.parquet, train_fold_01.parquet, train_1.parquet.
    """
    dst_fold_dir.mkdir(parents=True, exist_ok=True)
    _copytree_contents(src_fold_dir, dst_fold_dir)

    records = _fold_records(src_fold_dir, fold_set)
    alias_count = 0
    normalized_records: list[dict[str, Any]] = []

    for i, rec in enumerate(records, start=1):
        train_src = Path(rec.get("train_path", ""))
        val_src = Path(rec.get("val_path", ""))
        if not train_src.is_absolute():
            train_src = src_fold_dir / train_src.name
        if not val_src.is_absolute():
            val_src = src_fold_dir / val_src.name
        if not train_src.exists() or not val_src.exists():
            # Try using filename under source fold dir.
            train_src = src_fold_dir / Path(str(rec.get("train_path", ""))).name
            val_src = src_fold_dir / Path(str(rec.get("val_path", ""))).name
        if not train_src.exists() or not val_src.exists():
            continue

        fold_no = int(rec.get("fold", i)) if str(rec.get("fold", i)).isdigit() else i
        fold_id = str(rec.get("fold_id") or f"fold_{fold_no:02d}")

        # Copy original filenames if not already present.
        _copy_file(train_src, dst_fold_dir / train_src.name)
        _copy_file(val_src, dst_fold_dir / val_src.name)

        alias_names = [
            (f"fold_{fold_no:02d}_train.parquet", f"fold_{fold_no:02d}_val.parquet"),
            (f"train_fold_{fold_no:02d}.parquet", f"val_fold_{fold_no:02d}.parquet"),
            (f"train_{fold_no}.parquet", f"val_{fold_no}.parquet"),
            (f"{fold_id}_train.parquet", f"{fold_id}_val.parquet"),
        ]
        for train_name, val_name in alias_names:
            _copy_file(train_src, dst_fold_dir / train_name)
            _copy_file(val_src, dst_fold_dir / val_name)
            alias_count += 2

        nrec = dict(rec)
        nrec.update({
            "fold": fold_no,
            "fold_id": fold_id,
            "train_path": str((dst_fold_dir / f"fold_{fold_no:02d}_train.parquet").resolve()),
            "val_path": str((dst_fold_dir / f"fold_{fold_no:02d}_val.parquet").resolve()),
        })
        normalized_records.append(nrec)

    manifest = {
        "fold_set": fold_set,
        "source_fold_dir": str(src_fold_dir),
        "materialized_fold_dir": str(dst_fold_dir),
        "n_folds": len(normalized_records),
        "folds": normalized_records,
        "alias_count": alias_count,
    }
    for name in ["fold_manifest.json", f"fold_meta_{fold_set}.json", "fold_meta.json", "folds.json"]:
        (dst_fold_dir / name).write_text(json.dumps(manifest, indent=2, default=str), encoding="utf-8")
    return manifest


@contextmanager
def _legacy_training_artifact_bridge(root: Path, dataset: Path | None, fold_dir: Path | None, fold_set: str):
    if dataset is None and fold_dir is None:
        yield {"bridge_active": False}
        return

    if dataset is None or fold_dir is None:
        raise SystemExit("--dataset and --fold-dir must be supplied together for custom/continual training.")

    dataset = dataset.resolve()
    fold_dir = fold_dir.resolve()
    if not dataset.exists():
        raise FileNotFoundError(dataset)
    if not fold_dir.exists():
        raise FileNotFoundError(fold_dir)

    tag = time.strftime("%Y%m%d_%H%M%S")

    # Backup both old and new conventional locations, because different trainer revisions used both.
    paths_to_backup = [
        root / "data" / "datasets" / "training",
        root / "data" / "datasets" / "folds",
        root / "data" / "training",
    ]
    backups: list[tuple[Path, Path]] = []

    def backup_if_exists(path: Path) -> None:
        if path.exists():
            bak = _backup_path(path, tag)
            if bak.exists():
                if bak.is_dir():
                    shutil.rmtree(bak)
                else:
                    bak.unlink()
            path.rename(bak)
            backups.append((path, bak))

    try:
        for p in paths_to_backup:
            backup_if_exists(p)

        # Dataset aliases.
        dataset_targets = [
            root / "data" / "datasets" / "training" / "full_labeled.parquet",
            root / "data" / "training" / "full_labeled.parquet",
        ]
        for target in dataset_targets:
            _copy_file(dataset, target)
            for name in ["dataset_meta.json", "feature_registry.json", "label_summary.json", "training_dataset_qa.json"]:
                src = dataset.parent / name
                if src.exists():
                    _copy_file(src, target.parent / name)

        # Fold aliases.
        fold_targets = [
            root / "data" / "datasets" / "folds",
            root / "data" / "datasets" / "folds" / fold_set,
            root / "data" / "training" / "folds",
            root / "data" / "training" / "folds" / fold_set,
        ]
        fold_manifests = []
        for dst in fold_targets:
            fold_manifests.append(_materialize_fold_aliases(fold_dir, dst, fold_set))

        bridge_meta = {
            "bridge_active": True,
            "dataset": str(dataset),
            "fold_dir": str(fold_dir),
            "fold_set": fold_set,
            "created_at": tag,
            "dataset_targets": [str(x) for x in dataset_targets],
            "fold_targets": [str(x) for x in fold_targets],
            "fold_manifests": fold_manifests,
        }
        (root / "data" / "datasets" / "training" / "_CONTINUAL_BRIDGE_SOURCE.json").write_text(json.dumps(bridge_meta, indent=2, default=str), encoding="utf-8")
        yield bridge_meta
    finally:
        # Remove temporary replacements.
        for p in paths_to_backup:
            if p.exists():
                if p.is_dir():
                    shutil.rmtree(p)
                else:
                    p.unlink()
        # Restore originals.
        for original, bak in reversed(backups):
            if bak.exists():
                bak.rename(original)


def _diagnose_zero_records(root: Path, dataset: Path | None, fold_dir: Path | None, fold_set: str, families: list[str]) -> dict[str, Any]:
    diag: dict[str, Any] = {"fold_set": fold_set, "families": families}
    if dataset and dataset.exists():
        try:
            import polars as pl
            df = pl.read_parquet(dataset)
            diag["dataset_shape"] = df.shape
            diag["dataset_date_min"] = str(df.select(pl.col("date").min()).item()) if "date" in df.columns else None
            diag["dataset_date_max"] = str(df.select(pl.col("date").max()).item()) if "date" in df.columns else None
            target_cols = [c for c in df.columns if c.startswith("label_")]
            diag["target_cols"] = target_cols
        except Exception as e:
            diag["dataset_read_error"] = repr(e)
    if fold_dir and fold_dir.exists():
        diag["fold_dir"] = str(fold_dir)
        diag["fold_files_sample"] = sorted([p.name for p in fold_dir.iterdir()])[:50]
        meta = _read_json(fold_dir / "fold_manifest.json") or _read_json(fold_dir / f"fold_meta_{fold_set}.json")
        if isinstance(meta, dict):
            diag["fold_manifest_n_folds"] = meta.get("n_folds")
            diag["fold_manifest_keys"] = sorted(meta.keys())
    return diag


def _call_train_models(root: Path, fold_set: str, families: list[str], algos: list[str], seed: int, tune_trials: int,
                       dataset: Path | None, fold_dir: Path | None, run_prefix: str | None) -> dict[str, Any]:
    sig = inspect.signature(train_models)
    params = sig.parameters

    # Native trainer support path.
    if "dataset" in params or "dataset_path" in params or "fold_dir" in params or "run_prefix" in params:
        kwargs: dict[str, Any] = {}
        if "dataset" in params:
            kwargs["dataset"] = str(dataset) if dataset else None
        if "dataset_path" in params:
            kwargs["dataset_path"] = str(dataset) if dataset else None
        if "fold_dir" in params:
            kwargs["fold_dir"] = str(fold_dir) if fold_dir else None
        if "run_prefix" in params:
            kwargs["run_prefix"] = run_prefix
        result = train_models(str(root), fold_set, families, algos, seed, tune_trials, **kwargs)
        return result if isinstance(result, dict) else {"result": result}

    # Legacy trainer path.
    runs_dir = root / "models" / "runs"
    before = {p.name for p in runs_dir.iterdir()} if runs_dir.exists() else set()

    old_env = os.environ.get("ALPHA_RESEARCH_RUN_PREFIX")
    if run_prefix:
        os.environ["ALPHA_RESEARCH_RUN_PREFIX"] = run_prefix

    bridge_meta: dict[str, Any] = {}
    try:
        with _legacy_training_artifact_bridge(root, dataset, fold_dir, fold_set) as bm:
            bridge_meta = bm
            result = train_models(str(root), fold_set, families, algos, seed, tune_trials)
    finally:
        if old_env is None:
            os.environ.pop("ALPHA_RESEARCH_RUN_PREFIX", None)
        else:
            os.environ["ALPHA_RESEARCH_RUN_PREFIX"] = old_env

    after = {p.name for p in runs_dir.iterdir()} if runs_dir.exists() else set()
    new_runs = sorted(after - before)
    renamed: list[dict[str, str]] = []
    if run_prefix and new_runs:
        for run_id in new_runs:
            src = runs_dir / run_id
            if not src.exists() or not src.is_dir():
                continue
            dst_name = run_id if run_id.startswith(run_prefix) else f"{run_prefix}_{run_id}"
            dst = runs_dir / dst_name
            if dst.exists():
                dst_name = f"{dst_name}_{int(time.time())}"
                dst = runs_dir / dst_name
            src.rename(dst)
            renamed.append({"old": run_id, "new": dst_name})

    out = dict(result) if isinstance(result, dict) else {"result": result}
    out.update({
        "continual_training_mode": dataset is not None,
        "dataset": str(dataset) if dataset else None,
        "fold_dir": str(fold_dir) if fold_dir else None,
        "run_prefix": run_prefix,
        "renamed_runs": renamed,
        "bridge_meta": bridge_meta,
    })
    if int(out.get("n_records", 0) or 0) == 0:
        out["zero_record_diagnostics"] = _diagnose_zero_records(root, dataset, fold_dir, fold_set, families)
        # Make silent failure explicit. The user should not treat n_records=0 as success.
        raise SystemExit(json.dumps(out, indent=2, default=str))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--fold-set", default="quarterly")
    ap.add_argument("--families", default="sm_tracker,ara_predictor,multi_strategy_time,market_maker_accumulation,momentum_ranker")
    ap.add_argument("--algos", default="hgb,rank_hgb,regime_hgb")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--tune-trials", type=int, default=12)
    ap.add_argument("--dataset", default=None)
    ap.add_argument("--fold-dir", default=None)
    ap.add_argument("--run-prefix", default=None)
    a = ap.parse_args()

    root = Path(a.root).resolve()
    dataset = (root / a.dataset).resolve() if a.dataset and not Path(a.dataset).is_absolute() else (Path(a.dataset).resolve() if a.dataset else None)
    fold_dir = (root / a.fold_dir).resolve() if a.fold_dir and not Path(a.fold_dir).is_absolute() else (Path(a.fold_dir).resolve() if a.fold_dir else None)

    result = _call_train_models(root, a.fold_set, _split_csv(a.families), _split_csv(a.algos), a.seed, a.tune_trials, dataset, fold_dir, a.run_prefix)
    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
