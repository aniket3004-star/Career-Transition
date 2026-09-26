import unittest
from datetime import datetime, timezone

from src.astrology.golden_sets import compare_golden_case, compare_longitude_sets
from src.astrology.golden_case import GoldenCase, GoldenCaseMetadata


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


    def test_golden_case_supplies_provenance_and_tolerance(self):
        metadata = GoldenCaseMetadata(
            "case-bound", "reference-A", "2026.1",
            "https://example.invalid/reference",
            datetime(2026, 9, 26, tzinfo=timezone.utc),
            "UTC", "sidereal", "test-ayanamsha", "test-ephemeris",
            "geocentric", "test-node",
        )
        golden_case = GoldenCase(metadata, {"Sun": 20.0}, 0.001)
        evidence = compare_golden_case(golden_case, {"Sun": 20.0005},
                                       datetime(2026, 9, 26, tzinfo=timezone.utc))
        self.assertEqual(evidence[0].case_id, "case-bound")
        self.assertEqual(evidence[0].reference_source, "reference-A")
        self.assertEqual(evidence[0].reference_version, "2026.1")
        self.assertEqual(evidence[0].tolerance_degrees, 0.001)
        self.assertTrue(evidence[0].passed)

    def test_golden_case_rejects_body_mismatch(self):
        metadata = GoldenCaseMetadata(
            "case-bound", "reference-A", "2026.1",
            "https://example.invalid/reference",
            datetime(2026, 9, 26, tzinfo=timezone.utc),
            "UTC", "sidereal", "test-ayanamsha", "test-ephemeris",
            "geocentric", "test-node",
        )
        golden_case = GoldenCase(metadata, {"Sun": 20.0}, 0.001)
        with self.assertRaises(ValueError):
            compare_golden_case(golden_case, {"Moon": 20.0})
