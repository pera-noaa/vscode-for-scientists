# OpenOnDemand Walkthrough (MSU Orion / Hercules)

MSU's HPC clusters forbid Remote-SSH because it spawns persistent VSCode server processes that violate cluster policy. Remote Tunnels is out for the same reason. **Use OpenOnDemand instead.**

This is the supported path: a browser-based VSCode running as a SLURM job on a compute node.

## Step-by-step

### 1. Log in
Visit https://orion-ood.hpc.msstate.edu (or the equivalent Hercules URL). Authenticate with your MSU HPC credentials.

### 2. Launch Code Server
- From the top menu: **Interactive Apps → Code Server**.
- Fill in:
  - **Partition**: pick whatever your group normally uses (`orion`, `hercules`, etc.).
  - **Number of hours**: 4 is reasonable for a workshop session; extend later if needed.
  - **CPU / RAM**: modest is fine for editing. ~2 CPUs and 4 GB RAM is plenty unless you're also running an analysis.
- Click **Launch**.

### 3. Wait for the job to start
The job appears in your "My Interactive Sessions" page. Status will show "Queued" → "Starting" → "Running." Usually under a minute on shared partitions.

### 4. Connect
When the status is "Running," click **Connect to Code Server**. A new browser tab opens with VSCode running on the compute node.

### 5. Clone the workshop repo
- Open the integrated terminal: View → Terminal (or Ctrl+\`).
- You're on a compute node with access to your `$HOME` and group filesystems.
- Clone:
  ```
  git clone https://github.com/pera-noaa/vscode-for-scientists.git ~/vscode-workshop
  ```
- File → Open Folder → `~/vscode-workshop`.

### 6. Install workshop extensions
The marketplace inside OpenOnDemand's Code Server is **Open VSX**, not Microsoft's official marketplace. Most extensions are mirrored, but a few aren't:

- **Pylance** — not on Open VSX. Use **Pyright** (open-source core, behaves nearly identically).
- **Remote-SSH** — not needed (you're already on the cluster).
- **Live Share** — varies; check before assuming.

Install from `extensions.txt` (skip the ones marked OSS-only):

```
xargs -L 1 code --install-extension < extensions.txt
```

## What works the same as Remote-SSH
- Editor (file tree, multi-cursor, search, F12 navigation).
- Integrated terminal — already on the compute node.
- Git source-control panel.
- Jupyter notebooks (kernel runs in the job).
- Debugging.
- Format-on-save, linting.

## What's different
- **Persistence**: the editor lives inside a SLURM job. If the job times out, your unsaved changes are lost. Save often; the job's walltime is the real deadline.
- **Marketplace**: Open VSX, not Microsoft's. ~95% of extensions exist on both.
- **Settings Sync** via GitHub still works — your local config follows you.
- **Browser-based**: keybindings may collide with browser shortcuts (e.g. Cmd+W closes the tab). VSCode warns when this is likely.

## Tips
- Bookmark the launch page so you don't have to navigate the menu each time.
- For longer work, extend walltime when you launch — re-queueing can take longer than the original session.
- OpenOnDemand also offers Jupyter, RStudio, MATLAB, and a file browser as separate apps. Pick whichever fits the task; they all share the same filesystem.

## Common issues

### "Connect to Code Server" button doesn't appear
- Job is still queued. Wait a minute and refresh.
- Job failed. Check the session error log via the OOD interface.

### Code Server session disconnected unexpectedly
- Job hit its walltime. Launch a new session, then File → Open Folder on the same path.
- Network blip. Browser tab will usually reconnect; if not, click "Connect" again.

### Extensions won't install ("not found")
- The extension isn't on Open VSX. Search the registry: https://open-vsx.org.
- Workarounds: find an OSS alternative (e.g. Pyright for Pylance), or skip the extension.

### Performance feels sluggish
- Browser-based VSCode is slightly heavier than native VSCode + Remote-SSH. Usually fine for editing, can lag on huge files.
- Check the job has enough RAM (default may be too small for big Python/notebook sessions).
