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

## 3. Verify SSH from your terminal first
Before involving VSCode, confirm plain SSH works:

```
ssh <yourserver> echo "ok from $(hostname)"
```

Replace `<yourserver>` with whatever host you use day-to-day (`nimbus`, etc.). If you see `ok from <yourserver>`, you're good.

If you see an error, see [`setup/troubleshooting.md`](setup/troubleshooting.md). Common culprits: not on the VPN, missing `~/.ssh/config` entry, wrong key permissions.

## 4. Connect with VSCode
- Cmd+Shift+P → "Remote-SSH: Connect to Host" → pick your server.
- First connect installs `~/.vscode-server/` on the remote (≈30 seconds). Wait for the green corner indicator (bottom-left).

## 5. Clone the workshop repo to your remote server
In the VSCode integrated terminal (Ctrl+\`) — which is now running on the remote — clone the repo into your home directory:

```
git clone https://github.com/pera-noaa/vscode-for-scientists.git ~/vscode-workshop
```

Then File → Open Folder → `~/vscode-workshop`.

## 6. Run the verification script
From your **laptop** terminal (not the remote):

```
cd ~/vscode-workshop && ./setup/verify.sh
```

The script checks VSCode CLI on PATH, the ssh client, ssh-agent, Remote-SSH extension installed, and a live SSH connection to a host you specify.

## 7. Post status in the workshop channel
- ✅ "Setup complete on `<server>`" — you're ready.
- ❌ Paste your error message and someone will help triage before the session.

---

## MSU Orion / Hercules users
Steps 2–6 are different. MSU forbids Remote-SSH; use OpenOnDemand instead.

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
