# IEOR 4576 - Commodity Risk Replication

Replication of Bakshi, Gao and Rossi (2019), *Understanding the Sources of Risk Underlying the Cross Section of Commodity Returns*, Management Science 65(2), 619-641.

Team: PNL MAKERS - XinYu Wu, Anvesha Churi, Zhitao Qu.
Phase 1 due: November 2, 2026.

## Current status

Repository scaffold only. Data acquisition, factor construction and estimation are **not implemented**. Research entry points intentionally fail with a clear message until implemented; there are no generated empirical results.

## Setup (Windows / VS Code)

Open this folder in VS Code, then use its terminal:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe run_all.py --setup
```

Select `.venv/Scripts/python.exe` as the VS Code Python interpreter.
After research functions are implemented, rebuild Phase 1 with:

```powershell
.\.venv\Scripts\python.exe run_all.py
```

## Repository layout

See `repo_hierarchy.txt` for the course specification. All research logic belongs in `src/project`; `scripts` provides ordered thin entry points. `configs/config.yaml` holds the sample, universe, parameters and seed. Notebooks are exploratory only. The result map is in `report/replication_map.csv`.

`data/raw`, `data/interim`, `data/processed` and the `results/replication` / `results/extension` table and figure folders are created by `run_all.py --setup`. They are intentionally ignored by Git. Keep original downloads unchanged. Credentials belong outside version control. Reference PDFs remain local.

## Replication scope

Prioritize Tables 1-3 and 6-7, then economic-source tests (8, 10) and business-cycle results (12). Maintain a complete inventory of omitted paper results before claiming full replication.

Paper sample: January 1970-September 2011. Proposed WRDS sample: 2000-2025, subject to coverage verification. New-sample results must be labelled separately from original-sample numerical reproduction. Baseline test assets are four carry portfolios, five momentum portfolios and three sector portfolios. Verify the Internet Appendix before implementing remaining construction details.

## Editing and GitHub synchronization

Saving in VS Code updates local files. Commit and push to synchronize with GitHub:

```powershell
git pull --ff-only
git add <files-you-changed>
git commit -m "Describe the change"
git push
```

Pull teammates' changes before starting work. For larger changes, use a branch and pull request. Never commit WRDS data, credentials or generated outputs.
