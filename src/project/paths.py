"""Project-relative paths for an editable source checkout."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "configs" / "config.yaml"
GENERATED_DIRS = (
    "data/raw", "data/interim", "data/processed",
    "results/replication/tables", "results/replication/figures",
    "results/extension/tables", "results/extension/figures",
)

def ensure_directories():
    """Create ignored data/output folders in a fresh clone."""
    for directory in GENERATED_DIRS:
        (ROOT / directory).mkdir(parents=True, exist_ok=True)
