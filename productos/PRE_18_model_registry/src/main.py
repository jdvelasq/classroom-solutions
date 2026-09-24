"""Promueve un modelo candidato sin volver a explicar cómo fue entrenado."""

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
CANDIDATES_PATH = ROOT_DIR / "models" / "candidates.json"
REGISTRY_DIR = ROOT_DIR / "submission" / "model_registry"


def parse_arguments():
    """La actividad limita la decisión a promover un candidato conocido."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", default="candidate_v1")
    parser.add_argument("--stage", choices=["production", "archived"], required=True)
    return parser.parse_args()


def find_candidate(model_id):
    """El identificador estable evita promover un archivo por accidente."""

    candidates = json.loads(CANDIDATES_PATH.read_text(encoding="utf-8"))
    for candidate in candidates:
        if candidate["model_id"] == model_id:
            return candidate
    raise ValueError(f"No existe el modelo candidato: {model_id}")


def promote_model(candidate, stage):
    """El registro conserva qué artefacto fue aprobado para cada etapa."""

    stage_dir = REGISTRY_DIR / stage
    stage_dir.mkdir(parents=True, exist_ok=True)
    source_path = ROOT_DIR / candidate["artifact"]
    target_path = stage_dir / "model.pkl"
    shutil.copy2(source_path, target_path)

    record = {
        "model_id": candidate["model_id"],
        "stage": stage,
        "source_artifact": candidate["artifact"],
        "test_accuracy": candidate["test_accuracy"],
        "promoted_at": datetime.now(timezone.utc).isoformat(),
    }
    (stage_dir / "registry.json").write_text(
        json.dumps(record, indent=2), encoding="utf-8"
    )
    return record


def main():
    """La promoción separa la decisión operativa de la construcción del modelo."""

    arguments = parse_arguments()
    candidate = find_candidate(arguments.model_id)
    record = promote_model(candidate, arguments.stage)
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
