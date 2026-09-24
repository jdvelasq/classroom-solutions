"""Verifica que las corridas conserven los artefactos necesarios para recuperarlas."""

import json
import shutil
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
EXPERIMENTS_DIR = PRE_DIR / "submission" / "experiments"


def run_experiment(model_name, run_id):
    """Dos corridas hacen visible que la comparación requiere un registro común."""

    subprocess.run(
        [sys.executable, "src/main.py", "--model", model_name, "--run-id", run_id],
        cwd=PRE_DIR,
        check=True,
        capture_output=True,
        text=True,
    )


def test_experiments_are_visible_and_recoverable():
    """Cada corrida debe conservar configuración, datos, modelo y métrica."""

    try:
        run_experiment("tree", "tree-run")
        run_experiment("knn", "knn-run")
        index = json.loads((EXPERIMENTS_DIR / "index.json").read_text(encoding="utf-8"))

        assert [run["run_id"] for run in index] == ["tree-run", "knn-run"]
        for run_id in ["tree-run", "knn-run"]:
            run_dir = EXPERIMENTS_DIR / run_id
            assert (run_dir / "config.json").exists()
            assert (run_dir / "metrics.json").exists()
            assert (run_dir / "model.pkl").exists()
            assert (run_dir / "data" / "train.csv").exists()
            assert (run_dir / "data" / "test.csv").exists()
    finally:
        shutil.rmtree(EXPERIMENTS_DIR, ignore_errors=True)
