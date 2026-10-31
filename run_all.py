"""Initialize directories or run the research pipeline after implementation."""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--setup", action="store_true", help="Only create data/output folders")
    args = parser.parse_args()
    sys.path.insert(0, str(ROOT / "src"))
    from project.paths import ensure_directories
    ensure_directories()
    if args.setup:
        print("Project folders ready. Research pipeline is not implemented yet.")
        return
    for script in ("01_get_data.py", "02_build_dataset.py", "03_replicate.py"):
        subprocess.run([sys.executable, str(ROOT / "scripts" / script)], cwd=ROOT, check=True)

if __name__ == "__main__":
    main()
