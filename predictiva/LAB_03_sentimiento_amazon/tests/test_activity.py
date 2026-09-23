from pathlib import Path
import sys
import pandas as pd
ACTIVITY_DIR = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ACTIVITY_DIR))
from ..src.main import main
def test_sentiment_deliverables():
    main()
    original = pd.read_csv('data/amazon_cells_labelled.tsv', sep='\t', names=['review', 'sentiment'])
    results = pd.read_csv('submission/completed_reviews.csv')
    assert Path('submission/model.pkl').exists()
    assert results.shape == original.shape
    assert results['sentiment'].notna().all()
    assert results.loc[original['sentiment'].notna(), 'sentiment'].tolist() == original.loc[original['sentiment'].notna(), 'sentiment'].astype(int).tolist()
    assert set(results['sentiment']).issubset({0, 1})
