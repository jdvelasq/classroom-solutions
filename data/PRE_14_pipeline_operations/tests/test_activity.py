import importlib.util
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location("pre14",ROOT/"src/main.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def setup_module():m.build_submission()
def test_transient_failure_retries_and_continues():
    x=pd.read_csv(ROOT/"submission/run_history.csv");r=x[x.processing_date=="2026-10-02"];assert r[r.task=="extract"].status.tolist()==["FAILED","SUCCESS"] and r[r.task=="publish"].status.tolist()==["SUCCESS"]
def test_validation_failure_skips_downstream_without_retry():
    x=pd.read_csv(ROOT/"submission/run_history.csv");r=x[x.processing_date=="2026-10-03"];assert r[r.task=="validate"].status.tolist()==["FAILED"] and r[r.task.isin(["transform","publish"])].status.tolist()==["SKIPPED","SKIPPED"]
