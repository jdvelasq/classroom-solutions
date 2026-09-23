"""Las pruebas se implementarán junto con la solución del taller."""
from pathlib import Path
import importlib.util
import pandas as pd
FOLDER=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('pre17_main',FOLDER/'src'/'main.py'); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
def test_forecast_uncertainty_changes_order_value():
    result=module.evaluate(pd.read_csv(FOLDER/'data'/'order_options.csv'),pd.read_csv(FOLDER/'data'/'forecast_scenarios.csv'))
    assert result.expected_value.max()>0
    assert result.stockout_probability.tolist()==[0.75,0.25,0.0]
