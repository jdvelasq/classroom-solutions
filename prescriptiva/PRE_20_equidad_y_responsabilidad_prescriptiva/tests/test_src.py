"""Las pruebas se implementarán junto con la solución del taller."""
from pathlib import Path
import importlib.util, pandas as pd
FOLDER=Path(__file__).resolve().parents[1]; spec=importlib.util.spec_from_file_location('pre20',FOLDER/'src'/'main.py'); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
def test_audit_identifies_unequal_policy():
    audit=module.audit(pd.read_csv(FOLDER/'data'/'policy_impacts.csv'))
    assert audit.loc[audit.policy=='P0','contact_rate_gap'].iloc[0]==0
    assert audit.loc[audit.policy=='P1','contact_rate_gap'].iloc[0]>0.2
