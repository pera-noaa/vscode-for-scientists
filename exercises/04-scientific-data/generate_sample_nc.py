"""Generate sample.nc for the H5Web viewer exercise.

Run from this directory:

    python generate_sample_nc.py

Produces sample.nc — a small CF-style netCDF file with three channels
of synthetic instrument data over one hour at 30-second resolution.

Requires: numpy, xarray, netcdf4 (or h5netcdf).
"""

from datetime import datetime, timedelta

import numpy as np
import xarray as xr


def main() -> None:
    rng = np.random.default_rng(42)

    # 1 hour at 30 s -> 121 timesteps
    n_time = 121
    start = datetime(2026, 1, 1, 0, 0, 0)
    times = np.array([start + timedelta(seconds=30 * i) for i in range(n_time)])

    channels = np.array([1, 2, 3])
    n_channels = len(channels)

    # Per-channel mean and noise
    channel_means = np.array([10.0, 8.5, 5.0])
    channel_noise = np.array([0.2, 0.2, 0.1])
    channel_slopes = np.array([1.02, 0.97, 1.00])
    channel_offsets = np.array([-0.15, 0.04, 0.00])

    # Raw observations: (time, channel)
    raw = np.array([
        rng.normal(loc=mean, scale=noise, size=n_time)
        for mean, noise in zip(channel_means, channel_noise)
    ]).T  # shape (n_time, n_channels)

    calibrated = raw * channel_slopes + channel_offsets

    # Quality flags: mostly 0, a few 1s
    qflag = rng.choice([0, 1, 2], size=(n_time, n_channels), p=[0.94, 0.05, 0.01])

    ds = xr.Dataset(
        data_vars={
            "raw_value": (
                ("time", "channel"),
                raw,
                {"units": "counts", "long_name": "Raw instrument reading"},
            ),
            "calibrated_value": (
                ("time", "channel"),
                calibrated,
                {"units": "ppb", "long_name": "Calibrated mixing ratio"},
            ),
            "quality_flag": (
                ("time", "channel"),
                qflag.astype("int8"),
                {
                    "long_name": "Quality flag",
                    "flag_values": [0, 1, 2],
                    "flag_meanings": "ok suspect bad",
                },
            ),
            "slope": (
                ("channel",),
                channel_slopes,
                {"long_name": "Calibration slope per channel"},
            ),
            "offset": (
                ("channel",),
                channel_offsets,
                {"long_name": "Calibration offset per channel"},
            ),
        },
        coords={
            "time": (
                ("time",),
                times,
                {"long_name": "Observation time"},
            ),
            "channel": (
                ("channel",),
                channels,
                {"long_name": "Instrument channel number"},
            ),
        },
        attrs={
            "title": "Sample calibration data — VSCode workshop",
            "institution": "Sample lab",
            "history": "Generated synthetically by generate_sample_nc.py",
            "Conventions": "CF-1.8",
            "source": "VSCode workshop exercise",
        },
    )

    ds.to_netcdf("sample.nc")
    print("Wrote sample.nc:")
    print(ds)

    # Also write a PNG plot, so the workshop can demo VSCode's built-in
    # image viewer over Remote-SSH (click the .png in the file tree and
    # it renders in a tab — no scp needed).
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nmatplotlib not available; skipping PNG (pip install matplotlib to enable).")
        return

    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
    for i, ch in enumerate(channels):
        axes[0].hist(raw[:, i], bins=20, alpha=0.6, label=f"ch {ch}")
        axes[1].hist(calibrated[:, i], bins=20, alpha=0.6, label=f"ch {ch}")
    axes[0].set_title("Raw")
    axes[1].set_title("Calibrated")
    for ax in axes:
        ax.set_xlabel("value")
        ax.legend()
    axes[0].set_ylabel("count")
    fig.suptitle("Sample calibration data")
    fig.tight_layout()
    fig.savefig("sample_plot.png", dpi=120)
    print("Wrote sample_plot.png")


if __name__ == "__main__":
    main()
