import unittest

from src.astrology.sidereal import convert_longitudes, tropical_to_sidereal


class SiderealConversionTests(unittest.TestCase):
    def test_wraps_below_zero(self):
        self.assertAlmostEqual(tropical_to_sidereal(5.0, 24.0), 341.0)

    def test_wraps_above_360(self):
        self.assertAlmostEqual(tropical_to_sidereal(359.0, -5.0), 4.0)

    def test_conversion_is_explicit_and_reproducible(self):
        result = convert_longitudes(
            {"Sun": 100.0, "Moon": 200.0},
            "Test Convention",
            24.0,
        )
        self.assertEqual(result.ayanamsha_name, "Test Convention")
        self.assertEqual(result.ayanamsha_degrees, 24.0)
        self.assertEqual(result.sidereal_longitudes["Sun"], 76.0)
        self.assertEqual(result.sidereal_longitudes["Moon"], 176.0)

    def test_requires_named_convention(self):
        with self.assertRaises(ValueError):
            convert_longitudes({"Sun": 100.0}, "", 24.0)

    def test_rejects_non_finite_offset(self):
        with self.assertRaises(ValueError):
            tropical_to_sidereal(100.0, float("nan"))


if __name__ == "__main__":
    unittest.main()
