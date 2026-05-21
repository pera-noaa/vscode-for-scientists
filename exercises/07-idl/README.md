# Exercise 07 — Navigating IDL

Goal: same as exercises 01 and 06, but for IDL. Cross-procedure navigation, multi-cursor, rename — works the same once the IDL extension is installed.

## Setup
- Install the **IDL for VSCode** extension (`idl.idl-for-vscode`, by Harris Geospatial). It's in `extensions.txt`.
- IDL itself doesn't have to be installed to get syntax highlighting and basic navigation, but for the language server to do its full job (full type info), having an IDL install on PATH helps.

## Files
- `calibrate_value.pro` — function: linear calibration of a single value.
- `apply_calibration.pro` — procedure: vectorized calibration over an array.
- `calibration_summary.pro` — function: mean/min/max struct.
- `main.pro` — entry point that wires them together.

(One routine per file — the traditional IDL convention.)

## Exercises

### 1. Jump to definition
- Open `main.pro`.
- Cursor on `apply_calibration` (the procedure call).
- **F12** — lands in `apply_calibration.pro`.

### 2. Find references
- In `calibrate_value.pro`, cursor on the function name.
- **Shift+F12** — see every caller.

### 3. Multi-cursor on a variable name
- Open `apply_calibration.pro`.
- Cursor on a `slopes` reference.
- **Cmd+D** repeatedly to grab next occurrences.
- Rename to `slope_array` by typing once.

### 4. Cmd+P fuzzy file open
- Press **Cmd+P** and type `apply`. The .pro file appears.

### 5. Run IDL from the integrated terminal
- Ctrl+\` to open a terminal.
- `idl` to start the REPL (or `idl -e ".run main"` for one-shot execution).
- Edit-test-edit-test loops happen in the same window.

## Why this matters for the IDL → Python port story
A lot of lab work is mid-port from IDL to Python. VSCode helps both sides simultaneously:

- Open the IDL source on the left, the Python target on the right (drag a tab to split).
- F12 navigation works in both languages independently.
- Ask the AI ("/explain this IDL routine," then "rewrite in numpy") in the chat panel.
- Run both versions in two integrated terminals to compare outputs side-by-side.

## Tips
- The IDL extension respects the traditional one-routine-per-file convention; F12 jumps to the matching `.pro` file by name.
- If F12 doesn't work, check that the file name matches the procedure/function name (case-insensitive on most filesystems).
- For older codebases with multi-routine files, navigation may be flakier — the outline view still works.
- The IDLDE has features VSCode doesn't (variable browser tied to the running session, graphical debugger). For pure editing/navigation work, VSCode wins; for live IDL debugging sessions, keep the IDLDE next to it.
