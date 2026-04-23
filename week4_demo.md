# Week 4 Demo Runbook: Workflow and Project Management

This is a standard Markdown runbook for the Week 4 in-class demo.

## Overview

Use the ODOT crash geodatabase (same dataset used in [`week3_data_processing.ipynb`](https://usp510.github.io/week3_data_processing.ipynb)) to demonstrate a reproducible workflow in Antigravity.

Learning outcomes:

- scaffold a project in Antigravity
- use an isolated Python environment with [`uv`](https://docs.astral.sh/uv/)
- keep reusable logic in functions
- run a geodatabase pipeline script
- use [git](https://git-scm.com/) and [GitHub](https://github.com/) for version control
- keep sensitive/raw data out of Git with `.gitignore`
- commit and push project code to GitHub

## Demo Mode

Use Antigravity as the primary interface.

- Prefer GUI actions when possible: Explorer, Source Control, Command Palette, and integrated terminal.
- Use terminal only for commands that are naturally command-line tasks (`uv`, script execution, Git remote setup).

## Dataset

- Source file in this repo: `data/Statewide_Crashes_2023.gdb`
- Key layers used in this demo:
  - `crashes2023`
  - `crashes2023_VHCL`

## Prerequisites

- `uv` installed (`uv --version`)
- `git` installed (`git --version`)
- Antigravity installed and open
- GitHub account (or create one in Step 9)

## Step 1: Create Demo Project in Antigravity

In Antigravity:

1. Open this course repo folder.
2. In Explorer, create `demos/week4_workflow_demo`.
3. Inside it, create these folders:
   - `data/raw`
   - `data/processed`
   - `code/functions`
   - `outputs/tables`
   - `outputs/figures`

In integrated terminal (`Ctrl+``), run:

```bash
cd demos/week4_workflow_demo
ln -s ../../../data/Statewide_Crashes_2023.gdb data/raw/Statewide_Crashes_2023.gdb
```

## Step 2: Initialize Environment

Run in integrated terminal from `demos/week4_workflow_demo`:

```bash
uv init
uv add pandas geopandas pyogrio matplotlib jupyter
uv run python --version
uv pip list
```

## Step 3: Add `.gitignore` (Required)

In Antigravity Explorer, create `.gitignore` in `demos/week4_workflow_demo` with:

```gitignore
data/raw/
```

This prevents raw geodatabase files from being tracked.

## Step 4: Add Cleaning Function

Create `code/functions/cleaning.py`:

```python
import geopandas as gpd
import pandas as pd


def clean_crashes(gdf: gpd.GeoDataFrame, keep_portland_only: bool = False) -> gpd.GeoDataFrame:
    out = gdf.copy()

    if "CRASH_DT" in out.columns:
        out["CRASH_DT"] = pd.to_datetime(out["CRASH_DT"], errors="coerce", utc=True)

    if "CRASH_SVRTY_CD" in out.columns:
        out["CRASH_SVRTY_CD"] = pd.to_numeric(out["CRASH_SVRTY_CD"], errors="coerce")

    if "CRASH_ID" in out.columns:
        out = out.drop_duplicates(subset=["CRASH_ID"])

    if keep_portland_only and "CITY_SECT_NM" in out.columns:
        out = out[out["CITY_SECT_NM"].fillna("").str.upper().eq("PORTLAND")]

    return out
```

## Step 5: Add Pipeline Script

Create `code/01_gdb_cleaning.py`:

```python
from pathlib import Path

import geopandas as gpd
import pyogrio

from functions.cleaning import clean_crashes

GDB_PATH = Path("../data/raw/Statewide_Crashes_2023.gdb")
CRASH_LAYER = "crashes2023"
VEH_LAYER = "crashes2023_VHCL"

OUT_CSV = Path("../data/processed/crashes2023_clean.csv")
OUT_MONTHLY = Path("../outputs/tables/monthly_crashes.csv")


def main() -> None:
    layers = [name for name, _ in pyogrio.list_layers(GDB_PATH)]
    print(f"Available layers: {layers}")

    if CRASH_LAYER not in layers or VEH_LAYER not in layers:
        raise ValueError("Expected layers not found in geodatabase")

    crashes = gpd.read_file(GDB_PATH, layer=CRASH_LAYER)
    vehicles = gpd.read_file(GDB_PATH, layer=VEH_LAYER)

    crashes_clean = clean_crashes(crashes, keep_portland_only=False)

    veh_counts = vehicles.groupby("CRASH_ID").size().rename("VEH_ROWS")
    merged = crashes_clean.merge(veh_counts, on="CRASH_ID", how="left")
    merged["VEH_ROWS"] = merged["VEH_ROWS"].fillna(0).astype(int)

    keep_cols = [
        "CRASH_ID",
        "CRASH_DT",
        "CRASH_SVRTY_CD",
        "CITY_SECT_NM",
        "TOT_VHCL_CNT",
        "VEH_ROWS",
    ]
    keep_cols = [c for c in keep_cols if c in merged.columns]

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    merged[keep_cols].to_csv(OUT_CSV, index=False)

    monthly = (
        merged.assign(month=merged["CRASH_DT"].dt.month)
        .groupby("month", dropna=False)
        .agg(total_crashes=("CRASH_ID", "count"))
        .reset_index()
    )
    OUT_MONTHLY.parent.mkdir(parents=True, exist_ok=True)
    monthly.to_csv(OUT_MONTHLY, index=False)

    print(f"Crash rows in: {len(crashes):,}")
    print(f"Crash rows out: {len(merged):,}")
    print(f"Wrote: {OUT_CSV}")
    print(f"Wrote: {OUT_MONTHLY}")


if __name__ == "__main__":
    main()
```

## Step 6: Run Pipeline and Verify Outputs

Run in integrated terminal:

```bash
cd code
uv run python 01_gdb_cleaning.py
cd ..
ls -la data/processed
ls -la outputs/tables
head -n 5 data/processed/crashes2023_clean.csv
head -n 5 outputs/tables/monthly_crashes.csv
```

## Step 7: Add README

Create `README.md` in `demos/week4_workflow_demo`:

````md
# Week 4 Workflow Demo (ODOT Geodatabase)

## Data
- `data/raw/Statewide_Crashes_2023.gdb`

## Run
1. `uv sync`
2. `cd code`
3. `uv run python 01_gdb_cleaning.py`

## Outputs
- `data/processed/crashes2023_clean.csv`
- `outputs/tables/monthly_crashes.csv`
````

## Step 8: Commit with Antigravity Source Control (GUI)

In Antigravity Source Control panel:

1. Click `Initialize Repository` (if needed).
2. Stage all tracked files.
3. Enter commit message: `Scaffold geodatabase workflow demo`
4. Commit.

Optional second commit:

- Append notes to `README.md`.
- Stage only `README.md`.
- Commit message: `Add dataset note to README`.

## Step 9: Student Exercise - GitHub Account + Push Repo

Each student should complete all steps:

1. Create a GitHub account at <https://github.com/signup> (if they do not have one).
2. Create a new empty repository on GitHub named `week4-workflow-demo`.
3. In Antigravity Source Control, use `Publish Branch` if available.
4. If `Publish Branch` is unavailable, run in terminal:

```bash
git branch -M main
git remote add origin https://github.com/<github-username>/week4-workflow-demo.git
git push -u origin main
```

5. Verify on GitHub that files are pushed and `data/raw/` is not present.

## Deliverables for This Exercise

- Public or private GitHub repo with pushed commits
- `README.md` with run instructions
- `.gitignore` containing `data/raw/`
- Successful run of `code/01_gdb_cleaning.py`

## Optional Notebook Check

From `code/`:

```bash
uv run jupyter notebook
```

Validate Week 3 workflow by:

- listing layers with `pyogrio.list_layers(...)`
- loading `crashes2023` via `gpd.read_file(...)`
- comparing row counts and fields with script outputs

## Debrief Questions

1. Why list layers before reading geodatabase data?
2. Why keep cleaning logic in `code/functions/cleaning.py`?
3. Why should `data/raw/` be ignored by Git?
4. What validation checks should be added before Assignment 1 submission?

## Troubleshooting

- `ModuleNotFoundError: functions.cleaning`
  - Run script from `code/`.
- `Layer 'VHCL' could not be opened`
  - Use actual layer name `crashes2023_VHCL`.
- `uv: command not found`
  - Install uv and restart terminal.
- Push rejected or auth error
  - Confirm GitHub login in Antigravity, or use personal access token/SSH.
- Notebook uses wrong environment
  - Switch kernel to this project's `.venv`.
