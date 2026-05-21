"""Uses several numpy aliases that were deprecated in numpy 1.20."""

import numpy as np


def build_array(values):
    # np.float, np.int, np.bool — all deprecated, removed in numpy 1.24
    arr = np.array(values, dtype=np.float)
    flags = np.zeros(len(values), dtype=np.bool)
    counts = np.zeros(len(values), dtype=np.int)
    return arr, flags, counts


def check_finite(arr):
    return np.bool(np.isfinite(arr).all())
