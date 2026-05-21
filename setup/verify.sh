#!/usr/bin/env bash
# verify.sh — workshop setup verification
#
# Run this from your LAPTOP terminal (not the HPC).
# Exits 0 if you're ready for the workshop; otherwise prints what to fix.
#
# Usage:
#   ./setup/verify.sh                # prompts for hostname
#   ./setup/verify.sh nimbus         # tests SSH to 'nimbus'

set -u

status=0
ok()   { printf '  [OK]   %s\n' "$1"; }
fail() { printf '  [FAIL] %s\n' "$1"; status=1; }
warn() { printf '  [WARN] %s\n' "$1"; }

echo
echo "VSCode workshop setup check"
echo "==========================="

# 1. VSCode + code CLI
if command -v code >/dev/null 2>&1; then
    ver=$(code --version 2>/dev/null | head -1)
    ok "code CLI on PATH (version $ver)"
else
    fail "code CLI not found on PATH"
    echo "         Install VSCode, then run:"
    echo "         Cmd+Shift+P -> 'Shell Command: Install code command in PATH'"
fi

# 2. ssh client
if command -v ssh >/dev/null 2>&1; then
    sshver=$(ssh -V 2>&1 | head -1)
    ok "ssh client present ($sshver)"
else
    fail "ssh client not found. Install OpenSSH."
fi

# 3. ssh-agent
if [ -n "${SSH_AUTH_SOCK:-}" ] && ssh-add -l >/dev/null 2>&1; then
    nkeys=$(ssh-add -l 2>/dev/null | wc -l | tr -d ' ')
    ok "ssh-agent running with $nkeys key(s) loaded"
elif [ -n "${SSH_AUTH_SOCK:-}" ]; then
    warn "ssh-agent socket set but no keys loaded; run: ssh-add ~/.ssh/id_*"
else
    warn "ssh-agent not detected; you may be prompted for passphrases on each connect"
fi

# 4. ~/.ssh/config
if [ -f "$HOME/.ssh/config" ]; then
    if grep -q '^Host ' "$HOME/.ssh/config" 2>/dev/null; then
        nhosts=$(grep -c '^Host ' "$HOME/.ssh/config" 2>/dev/null)
        ok "~/.ssh/config exists with $nhosts Host entry/entries"
    else
        warn "~/.ssh/config exists but has no Host entries"
    fi
else
    warn "~/.ssh/config not found; see setup/ssh-config.examples for templates"
fi

# 5. Remote-SSH extension
if command -v code >/dev/null 2>&1; then
    if code --list-extensions 2>/dev/null | grep -qi 'ms-vscode-remote.remote-ssh'; then
        ok "Remote-SSH extension installed"
    else
        fail "Remote-SSH extension not installed"
        echo "         Run: code --install-extension ms-vscode-remote.remote-ssh"
    fi
fi

# 6. Live SSH test
host="${1:-}"
if [ -z "$host" ]; then
    echo
    printf "Enter HPC hostname to test (or 'skip'): "
    read host
fi

if [ -z "$host" ] || [ "$host" = "skip" ]; then
    warn "Skipping live SSH test"
else
    echo
    printf "Testing ssh %s ...\n" "$host"
    # Try non-interactive first (BatchMode); if it needs Duo/password, retry interactively.
    if ssh -o BatchMode=yes -o ConnectTimeout=8 "$host" 'echo CONNECTED' 2>/dev/null | grep -q CONNECTED; then
        ok "ssh $host works without interaction"
    else
        echo "  (BatchMode failed; retrying interactively — answer any Duo / passphrase prompts)"
        if ssh -o ConnectTimeout=30 "$host" 'echo CONNECTED' 2>/dev/null | grep -q CONNECTED; then
            ok "ssh $host works (interactive)"
        else
            fail "ssh $host failed"
            echo "         Check: VPN, hostname spelling, ~/.ssh/config Host entry, key in agent"
            echo "         See setup/troubleshooting.md"
        fi
    fi
fi

echo
if [ "$status" -eq 0 ]; then
    echo "You're ready for the workshop."
else
    echo "Fix the [FAIL] items above, then re-run this script."
fi
exit $status
