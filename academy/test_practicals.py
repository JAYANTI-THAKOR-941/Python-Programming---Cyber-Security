import hashlib
import tempfile
import unittest
from pathlib import Path
from log_review import summarize
from integrity import sha256_file


class PracticeTests(unittest.TestCase):
    def test_log_summary(self):
        rows = [{"account": "a", "outcome": "failed"}] * 3
        self.assertEqual(summarize(rows)["review_accounts"], ["a"])
        self.assertEqual(summarize([])["success_rate"], None)

    def test_bad_record(self):
        with self.assertRaises(ValueError):
            summarize([{"account": "a", "outcome": "unknown"}])

    def test_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / "sample.txt"
            p.write_bytes(b"abc")
            self.assertEqual(sha256_file(p), hashlib.sha256(b"abc").hexdigest())


if __name__ == "__main__":
    unittest.main()
