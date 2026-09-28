"""Construye un manifiesto para una liberación versionada del producto."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def main():
    """Una versión legible permite identificar qué capacidad recibió el consumidor."""

    version = (ROOT_DIR / "VERSION").read_text().strip()
    manifest = {"product": "factory-risk-indicator", "version": version, "release_notes": "CHANGELOG.md"}
    (ROOT_DIR / "submission" / "release_manifest.json").write_text(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
