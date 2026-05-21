# Exercise 06 — Navigating Fortran

Goal: see that F12 / Shift+F12 / F2 / multi-cursor work for Fortran the same way they did for Python in exercise 01.

For TM5-scale codebases (hundreds of files, thousands of subroutines), this is the single biggest reason to use VSCode.

## Setup
- Install the **Modern Fortran** extension (`fortran-lang.linter-gfortran`). It's in `extensions.txt`.
- Make sure `gfortran` (or `ifx`/`ifort`) is on your PATH for the language server to do anything useful. (Most HPC nodes have gfortran; check with `which gfortran`.)

## Files
- `calibration_mod.f90` — module defining a derived type, a function, and a subroutine.
- `main.f90` — a `program` that uses the module.
- `Makefile` — `make` builds the executable.

## Exercises

### 1. Jump to definition
- Open `main.f90`.
- Put your cursor on `apply_calibration` in the loop body.
- Press **F12**. You land in `calibration_mod.f90` at the function definition.
- **Ctrl+-** (or **Opt+Cmd+Left**) jumps back.

### 2. Peek without leaving
- Same cursor position.
- **Opt+F12**. The definition appears in a popup; Esc to close.

### 3. Find all references
- In `calibration_mod.f90`, put your cursor on the function name `apply_calibration`.
- **Shift+F12**. The references panel shows every call site (including from `main.f90`).

### 4. Rename a procedure
- F2 on `calibration_summary`. Type a new name. Enter.
- The rename propagates from `calibration_mod.f90` to `main.f90` automatically.

### 5. Outline view
- Click the **Outline** section in the Explorer sidebar (Cmd+B if hidden).
- For `calibration_mod.f90`, you see the module, its derived type, and the procedures — clickable.

### 6. Build via integrated terminal
- Open the terminal (Ctrl+\`).
- Run:
  ```
  make
  ./calibration_demo
  ```
- The Problems panel (Cmd+Shift+M) collects any compiler warnings — clicking one jumps to the file and line.

### 7. Sticky scroll
- In a long Fortran file, the `module` / `subroutine` / `function` header stays pinned at the top of the viewport as you scroll past. Useful in 2000-line modules.

## TM5 / production codebases
The exercise files are tiny on purpose; the real value shows on a multi-thousand-file project like TM5. Try these after the workshop:

- F12 on a subroutine call buried in a deeply-nested module.
- Shift+F12 on a frequently-called helper — see every caller at a glance.
- Cmd+T to fuzzy-search across all subroutine names in the codebase.

## Tips
- The Modern Fortran extension uses the **fortls** language server. If F12 isn't working, check the Problems panel for "fortls not found" — install with `pip install fortls`.
- For codebases with custom build systems (TM5's pycasso), point fortls at the right include paths via `.vscode/settings.json`:
  ```json
  "fortran.fortls.includePaths": [
      "src",
      "include",
      "${workspaceFolder}/build/include"
  ]
  ```
- The extension also lints on save — if you see red squigglies, hover for the message.
