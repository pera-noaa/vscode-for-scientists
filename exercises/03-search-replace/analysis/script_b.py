"""Weekly QC report."""


def collect_metrics(records):
    # XXX: 'records' is a list-of-dicts now; will be a DataFrame after PR #42
    return {
        "n": len(records),
        "n_bad": sum(1 for r in records if r.get("flag") == "bad"),
    }


def render_report(metrics):
    # TODO: replace this string template with the markdown one from docs/
    return f"Weekly QC: n={metrics['n']}, bad={metrics['n_bad']}"
