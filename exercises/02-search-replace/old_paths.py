"""A handful of stale hardcoded paths from a previous user's setup."""

INPUT_DIR = "/home/old_user/data/inputs"
OUTPUT_DIR = "/home/old_user/data/outputs"
COEFF_FILE = "/home/old_user/calibration/coeffs_2024.csv"
LOG_DIR = "/home/old_user/logs"
ARCHIVE = "/home/old_user/archive/2023"


def get_input_path(name: str) -> str:
    return f"{INPUT_DIR}/{name}.nc"


def get_output_path(name: str) -> str:
    return f"{OUTPUT_DIR}/{name}.calibrated.nc"
