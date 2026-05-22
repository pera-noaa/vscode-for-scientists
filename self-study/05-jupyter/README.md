# Exercise 05 — Jupyter Notebooks in VSCode

Goal: use a notebook like you would in JupyterLab, but get the bonus features (variable explorer, sane git diffs, cell-by-cell debugging) that VSCode adds.

## Setup
- Make sure the **Jupyter** extension is installed (it ships in the Python pack).
- Open `calibration.ipynb`.
- Top-right of the notebook: click "Select Kernel" → pick a Python interpreter with `numpy` and `matplotlib` available. (Any reasonable scientific Python env works.)

If you don't have numpy/matplotlib locally:
```
pip install numpy matplotlib
```
…or use a conda env that already has them.

## Exercises

### 1. Run cells
- Click on the first code cell. **Shift+Enter** runs it and advances to the next.
- **Ctrl+Enter** runs the cell and stays put.
- Notice the cell input/output area updates in place — no scrolling lost.

### 2. The variable explorer
- After running cells, click the **"Variables"** button at the top of the notebook (or "Jupyter: Show Variable View" from the command palette).
- A panel appears showing every variable in scope, its type, shape, and a preview.
- For numpy arrays, you see shape and dtype without typing `arr.shape`.
- Double-click a variable for a tabular view.

### 3. Cell-level git diff
- Modify a code cell. Save (Cmd+S).
- Open the Source Control panel. The notebook appears with a *cell-aware* diff — you see which cell changed and what changed in it. No giant JSON blob.

### 4. Inline plots
- Run the cell that calls `plt.plot(...)`. The figure renders directly under the cell.
- Right-click the figure → "Save Image As…" if you want a PNG.

### 5. The data viewer
- After running, double-click a numpy array in the Variables panel. A spreadsheet-style viewer opens. Filter and sort columns interactively.

### 6. Convert to script-style
- Cmd+Shift+P → "Jupyter: Convert to Python Script."
- The notebook is exported as a `.py` file with `# %%` cell markers.
- That `.py` file is fully runnable as a script AND can still be executed cell-by-cell in VSCode. Great for code you want to version-control diffably.

### 7. Connect to a remote kernel
- Cmd+Shift+P → "Jupyter: Specify Local or Remote Jupyter Server for Connections."
- Paste a URL like `http://hpc-node:8888/?token=…` from a Jupyter server running on the HPC.
- Your notebook now executes on the cluster while you edit on your laptop.
- (When running through VSCode Remote-SSH, the kernel is already on the cluster — this is for the case where you want a different topology.)

## Tips
- `Esc` enters command mode (blue cell border); `Enter` re-enters edit mode.
- `A` / `B` (command mode) insert a cell above / below.
- `D D` deletes a cell.
- `M` / `Y` toggle between Markdown / code.
- Cell tags (like `parameters` for papermill) are supported via the cell metadata editor.

## Why this beats classic Jupyter
- Variable explorer with array shape/dtype at a glance.
- Diffable git history (per-cell changes, not opaque JSON).
- Same editor for the notebook *and* the imported `.py` files — F12 navigation works across both.
- Debugger works on notebook cells (click in the gutter to set a breakpoint, run cell with debugger).
- LSP autocomplete in cells (Pylance type-checks while you write).
