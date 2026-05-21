"""Load and pre-process raw instrument observations."""

from datetime import datetime
from pathlib import Path


def load_raw_data(path: Path) -> list[dict]:
    """Read raw observations from a CSV-like file.

    Returns a list of dicts: {timestamp, channel, raw_value}.
    """
    rows = []
    for line in path.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        ts, channel, value = line.split(",")
        rows.append(
            {
                "timestamp": parse_timestamp(ts),
                "channel": int(channel),
                "raw_value": float(value),
            }
        )
    return rows


def parse_timestamp(ts: str) -> datetime:
    """Parse an ISO-8601 timestamp string."""
    return datetime.fromisoformat(ts)


def is_within_window(
    timestamp: datetime,
    start: datetime,
    end: datetime,
) -> bool:
    """Return True if timestamp falls within [start, end]."""
    return start <= timestamp <= end
