import unittest
from datetime import datetime, timezone

from src.astrology.astropy_reference import calculate_tropical_longitudes


class AstropyReferenceTests(unittest.TestCase):
    def test_rejects_naive_datetime(self):
        with self.assertRaises(ValueError):
            calculate_tropical_longitudes(datetime(2000, 1, 1), 0, 0)

    def test_rejects_invalid_location(self):
        with self.assertRaises(ValueError):
            calculate_tropical_longitudes(
                datetime(2000, 1, 1, tzinfo=timezone.utc), 91, 0
            )

    def test_dependency_boundary_is_explicit(self):
        try:
            result = calculate_tropical_longitudes(
                datetime(2000, 1, 15, 6, 30, tzinfo=timezone.utc), 20, 85
            )
        except RuntimeError as exc:
            self.assertIn("astropy", str(exc).lower())
        else:
            self.assertEqual(set(result), {
                "Sun", "Moon", "Mercury", "Venus", "Mars",
                "Jupiter", "Saturn", "Uranus", "Neptune",
            })
            self.assertTrue(all(0 <= value < 360 for value in result.values()))


if __name__ == "__main__":
    unittest.main()
