# Exercise 02 — Code Navigation

Goal: replace `grep -r` + manual file-jumping with F12 and Shift+F12.

You'll work with a tiny three-file Python package that simulates an instrument-calibration workflow. The files reference each other across the package.

## Files
- `data_loader.py` — defines `load_raw_data()` and `parse_timestamp()`.
- `calibration.py` — defines `apply_calibration()`, which calls `load_raw_data()`.
- `main.py` — entry point that calls `apply_calibration()` and `parse_timestamp()`.

## Exercises

### 1. Jump to definition (F12)
- Open `main.py`.
- Find the call to `apply_calibration` inside `main()` (near the bottom of the file). Put your cursor on the name.
- Press **F12**. You land in `calibration.py`.
- Press **Ctrl+-** (or **Opt+Cmd+Left** on macOS) to jump back to `main.py`.

### 2. Peek definition (Opt+F12)
- Same cursor position as above.
- Press **Opt+F12**. You see the definition in a popup without leaving `main.py`. Esc to close.

### 3. Find all references (Shift+F12)
- Open `calibration.py`.
- Put your cursor on the name `load_raw_data` (in the import or in the function body).
- Press **Shift+F12**. The references panel shows every place that name appears across the package.
- Click a reference to jump.

### 4. Rename across files (F2)
- Open `data_loader.py`.
- Put your cursor on the function name `load_raw_data`.
- Press **F2**, type `load_raw_observations`, hit Enter.
- VSCode renames it here AND in `calibration.py` AND in `main.py` simultaneously.
- Open `main.py` and verify — no manual editing needed.

(If F2 doesn't work, make sure you have the Python extension installed and the Python interpreter is selected — bottom-right status bar.)

### 5. Multi-cursor with Cmd+D
- Open `calibration.py`.
- Put your cursor on any occurrence of the variable `coeff`.
- Press **Cmd+D** repeatedly to add the next occurrence to your selection.
- Type a new name — it replaces all selected occurrences at once.

### 6. Jump to symbol within a file (Cmd+Shift+O)
- Open `calibration.py`.
- Press **Cmd+Shift+O** — get a fuzzy-searchable list of functions/classes in this file.
- Type `apply` and Enter — jump directly to `apply_calibration`.

### 7. Fuzzy file open (Cmd+P)
- Press **Cmd+P**.
- Type `load` — `data_loader.py` is suggested. Enter to open it.

## Try this without VSCode for comparison
On the command line:
```
grep -rn 'load_raw_data' exercises/02-navigation/
```
That's the slow path. F12 / Shift+F12 do the same thing without leaving the editor.

## When this breaks
Navigation depends on the Python language server (Pylance, or Pyright on OOD). If F12 does nothing:
- Check bottom-right status bar: a Python interpreter must be selected.
- If you see "Loading…" in the status bar, wait — Pylance is still indexing.
- For Fortran navigation, the same shortcuts work via the Modern Fortran extension (see `self-study/03-fortran/`).
