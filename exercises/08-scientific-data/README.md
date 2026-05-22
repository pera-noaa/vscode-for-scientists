# Exercise 08 — Viewing Scientific Data

Goal: read CSV, netCDF, and HDF5 without leaving the editor or writing throwaway code.

## Setup
Install these extensions (in `extensions.txt`):
- **Rainbow CSV** — column-aware CSV viewer.
- **H5Web** — netCDF / HDF5 browser.
- **Data Wrangler** (optional) — Excel-like tabular viewer for CSV and pandas DataFrames.

## Files
- `calibration_data.csv` — one hour of synthetic per-channel calibration observations (timestamp, channel, raw, calibrated, flag).
- `generate_sample_nc.py` — small script that writes `sample.nc` for the netCDF viewer exercise. Run it to create the file.

## Exercises

### 1. CSV with Rainbow CSV
- Open `calibration_data.csv`.
- Columns are color-coded for visibility.
- Click in any cell; the column name and index show in the status bar.
- Run "CSVLint" from the command palette to validate the file structure.

### 2. CSV with Data Wrangler (optional, if installed)
- Right-click `calibration_data.csv` in the file tree → "Open in Data Wrangler."
- Excel-like view with filter, sort, summary statistics, and a "generate cleaning code" panel that writes pandas code for you.

### 3. Plot CSV inline with Rainbow CSV
- With the CSV open, right-click → "Rainbow CSV: Run RBQL Query."
- Try a SQL-like query: `SELECT a1, a3, a4 WHERE a2 = '1' LIMIT 20` (timestamp, raw, calibrated for channel 1).
- Results appear in a new tab.

### 4. Generate a netCDF and view it with H5Web
- Open the integrated terminal (Ctrl+\`).
- Run:
  ```
  python generate_sample_nc.py
  ```
  (Needs `numpy` and `xarray` — `pip install numpy xarray netcdf4` if missing.)
- `sample.nc` appears in the folder.
- Click `sample.nc` in the file tree → H5Web opens it as a tab.
- Browse the group hierarchy on the left.
- Click a variable → see metadata, attributes, and an inline plot or heatmap.
- Filter by dimension; export PNG.

### 5. The same for HDF5
- H5Web works the same way on `.h5` and `.hdf5` files. If you have any lying around on your HPC home dir, try one.

### 6. View a PNG over SSH
Scientists generate PNG plots constantly (matplotlib `savefig`). With VSCode + Remote-SSH, viewing them is one click:

- After running `generate_sample_nc.py` (with `matplotlib` available) you also have `sample_plot.png` in the folder.
- Click it in the file tree — VSCode renders the PNG in a tab.
- That's it. No more `scp run42/plot.png laptop:/tmp/` and switching to a viewer.
- It works the same for SVG (rendered inline) and PDF (via a PDF Preview extension).

This is the "I just dumped a figure on the HPC and want to glance at it" workflow, collapsed to a single click.

## When to use what
- **Rainbow CSV**: quick glance at structure, light filtering, sanity check that columns line up.
- **Data Wrangler**: serious data exploration (filter chains, summary stats, "show me the rows where X > Y"). Generates pandas code you can paste into a notebook.
- **H5Web**: anything netCDF / HDF5. Replaces `ncdump | less` and `ncview` for a quick visual check.
- **Notebook (exercise 05)**: when you need full numpy / xarray analysis and plotting in code.

## Tips
- For large CSV (millions of rows), Rainbow CSV may slow down. Use `csvlens` from the terminal as a fast alternative, or load into a notebook with pandas / polars.
- H5Web respects netCDF conventions — CF-compliant files render coordinate axes correctly.
- The Variables panel in a Jupyter notebook (exercise 05) is the same idea applied to in-memory data — `H5Web` for files, Variables panel for live objects.
