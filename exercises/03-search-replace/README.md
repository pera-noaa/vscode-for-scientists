# Exercise 03 — Search and Replace at Scale

Goal: replace `grep -rn | xargs sed -i` with the workspace search panel.

You'll search across a small mixed-content tree containing Python, YAML, Markdown, and notebook-style files — like a real project. The patterns to find are realistic ones: deprecated function calls, stale paths, TODO comments, an old project codename.

## Files
- `old_paths.py` — has several hardcoded `/home/old_user/...` paths.
- `todo_list.py` — sprinkled with TODO/FIXME comments.
- `legacy_imports.py` — uses deprecated numpy aliases.
- `config.yaml` — has a project codename `phoenix-prototype` that needs renaming.
- `analysis/script_a.py` — also mentions `phoenix-prototype`.
- `analysis/script_b.py` — has its own TODOs.
- `docs/notes.md` — narrative reference to the old codename.

## Exercises

### 1. Plain text search across the workspace
- **Cmd+Shift+F** opens the workspace search panel.
- Search for: `TODO`
- Notice the result list groups by file, with line context.
- Click any result to jump to that line.

### 2. Regex search
- In the search panel, click the `.*` button to enable regex.
- Search for: `TODO|FIXME|XXX`
- Now you see all three flavors of "this needs fixing" markers.

### 3. Restrict by file type
- In the "files to include" box, type: `*.py`
- Notice docs/notes.md and config.yaml drop out of results.
- Try `*.{yaml,md}` to include only those two.

### 4. Exclude a folder
- In the "files to exclude" box, type: `analysis`
- The `analysis/` folder is now skipped.

### 5. Replace across files with preview
- Search for: `phoenix-prototype` (regex off).
- Click the down-arrow next to the search box to expand the replace field.
- Replace with: `aurora-v2`
- **Don't click "Replace All" yet.** Click into individual results — each shows a green/red diff preview.
- Untick any results you don't want.
- Then click "Replace All" — VSCode writes the changes to all included files at once.

### 6. Find a hardcoded path with regex
- Enable regex.
- Search for: `/home/old_user/[a-z_]+`
- See every hardcoded path that follows that pattern. Try a replace to `/work/${USER}/`.

### 7. Search by symbol type — bonus
- **Cmd+T** opens workspace-wide symbol search (functions, classes).
- Type a function name from one of the files; jump directly there.

## Try this without VSCode for comparison
```
grep -rn 'TODO\|FIXME\|XXX' exercises/03-search-replace/ --include='*.py'
```
Same result, no preview, no interactive untick, no in-place rename. VSCode's panel is the same `ripgrep` under the hood — it's just wrapped in a useful UI.

## Tips
- The search panel remembers your last query — Cmd+Shift+F twice often does what you want.
- For very large projects, add the heaviest folders to `search.exclude` in settings (the example `settings.example.json` excludes `__pycache__` etc. by default).
- "Files to include" supports globs like `**/*.f90` (recursive) or `src/*.py` (one level).
