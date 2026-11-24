"""Compute SHA-256 of a local training file."""
import argparse
import hashlib
from pathlib import Path

def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as file:
        for block in iter(lambda: file.read(65536), b""):
            h.update(block)
    return h.hexdigest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    parser.add_argument("--expected", help="Trusted reference SHA-256")
    args = parser.parse_args()
    try:
        result = digest(args.file)
        print(result)
        if args.expected:
            print("Match" if result == args.expected.lower() else "Mismatch")
    except OSError as exc:
        parser.exit(1, f"Error: {exc}\n")
