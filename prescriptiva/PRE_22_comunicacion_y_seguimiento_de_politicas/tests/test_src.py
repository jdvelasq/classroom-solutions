from pathlib import Path
import subprocess
FOLDER=Path(__file__).resolve().parents[1]
def test_brief_is_generated():
    subprocess.run(['python3', str(FOLDER/'src'/'main.py')], check=True)
    assert (FOLDER/'submission'/'policy_brief.csv').exists()
