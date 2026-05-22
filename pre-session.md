# Pre-Session Setup

Complete this **at least 24 hours before the workshop**. The first 10 minutes of the in-person session are for SSH verification, not setup — if your SSH isn't working when you walk in, you'll fall behind.

Estimated time: 15 minutes if everything works, 30+ minutes if you hit snags. **If you hit snags, post in the workshop channel early so we can triage before the session.**

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

If you see an error, see [`setup/troubleshooting.md`](setup/troubleshooting.md). Common culprits: not on the VPN, missing `~/.ssh/config` entry, wrong key permissions.

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

The script checks: VSCode CLI on PATH, ssh client, ssh-agent, ssh config, Remote-SSH extension installed, and a live SSH connection to a host you specify. **Wait until it says "ready" before moving on.**

If the script reports failures, fix them and re-run. The whole flow downstream depends on these working.

## 6. Connect with VSCode
- Cmd+Shift+P → "Remote-SSH: Connect to Host" → pick your server.
- First connect installs `~/.vscode-server/` on the remote (≈30 seconds). Wait for the green corner indicator (bottom-left).

## 7. Clone the workshop repo on the remote
In the VSCode integrated terminal (Ctrl+\`) — which is now running on the remote — clone the repo into your remote home directory:

```
git clone https://github.com/pera-noaa/vscode-for-scientists.git ~/vscode-workshop
```

Then File → Open Folder → `~/vscode-workshop` (on the remote).

## 8. Post status in the workshop channel
- ✅ "Setup complete on `<server>`" — you're ready.
- ❌ Paste your error message and someone will help triage before the session.

---

## MSU Orion / Hercules users
MSU forbids Remote-SSH; use OpenOnDemand instead. The flow is different from the standard path above.

You still need:
- **Step 1**: VSCode installed locally (for browsing this repo on your laptop).

You don't need:
- The Remote-SSH extension (step 2).
- `setup/verify.sh` (step 5) — it's checking Remote-SSH things that don't apply.

Instead, do this:

1. Visit https://orion-ood.hpc.msstate.edu.
2. Log in with your MSU HPC credentials.
3. Launch a **Code Server** interactive job (4 hours walltime, modest CPU/RAM is fine).
4. When the job starts, click "Connect" to open browser-based VSCode.
5. Open a terminal in that VSCode (Ctrl+\`) and clone the workshop repo:
   ```
   git clone https://github.com/pera-noaa/vscode-for-scientists.git ~/vscode-workshop
   ```
6. Open the folder via the VSCode UI: File → Open Folder → `~/vscode-workshop`.
7. Post status in the workshop channel.

See [`setup/msu-ood-walkthrough.md`](setup/msu-ood-walkthrough.md) for the full walkthrough.
