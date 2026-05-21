"""Daily summary script for the phoenix-prototype calibration runs."""

import yaml


def load_config():
    # TODO: error-handle missing config gracefully
    with open("config.yaml") as f:
        return yaml.safe_load(f)


def main():
    cfg = load_config()
    if cfg["project"] != "phoenix-prototype":
        raise ValueError("This script only supports phoenix-prototype.")
    print(f"Running daily summary for {cfg['project']} v{cfg['version']}")


if __name__ == "__main__":
    main()
