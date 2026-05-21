"""Apply per-channel calibration coefficients to raw observations."""

from pathlib import Path

from data_loader import load_raw_data


# Toy calibration coefficients: linear y = slope * x + offset, per channel.
COEFFICIENTS = {
    1: (1.02, -0.15),
    2: (0.97, 0.04),
    3: (1.00, 0.00),
}


def apply_calibration(path: Path) -> list[dict]:
    """Load raw data from `path` and apply per-channel calibration."""
    raw = load_raw_data(path)
    calibrated = []
    for row in raw:
        slope, offset = COEFFICIENTS.get(row["channel"], (1.0, 0.0))
        coeff = slope  # alias used a few times below for the multi-cursor exercise
        row_out = dict(row)
        row_out["calibrated_value"] = coeff * row["raw_value"] + offset
        row_out["coeff_slope"] = coeff
        row_out["coeff_offset"] = offset
        calibrated.append(row_out)
    return calibrated


def calibration_summary(calibrated: list[dict]) -> dict:
    """Summary statistics over a calibrated dataset."""
    if not calibrated:
        return {"n": 0, "mean": None, "min": None, "max": None}
    values = [r["calibrated_value"] for r in calibrated]
    return {
        "n": len(values),
        "mean": sum(values) / len(values),
        "min": min(values),
        "max": max(values),
    }
