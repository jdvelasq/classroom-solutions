"""Verifica que un respaldo pueda reconstruir el artefacto original."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import BACKUP, RESTORED, backup_and_restore


def test_backup_can_be_restored():
    """La recuperación debe preservar el contenido que estaba en operación."""

    try:
        assert backup_and_restore() == {"production_version": "v1", "model": "factory-risk"}
        assert BACKUP.exists() and RESTORED.exists()
    finally:
        BACKUP.unlink(missing_ok=True)
        RESTORED.unlink(missing_ok=True)
