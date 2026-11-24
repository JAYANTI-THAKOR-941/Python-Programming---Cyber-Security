"""Summarize failed logins in a local fictional CSV."""
import argparse
import csv
from collections import Counter
from pathlib import Path

def review(path, threshold=3):
    if threshold < 1:
        raise ValueError("Threshold must be positive")
    counts = Counter()
    with Path(path).open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not {"account", "result"} <= set(reader.fieldnames or []):
            raise ValueError("Expected account and result columns")
        for row in reader:
            account = (row.get("account") or "").strip()
            result = (row.get("result") or "").strip().lower()
            if not account or result not in {"success", "failed"}:
                raise ValueError("Invalid event row")
            if result == "failed":
                counts[account] += 1
    return [{"account": name, "failed": count, "review": count >= threshold}
            for name, count in sorted(counts.items())]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    parser.add_argument("--threshold", type=int, default=3)
    args = parser.parse_args()
    try:
        for item in review(args.file, args.threshold):
            print(item)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")
