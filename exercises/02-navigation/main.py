"""Entry point: run a calibration over a sample observations file."""

from pathlib import Path

from calibration import apply_calibration, calibration_summary
from data_loader import parse_timestamp


def main() -> None:
    sample = Path(__file__).parent / "sample_observations.csv"
    if not sample.exists():
        print("No sample file; writing one.")
        sample.write_text(
            "# timestamp,channel,raw_value\n"
            "2026-01-01T00:00:00,1,12.4\n"
            "2026-01-01T00:00:01,2,8.7\n"
            "2026-01-01T00:00:02,1,12.8\n"
            "2026-01-01T00:00:03,3,5.0\n"
            "2026-01-01T00:00:04,2,8.5\n"
        )

    calibrated = apply_calibration(sample)
    summary = calibration_summary(calibrated)

    first_ts = parse_timestamp("2026-01-01T00:00:00")
    print(f"Calibration run starting {first_ts}")
    print(f"  n = {summary['n']}")
    print(f"  mean = {summary['mean']:.3f}")
    print(f"  min = {summary['min']:.3f}")
    print(f"  max = {summary['max']:.3f}")


if __name__ == "__main__":
    main()
