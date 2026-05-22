# Exercise 08 — Viewing Scientific Data

Goal: load → inspect → visualize scientific data without leaving the editor or writing throwaway code. The full loop — raw CSV, structured netCDF, and the rendered plot — happens inside one VSCode window, on the HPC.

## Setup
Install these extensions (in `extensions.txt`):
- **Rainbow CSV** — column-aware CSV viewer.
- **H5Web** — netCDF / HDF5 browser.
- **Data Wrangler** (optional) — Excel-like tabular viewer for CSV and pandas DataFrames.

## Files
- `calibration_data.csv` — one hour of synthetic per-channel calibration observations (timestamp, channel, raw, calibrated, flag).
- `generate_sample_nc.py` — script that writes BOTH `sample.nc` (the data) and `sample_plot.png` (a histogram of the same data) when you run it.

## Exercises

### 1. CSV with Rainbow CSV
- Open `calibration_data.csv`.
- Columns are color-coded for visibility.
- Click in any cell; the column name and index show in the status bar.
- Run "CSVLint" from the command palette to validate the file structure.

### 2. CSV with Data Wrangler (optional, if installed)
- Right-click `calibration_data.csv` in the file tree → "Open in Data Wrangler."
- Excel-like view with filter, sort, summary statistics, and a "generate cleaning code" panel that writes pandas code for you.

### 3. Query the CSV with Rainbow CSV's RBQL
- With the CSV open, right-click → "Rainbow CSV: Run RBQL Query."
- Try a SQL-like query: `SELECT a1, a3, a4 WHERE a2 = '1' LIMIT 20` (timestamp, raw, calibrated for channel 1).
- Results appear in a new tab.

### 4. Generate a netCDF and its visualization
- Open the integrated terminal (Ctrl+\`).
- Run:
  ```
  python generate_sample_nc.py
  ```
  (Needs `numpy`, `xarray`, `netcdf4`, and `matplotlib` — `pip install` if missing.)
- Two files appear in the folder:
  - `sample.nc` — a CF-compliant netCDF with raw + calibrated observations, coordinates, attributes, and quality flags.
  - `sample_plot.png` — histograms of the same data, raw vs calibrated, per channel.

### 5. Browse the netCDF structure with H5Web
- Click `sample.nc` in the file tree → H5Web opens it as a tab.
- Browse the group hierarchy on the left: variables, dimensions, attributes.
- Click a variable → see its metadata and an inline plot or heatmap.
- Filter by dimension; export PNG.

### 6. View the plot of that same data
- Click `sample_plot.png` in the file tree → it renders in a tab.
- This is the *same data* you just browsed in H5Web, plotted as histograms. The whole load-inspect-visualize loop happened in one window, on the HPC.
- Replaces the `scp /work/plots/run42.png laptop:/tmp/` workflow — the file lives on the cluster and you just look at it.
- Works the same for **SVG** (rendered inline) and **PDF** (via a PDF Preview extension).

### 7. Bonus: HDF5 and other formats
- H5Web also works on `.h5` and `.hdf5` files. If you have any lying around on your HPC home dir, try one.
- The PNG / SVG / PDF viewing applies to any plot or figure file your scripts dump.

## When to use what
- **Rainbow CSV**: quick glance at structure, light filtering, sanity check that columns line up.
- **Data Wrangler**: serious data exploration (filter chains, summary stats, "show me the rows where X > Y"). Generates pandas code you can paste into a notebook.
- **H5Web**: anything netCDF / HDF5. Replaces `ncdump | less` and `ncview` for a quick visual check.
- **Built-in image viewer**: click any `.png`, `.svg`, `.jpg`, `.gif` and it renders. PDF needs an extension. Replaces "scp to laptop then open."
- **Notebook (exercise 05)**: when you need full numpy / xarray analysis and plotting in code.

## Tips
- For large CSV (millions of rows), Rainbow CSV may slow down. Use `csvlens` from the terminal as a fast alternative, or load into a notebook with pandas / polars.
- H5Web respects netCDF conventions — CF-compliant files render coordinate axes correctly.
- The Variables panel in a Jupyter notebook (exercise 05) is the same idea applied to in-memory data — `H5Web` for files, Variables panel for live objects.
