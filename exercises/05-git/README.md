# Exercise 05 — Visual Hunk Staging

Goal: stop running `git add -p` blindly. Stage by clicking individual hunks (or even individual lines) in the diff gutter.

You'll work in a fresh tiny sub-repo with three dirty files. Each file has multiple hunks.

## Setup
From the workshop repo root, run:

```
bash exercises/05-git/setup.sh
```

This creates `exercises/05-git/exercise-repo/` — a small git repo with one committed baseline and three modified files containing multi-hunk changes.

Open the sub-repo: File → Open Folder → `exercises/05-git/exercise-repo/`.

(If you re-run the setup script, it wipes and recreates the sub-repo so you can redo the exercise from scratch.)

## Exercises

### 1. The Source Control panel
- **Cmd+Shift+G** opens the Source Control panel.
- You see "Changes" with three files listed: `calibration.py`, `README.md`, `config.yaml`.
- Click each file → the diff opens in the editor with red (removed) and green (added) gutters.

### 2. Stage a whole file
- Hover over `config.yaml` in the panel → the `+` button appears.
- Click `+`. The file moves up to "Staged Changes."
- You could `git commit` now and only that file would be in the commit.

### 3. Stage one hunk
- Unstage `config.yaml` (`-` button).
- Open `calibration.py` in the diff view.
- In the gutter to the left of each hunk, you see a small `…` icon. Hover over a hunk and click the `+` icon that appears.
- Only that hunk is staged. Look at the panel — you see the file in *both* "Changes" and "Staged Changes" with different content in each.

### 4. Stage a single line
- Right-click a green/red line in the diff view → "Stage Selected Range."
- Even more granular than hunks.

### 5. Commit only what's staged
- Type a commit message in the Source Control panel input.
- Cmd+Enter (or click ✓) to commit.
- Only staged changes go into the commit; everything else stays in your working tree.

### 6. Discard a hunk
- Find a hunk you don't want.
- In the gutter, click the curved arrow icon → "Revert Block."
- The hunk disappears from your working tree (careful — this is destructive).

### 7. View blame inline (GitLens)
- If you have GitLens installed, hover over any line → the commit/author/date appears in a popup.
- Press Opt+W (or Cmd+Shift+P → "GitLens: Toggle Line Blame") for a persistent inline blame annotation.

## Try this without VSCode for comparison
On the command line:
```
git add -p
```
You step through hunks interactively, typing `y/n/s/e/?`. Works, but with no syntax-highlighted preview and no way to see the bigger picture.

VSCode's panel is the same idea, with the diff visible while you choose.

## Tips
- Cmd+Shift+G then Cmd+Enter is the fastest "commit staged" path.
- The panel's commit message input supports the same Git config (signing, GPG) as the CLI — there's no separate VSCode-only commit machinery.
- If you accidentally stage too much, the `-` button on a staged file moves it back to "Changes" without losing the edits.
