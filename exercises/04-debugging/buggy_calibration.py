"""Daily calibration summary — has a bug somewhere.

Run it:

    python buggy_calibration.py

The reported mean is wrong. Find the bug using the VSCode debugger
(set a breakpoint inside `compute_mean` and inspect the variables).
"""

# Per-channel slope coefficients
COEFFICIENTS = {
    1: 1.02,
    2: 0.97,
    3: 1.00,
}

# (channel, raw_value) pairs
OBSERVATIONS = [
    (1, 10.0),
    (1, 12.0),
    (2, 8.5),
    (2, 9.0),
    (3, 5.0),
]


def calibrate(channel: int, raw: float) -> float:
    """Apply the per-channel slope coefficient."""
    coef = COEFFICIENTS.get(channel, 1.0)
    return raw * coef


def compute_mean(values: list[float]) -> float:
    """Return the arithmetic mean of `values`."""
    return sum(values[1:]) / len(values)


def main() -> None:
    calibrated = [calibrate(ch, v) for ch, v in OBSERVATIONS]
    mean = compute_mean(calibrated)
    print(f"Calibrated values: {calibrated}")
    print(f"Calibrated mean:   {mean:.3f}")
    print(f"(Expected ~8.88 once the bug is fixed.)")


if __name__ == "__main__":
    main()
