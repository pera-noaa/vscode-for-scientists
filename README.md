# VSCode for Scientists — Workshop

Hands-on, in-person workshop to get the lab using **VSCode** for daily work: Fortran (TM5), IDL, legacy Python, Jupyter notebooks, instrument calibration, and LaTeX paper writing.

If you've **never used VSCode before**, this workshop is for you. We assume you arrive with VSCode + the Remote-SSH extension installed (about 10 minutes of pre-arrival work — see [`pre-session.md`](pre-session.md), Part 1). The in-session hour is for the parts that actually need a live demo.

## What is VSCode?

A free, open-source code editor from Microsoft. It runs on your laptop and looks like this:

- A **file tree** on the left.
- A **main editor area** in the center, where files open as tabs.
- A **terminal** at the bottom (toggle with Ctrl+\`).
- A **status bar** at the very bottom — shows your Python interpreter, git branch, error count.
- A **command palette** searchable with **Cmd+Shift+P** — the "M-x" analog for emacs users.

What makes it relevant to a scientific lab:

1. **It edits files on your HPC server as if they were local**, via Remote-SSH. No more PuTTY + scp.
2. **It understands your code**: jump to a function's definition with F12, find every caller with Shift+F12, rename a variable across files with F2 — for Python, Fortran, *and* IDL.
3. **It runs Jupyter notebooks inline**, with a variable explorer that shows array shapes and dtypes at a glance.
4. **It has tens of thousands of extensions** — Fortran syntax, IDL syntax, LaTeX live preview, AI assistants, netCDF viewers — installable in one click.

## What to bring

- **Laptop** with admin rights to install software.
- **VSCode + Remote-SSH pre-installed.** See [`pre-session.md`](pre-session.md), Part 1 — about 10 minutes. Required.
- **Your SSH credentials** for your HPC server (whatever you use today to log in from your terminal).
- **Charger.**

## Repo layout
```
.
├── README.md                # this file — the session script
├── pre-session.md           # Part 1 (homework) + Part 2 (Block 0 walkthrough)
├── cheatsheet.md            # one-page shortcut reference (print this)
├── extensions.txt           # `code --install-extension`-able list
├── settings.example.json    # sensible defaults for User Settings JSON
├── setup/                   # SSH config examples, verify.sh, troubleshooting, OOD walkthrough
├── exercises/               # hands-on exercises done in the session
│   ├── 01-navigation/       # F12 / Shift+F12 / F2 / multi-cursor      (live)
│   ├── 02-search-replace/   # Cmd+Shift+F across the workspace          (live)
│   ├── 03-git/              # visual hunk staging                        (live)
│   ├── 04-debugging/        # breakpoints, variable inspection           (self-study)
│   ├── 05-jupyter/          # notebooks with variable explorer           (self-study)
│   ├── 08-scientific-data/  # netCDF / HDF5 / CSV viewers                (live)
│   └── 10-ruff-magic/       # the "magic save" — ruff fixes on Cmd+S    (live)
└── self-study/              # language/format-specific exercises + reference docs
    ├── 06-fortran/          # navigation in Fortran
    ├── 07-idl/              # navigation in IDL
    ├── 09-latex/            # LaTeX live preview
    ├── adjacent-tools.md    # CLI tools worth knowing (ruff, uv, fzf, tmux…)
    ├── ai-assistants.md     # Gemini, Copilot, BYO-key in depth
    └── customization.md     # emacs keymap, profiles, settings sync
```

## Session arc (70 minutes)

| Time | Block | Exercise |
|---|---|---|
| 0:00–0:15 | **Block 0 — Setup together** — verify SSH from terminal, clone the workshop repo locally, run `verify.sh`, connect via Remote-SSH, clone the repo on the remote, confirm with `hostname`. Walk through [`pre-session.md`](pre-session.md) Part 2 step-by-step on the projector. MSU users follow [`setup/msu-ood-walkthrough.md`](setup/msu-ood-walkthrough.md) in parallel. | — |
| 0:15–0:20 | **First contact** — UI tour: file tree, editor, terminal (Ctrl+\` — already on the remote you just connected to; `ls` shows your HPC home, `hostname` confirms it), status bar, command palette as the M-x analog. The "this is what replaces PuTTY" moment. | — |
| 0:20–0:30 | **The magic save** — open `messy.py`, hit Cmd+S, watch ruff clean up unsorted imports, deprecated numpy aliases, `== None`, whitespace, all at once. The "good defaults already exist" pitch made concrete. | [10](exercises/10-ruff-magic/) |
| 0:30–0:45 | **Editor superpowers** — F12, Shift+F12, F2, multi-cursor, Cmd+Shift+F across the workspace. The "navigation that respects your codebase" pitch. | [01](exercises/01-navigation/), [02](exercises/02-search-replace/) |
| 0:45–0:55 | **Scientific data** — open a CSV with Rainbow CSV, open a netCDF with H5Web (graphical browser inside the editor), click on a PNG sitting on the HPC and watch it render in a tab — no `scp` needed. Replaces `ncdump \| less` and the "copy plot to laptop to look at it" workflow. | [08](exercises/08-scientific-data/) |
| 0:55–1:05 | **Git** — visual hunk staging, inline blame. | [03](exercises/03-git/) |
| 1:05–1:10 | **Wrap** — cheatsheet, self-study pointers (debugger, notebooks, Fortran, IDL, LaTeX, AI), Q&A. | — |

**Self-study exercises:** debugger (`exercises/04-debugging/`) and notebooks (`exercises/05-jupyter/`) extend the live arc with Python-daily features that wouldn't fit in 70 minutes. Fortran (`self-study/06-fortran/`), IDL (`self-study/07-idl/`), and LaTeX (`self-study/09-latex/`) are language- and format-specific re-runs of the navigation and preview exercises — anyone whose daily work involves those will want to do them on their own time. The mechanics are the same; only the languages and tools change.

## The three-sentence pitch

1. **You stop alt-tabbing.** Editor and terminal in the same window, both on the remote, no PuTTY chaos.
2. **Navigation that respects your codebase.** F12 jumps to a definition across files; Shift+F12 finds all callers. Works on Fortran, IDL, Python, even Markdown links. Once you have this, you can't go back.
3. **The good defaults already exist.** Multi-cursor rename, visual hunk staging, format-on-save, integrated Jupyter, AI completion. You don't have to assemble or maintain it. (Exercise 10 demonstrates this in 30 seconds.)

The big counter-objection — "but my emacs muscle memory" — is solved by the [Awesome Emacs Keymap](https://marketplace.visualstudio.com/items?itemName=tuttieee.emacs-mcx) extension. Keybindings carry over.

## The one shortcut that matters

**`Cmd+Shift+P`** (Ctrl+Shift+P on Linux/Windows) opens the command palette — a searchable list of every action and setting in VSCode. The `M-x` analog.

Don't bother memorizing the rest of the shortcuts. Type the verb: "format", "rename", "compare", "git stash", "fold", "reload". If you can describe what you want, you can find it.

The [cheatsheet](cheatsheet.md) has the dozen shortcuts that are worth learning anyway, but the command palette is the only one that's non-negotiable.

## After the workshop

- Keep this repo as reference; every exercise is designed to be re-attempted.
- Work through the self-study exercises on your own as you encounter the relevant work: Python debugging (`exercises/04-debugging/`), notebooks (`exercises/05-jupyter/`), Fortran (`self-study/06-fortran/`), IDL (`self-study/07-idl/`), LaTeX (`self-study/09-latex/`).
- Read [`self-study/adjacent-tools.md`](self-study/adjacent-tools.md) for the CLI tools (ruff, uv, fzf, tmux, …) that pair with VSCode.
- Read [`self-study/ai-assistants.md`](self-study/ai-assistants.md) for the AI story — what the lab pays for, what CIRES users get free, BYO-key options.
- Read [`self-study/customization.md`](self-study/customization.md) for emacs keymaps, profiles, settings sync.
- Look at `git log` of this repo — it's a worked example of how a small project's history can read well.
