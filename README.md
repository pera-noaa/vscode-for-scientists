# VSCode for Scientists — Workshop

Hands-on, in-person workshop showing why VSCode is a better day-to-day editor than emacs + PuTTY for this lab's work: Fortran (TM5), IDL, legacy Python, Jupyter notebooks, instrument calibration, and LaTeX paper writing.

You'll spend the workshop editing files on **your own HPC server** via VSCode Remote-SSH (or OpenOnDemand if you're at MSU). By the end of 90 minutes you'll have used every feature here on real code, on the cluster you actually work on.

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
├── exercises/               # hands-on exercise folders (01 through 09)
│   ├── 01-navigation/
│   ├── 02-search-replace/
│   ├── 03-git/
│   ├── 04-debugging/
│   ├── 05-jupyter/
│   ├── 06-fortran/
│   ├── 07-idl/
│   ├── 08-scientific-data/
│   └── 09-latex/
└── self-study/              # reference material we won't cover live
    ├── adjacent-tools.md    # CLI tools worth knowing (ruff, uv, fzf, tmux…)
    ├── ai-assistants.md     # Gemini, Copilot, BYO-key in depth
    └── customization.md     # emacs keymap, profiles, settings sync
```

## Session arc (90 minutes)

| Time | Block | Exercise |
|---|---|---|
| 0:00–0:10 | **Setup verification + UI tour** — everyone connects to their server, opens this repo, runs `hostname` in the integrated terminal. Quick tour: sidebar, status bar, command palette. | — |
| 0:10–0:25 | **Editor superpowers** — F12, Shift+F12, F2, multi-cursor, Cmd+Shift+F | [01](exercises/01-navigation/), [02](exercises/02-search-replace/) |
| 0:25–0:40 | **Git** — visual hunk staging, inline blame, branch switcher | [03](exercises/03-git/) |
| 0:40–0:55 | **Python daily workflow** — interpreter switcher, debugger, format-on-save, pytest gutter | [04](exercises/04-debugging/) |
| 0:55–1:05 | **Notebooks** — variable explorer, inline plots, cell git diffs | [05](exercises/05-jupyter/) |
| 1:05–1:20 | **HPC + remote workflow** — what just happened with Remote-SSH, OpenOnDemand for MSU, Tasks, Tunnels | — |
| 1:20–1:25 | **AI (honest)** — Gemini's strengths/weaknesses, Copilot Free, CIRES eligibility | — |
| 1:25–1:30 | **Wrap** — cheatsheet, self-study pointers, Q&A | — |

Exercises 06–09 (Fortran, IDL, scientific data, LaTeX) are **self-study** — they cover language-specific features for people who need them. The mechanics are the same as the live exercises; the languages are different.

## Why VSCode over emacs + PuTTY

The pitch in three sentences:

1. **You stop alt-tabbing.** Editor and terminal in the same window, both on the remote, no PuTTY chaos.
2. **Navigation that respects your codebase.** F12 jumps to a definition across files; Shift+F12 finds all callers. Works on Fortran, IDL, Python, even Markdown links. Once you have this, you can't go back.
3. **The good defaults already exist.** Multi-cursor rename, visual hunk staging, format-on-save, integrated Jupyter, AI completion. You don't have to assemble or maintain it.

The big counter-objection — "but my emacs muscle memory" — is solved by the [Awesome Emacs Keymap](https://marketplace.visualstudio.com/items?itemName=tuttieee.emacs-mcx) extension. Keybindings carry over.

## The one shortcut that matters

**`Cmd+Shift+P`** (Ctrl+Shift+P on Linux/Windows) opens the command palette — a searchable list of every action and setting in VSCode. The `M-x` analog.

Don't bother memorizing the rest of the shortcuts. Type the verb: "format", "rename", "compare", "git stash", "fold", "reload". If you can describe what you want, you can find it.

The [cheatsheet](cheatsheet.md) has the dozen shortcuts that are worth learning anyway, but the command palette is the only one that's non-negotiable.

## After the workshop

- Keep this repo as reference; the exercises are designed to be re-attempted.
- Read [`self-study/adjacent-tools.md`](self-study/adjacent-tools.md) for the CLI tools (ruff, uv, fzf, tmux, …) that pair with VSCode.
- Read [`self-study/ai-assistants.md`](self-study/ai-assistants.md) for the AI story — what the lab pays for, what CIRES users get free, BYO-key options.
- Read [`self-study/customization.md`](self-study/customization.md) for emacs keymaps, profiles, settings sync.
- Look at `git log` of this repo — it's a worked example of how a small project's history can read well.
