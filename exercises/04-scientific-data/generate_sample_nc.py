"""Generate sample.nc for the H5Web viewer exercise.

Run from this directory:

    python generate_sample_nc.py

Produces sample.nc — a CF-style netCDF file with a mix of 1D, 2D, and 3D
variables so H5Web's line plot, heatmap, and dimension-slider views all
have something interesting to show.

Requires: numpy, xarray, netcdf4 (or h5netcdf).
"""

from datetime import datetime, timedelta

import numpy as np
import xarray as xr


FILL = -9999.0


def main() -> None:
    rng = np.random.default_rng(42)

    # ---- 1D / 2D: per-channel calibration time series (unchanged shape) ----
    n_time = 121
    start = datetime(2026, 1, 1, 0, 0, 0)
    times = np.array([start + timedelta(seconds=30 * i) for i in range(n_time)])

    channels = np.array([1, 2, 3])
    n_channels = len(channels)
    channel_means = np.array([10.0, 8.5, 5.0])
    channel_noise = np.array([0.2, 0.2, 0.1])
    channel_slopes = np.array([1.02, 0.97, 1.00])
    channel_offsets = np.array([-0.15, 0.04, 0.00])

    # Add a slow diurnal-ish drift so the line plot has visible structure.
    t_frac = np.linspace(0, 2 * np.pi, n_time)
    drift = 0.3 * np.sin(t_frac)[:, None]

    raw = np.array([
        rng.normal(loc=mean, scale=noise, size=n_time)
        for mean, noise in zip(channel_means, channel_noise)
    ]).T + drift  # (n_time, n_channels)

    calibrated = raw * channel_slopes + channel_offsets

    qflag = rng.choice([0, 1, 2], size=(n_time, n_channels), p=[0.94, 0.05, 0.01])

    # ---- 3D: temperature(time, lat, lon) with realistic spatial structure ----
    n_hour = 24
    lats = np.linspace(-80, 80, 40)
    lons = np.linspace(-180, 175, 60)
    hours = np.arange(n_hour, dtype="float64")

    lat_grid, lon_grid = np.meshgrid(lats, lons, indexing="ij")

    # Latitudinal gradient: warm at equator, cold at poles (~ -30 to 30 C).
    base = 30.0 * np.cos(np.deg2rad(lat_grid)) - 10.0

    # A couple of stationary "continents" — gaussian bumps that warm the surface.
    def bump(lat0, lon0, amp, sigma):
        return amp * np.exp(
            -((lat_grid - lat0) ** 2 + (lon_grid - lon0) ** 2) / (2 * sigma**2)
        )

    land = bump(40, -100, 6, 25) + bump(20, 20, 5, 30) + bump(-25, 135, 4, 20)

    # Diurnal wave that sweeps westward across longitude over 24 h.
    temperature = np.empty((n_hour, lats.size, lons.size), dtype="float32")
    for h in range(n_hour):
        phase = np.deg2rad(lon_grid + 15 * h)
        diurnal = 6.0 * np.cos(phase) * np.cos(np.deg2rad(lat_grid))
        noise = rng.normal(0.0, 0.4, size=lat_grid.shape)
        temperature[h] = (base + land + diurnal + noise).astype("float32")

    # Punch a small "missing data" patch so _FillValue masking is visible.
    temperature[:, 5:9, 10:18] = FILL

    # ---- 2D: a recognizable image — a swirl, for the heatmap demo. ----
    n_px = 128
    yy, xx = np.mgrid[-1:1:n_px * 1j, -1:1:n_px * 1j]
    r = np.sqrt(xx**2 + yy**2)
    theta = np.arctan2(yy, xx)
    swirl = np.exp(-3 * r**2) * np.cos(6 * theta + 8 * r)
    swirl = swirl.astype("float32")

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
            "temperature": (
                ("hour", "lat", "lon"),
                temperature,
                {
                    "units": "degC",
                    "long_name": "Near-surface air temperature",
                    "standard_name": "air_temperature",
                },
            ),
            "swirl": (
                ("y", "x"),
                swirl,
                {
                    "long_name": "Synthetic 2D pattern (swirl)",
                    "units": "1",
                },
            ),
        },
        coords={
            "time": (
                ("time",),
                times,
                {"long_name": "Observation time", "standard_name": "time"},
            ),
            "channel": (
                ("channel",),
                channels,
                {"long_name": "Instrument channel number"},
            ),
            "hour": (
                ("hour",),
                hours,
                {
                    "long_name": "Hour of day (UTC)",
                    "units": "hours since 2026-01-01 00:00:00",
                    "standard_name": "time",
                    "axis": "T",
                },
            ),
            "lat": (
                ("lat",),
                lats.astype("float32"),
                {
                    "long_name": "Latitude",
                    "standard_name": "latitude",
                    "units": "degrees_north",
                    "axis": "Y",
                },
            ),
            "lon": (
                ("lon",),
                lons.astype("float32"),
                {
                    "long_name": "Longitude",
                    "standard_name": "longitude",
                    "units": "degrees_east",
                    "axis": "X",
                },
            ),
            "x": (
                ("x",),
                np.linspace(-1, 1, n_px, dtype="float32"),
                {"long_name": "x", "units": "1", "axis": "X"},
            ),
            "y": (
                ("y",),
                np.linspace(-1, 1, n_px, dtype="float32"),
                {"long_name": "y", "units": "1", "axis": "Y"},
            ),
        },
        attrs={
            "title": "Sample calibration + gridded data — VSCode workshop",
            "institution": "Sample lab",
            "history": "Generated synthetically by generate_sample_nc.py",
            "Conventions": "CF-1.8",
            "source": "VSCode workshop exercise",
            "summary": (
                "Mixed 1D/2D/3D synthetic data: instrument calibration time "
                "series, a global temperature field with a diurnal wave, and "
                "a 2D swirl pattern — chosen so H5Web's line, heatmap, and "
                "slider views all render something visually distinct."
            ),
        },
    )

    # Encoding: compress the bigger arrays so the file stays small.
    encoding = {
        "temperature": {"zlib": True, "complevel": 4, "_FillValue": np.float32(FILL)},
        "swirl": {"zlib": True, "complevel": 4},
    }
    ds.to_netcdf("sample.nc", encoding=encoding)
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

    fig, axes = plt.subplots(2, 2, figsize=(11, 8))

    # Top-left: calibration histograms (the original plot).
    for i, ch in enumerate(channels):
        axes[0, 0].hist(raw[:, i], bins=20, alpha=0.6, label=f"ch {ch}")
        axes[0, 1].hist(calibrated[:, i], bins=20, alpha=0.6, label=f"ch {ch}")
    axes[0, 0].set_title("Raw")
    axes[0, 1].set_title("Calibrated")
    for ax in axes[0]:
        ax.set_xlabel("value")
        ax.legend()
    axes[0, 0].set_ylabel("count")

    # Bottom-left: a temperature snapshot.
    snap = np.where(temperature[12] == FILL, np.nan, temperature[12])
    im = axes[1, 0].imshow(
        snap,
        origin="lower",
        extent=[lons.min(), lons.max(), lats.min(), lats.max()],
        cmap="RdYlBu_r",
        aspect="auto",
    )
    axes[1, 0].set_title("temperature, hour=12")
    axes[1, 0].set_xlabel("lon")
    axes[1, 0].set_ylabel("lat")
    fig.colorbar(im, ax=axes[1, 0], label="degC")

    # Bottom-right: the swirl.
    im2 = axes[1, 1].imshow(swirl, origin="lower", extent=[-1, 1, -1, 1], cmap="viridis")
    axes[1, 1].set_title("swirl")
    axes[1, 1].set_xlabel("x")
    axes[1, 1].set_ylabel("y")
    fig.colorbar(im2, ax=axes[1, 1])

    fig.suptitle("Sample calibration + gridded data")
    fig.tight_layout()
    fig.savefig("sample_plot.png", dpi=120)
    print("Wrote sample_plot.png")


if __name__ == "__main__":
    main()
