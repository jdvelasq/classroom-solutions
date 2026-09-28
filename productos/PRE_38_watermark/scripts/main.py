"""Procesa solo eventos posteriores a una marca de agua declarada."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def process_new_events():
    """La marca de agua evita reprocesar todo el historial en cada ejecución."""

    events = json.loads((ROOT_DIR / "data" / "events.json").read_text())
    watermark = json.loads((ROOT_DIR / "data" / "watermark.json").read_text())["last_processed"]
    new_events = [event for event in events if event["timestamp"] > watermark]
    new_watermark = max(event["timestamp"] for event in new_events) if new_events else watermark
    return {"processed_ids": [event["id"] for event in new_events], "new_watermark": new_watermark}


def main():
    """Los eventos procesados y la nueva marca de agua quedan registrados."""

    output_path = ROOT_DIR / "submission" / "watermark_result.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(process_new_events(), indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
