# VSCode for Scientists — Workshop

Hands-on, in-person workshop to get the lab using **VSCode** for daily work: Fortran (TM5), IDL, legacy Python, Jupyter notebooks, instrument calibration, and LaTeX paper writing.

If you've **never used VSCode before**, this workshop is for you. We start from "I just installed it, now what?" and end at "I can do my normal day in VSCode on my HPC server, and I never want to go back to PuTTY."

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

The workshop is structured so each block answers one question: *what does this thing do for me?* Each block has a hands-on exercise you do on your own machine while watching the live demo.

## Before the workshop

**Complete [`pre-session.md`](pre-session.md) at least 24 hours ahead.** It walks you through installing VSCode, getting Remote-SSH working with your server, and cloning this repo to that server. The first 10 minutes of the in-person session are for SSH verification, not setup — if your SSH isn't working when you walk in, you'll fall behind.

If you hit snags, post in the workshop channel. The earlier we triage, the smoother the session.

## Repo layout
```
.
├── README.md                # this file — the session script
├── pre-session.md           # homework checklist
├── cheatsheet.md            # one-page shortcut reference (print this)
├── extensions.txt           # `code --install-extension`-able list
├── settings.example.json    # sensible defaults for User Settings JSON
├── setup/                   # SSH config examples, verify.sh, troubleshooting, OOD walkthrough
├── exercises/               # hands-on exercise folders (01 through 10)
│   ├── 01-navigation/       # F12 / Shift+F12 / F2 / multi-cursor
│   ├── 02-search-replace/   # Cmd+Shift+F across the workspace
│   ├── 03-git/              # visual hunk staging
│   ├── 04-debugging/        # breakpoints, variable inspection
│   ├── 05-jupyter/          # notebooks with variable explorer
│   ├── 06-fortran/          # navigation in Fortran (self-study)
│   ├── 07-idl/              # navigation in IDL (self-study)
│   ├── 08-scientific-data/  # netCDF / HDF5 / CSV viewers (self-study)
│   ├── 09-latex/            # LaTeX live preview (self-study)
│   └── 10-ruff-magic/       # the "magic save" — ruff fixes the file on Cmd+S
└── self-study/              # reference material we won't cover live
    ├── adjacent-tools.md    # CLI tools worth knowing (ruff, uv, fzf, tmux…)
    ├── ai-assistants.md     # Gemini, Copilot, BYO-key in depth
    └── customization.md     # emacs keymap, profiles, settings sync
```

## Session arc (90 minutes)

| Time | Block | Exercise |
|---|---|---|
| 0:00–0:10 | **First contact** — everyone connects to their server. UI tour: file tree, editor, terminal, status bar, command palette as the M-x analog. We run `hostname` in the terminal to confirm we're on the cluster. | — |
| 0:10–0:20 | **The magic save** — open `messy.py`, hit Cmd+S, watch ruff clean up unsorted imports, deprecated numpy aliases, `== None`, whitespace, all at once. The "good defaults already exist" pitch made concrete. | [10](exercises/10-ruff-magic/) |
| 0:20–0:35 | **Editor superpowers** — F12, Shift+F12, F2, multi-cursor, Cmd+Shift+F across the workspace. The "navigation that respects your codebase" pitch. | [01](exercises/01-navigation/), [02](exercises/02-search-replace/) |
| 0:35–0:50 | **Git** — visual hunk staging, inline blame, branch switcher. | [03](exercises/03-git/) |
| 0:50–1:05 | **Python daily workflow** — interpreter switcher, debugger, pytest gutter. | [04](exercises/04-debugging/) |
| 1:05–1:15 | **Notebooks** — variable explorer, inline plots, cell git diffs. | [05](exercises/05-jupyter/) |
| 1:15–1:25 | **HPC + AI (honest)** — what just happened with Remote-SSH, OpenOnDemand for MSU, Gemini vs Copilot Free vs CIRES eligibility. | — |
| 1:25–1:30 | **Wrap** — cheatsheet, self-study pointers, Q&A. | — |

Exercises **06–09** (Fortran, IDL, scientific data, LaTeX) are **self-study**. The mechanics are the same as the live exercises; the languages and tools are different. Anyone working with those will want to re-do the exercise list on their own time.

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
- Read [`self-study/adjacent-tools.md`](self-study/adjacent-tools.md) for the CLI tools (ruff, uv, fzf, tmux, …) that pair with VSCode.
- Read [`self-study/ai-assistants.md`](self-study/ai-assistants.md) for the AI story — what the lab pays for, what CIRES users get free, BYO-key options.
- Read [`self-study/customization.md`](self-study/customization.md) for emacs keymaps, profiles, settings sync.
- Look at `git log` of this repo — it's a worked example of how a small project's history can read well.
