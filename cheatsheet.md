# VSCode Cheatsheet — One Page

The shortcuts in this list are the ones worth memorizing first. If you can describe an action in English, you can probably find it with **Cmd+Shift+P** (the command palette) — don't bother memorizing the rest.

`Cmd` on macOS = `Ctrl` on Linux/Windows. `Opt` = `Alt`.

## Universal
| Shortcut | Action |
|---|---|
| `Cmd+Shift+P` | Command palette — search any action or setting |
| `Cmd+P` | Quick open — fuzzy-search files by name |
| `Cmd+T` | Quick symbol search across the workspace |
| `Cmd+,` | Open settings |
| `Cmd+B` | Toggle sidebar |
| `Ctrl+\`` | Toggle integrated terminal |

## Navigation (works in Python, Fortran, IDL, Markdown…)
| Shortcut | Action |
|---|---|
| `F12` | Go to definition |
| `Opt+F12` | Peek definition (popup, doesn't leave file) |
| `Shift+F12` | Find all references |
| `Cmd+Click` | Jump to definition (same as F12) |
| `Ctrl+-` / `Ctrl+Shift+-` | Navigate back / forward |
| `Cmd+Shift+O` | Jump to symbol in current file |

## Editing
| Shortcut | Action |
|---|---|
| `F2` | Rename symbol (refactor-aware, propagates across files) |
| `Cmd+D` | Add next occurrence to multi-cursor |
| `Cmd+Shift+L` | Add ALL occurrences to multi-cursor |
| `Opt+Click` | Add a cursor anywhere |
| `Cmd+/` | Toggle line comment |
| `Cmd+Shift+K` | Delete line |
| `Opt+↑` / `Opt+↓` | Move line up / down |
| `Shift+Opt+↓` | Copy line down |
| `Cmd+Shift+P → "format"` | Format current file |

## Search and replace
| Shortcut | Action |
|---|---|
| `Cmd+F` | Find in file |
| `Cmd+Opt+F` | Find and replace in file |
| `Cmd+Shift+F` | Find across the workspace |
| `Cmd+Shift+H` | Find and replace across the workspace |

## Git (Source Control panel = `Cmd+Shift+G`)
| Action | Where |
|---|---|
| Stage a hunk | Click `+` in the diff gutter |
| Stage a single line | Right-click line in diff → "Stage Selected Range" |
| Inline blame | GitLens: hover any line |
| View file history | Right-click file → "View File History" (GitLens) |
| Compare with branch | Cmd+Shift+P → "Git: Compare with…" |

## Files and tabs
| Shortcut | Action |
|---|---|
| `Cmd+N` | New file |
| `Cmd+W` | Close tab |
| `Cmd+Shift+T` | Reopen closed tab |
| `Cmd+1` / `Cmd+2` / `Cmd+3` | Focus editor group 1/2/3 |
| `Cmd+\\` | Split editor |
| Drag tab to edge | Split horizontally / vertically |

## Notebooks (Jupyter)
| Shortcut | Action |
|---|---|
| `Shift+Enter` | Run cell, advance to next |
| `Ctrl+Enter` | Run cell, stay |
| `A` / `B` (command mode) | Insert cell above / below |
| `D D` (command mode) | Delete cell |
| `Esc` / `Enter` | Toggle command / edit mode |

## Debugging
| Shortcut | Action |
|---|---|
| `F5` | Start / continue |
| `F9` | Toggle breakpoint |
| `F10` | Step over |
| `F11` | Step into |
| `Shift+F11` | Step out |

## Remote
| Shortcut | Action |
|---|---|
| `Cmd+Shift+P → "Remote-SSH: Connect to Host"` | Open a remote folder |
| Green corner indicator | Current connection status |
| `Ctrl+\`` (after connecting) | Terminal is on the remote |

## Markdown
| Shortcut | Action |
|---|---|
| `Cmd+K V` | Preview to the side |
| `Cmd+Shift+V` | Preview in same tab |
