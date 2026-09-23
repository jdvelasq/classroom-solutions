"""Utilidad de pruebas para ejecutar notebooks docentes locales."""

import os
from pathlib import Path

import nbformat


def execute_notebook(path: Path) -> None:
    path = path.resolve()
    notebook = nbformat.read(path, as_version=4)
    previous_directory = Path.cwd()
    try:
        os.chdir(path.parent)
        namespace = {"__name__": "__main__"}
        for cell in notebook.cells:
            if cell.cell_type == "code":
                exec(cell.source, namespace)
    finally:
        os.chdir(previous_directory)
