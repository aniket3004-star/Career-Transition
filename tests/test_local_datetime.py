"""Tests for timezone wall-time resolution, not astrology calculations."""
import unittest

from src.validation.local_datetime import resolve_local_datetime


class LocalDateTimeTests(unittest.TestCase):
    def test_ordinary_india_time_is_single_instant(self):
        result = resolve_local_datetime("1987-03-09", "10:17", "Asia/Kolkata")
        self.assertEqual(result.status, "VALID")
        self.assertEqual(len(result.candidates_utc), 1)

    def test_spring_forward_gap_is_rejected(self):
        result = resolve_local_datetime("2024-03-10", "02:30", "America/New_York")
        self.assertEqual(result.status, "NONEXISTENT")
        self.assertEqual(result.candidates_utc, ())

    def test_fall_back_repeated_time_is_ambiguous(self):
        result = resolve_local_datetime("2024-11-03", "01:30", "America/New_York")
        self.assertEqual(result.status, "AMBIGUOUS")
        self.assertEqual(len(result.candidates_utc), 2)
        self.assertNotEqual(result.candidates_utc[0], result.candidates_utc[1])

    def test_invalid_timezone_is_reported(self):
        result = resolve_local_datetime("2024-01-01", "12:00", "Mars/Olympus")
        self.assertEqual(result.status, "INVALID")

    def test_rejects_non_strict_date(self):
        result = resolve_local_datetime("2024-1-1", "12:00", "UTC")
        self.assertEqual(result.status, "INVALID")


if __name__ == "__main__":
    unittest.main()
