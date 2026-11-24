import unittest
import tempfile
from pathlib import Path
from log_review import review
from integrity import digest

class LearningTests(unittest.TestCase):
    def test_review(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "events.csv"
            p.write_text("account,result\na,failed\na,failed\n", encoding="utf-8")
            self.assertEqual(review(p, 2), [{"account":"a","failed":2,"review":True}])

    def test_digest(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "sample.txt"
            p.write_bytes(b"abc")
            self.assertEqual(digest(p), "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

if __name__ == "__main__":
    unittest.main()
