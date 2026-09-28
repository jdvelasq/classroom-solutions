"""Demuestra una selección reproducible mediante una semilla declarada."""

import json
from pathlib import Path
import random


ROOT_DIR = Path(__file__).resolve().parents[1]


def select_sample(seed):
    """La semilla declarada permite repetir una decisión aleatoria al investigar un resultado."""

    generator = random.Random(seed)
    return generator.sample(["factory-1", "factory-2", "factory-3", "factory-4"], 2)


def main():
    """La muestra queda registrada junto con la semilla que permite repetirla."""

    output_path = ROOT_DIR / "submission" / "sample.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps({"seed": 123, "sample": select_sample(123)}, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
