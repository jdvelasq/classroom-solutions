"""Las pruebas se implementarán junto con la solución del taller."""
from pathlib import Path
import importlib.util
import pandas as pd
FOLDER = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pre15_main", FOLDER / "src" / "main.py")
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)

def test_tradeoffs_make_value_visible():
    result = module.evaluate(pd.read_csv(FOLDER / "data" / "service_options.csv"))
    assert result.loc[result.option_id == "P1", "net_value"].iloc[0] > 0
    assert result.loc[result.option_id == "P2", "net_value"].iloc[0] > 0
