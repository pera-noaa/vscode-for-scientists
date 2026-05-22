# Setup — Pre-Arrival and Block 0

This doc covers everything needed to be at "I'm editing on my HPC server in VSCode" by 0:15 of the workshop. It's split into two parts:

- **Part 1 — Before you arrive** (~10 min, on your own): install VSCode and the Remote-SSH extension. Required.
- **Part 2 — Block 0** (15 min, in-session): SSH config, connect to your server, clone the workshop repo, confirm you're on the cluster. Walked through together on the projector.

**Don't try to do Part 2 ahead of time** — we want everyone at the same place when the editor demos start, and the live walkthrough is also useful content (it's how you'd onboard a new lab member).

---

## Part 1 — Before you arrive (~10 min on your own)

### 1. Install VSCode
Download from https://code.visualstudio.com/ and install. Then enable the `code` CLI:

- **macOS**: Open VSCode → Cmd+Shift+P → "Shell Command: Install 'code' command in PATH".
- **Linux**: Most installers add it automatically. Check with `code --version`.
- **Windows**: The installer asks during setup; if you missed it, re-run the installer.

### 2. Install the Remote-SSH extension
From your laptop terminal:

```
code --install-extension ms-vscode-remote.remote-ssh
```

Or open VSCode → Extensions sidebar (Cmd+Shift+X) → search "Remote - SSH" → Install.

That's all of Part 1. If you already had VSCode and Remote-SSH, you're done with the homework — see you at the workshop.

---

## Part 2 — Block 0 (15 min, together)

### 3. Quick sanity-check: does plain SSH work?
Before involving VSCode, confirm plain SSH works from your terminal:

```
ssh <yourserver> echo "ok from $(hostname)"
```

Replace `<yourserver>` with whatever host you use day-to-day (`nimbus`, etc.). If you see `ok from <yourserver>`, you're good. If not, flag a helper. Common culprits: not on the VPN, missing `~/.ssh/config` entry, wrong key permissions. See [`setup/troubleshooting.md`](setup/troubleshooting.md).

### 4. Clone the workshop repo to your laptop
Pick a place on your laptop and clone:

```
git clone https://github.com/pera-noaa/vscode-for-scientists.git ~/vscode-workshop
```

You now have a local copy. This is what gives you `setup/verify.sh` for the next step. (You'll clone it again to your HPC server later — that's expected.)

### 5. Run the verification script
From your laptop terminal:

```
cd ~/vscode-workshop && ./setup/verify.sh
```

The script checks: VSCode CLI on PATH, ssh client, ssh-agent, ssh config, Remote-SSH extension installed, and a live SSH connection to a host you specify. Everyone should see "ready" before we move on.

### 6. Connect with VSCode
- Cmd+Shift+P → "Remote-SSH: Connect to Host" → pick your server.
- First connect installs `~/.vscode-server/` on the remote (≈30 seconds). Wait for the green corner indicator (bottom-left).

### 7. Clone the workshop repo on the remote
In the VSCode integrated terminal (Ctrl+\`) — which is now running on the remote — clone the repo into your remote home directory:

```
git clone https://github.com/pera-noaa/vscode-for-scientists.git ~/vscode-workshop
```

Then File → Open Folder → `~/vscode-workshop` (on the remote).

### 8. Confirm you're on the cluster
In the integrated terminal:

```
hostname
```

If it returns your HPC server's name (and not your laptop's), Block 0 is done. The rest of the workshop happens on that remote, with all the navigation/git features working on real files on your real cluster.

---

## MSU Orion / Hercules users
MSU forbids Remote-SSH; use OpenOnDemand instead. A helper sits with you in parallel during Block 0 — you'll follow the flow below while the rest of the room does steps 3–8 above.

You still need:
- **Part 1, step 1** above: VSCode installed locally (for browsing this repo on your laptop after the workshop).

You don't need:
- The Remote-SSH extension (Part 1, step 2).
- `setup/verify.sh` (step 5) — it's checking Remote-SSH things that don't apply.

Instead, do this (also during Block 0):

1. Visit https://orion-ood.hpc.msstate.edu.
2. Log in with your MSU HPC credentials.
3. Launch a **Code Server** interactive job (2 hours walltime, modest CPU/RAM is fine — the workshop fits in one session with margin).
4. When the job starts, click "Connect" to open browser-based VSCode.
5. Open a terminal in that VSCode (Ctrl+\`) and clone the workshop repo:
   ```
   git clone https://github.com/pera-noaa/vscode-for-scientists.git ~/vscode-workshop
   ```
6. Open the folder via the VSCode UI: File → Open Folder → `~/vscode-workshop`.
7. Run `hostname` in the terminal — it should return a compute node name, confirming you're on the cluster.

See [`setup/msu-ood-walkthrough.md`](setup/msu-ood-walkthrough.md) for the full walkthrough with screenshots.
