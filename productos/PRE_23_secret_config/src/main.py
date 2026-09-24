"""Lee una configuración sensible sin incluirla en el código ni en los reportes."""

import json
import os
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
SECRET_NAME = "ANALYTICS_API_KEY"


def get_api_key():
    """El ambiente evita exponer una credencial al compartir el repositorio."""

    api_key = os.environ.get(SECRET_NAME)
    if not api_key:
        raise RuntimeError(f"Debe configurar la variable de ambiente {SECRET_NAME}.")
    return api_key


def main():
    """La evidencia confirma la configuración sin revelar el secreto utilizado."""

    get_api_key()
    report = {"secret_name": SECRET_NAME, "configured": True}
    output_path = ROOT_DIR / "submission" / "secret_config_report.json"
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
