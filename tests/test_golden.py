import unittest
from datetime import datetime, timezone

from src.astrology.golden import (
    GoldenObservation,
    compare_observation,
    circular_difference_degrees,
)


class GoldenComparisonTests(unittest.TestCase):
    def test_wraparound_uses_shortest_angle(self):
        self.assertAlmostEqual(circular_difference_degrees(359.9, 0.1), -0.2)

    def test_exact_match_passes(self):
        e = compare_observation(GoldenObservation(
            "case-001", "Moon", 120.0, 120.0, 0.001, "independent-reference", "v1"
        ), datetime(2026, 9, 26, tzinfo=timezone.utc))
        self.assertTrue(e.passed)
        self.assertEqual(e.delta_degrees, 0.0)

    def test_outside_tolerance_fails(self):
        e = compare_observation(GoldenObservation(
            "case-002", "Sun", 120.0, 120.01, 0.001, "independent-reference", "v1"
        ), datetime(2026, 9, 26, tzinfo=timezone.utc))
        self.assertFalse(e.passed)

    def test_requires_named_reference_and_tolerance(self):
        with self.assertRaises(ValueError):
            compare_observation(GoldenObservation(
                "case-003", "Sun", 120, 120, -0.001, "", ""
            ))

    def test_rejects_naive_comparison_time(self):
        with self.assertRaises(ValueError):
            compare_observation(
                GoldenObservation("case-004", "Sun", 120, 120, 0.1, "ref", "v1"),
                datetime(2026, 9, 26),
            )


if __name__ == "__main__":
    unittest.main()
