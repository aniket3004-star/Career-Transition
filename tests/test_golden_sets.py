import unittest
from datetime import datetime, timezone

from src.astrology.golden_sets import compare_longitude_sets


class GoldenSetComparisonTests(unittest.TestCase):
    def test_compares_complete_matching_set(self):
        evidence = compare_longitude_sets(
            {"Moon": 10.0, "Sun": 20.0},
            {"Moon": 10.0005, "Sun": 19.9995},
            "independent-reference", "v1", 0.001, "case-001",
            datetime(2026, 9, 26, tzinfo=timezone.utc),
        )
        self.assertEqual(len(evidence), 2)
        self.assertTrue(all(item.passed for item in evidence))

    def test_rejects_missing_body(self):
        with self.assertRaises(ValueError):
            compare_longitude_sets(
                {"Moon": 10.0, "Sun": 20.0},
                {"Moon": 10.0},
                "ref", "v1", 0.001, "case-002",
            )

    def test_rejects_extra_body(self):
        with self.assertRaises(ValueError):
            compare_longitude_sets(
                {"Moon": 10.0},
                {"Moon": 10.0, "Sun": 20.0},
                "ref", "v1", 0.001, "case-003",
            )

    def test_does_not_hide_failed_body(self):
        evidence = compare_longitude_sets(
            {"Moon": 10.0},
            {"Moon": 10.01},
            "ref", "v1", 0.001, "case-004",
        )
        self.assertFalse(evidence[0].passed)


if __name__ == "__main__":
    unittest.main()
