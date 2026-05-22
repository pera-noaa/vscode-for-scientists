# Block 0 — Setup Walkthrough

This is the script for the first 30 minutes of the workshop. The instructor walks through each step on the projector; you follow along on your laptop. **Don't try to do this ahead of time** — we want everyone at the same place when the editor demos start, and live setup is also useful content (it's how you'd onboard a new lab member).

If you really want to save time, you can pre-install VSCode (step 1) and the Remote-SSH extension (step 2). Everything else we do together. Coming with nothing pre-installed is fine.

## What to bring

- **Laptop** with admin rights to install software.
- **Charger** — 2 hours is long enough that batteries fade.
- **Your SSH credentials** for your HPC server (you log in to `nimbus` or wherever from your terminal at least sometimes — bring whatever password/Duo/key setup you normally use).
- A **GitHub account** is nice for cloning over HTTPS without prompting, but not required for the public workshop repo.

## 1. Install VSCode
Download from https://code.visualstudio.com/ and install. Then enable the `code` CLI:

- **macOS**: Open VSCode → Cmd+Shift+P → "Shell Command: Install 'code' command in PATH".
- **Linux**: Most installers add it automatically. Check with `code --version`.
- **Windows**: The installer asks during setup; if you missed it, re-run the installer.

## 2. Install the Remote-SSH extension
From your laptop terminal:

```
code --install-extension ms-vscode-remote.remote-ssh
```

Or open VSCode → Extensions sidebar (Cmd+Shift+X) → search "Remote - SSH" → Install.

## 3. Quick sanity-check: does plain SSH work?
Before involving VSCode, confirm plain SSH works from your terminal:

```
ssh <yourserver> echo "ok from $(hostname)"
```

Replace `<yourserver>` with whatever host you use day-to-day (`nimbus`, etc.). If you see `ok from <yourserver>`, you're good.

If you see an error, flag a helper. Common culprits: not on the VPN, missing `~/.ssh/config` entry, wrong key permissions. See [`setup/troubleshooting.md`](setup/troubleshooting.md).

## 4. Clone the workshop repo to your laptop
Pick a place on your laptop and clone:

```
git clone https://github.com/pera-noaa/vscode-for-scientists.git ~/vscode-workshop
```

You now have a local copy. This is what gives you `setup/verify.sh` for the next step. (You'll clone it again to your HPC server later — that's expected.)

## 5. Run the verification script
From your laptop terminal:

```
cd ~/vscode-workshop && ./setup/verify.sh
```

The script checks: VSCode CLI on PATH, ssh client, ssh-agent, ssh config, Remote-SSH extension installed, and a live SSH connection to a host you specify. Everyone should see "ready" before we move on.

If you don't, the helpers will come over and triage.

## 6. Connect with VSCode
- Cmd+Shift+P → "Remote-SSH: Connect to Host" → pick your server.
- First connect installs `~/.vscode-server/` on the remote (≈30 seconds). Wait for the green corner indicator (bottom-left).

## 7. Clone the workshop repo on the remote
In the VSCode integrated terminal (Ctrl+\`) — which is now running on the remote — clone the repo into your remote home directory:

```
git clone https://github.com/pera-noaa/vscode-for-scientists.git ~/vscode-workshop
```

Then File → Open Folder → `~/vscode-workshop` (on the remote).

## 8. Confirm you're on the cluster
In the integrated terminal:

```
hostname
```

If it returns your HPC server's name (and not your laptop's), you're done with Block 0. The rest of the workshop happens on that remote, with all the navigation/git/notebook features working on real files on your real cluster.

---

## MSU Orion / Hercules users
MSU forbids Remote-SSH; use OpenOnDemand instead. A helper will sit with you in parallel during Block 0 — you'll follow the flow below while the rest of the room does steps 2–7 above.

You still need:
- **Step 1** above: VSCode installed locally (for browsing this repo on your laptop after the workshop).

You don't need:
- The Remote-SSH extension (step 2).
- `setup/verify.sh` (step 5) — it's checking Remote-SSH things that don't apply.

Instead, do this:

1. Visit https://orion-ood.hpc.msstate.edu.
2. Log in with your MSU HPC credentials.
3. Launch a **Code Server** interactive job (3 hours walltime, modest CPU/RAM is fine — the workshop fits in one session).
4. When the job starts, click "Connect" to open browser-based VSCode.
5. Open a terminal in that VSCode (Ctrl+\`) and clone the workshop repo:
   ```
   git clone https://github.com/pera-noaa/vscode-for-scientists.git ~/vscode-workshop
   ```
6. Open the folder via the VSCode UI: File → Open Folder → `~/vscode-workshop`.
7. Run `hostname` in the terminal — it should return a compute node name, confirming you're on the cluster.

See [`setup/msu-ood-walkthrough.md`](setup/msu-ood-walkthrough.md) for the full walkthrough with screenshots.
