#!/usr/bin/env bash
# Creates a small sub-repo with multi-hunk dirty state for the hunk-staging exercise.
# Re-running this script wipes and recreates the sub-repo from scratch.
set -euo pipefail

cd "$(dirname "$0")"
rm -rf exercise-repo
mkdir exercise-repo
cd exercise-repo

git init -b main -q
git config user.email "workshop@example.org"
git config user.name "Workshop User"

# ----- baseline commit -----
cat > calibration.py <<'EOF'
"""Apply calibration to raw observations."""


def apply_calibration(raw_values, slope, offset):
    """Linear calibration: y = slope * x + offset."""
    return [slope * v + offset for v in raw_values]


def summary(values):
    """Return mean, min, max."""
    return {
        "mean": sum(values) / len(values),
        "min": min(values),
        "max": max(values),
    }
EOF

cat > README.md <<'EOF'
# Calibration

A small calibration utility.

## Usage
See `calibration.py`.
EOF

cat > config.yaml <<'EOF'
slope: 1.0
offset: 0.0
threshold: 100
EOF

git add -A
git commit -m "Initial commit" -q

# ----- dirty state -----

# calibration.py — three logical hunks (imports, function signature/body, summary expansion)
cat > calibration.py <<'EOF'
"""Apply calibration to raw observations."""

import logging

logger = logging.getLogger(__name__)


def apply_calibration(raw_values, slope, offset, *, clip=None):
    """Linear calibration: y = slope * x + offset.

    If clip is given, output is clipped to that maximum value.
    """
    out = [slope * v + offset for v in raw_values]
    if clip is not None:
        out = [min(v, clip) for v in out]
    logger.debug("Calibrated %d values", len(out))
    return out


def summary(values):
    """Return mean, min, max, and stdev."""
    n = len(values)
    mean = sum(values) / n
    variance = sum((v - mean) ** 2 for v in values) / n
    return {
        "mean": mean,
        "min": min(values),
        "max": max(values),
        "stdev": variance ** 0.5,
    }
EOF

# README.md — appended changelog section
cat >> README.md <<'EOF'

## Configuration
Slope, offset, and threshold come from `config.yaml`.

## Changes
- v0.2: added optional clipping to apply_calibration
- v0.2: added stdev to summary
EOF

# config.yaml — one value changed
# (Portable sed: write a new file rather than -i, which differs on BSD vs GNU.)
awk '{ gsub(/threshold: 100/, "threshold: 250"); print }' config.yaml > config.yaml.new
mv config.yaml.new config.yaml

echo
echo "Created $(pwd)"
echo
echo "Three files are now dirty with multi-hunk changes:"
echo "  - calibration.py (3 hunks: logging import, function signature/body, summary expansion)"
echo "  - README.md      (1 hunk: appended Configuration + Changes sections)"
echo "  - config.yaml    (1 hunk: threshold 100 -> 250)"
echo
echo "Open this folder in VSCode (File -> Open Folder) and follow README.md."
