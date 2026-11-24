"""Review synthetic/local CSV authentication events without network access."""
import argparse
import csv
import json
from collections import Counter


def summarize(records, threshold=3):
    if not isinstance(threshold, int) or threshold < 1:
        raise ValueError("Threshold must be a positive integer")
    failed = Counter()
    total = successes = 0
    for record in records:
        account = (record.get("account") or "").strip()
        outcome = (record.get("outcome") or "").strip().lower()
        if not account or outcome not in {"success", "failed"}:
            raise ValueError("Malformed authentication record")
        total += 1
        if outcome == "failed":
            failed[account] += 1
        else:
            successes += 1
    return {
        "total": total,
        "successes": successes,
        "failures": total - successes,
        "success_rate": successes / total if total else None,
        "review_accounts": sorted(k for k, v in failed.items() if v >= threshold),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    parser.add_argument("--threshold", type=int, default=3)
    args = parser.parse_args()
    try:
        with open(args.file, newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if not {"account", "outcome"}.issubset(reader.fieldnames or []):
                raise ValueError("Required columns: account, outcome")
            print(json.dumps(summarize(reader, args.threshold), indent=2))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
