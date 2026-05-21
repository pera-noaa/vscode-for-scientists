# SSH / Remote-SSH Troubleshooting

If `setup/verify.sh` fails or VSCode can't connect, the issue is almost always one of these.

## "Permission denied (publickey)"
Your SSH key isn't being offered or isn't authorized on the server.

- Check the server's `~/.ssh/authorized_keys` contains your **public** key (`~/.ssh/id_ed25519.pub` or `id_rsa.pub`).
- Check your private key permissions: must be 600.
  ```
  chmod 600 ~/.ssh/id_ed25519
  chmod 700 ~/.ssh
  ```
- Check the key is in your agent: `ssh-add -l`. If empty, `ssh-add ~/.ssh/id_ed25519`.
- On macOS, add to keychain so it auto-loads: `ssh-add --apple-use-keychain ~/.ssh/id_ed25519`.

## "Could not resolve hostname"
The host name doesn't resolve in DNS.

- Are you on the lab/institute VPN? Many HPC hosts only resolve from inside.
- Is the `HostName` in `~/.ssh/config` spelled correctly?
- Try the IP directly to isolate DNS vs networking: `ssh user@10.0.0.1`.

## "Connection timed out"
Network reachability problem.

- VPN check (same as above).
- Firewall: some networks block outbound SSH on port 22. Try from a different network or use Remote Tunnels (see master tutorial).
- If the cluster uses a non-standard port, add `Port <N>` to your `~/.ssh/config`.

## "Duo Push timed out" / Duo loops
Two-factor auth interacting badly with ssh.

- Use the Duo app push (not SMS) — push arrives faster.
- If using `ControlMaster`, an existing connection may skip Duo; if Duo prompts repeatedly, check that the first connection actually completed.
- Hardware keys (YubiKey) work too and skip the push entirely; configure with `Authenticator: <yubikey>` in your Duo settings.

## "vscode-server" install hangs or is very slow
The first time you connect, VSCode downloads its server-side helper into `~/.vscode-server/` on the remote.

- If your remote home directory is on a slow shared filesystem (e.g. Lustre), install on local scratch instead:
  - VSCode settings → search `remote.SSH.serverInstallPath` → set to `/scratch/$USER/.vscode-server` (or similar).
  - Or in `settings.json`:
    ```json
    "remote.SSH.serverInstallPath": {
        "your-host-name": "/scratch/your_username"
    }
    ```
- If it's just slow (not hung): wait. First install can take a minute on a 1 Gb/s link.

## "Connection refused" or fingerprint mismatch
Server-identity issue.

- Fingerprint changed: someone may have reinstalled the host. Verify with your sysadmin, then remove the old entry: `ssh-keygen -R <hostname>`.
- Connection refused: SSH daemon down on the server, or wrong port.

## VSCode shows "Connecting…" forever
Sometimes the first connection fails silently after the password/Duo step.

- Cmd+Shift+P → "Remote-SSH: Kill VS Code Server on Host" → reconnect.
- Cmd+Shift+P → "Remote-SSH: Show Log" — read the actual error.
- If the server is full (`No space left on device`), clear `~/.vscode-server/`.

## ControlMaster collisions
You see "mux_client_request_session: read from master failed" or similar.

- Old socket lingering: `rm ~/.ssh/controlmasters/*`.
- Make sure the directory exists and has the right permissions:
  ```
  mkdir -p ~/.ssh/controlmasters && chmod 700 ~/.ssh/controlmasters
  ```

## MSU Orion / Hercules: Remote-SSH disabled
These clusters explicitly forbid Remote-SSH. Use OpenOnDemand instead — see [`msu-ood-walkthrough.md`](msu-ood-walkthrough.md).

## When all else fails
- Bring your laptop to the front of the room 15 minutes before the workshop.
- Or: pair with a buddy whose setup works; you can run a Live Share session and follow along on their machine.
- Or: use `vscode.dev` / GitHub Codespaces as a fallback — most exercises work without SSH at all.
