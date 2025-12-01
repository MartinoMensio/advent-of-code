from pathlib import Path

REPO_PATH = Path(__file__).parent.parent

DATA_PATH = REPO_PATH / "data"
DATA_PATH.mkdir(exist_ok=True)
