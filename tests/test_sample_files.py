import csv
from pathlib import Path
import unittest

SAMPLES = Path(__file__).resolve().parents[1] / "samples"

class SampleFileContract(unittest.TestCase):
    def test_every_csv_is_readable_and_rectangular(self):
        paths = sorted(SAMPLES.glob("*.csv"))
        self.assertGreaterEqual(len(paths), 4)
        for path in paths:
            with self.subTest(file=path.name):
                with path.open(encoding="utf-8", newline="") as source:
                    reader = csv.DictReader(source, strict=True)
                    self.assertGreaterEqual(len(reader.fieldnames or []), 2)
                    self.assertEqual(len(reader.fieldnames), len(set(reader.fieldnames)))
                    rows = list(reader)
                self.assertTrue(rows)
                self.assertTrue(all(None not in row for row in rows))
                self.assertTrue(all(None not in row.values() for row in rows))

if __name__ == "__main__":
    unittest.main()
