"""Calculate SHA-256 of an explicitly selected local file."""
import argparse
import hashlib
from pathlib import Path


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    parser.add_argument("--expected", help="Optional trusted SHA-256 digest")
    args = parser.parse_args()
    try:
        result = sha256_file(args.file)
        print(result)
        if args.expected:
            expected = args.expected.lower()
            if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
                parser.error("Expected digest must contain 64 hexadecimal characters")
            print("MATCH" if expected == result else "DIFFERENT")
            raise SystemExit(0 if expected == result else 1)
    except OSError as exc:
        parser.error(str(exc))
