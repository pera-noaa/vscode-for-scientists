# Adjacent Tools Worth Integrating

Tools that live outside VSCode but pair with it. Most are CLI tools or libraries; many have a matching VSCode extension but the value is the underlying tool.

Pick aggressively — this list is meant to be cut down to the few that matter for your workflow.

## Python — linting, formatting, type checking
- **ruff** — fast all-in-one linter + formatter (subsumes flake8, black, isort, pyupgrade, pydocstyle). Single biggest Python-quality upgrade if you're not already using it.
- **mypy** — static type checker.
- **Pylance / Pyright** — Microsoft's type checker; ships with the VSCode Python extension.
- **pre-commit** — git hook framework that runs ruff / mypy / typos / etc. on every commit. Set-and-forget code quality.
- **bandit** — security-focused linter (insecure crypto, shell injection, hardcoded passwords).
- **vulture** — finds dead code; great for cleaning legacy scripts.

## Python — environments and packages
- **uv** — fast `pip` + `venv` replacement (10–100× faster). Astral. Arguably the biggest day-to-day Python workflow upgrade in 2026.
- **pixi** — conda-compatible env manager with lockfiles. Good for scientific stacks with binary deps.
- **poetry**, **pdm** — dependency + packaging tools.
- **conda-lock** — lockfiles for conda envs (reproducibility).
- **direnv** — auto-activate envs on `cd` into a project dir.

## Python — testing and profiling
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

## Python — interactive / debugging
- **IPython** — better REPL; auto-import, magic commands, easy plotting.
- **icecream** (`ic`) — print-debugging that shows variable name and value (`ic(x)` → `ic| x: 42`).
- **rich** — pretty console output, tracebacks, tables, progress bars.

## Python — scientific stack worth flagging
- **xarray** — labeled n-d arrays; natural fit for netCDF.
- **dask** — parallel arrays / dataframes; scale numpy / pandas to HPC.
- **polars** — fast DataFrame library, pandas alternative.
- **numba** — JIT compiler for numpy code; near-Fortran speed with one decorator.
- **cython** — C extensions from Python-like syntax.
- **f2py** (ships with numpy) — call Fortran from Python directly. Useful for IDL/Fortran → Python ports.
- **meson-python** — modern build for Python packages with native code.

## Fortran tools
- **fortls** — Fortran language server (powers Modern Fortran extension; also works in vim / emacs).
- **fprettify** — auto-formatter.
- **fpm** (Fortran Package Manager) — package management, still maturing but usable.
- **stdlib** — community standard library (sorting, strings, statistics).
- **FORD** — documentation generator that reads Fortran source comments.
- **flang** — LLVM-based Fortran compiler; alternative to gfortran / ifx.

## Build and project
- **CMake** + **Ninja** — modern build pipeline; faster than `make`.
- **Meson** — alternative build system (Python-style config).
- **just** — modern task runner; `justfile` replaces a Makefile for command shortcuts.
- **entr** / **watchexec** — re-run commands when files change.

## Git supporting tools
- **gh** (GitHub CLI) — PRs, issues, releases, repo creation from the terminal.
- **lazygit** — TUI git client; staging hunks, branching, rebasing without memorizing git commands.
- **git-delta** — pretty syntax-highlighted diffs; drop-in replacement for `git diff` output.
- **difftastic** — syntactic, language-aware diff. Hides whitespace and formatting changes, shows actual logic changes. Game-changer for refactors.
- **git-lfs** — large file storage for binaries.
- **dvc** — data version control; for big scientific datasets that don't belong in git.

## Scientific data — command line
- **CDO** (Climate Data Operators) — bread-and-butter netCDF: regrid, average, subset, time-mean.
- **NCO** (NetCDF Operators) — `ncks`, `ncdiff`, `ncwa`, `ncatted` etc. for fine-grained netCDF ops.
- **ncview** — quick netCDF browser.
- **Panoply** (NASA) — GUI netCDF / HDF / GRIB plotter.
- **ParaView** — large-scale 3D visualization.
- **ImageMagick** — image processing CLI (convert, montage, crop).
- **ffmpeg** — frame sequences → movies for animations.
- **jq** — JSON query language; essential for scripting against APIs.
- **yq** — YAML version of jq.

## Shell and terminal upgrades
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

## LaTeX and writing
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

## HPC
- **module** / **lmod** — environment modules.
- **Apptainer** (formerly Singularity) — containers for HPC; reproducible env without root.
- **Spack** — HPC package manager.
- **darshan** — I/O profiler for HPC jobs.
- **likwid**, **perf** — performance counters.
- **gprof**, **valgrind/callgrind** — classic profilers.

## Documentation
- **Sphinx** — Python docs standard.
- **MkDocs** + **Material for MkDocs** — markdown-based docs site.
- **Jupyter Book** — books from notebooks; good for reproducible tutorials.
- **Read the Docs** — free hosting.

## Reproducibility and containers
- **Docker** / **Podman** — standard containers.
- **Apptainer** — HPC version.
- **Nix** — reproducible builds and dev shells; steep curve but powerful.
- **devbox** — Nix-based dev environments with a simpler UX.

## Misc
- **typos** / **codespell** — typo checkers for source code and comments.
- **gitleaks** — scan for accidentally-committed secrets.
- **age** — modern file encryption (replaces gpg for many use cases).
- **1Password CLI** (`op`) — secrets and SSH key management.
- **httpie** / **xh** — better `curl`.
- **draw.io** / **excalidraw** — diagramming (both have VSCode integrations).
- **mermaid** — text-based diagrams; renders in GitHub markdown and VSCode preview.
