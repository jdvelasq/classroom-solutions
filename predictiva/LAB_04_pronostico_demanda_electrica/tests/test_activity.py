from pathlib import Path
import sys
import json
import pandas as pd
ACTIVITY_DIR = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ACTIVITY_DIR))
from ..src.main import main
def test_forecast_deliverables():
    main()
    forecast = pd.read_csv('submission/forecast.csv')
    metrics = json.loads(Path('submission/metrics.json').read_text())
    assert forecast['Fecha'].is_monotonic_increasing
    assert forecast[['baseline_forecast', 'weekday_forecast']].notna().all().all()
    assert metrics['baseline_mae'] > 0 and metrics['weekday_mae'] > 0
