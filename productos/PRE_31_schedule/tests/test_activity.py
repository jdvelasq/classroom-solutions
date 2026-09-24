"""Verifica que la actividad declare una tarea periódica local."""

from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]


def test_local_schedule_is_declared():
    """La programación debe expresar frecuencia y ejecución de tareas pendientes."""

    source = (PRE_DIR / "src" / "main.py").read_text(encoding="utf-8")

    assert "schedule.every(10).seconds.do(generate_report)" in source
    assert "schedule.run_pending()" in source
