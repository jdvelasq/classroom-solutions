"""Registra escenarios mínimos de operación de un pipeline."""
from pathlib import Path
import csv
ROOT=Path(__file__).parents[1]; OUTPUT=ROOT/"submission/run_history.csv"
def build_submission():
    rows=[("2026-10-01","extract",1,"SUCCESS"),("2026-10-01","validate",1,"SUCCESS"),("2026-10-01","transform",1,"SUCCESS"),("2026-10-01","publish",1,"SUCCESS"),("2026-10-02","extract",1,"FAILED"),("2026-10-02","extract",2,"SUCCESS"),("2026-10-02","validate",1,"SUCCESS"),("2026-10-02","transform",1,"SUCCESS"),("2026-10-02","publish",1,"SUCCESS"),("2026-10-03","extract",1,"SUCCESS"),("2026-10-03","validate",1,"FAILED"),("2026-10-03","transform",0,"SKIPPED"),("2026-10-03","publish",0,"SKIPPED"),("2026-09-01","extract",1,"SUCCESS"),("2026-09-01","validate",1,"SUCCESS"),("2026-09-01","transform",1,"SUCCESS"),("2026-09-01","publish",1,"SUCCESS")]
    with OUTPUT.open("w",newline="",encoding="utf-8") as f: w=csv.writer(f);w.writerow(["processing_date","task","attempt","status"]);w.writerows(rows)
if __name__=="__main__":build_submission()
