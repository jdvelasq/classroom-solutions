"""Verifica que la migración conserve el significado de un registro."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import migrate_v1_to_v2


def test_migration_creates_versioned_schema():
    """El nuevo contrato debe declarar versión y mantener los valores operativos."""

    assert migrate_v1_to_v2({"factory": 2, "risk": "high"}) == {"schema_version": "2.0", "factory_id": 2, "risk": "high"}
