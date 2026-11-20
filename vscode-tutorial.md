# VSCode for Scientists — Tutorial Outline

Things to show off when converting an emacs + PuTTY crowd. Roughly in order of how much each will move the needle for an HPC-using lab that does Fortran, IDL, legacy Python, and instrument calibration work.

## Getting started — the 5-step setup
Before showing any feature, give attendees the on-ramp:

1. Install VSCode (or VSCodium for the open-source-only crowd).
2. Install the **Remote-SSH** extension from the marketplace.
3. Add nimbus to `~/.ssh/config` with `HostName`, `User`, and any Duo / jump-host config.
4. Click the green corner button → "Connect to Host" → pick the host. VSCode installs a server-side helper into `~/.vscode-server/` automatically.
5. Open a folder on the remote, then install the **recommended extensions** (Python, Modern Fortran, IDL, GitLens, etc. — full list at the end).

Everything below assumes they're past this point.

> **MSU Orion / Hercules users:** these clusters explicitly forbid Remote-SSH. Skip steps 2–4 and see the **MSU Orion / Hercules** section below for the OpenOnDemand path.

## MSU Orion / Hercules — use OpenOnDemand, not Remote-SSH
MSU's HPC clusters explicitly forbid the Remote-SSH workflow — it spawns persistent VSCode server processes that violate cluster policy. Remote Tunnels is out for the same reason. Use **OpenOnDemand** instead:

1. Browse to **https://orion-ood.hpc.msstate.edu** (or the Hercules equivalent).
2. Log in with your MSU HPC credentials.
3. Launch the **Code Server** interactive app — pick a partition, walltime, and resources, submit.
4. When the job starts, click "Connect" to open browser-based VSCode running on a compute node.

What you get vs Remote-SSH:
- Same editor, terminal, git, debugging, notebooks.
- Files live on the cluster filesystem — no sync overhead.
- Persistent across browser sessions; the job runs to its walltime.
- Real resource limits via SLURM; no risk of getting flagged for hogging a login node.

What's different:
- The extension marketplace is **Open VSX**, not Microsoft's. ~95% of extensions exist on both, but a few Microsoft-proprietary ones don't — notably **Pylance** (use **Pyright**, the open-source core, instead) and the Remote-* extensions (moot here since you're already on the cluster). Check AI assistants before assuming they'll install.
- Settings Sync via GitHub still works.
- Keybindings, themes, snippets, tasks — all work normally.

Bonus: OpenOnDemand also has Jupyter, RStudio, MATLAB, and a file browser as separate apps. Pick whichever fits the task.

## The command palette — the only shortcut they need to remember
`Cmd+Shift+P` (or `Ctrl+Shift+P` on Linux) opens a searchable list of *every* command, menu item, and setting in VSCode. This is the `M-x` analog and resonates strongly with the emacs crowd.

- Don't bother memorizing keybindings. Type the verb: "format", "rename", "compare", "git stash", "wrap", "fold", "reload".
- Settings, themes, keybindings, extensions — all reachable from here.

Sell this as: "If you can describe it, you can find it."

## Replacing PuTTY in one shot
- **Remote-SSH** keeps a persistent VSCode server on the HPC node, so opening 50 files is fast.
- **Integrated terminals**: edit a Fortran file and run `squeue` / `tail -f run.log` / `sbatch` in a panel below, all on the same SSH session. No alt-tabbing, no PuTTY window juggling.
- `code <file>` and `code --diff a b` from the integrated terminal pop files into the editor.
- **Tasks** (`.vscode/tasks.json`): bind `sbatch run.slurm` to a keystroke.
- **Remote Tunnels**: when SSH ports are blocked (conference wifi, restrictive firewalls), connect via a GitHub-auth tunnel.

## Code navigation (huge for Fortran, IDL, and legacy Python)
- **F12 / Cmd-click** to jump to a definition; **Alt+Left** to jump back. Works on remote files.
- **Shift+F12** finds all references — every caller of a routine.
- **Outline panel + breadcrumb bar** for navigation inside multi-thousand-line files.
- **Cmd+P** fuzzy file open, **Cmd+T** fuzzy symbol search across the workspace.
- **Sticky scroll** pins function / subroutine headers as you scroll past them.

## Search / replace at scale
- **Cmd+Shift+F** runs ripgrep across the workspace with regex + include/exclude globs, then a preview pane where you untick individual matches before applying. Obsoletes `grep -r … | xargs sed`.

## Editing tricks that look like magic
- **Multi-cursor**: Cmd+D adds next occurrence, Alt+click adds cursors anywhere — rename a variable in 20 spots in 5 seconds.
- **Cmd+Shift+L** selects all occurrences at once.
- **F2** = rename symbol, refactor-aware, propagates across files (Python via Pylance, Fortran via Modern Fortran).
- **Format-on-save** with Black / Ruff (Python), fprettify (Fortran), Prettier (JSON / YAML / web). Cleans up commits automatically.
- **EditorConfig**: a `.editorconfig` file in the repo root enforces team-wide formatting rules (tabs vs spaces, line endings, trailing whitespace).

## Git integration
- **Inline blame** (GitLens extension): hover any line, see commit / author / date.
- **Stage individual hunks** (or single lines) by clicking the diff gutter — most emacs users don't do this and it changes how they commit.
- **3-way merge conflict UI.**
- Visual log + branch graph; compare any two files / branches / commits via `Cmd+Shift+P → diff`.
- **GitHub Pull Requests** extension: review PRs inside the editor — see the diff, comment on lines, approve / request changes. Replaces the github.com tab.

## AI assistance — honest version
The lab pays for **Gemini Code Assist** (VSCode extension). It's helpful for boilerplate, inline comments, and simple completions, but the quality gap vs Copilot / Claude is real — don't oversell it.

Upgrade paths to mention:
- **GitHub Copilot Free** (since late 2024) is available to anyone with a GitHub account — 2000 completions and 50 chat messages per month. Zero-friction supplement to Gemini; worth turning on for everyone.
- **GitHub Copilot full (unlimited)** is free for verified students, teachers, and open-source maintainers. **The CIRES half of the lab qualifies through CU Boulder** — sign up at education.github.com with your `colorado.edu` email and an affiliation document. The NOAA half can fall back to Copilot Free or bring-your-own-key.
- **Continue.dev** or **Cline** are open-source VSCode extensions that let you plug in your own Anthropic / OpenAI / local API key for chat + autocomplete. Pay-per-token, no subscription. Useful for the NOAA half, or anyone who wants Claude-quality completions on top of whatever they already have.
- Even mediocre LLM autocomplete beats no LLM. For undocumented legacy code, "/explain this subroutine" with Gemini is still faster than reading 400 lines by hand.

## Debugging
- Click the gutter to set a breakpoint, **F5** to run, step through with a variable inspector. Built in for Python; Fortran via Modern Fortran + a debugger backend.
- Most scientists print-debug forever — this is a genuine upgrade.

## Python — daily workflow
- **Environment switcher**: status bar shows the active interpreter; click to pick between conda envs / venvs / poetry / system. Each project remembers its own.
- **Test integration**: pytest discovery, gutter run/debug buttons, results panel. Replaces "ssh in, activate env, run pytest, scroll output."
- **Refactoring**: F2 rename, extract method, organize imports.
- **Coverage gutters** (extension): see line-by-line which lines your tests hit.

## Working with legacy Python scripts
For the "I have a folder of 2014 scripts I'm afraid to touch" crowd:

- **Pylance** type-checks untyped legacy code on the fly — surfaces undefined names, unreachable code, wrong-arity calls, type mismatches.
- **F2 rename** + **extract function** make refactoring safe.
- **Side-by-side diff** for before/after refactor sanity checks.
- **Debugger** to actually understand what the script does (set a breakpoint, run it, inspect the world).
- AI assistance (limited as it is) is genuinely useful for "add docstrings to this 400-line script" or "modernize this Python 2 print statement."

## Working with IDL
A lot of lab work lives in IDL or is mid-port to Python. VSCode helps both sides:

- **IDL for VSCode** extension (Harris Geospatial) gives syntax highlighting, problem detection, navigation, and outline view for `.pro` files.
- All the multi-cursor / search / refactoring tricks apply to IDL just as much as Python.
- For IDL → Python ports, open both files side-by-side in a split editor; use Copilot / Gemini to draft the translation, then debug interactively.
- IDL itself runs from the integrated terminal — no separate IDLDE window needed.

## Jupyter notebooks — the underrated parts
- **Variable explorer pane**: shape / dtype for arrays without `print(x.shape)`.
- **Cell-by-cell git diffs** (the most painful notebook problem, solved).
- **`# %%` cell markers** — keep code in .py files but execute as notebooks; great for diffable code that's still REPL-friendly.
- Inline plots, including interactive (Plotly, ipywidgets).
- Direct support for connecting to a remote Jupyter kernel.

## Scientific data viewers — great for calibration and instrument work
The "load raw instrument data → apply coefficients → plot → diff against reference" loop lives entirely in one window with these:

- **H5Web** extension: native viewer for netCDF / HDF5. Browse groups, plot variables, inspect attributes — no `ncdump | less`.
- **Rainbow CSV** + **Data Wrangler**: tabular view, filtering, summary stats for CSV / TSV calibration files.
- Built-in PNG / SVG / PDF preview — when your script dumps a plot to disk and you just want to glance.
- Combined with the notebook variable explorer, the whole calibration runbook (raw → calibrated → reference comparison) is one window.

## LaTeX / paper writing
- **LaTeX Workshop** extension: live PDF preview, BibTeX citation autocomplete, forward/inverse search (Ctrl+click in the PDF jumps to the source line), build-on-save.
- Spell check for prose via **Code Spell Checker** (also catches typos in code comments).
- Math, Mermaid, PlantUML all render in Markdown preview too — useful for project notes and slide source.

## Multi-root workspaces + split editors
- One window can hold analysis repo + simulation source + plots-output folder side-by-side.
- Drag a tab to the edge of the editor to split horizontally or vertically. Up to four splits.
- **Pin tabs** you don't want to lose to MRU eviction.
- `.code-workspace` files capture this layout (which folders are open + settings) so you can share it with collaborators.

## Markdown extras
- KaTeX math, Mermaid diagrams, PlantUML — all render in preview.
- Auto-generated table of contents.
- Drag-drop images into a Markdown file → it inserts the link.
- Good for README, group wiki, lab notebook entries.

## Snippets / templates
- Define a Fortran subroutine skeleton, an IDL procedure template, a matplotlib figure boilerplate, a SLURM batch script once; reuse with three keystrokes.
- Per-language and per-project snippets, all version-controllable.

## Customization — preempt the "but my emacs" objection
- **Awesome Emacs Keymap** preserves muscle memory; **VSCodeVim** for the vim minority.
- Per-project `.vscode/settings.json` — Python interpreter, formatter, linter per project, version-controlled.
- **Settings Sync** via GitHub — same config on laptop and HPC.
- **Profiles**: lightweight Fortran profile vs heavy Python / ML profile, switchable.
- **Workspace Trust** prompt the first time you open an unknown repo — sandbox mode disables auto-running extensions until you opt in.

## Things that just look impressive in a demo
- Drag a file from Finder into the file tree → uploads to HPC.
- Markdown preview side-by-side with KaTeX-rendered math.
- Format-on-save turning ugly indentation into clean code as they save.
- **Live Share**: start a session, send a link, a colleague edits the same file with their own cursor visible.
- Press `.` on any GitHub repo page → opens the entire repo in browser-based VSCode (**github.dev**) with no checkout. Quick code review anywhere.

## Dev Containers (the reproducibility pitch)
- Define an environment in `devcontainer.json` (base image + extensions + post-create script); VSCode builds the container and attaches.
- One-line "this is the analysis environment for paper X" — works the same on anyone's laptop.
- Fits scientific computing culture: reproducibility, version-pinned environments, shareable.

## Suggested demo flow (the sequence that wins converts)
Open one of *their own* files on Orion via Remote-SSH and run this sequence in under three minutes:

1. F12 jump into a subroutine.
2. Shift+F12 to see every caller.
3. Multi-cursor rename a variable.
4. Stage a single hunk visually in the Source Control panel.
5. Ask the AI to add docstrings to the function (with the honest caveat that Gemini is fine for this, less impressive for big refactors).

That sequence on code they recognize does more persuasion than any feature list.

## Anticipated pushback
- *"It's a Microsoft product"* → MIT-licensed; VSCodium is the de-Microsoft'd build.
- *"It's bloated"* → modern hardware handles it fine; per-workspace extension lists keep it light.
- *"I'll lose my .emacs"* → keymap extension + the customization story above.
- *"Our AI is bad"* → true; the editor is still worth it for the non-AI features, and the bring-your-own-key path exists.
- *"My IDL workflow is already fine in the IDLDE"* → fair, but the navigation, multi-cursor, git, and side-by-side-with-Python story still applies.

## Useful extensions to mention
- **Remote-SSH**, **Remote Tunnels** (built-in)
- **Modern Fortran** — syntax, navigation, linting for F90 / 2003 / 2018
- **IDL for VSCode** (Harris Geospatial)
- **Python** + **Pylance** — type-aware autocomplete and refactoring
- **Jupyter** — notebook + variable explorer
- **H5Web** — netCDF / HDF5 viewer
- **Rainbow CSV**, **Data Wrangler** — tabular data
- **LaTeX Workshop**
- **GitLens** — inline blame, history
- **GitHub Pull Requests**
- **Awesome Emacs Keymap** (or **VSCodeVim**)
- **Gemini Code Assist** (lab default) / **Continue.dev** (bring-your-own-key)
- **TODO Tree** — surfaces TODO / FIXME across the repo
- **Code Spell Checker** — for prose in comments and docs
- **EditorConfig**
- **Path Intellisense** — autocompletes filenames in strings

## Adjacent tools worth integrating
Things that live outside VSCode but pair with it. Most are CLI tools or libraries; many have a matching VSCode extension but the value is the underlying tool. Pick aggressively — the lab probably has lots of "I write 2014-style Python in 2026" friction this list addresses.

### Python — linting / formatting / type checking
- **ruff** — fast all-in-one linter + formatter (subsumes flake8, black, isort, pyupgrade, pydocstyle, …). Astral. Single biggest Python-quality upgrade if they're not already using it.
- **mypy** — static type checker.
- **Pylance / pyright** — Microsoft's type checker; ships with the VSCode Python extension.
- **pre-commit** — git hook framework that runs ruff / mypy / typos / etc. on every commit. Set-and-forget code quality.
- **bandit** — security-focused linter (insecure crypto, shell injection, hardcoded passwords).
- **vulture** — finds dead code; great for cleaning legacy scripts.

### Python — environments and packages
- **uv** — fast `pip` + `venv` replacement (10–100× faster). Astral. Arguably the biggest day-to-day Python workflow upgrade in 2026.
- **pixi** — conda-compatible env manager with lockfiles. Good for scientific stacks with binary deps.
- **poetry**, **pdm** — dependency + packaging tools.
- **conda-lock** — lockfiles for conda envs (reproducibility).
- **direnv** — auto-activate envs on `cd` into a project dir.

### Python — testing and profiling
- **pytest** — testing standard.
- **pytest-cov** — coverage.
- **hypothesis** — property-based testing; great for catching edge cases in numerical code.
- **nox** / **tox** — run tests across Python versions and envs.
- **py-spy** — sampling profiler; no code changes needed, attaches to running processes (including remote ones).
- **memray** — memory profiler with flame graphs.
- **scalene** — CPU + memory + GPU + line-level profiling, in one tool.
- **line_profiler** — line-by-line CPU.
- **snakeviz** — interactive viewer for cProfile output.
- **hyperfine** — benchmarking CLI (`hyperfine 'cmd1' 'cmd2'` to compare).

### Python — interactive / debugging
- **IPython** — better REPL; auto-import, magic commands, easy plotting.
- **icecream** (`ic`) — print-debugging that shows variable name and value (`ic(x)` → `ic| x: 42`).
- **rich** — pretty console output, tracebacks, tables, progress bars.

### Python — scientific stack worth flagging
- **xarray** — labeled n-d arrays; natural fit for netCDF.
- **dask** — parallel arrays / dataframes; scale numpy / pandas to HPC.
- **polars** — fast DataFrame library, pandas alternative.
- **numba** — JIT compiler for numpy code; near-Fortran speed with one decorator.
- **cython** — C extensions from Python-like syntax.
- **f2py** (ships with numpy) — call Fortran from Python directly. Useful for IDL/Fortran → Python ports.
- **meson-python** — modern build for Python packages with native code.

### Fortran tools
- **fortls** — Fortran language server (powers Modern Fortran extension; also works in vim / emacs).
- **fprettify** — auto-formatter.
- **fpm** (Fortran Package Manager) — package management, still maturing but usable.
- **stdlib** — community standard library (sorting, strings, statistics).
- **FORD** — documentation generator that reads Fortran source comments.
- **flang** — LLVM-based Fortran compiler; alternative to gfortran / ifx.

### Build and project
- **CMake** + **Ninja** — modern build pipeline; faster than `make`.
- **Meson** — alternative build system (Python-style config).
- **just** — modern task runner; `justfile` replaces a Makefile for command shortcuts.
- **entr** / **watchexec** — re-run commands when files change.

### Git supporting tools
- **gh** (GitHub CLI) — PRs, issues, releases, repo creation from the terminal.
- **lazygit** — TUI git client; staging hunks, branching, rebasing without memorizing git commands.
- **git-delta** — pretty syntax-highlighted diffs; drop-in replacement for `git diff` output.
- **difftastic** — syntactic, language-aware diff. Hides whitespace and formatting changes, shows actual logic changes. Game-changer for refactors.
- **git-lfs** — large file storage for binaries.
- **dvc** — data version control; for big scientific datasets that don't belong in git.

### Scientific data — command line
- **CDO** (Climate Data Operators) — bread-and-butter netCDF: regrid, average, subset, time-mean.
- **NCO** (NetCDF Operators) — `ncks`, `ncdiff`, `ncwa`, `ncatted` etc. for fine-grained netCDF ops.
- **ncview** — quick netCDF browser.
- **Panoply** (NASA) — GUI netCDF / HDF / GRIB plotter.
- **ParaView** — large-scale 3D visualization.
- **ImageMagick** — image processing CLI (convert, montage, crop).
- **ffmpeg** — frame sequences → movies for animations.
- **jq** — JSON query language; essential for scripting against APIs.
- **yq** — YAML version of jq.

### Shell and terminal upgrades
For people who live in PuTTY, swapping in modern terminal tools is often a bigger quality-of-life win than the editor itself:

- **tmux** (or **zellij**) — terminal multiplexer; persistent sessions that survive SSH disconnects.
- **mosh** — UDP-based shell; survives wifi drops, faster over slow links than ssh.
- **fzf** — fuzzy finder: `Ctrl+R` history search, file picker, generic interactive filter.
- **ripgrep** (`rg`) — fast grep (VSCode uses it internally).
- **fd** — fast `find` replacement with sane defaults.
- **bat** — `cat` with syntax highlighting and paging.
- **eza** — modern `ls` with git status, icons, tree view.
- **zoxide** (`z`) — smarter `cd` that learns frequent directories.
- **atuin** — shell history with sync across machines + fuzzy search.
- **starship** — fast cross-shell prompt with git status, env info.
- **htop** / **btop** — better `top`.
- **dust** — better `du`.
- **duf** — better `df`.
- **tldr** — simplified man pages with examples.
- **direnv** — per-directory env vars (project-local `PATH`, env files).
- **shellcheck** — bash linter; finds bugs in shell scripts.
- **shfmt** — shell formatter.

### LaTeX and writing
- **TeX Live** — full distribution.
- **tectonic** — modern LaTeX engine that auto-fetches missing packages; easier than TeX Live for casual use.
- **latexmk** — build automation (one command, handles bib + multiple passes).
- **chktex** — LaTeX linter.
- **latexindent** — formatter.
- **biber** + **biblatex** — modern bibliography stack.
- **Zotero** + **Better BibTeX** — reference manager with live BibTeX export.
- **Pandoc** — universal document converter (markdown ↔ LaTeX ↔ Word ↔ HTML ↔ PDF).
- **Quarto** — scientific publishing (Jupyter + RMarkdown + Pandoc); great for reports with embedded code and plots.
- **typst** — modern LaTeX alternative; faster compile, cleaner syntax. Worth knowing exists.

### HPC
- **module** / **lmod** — environment modules (already on Orion).
- **Apptainer** (formerly Singularity) — containers for HPC; reproducible env without root.
- **Spack** — HPC package manager.
- **darshan** — I/O profiler for HPC jobs.
- **likwid**, **perf** — performance counters.
- **gprof**, **valgrind/callgrind** — classic profilers.

### Documentation
- **Sphinx** — Python docs standard.
- **MkDocs** + **Material for MkDocs** — markdown-based docs site.
- **Jupyter Book** — books from notebooks; good for reproducible tutorials.
- **Read the Docs** — free hosting.

### Reproducibility and containers
- **Docker** / **Podman** — standard containers.
- **Apptainer** — HPC version.
- **Nix** — reproducible builds and dev shells; steep curve but powerful.
- **devbox** — Nix-based dev environments with a simpler UX.

### AI assistants (alternatives or supplements to Gemini)
- **Continue.dev** — VSCode extension; bring your own Anthropic / OpenAI / local API key.
- **Cline** — agent-style VSCode extension that reads files, edits, runs commands.
- **Aider** — terminal-based AI pair programmer; great for batch refactors.
- **Claude Code** — Anthropic CLI tool.
- **Codeium** — free AI completion (closed source, but free tier exists).
- **Tabby** — self-hosted AI completion (run on your own GPU).

### Misc
- **typos** / **codespell** — typo checkers for source code and comments.
- **gitleaks** — scan for accidentally-committed secrets.
- **age** — modern file encryption (replaces gpg for many use cases).
- **1Password CLI** (`op`) — secrets and SSH key management.
- **httpie** / **xh** — better `curl`.
- **draw.io** / **excalidraw** — diagramming (both have VSCode integrations).
- **mermaid** — text-based diagrams; renders in GitHub markdown and VSCode preview.
