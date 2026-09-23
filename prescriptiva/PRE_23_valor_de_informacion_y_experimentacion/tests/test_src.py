from pathlib import Path
import importlib.util,pandas as pd
FOLDER=Path(__file__).resolve().parents[1]; spec=importlib.util.spec_from_file_location('pre23',FOLDER/'src'/'main.py'); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
def test_information_is_compared_to_action():
    result=module.evaluate(pd.read_csv(FOLDER/'data'/'decision_scenarios.csv'))
    assert set(result.action)=={'lanzar_ahora','medir_antes'}
