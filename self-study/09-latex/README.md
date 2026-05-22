# Exercise 09 — LaTeX with Live Preview

Goal: write a paper with the PDF preview rendering in real time, citations autocompleting, and forward/inverse search between source and PDF.

## Setup
- Install **LaTeX Workshop** (`james-yu.latex-workshop`). It's in `extensions.txt`.
- You need a TeX distribution on PATH. `tectonic` is the easiest (auto-fetches packages); TeX Live works too.
  - macOS: `brew install --cask mactex` (large) or `brew install tectonic` (small).
  - Linux: `apt install texlive-full` (big) or `cargo install tectonic`.
  - HPC: usually pre-installed; check `which latexmk` or `which tectonic`.

## Files
- `main.tex` — minimal paper skeleton (sections, equation, figure, citation).
- `refs.bib` — bibliography database with a couple of placeholder entries.
- `.latexmkrc` — build config so `latexmk` Just Works.

## Exercises

### 1. Open and build
- Open `main.tex`.
- LaTeX Workshop builds on save by default; you'll see the build status in the bottom bar.
- Or manually: Cmd+Shift+P → "LaTeX Workshop: Build LaTeX project."

### 2. Live PDF preview
- Cmd+Opt+V (or click the magnifying-glass icon top-right) → "View LaTeX PDF in VSCode tab."
- The PDF opens in a side tab. Drag the tab to split horizontally.
- Edit the source; on save, the PDF refreshes.

### 3. Forward search (source → PDF)
- Cursor on a line in `main.tex`.
- Cmd+Opt+J → the PDF tab highlights the corresponding location.

### 4. Inverse search (PDF → source)
- Ctrl+Click on any text in the PDF → jumps to that line in the source.

### 5. Citation autocomplete
- In `main.tex`, find the `\cite{}` command in the Introduction.
- Inside the braces, type `Anderson` — autocomplete pops up showing the BibTeX entry from `refs.bib`.
- Select with Enter.

### 6. Cross-reference autocomplete
- Add a `\ref{}` somewhere.
- Inside the braces, autocomplete suggests all labels defined in your document.

### 7. Spell check
- Install **Code Spell Checker** (`extensions.txt`).
- Misspelled words in prose (not code, not LaTeX commands) get blue squigglies.

### 8. Math snippets
- LaTeX Workshop has built-in snippets. Type `beg` then Tab — `\begin{}` skeleton appears.
- Type `frac` then Tab — `\frac{}{}` skeleton with cursor in the numerator first.

## When to use a real editor over Overleaf
- Local builds are faster on a big document.
- Git integration is real (Overleaf's is a paid feature).
- Your editor is the same one you use for code — same shortcuts, same theme.
- Offline.

When to use Overleaf:
- Sharing with non-technical co-authors.
- Avoiding the TeX installation entirely.
- Browser-only environments.

## Tips
- For very long documents, use the `\include{section1}` pattern and split into multiple files — F12 to jump between included files works the same as Python F12.
- Bind a key to "build" so you don't have to save to trigger it: Cmd+K Cmd+S → search "Build LaTeX project."
- The Outline panel shows your section structure — clickable navigation through `\section{}`, `\subsection{}`, etc.
