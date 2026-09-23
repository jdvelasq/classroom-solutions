from pathlib import Path
import sys
import json
import pandas as pd
ACTIVITY_DIR = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ACTIVITY_DIR))
from ..src.main import main
def test_sentiment_deliverables():
    main()
    results = pd.read_csv('submission/test_predictions.csv')
    metrics = json.loads(Path('submission/metrics.json').read_text())
    assert Path('submission/model.pkl').exists()
    assert {'review', 'sentiment', 'predicted_sentiment'}.issubset(results.columns)
    assert metrics['test_f1'] > 0.5
