from __future__ import annotations
from pathlib import Path
import shutil
from alpha_research.labels.builder import build_training_dataset
from alpha_research.validation.folds import build_folds
from alpha_research.training.trainer import train_models

def run_continual(root, as_of_date, start_date="2018-01-01", freq="month", families=None, algos=None):
    # For v3, continual uses history feature store refreshed to as_of_date by caller.
    meta=build_training_dataset(root,"history",start_date,as_of_date)
    build_folds(root, freq=freq, fold_set="continual", first_val_year=2025, last_val_year=int(str(as_of_date)[:4]), train_start=start_date)
    tr=train_models(root, fold_set="continual", families=families, algos=algos)
    return {"dataset":meta,"training":tr}
