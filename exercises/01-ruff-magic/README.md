# Exercise 01 — The Magic Save

Goal: the "good defaults already exist" pitch, demonstrated in 30 seconds.

In this exercise you save a deliberately ugly Python file and watch **ruff** clean it up. You don't write a single character of code. You just press Cmd+S.

This is the workshop's hook moment — most people who watch this happen want it on their own machine before the next break.

## Setup
- Install the **ruff** extension (`charliermarsh.ruff`). It's in [`extensions.txt`](../../extensions.txt).
- You do **not** need to install ruff itself separately — the extension ships a bundled binary that just works.
- This exercise folder has a `.vscode/settings.json` that enables `formatOnSave` and ruff's "fix all" + "organize imports" code actions automatically when you open the folder.

## Exercise

### 1. Open `messy.py`
Look at it for ten seconds. Notice:

- Unsorted imports; some are unused.
- Mixed quote styles (`'a'` and `"a"`).
- Spurious whitespace inside parens and around operators.
- Deprecated numpy aliases (`np.bool`, `np.int`).
- `if path == None` (should be `is None`).
- A `return None` jammed onto the same line as the `if`.
- Trailing whitespace, extra blank lines.

### 2. Save it.
**Cmd+S**. That's the whole exercise.

### 3. Watch what changed.
- `import os` and `import sys` are gone — they were unused.
- `from collections import OrderedDict` *stayed* — it's actually used down below.
- Imports sorted and grouped (third-party then standard-library, by ruff's isort config).
- `path == None` → `path is None`.
- `np.bool` → `np.bool_`, `np.int` → `np.int_` (numpy 2 compatibility).
- Quotes normalized to double.
- Whitespace and indentation cleaned up everywhere.
- The `if … : return None` is on its own line.
- Trailing whitespace gone, extra blank lines collapsed.

You didn't touch the code. You saved the file.

### 4. (Optional) Try to break it.
Add some bad code at the bottom — extra spaces, deprecated aliases, `== None`, anything. Save again. Watch it clean up.

### 5. (Optional) A/B compare
- **Cmd+Z** reverts the save's changes (it's a single undoable transaction).
- **Cmd+Shift+Z** redoes.
- Flip back and forth to see the diff.

## What just happened
Three things working together:

1. **`editor.formatOnSave: true`** — VSCode runs the file's formatter on save.
2. **`"editor.defaultFormatter": "charliermarsh.ruff"`** — ruff is registered as the Python formatter.
3. **`"source.fixAll.ruff"` and `"source.organizeImports.ruff"` as code actions on save** — ruff also runs its linter's autofix rules.

The config that makes this work is two files:

- `.vscode/settings.json` (workspace settings — committed in this folder).
- `pyproject.toml` (ruff's rule selection — committed in this folder).

To use this in your own projects, copy both files into your project root.

## Why this matters
This is the "good defaults already exist" pitch made concrete. With formatter + linter + format-on-save wired up once, you stop:

- Writing whitespace and indentation manually
- Sorting imports
- Fixing `== None` vs `is None`
- Tracking deprecated numpy aliases
- Normalizing quote styles

…and you just write the interesting parts. The editor catches the rest.

## Equivalents in other languages
The same pattern exists for everything in this workshop:

- **Fortran**: `fprettify` via the Modern Fortran extension.
- **JSON / YAML / Markdown**: `prettier` extension.
- **LaTeX**: `latexindent` via LaTeX Workshop.
- **Shell**: `shfmt`.

Each has the same shape: a CLI tool you can also run from the command line, wrapped in an extension that runs it for you on save.
