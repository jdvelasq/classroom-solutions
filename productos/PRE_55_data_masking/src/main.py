"""Enmascara identificadores antes de compartir una salida operativa."""

import csv
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
