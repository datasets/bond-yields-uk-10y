# Update Script Maintenance Report

Date: 2026-03-03

- Executed updater: `python scripts/bond_uk_flow.py`.
- Refreshed dataset outputs:
  - `data/annual.csv`
  - `data/quarterly.csv`
  - `datapackage.json`
- Added workflow write permission in `.github/workflows/actions.yml` (`permissions: contents: write`) for reliable scheduled push behavior.
