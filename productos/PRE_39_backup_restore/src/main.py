"""Respalda y restaura un artefacto de operación mínimo."""

import json
import shutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
SOURCE = ROOT_DIR / "data" / "registry.json"
BACKUP = ROOT_DIR / "submission" / "registry.backup.json"
RESTORED = ROOT_DIR / "submission" / "registry.restored.json"


def backup_and_restore():
    """La restauración comprobable hace que el respaldo sea más que una copia olvidada."""

    shutil.copy2(SOURCE, BACKUP)
    shutil.copy2(BACKUP, RESTORED)
    return json.loads(RESTORED.read_text())
