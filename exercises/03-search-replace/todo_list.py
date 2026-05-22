"""Various unfinished work scattered across a module."""


def load_observations(path):
    # TODO: validate the file exists before parsing
    # FIXME: this assumes UTF-8; some legacy files are latin-1
    return open(path).read()


def apply_offset(values, offset):
    # XXX: hardcoded sign convention; check with PI before re-running
    return [v + offset for v in values]


def quality_flag(value):
    # TODO: replace with the agreed thresholds from Anderson 2024
    if value < 0:
        return "bad"
    if value > 1000:
        return "saturated"
    return "ok"


def export_report():
    # FIXME: writes to /tmp, should respect OUTPUT_DIR from config
    pass
