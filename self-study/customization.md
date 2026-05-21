# Customization

Things to tweak after the workshop so VSCode fits the way you already work.

## Preempting the "but my emacs / vim" objection
- **Awesome Emacs Keymap** (`tuttieee.emacs-mcx`) — preserves your emacs muscle memory inside VSCode. Most C-x C-something bindings work. `M-x` is mapped to Cmd+Shift+P (the command palette), which is fitting.
- **VSCodeVim** (`vscodevim.vim`) — vim mode, including `:` commands, registers, and most motions.

If you're a heavy emacs user, install the keymap first thing. It removes ~80% of the muscle-memory frustration in one click.

## Per-project settings
Each project can have its own `.vscode/settings.json` that overrides your global settings. Keep this file in version control with the project.

Useful per-project overrides:
- `python.defaultInterpreterPath` — pin to a specific conda env.
- `python.testing.pytestArgs` — pass project-specific pytest flags.
- `editor.rulers` — different line-length rules per project.
- `[python]` formatter / linter — different rules for different repos.

Example `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.testing.pytestArgs": ["tests"],
    "editor.rulers": [88],
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff"
    }
}
```

## Settings Sync via GitHub
Cmd+Shift+P → "Settings Sync: Turn On" → sign in with GitHub.

This pushes your settings, keybindings, snippets, UI state, and (optionally) extensions to GitHub. Sign in on a second machine — laptop, HPC, friend's computer — and the same config follows you.

The sync is encrypted at rest; it stores in a private gist on your account. You can pause it for specific machines if your HPC and laptop need to diverge.

## Profiles
A VSCode "profile" is a bundle of: extensions enabled, keybindings, settings, UI layout. You can have multiple and switch between them.

Useful profiles:
- **Fortran** — Modern Fortran + minimal extras, fast to start, no Python noise.
- **Python ML** — Python, Pylance, Jupyter, plus ML extensions (Tensorboard, etc.).
- **Writing** — LaTeX Workshop, Markdown All in One, Code Spell Checker, distraction-free theme.
- **Default** — everything everywhere.

Cmd+Shift+P → "Profiles: Create Profile" → pick which extensions and settings to include.

Switching profiles takes a couple of seconds and is non-destructive — your other profiles stay intact.

## Keybindings
Cmd+K Cmd+S opens the keyboard shortcut editor. Search for any command and rebind. JSON view (top-right icon) lets you edit `keybindings.json` directly — useful for emacs-like chord sequences.

Sample binding: bind Cmd+Shift+E to "Reveal Active File in Explorer" (a common need that doesn't have a default shortcut):
```json
{
    "key": "cmd+shift+e",
    "command": "workbench.files.action.showActiveFileInExplorer"
}
```

## Snippets
User snippets live in `~/Library/Application Support/Code/User/snippets/` (macOS).

Create snippets per language with Cmd+Shift+P → "Snippets: Configure User Snippets".

Useful examples:
- A Fortran subroutine skeleton.
- An IDL procedure with standard header.
- A matplotlib figure boilerplate (figure + axes + savefig).
- A SLURM batch script template.

Example Python snippet (`python.json`):
```json
{
    "Matplotlib figure": {
        "prefix": "plotfig",
        "body": [
            "import matplotlib.pyplot as plt",
            "",
            "fig, ax = plt.subplots(figsize=(8, 5))",
            "ax.plot($1)",
            "ax.set_xlabel('$2')",
            "ax.set_ylabel('$3')",
            "ax.set_title('$4')",
            "fig.tight_layout()",
            "fig.savefig('$5.png', dpi=150)",
            "$0"
        ],
        "description": "Standard matplotlib figure setup"
    }
}
```

Then in any `.py` file, type `plotfig` + Tab to expand.

## Tasks
`.vscode/tasks.json` lets you define commands you run often and bind them to keystrokes.

Example for an HPC project:
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Submit run",
            "type": "shell",
            "command": "sbatch run.slurm",
            "problemMatcher": []
        },
        {
            "label": "Check queue",
            "type": "shell",
            "command": "squeue -u $USER",
            "problemMatcher": []
        },
        {
            "label": "Tail latest log",
            "type": "shell",
            "command": "tail -f $(ls -t logs/*.log | head -1)",
            "problemMatcher": []
        }
    ]
}
```

Run with Cmd+Shift+P → "Tasks: Run Task" → pick one. Or bind to a keystroke via the keybindings editor.

## Workspace Trust
The first time you open an unknown repo, VSCode asks whether you trust the folder. Untrusted folders run in a sandboxed mode that disables auto-running extensions (linters, formatters, debug adapters). This is the security model — don't disable it globally just to make the prompt go away.

For trusted folders (your own projects, lab repos), click "Trust" once and it remembers.

## Themes
- **Dark+** (default dark) and **Light+** (default light) are fine.
- **GitHub Dark** / **GitHub Light** for familiarity with GitHub diffs.
- **Solarized** for the classic feel.
- Cmd+K Cmd+T cycles themes — try the previews.

For projector legibility during the workshop, **Light+** with `editor.fontSize` bumped to 16+ reads better in a lit room.
