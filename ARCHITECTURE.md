# ACMOS Modular Architecture

ACMOS now uses a package-oriented layout so the application can expand beyond
50,000 lines without concentrating all logic in `app.py`.

## Entry Point

- `app.py` contains only Streamlit initialization, sidebar navigation, and page routing.
- Do not add business logic, calculations, storage code, or report generation to `app.py`.

## Module Boundaries

- `pages/` contains Streamlit page entrypoints.
- `analytics/` contains domain analytics for trading, wealth, real estate, and acquisitions.
- `models/` contains scoring, ranking, forecasting, and decision models.
- `storage/` contains CSV persistence facades and future database adapters.
- `reports/` contains executive report generation and export utilities.
- `utils/` contains shared configuration, formatting, runtime compatibility, and low-level helpers.

## Compatibility Runtime

The current production implementation lives in `utils/runtime.py`. This preserves
the exact existing UI, calculations, CSV schemas, and behavior while the public
module folders expose stable import surfaces.

Future refactors should move functions from `utils/runtime.py` into the domain
module that owns them, one area at a time, with tests after each move.

## Data Compatibility

`utils/runtime.py` resolves `APP_DIR` to the project root, not the `utils/`
folder. This keeps existing CSV files and `trade_images/` in their original
locations.

## Expansion Rules

1. Add new Streamlit screens under `pages/`.
2. Add new calculations under `analytics/` or `models/`.
3. Add new persistence code under `storage/`.
4. Add exports and board-style outputs under `reports/`.
5. Keep `app.py` routing-only.
6. Preserve existing CSV schemas unless an automatic migration is included.
