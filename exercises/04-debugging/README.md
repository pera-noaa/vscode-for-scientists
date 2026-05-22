# Exercise 04 — Debugging a Buggy Script

Goal: stop print-statement-debugging. Use a breakpoint and the Variables panel.

You'll work with `buggy_calibration.py`, a small script with a planted bug somewhere. It runs without error, but the reported mean is wrong (it prints the expected value at the bottom — they don't match).

## Setup
- Open `exercises/04-debugging/buggy_calibration.py`.
- Make sure the Python extension is installed and a Python interpreter is selected (status bar, bottom-right).

## Exercises

### 1. Run it once and see the wrong answer
- Right-click in the editor → "Run Python File in Terminal."
- The script prints a calibrated mean and the expected value. They don't match.

### 2. Find the bug with the debugger
The bug is small. Don't read the code first — use the debugger to find it.

- Click in the gutter to the left of any `return` statement in the file. A red dot appears — that's a breakpoint.
- Press **F5**. VSCode asks for a debug config the first time — pick "Python File."
- Execution pauses at your breakpoint. The current line is highlighted.

### 3. Read the world
- Look at the **Variables** panel (left sidebar, top).
- Expand any local variables — read what's in them.

### 4. Hover-evaluate
- Hover your mouse over any expression in the code. A tooltip shows its current value.
- Try hovering over slices, function arguments, anything that looks suspicious.

### 5. Use the Debug Console
- Bottom panel → **Debug Console** tab.
- Type any Python expression and Enter — it evaluates in the paused frame.
- This is where you compare what *should* equal what — `sum(values)` vs `sum(values[1:])`, `len(x)` vs the divisor in a mean, etc.

### 7. Step through (optional)
- Disable the breakpoint and step from earlier in the program with **F10** (step over) or **F11** (step into).
- The yellow arrow shows the current line; variables update live.

### 8. Fix and re-run
- Stop the debugger (Shift+F5).
- Fix the bug in `compute_mean`. Save.
- F5 again — verify the answer is now correct.

## Try this with print debugging for comparison
Adding `print(f"values = {values}")` and `print(f"sum(values[1:]) = {sum(values[1:])}")` would have worked too. But you'd have edited the file, re-run, read scrollback, edited again to remove the prints, re-run, …

The debugger gives you the same information without modifying the source.

## Tips
- **Conditional breakpoints**: right-click a breakpoint dot → "Edit Breakpoint" → enter a Python expression. The breakpoint only fires when the condition is true (e.g. "fire only when `len(values) > 100`").
- **Logpoints**: same right-click menu → "Add Logpoint" → enter a message. Like a print statement but without modifying source. The message can reference variables in `{}`.
- **Watch panel**: add expressions to the Watch panel; they re-evaluate on every step. Useful for tracking how a variable evolves through a loop.
- **Step into / step out** are F11 and Shift+F11 — for walking into and out of function calls.

## When this is the wrong tool
- For HPC batch jobs that have already failed, the debugger doesn't help — you need the post-mortem traceback. Look at `python -X dev`, `traceback.print_exc()`, or `import pdb; pdb.post_mortem()`.
- For race conditions or MPI parallel bugs, single-process debugging is misleading. Use logging.
- For numerical issues that only show up at large scale (NaN propagation, overflow), the debugger is fine for the immediate cause but the underlying mismatch usually needs `assert` statements or property-based tests (see hypothesis in self-study/adjacent-tools.md).
