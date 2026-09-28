"""Enmascara identificadores antes de compartir una salida operativa."""

import csv
import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def mask_email(email):
    """El identificador se reduce para que el reporte no revele más de lo necesario."""

    name, domain = email.split("@")
    return f"{name[0]}***@{domain}"


def create_masked_report():
    """La salida conserva el riesgo sin exponer el correo completo del consumidor."""

    with (ROOT_DIR / "data" / "customers.csv").open() as source:
        row = next(csv.DictReader(source))
    return {"customer_id": row["customer_id"], "email": mask_email(row["email"]), "risk": row["risk"]}


def main():
    """El reporte enmascarado queda listo para compartirse."""

    output_path = ROOT_DIR / "submission" / "masked_report.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(create_masked_report(), indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
