import unittest
from datetime import datetime, timezone

from src.astrology.dasha import (
    DASHA_YEARS, antardasha_timeline, vimshottari_timeline,
)


class VimshottariTests(unittest.TestCase):
    def test_zero_longitude_starts_ketu_with_full_period(self):
        periods = vimshottari_timeline(datetime(2000, 1, 1, tzinfo=timezone.utc), 0, 2)
        self.assertEqual([p.lord for p in periods], ["Ketu", "Venus"])
        self.assertAlmostEqual((periods[0].end - periods[0].start).total_seconds(),
                               DASHA_YEARS["Ketu"] * 365.2425 * 86400)
        self.assertEqual(periods[0].end, periods[1].start)

    def test_mid_nakshatra_has_half_of_starting_dasha(self):
        moon = (360 / 27) / 2
        periods = vimshottari_timeline(datetime(2000, 1, 1, tzinfo=timezone.utc), moon, 1)
        self.assertEqual(periods[0].lord, "Ketu")
        self.assertAlmostEqual((periods[0].end - periods[0].start).total_seconds(),
                               3.5 * 365.2425 * 86400)

    def test_longitude_wraps_to_correct_lord(self):
        periods = vimshottari_timeline(datetime(2000, 1, 1, tzinfo=timezone.utc), 359.999, 2)
        self.assertEqual(periods[0].lord, "Mercury")
        self.assertEqual(periods[1].lord, "Ketu")

    def test_antardashas_are_ordered_and_cover_mahadasha(self):
        md = vimshottari_timeline(datetime(2000, 1, 1, tzinfo=timezone.utc), 100, 1)[0]
        ads = antardasha_timeline(md)
        self.assertEqual(len(ads), 9)
        self.assertEqual(ads[0].start, md.start)
        self.assertEqual(ads[-1].end, md.end)
        self.assertTrue(all(a.end == b.start for a, b in zip(ads, ads[1:])))

    def test_rejects_naive_datetime_and_bad_inputs(self):
        with self.assertRaises(ValueError):
            vimshottari_timeline(datetime(2000, 1, 1), 0)
        for longitude in (-0.1, 360, float("nan"), float("inf"), True, "12"):
            with self.assertRaises(ValueError):
                vimshottari_timeline(datetime(2000, 1, 1, tzinfo=timezone.utc), longitude)
        for count in (0, 109, True, 2.5, "2"):
            with self.assertRaises(ValueError):
                vimshottari_timeline(datetime(2000, 1, 1, tzinfo=timezone.utc), 0, count)

    def test_rejects_non_datetime_birth_value(self):
        with self.assertRaises(ValueError):
            vimshottari_timeline("2000-01-01", 0)

    def test_rejects_invalid_antardasha_object(self):
        with self.assertRaises(ValueError):
            antardasha_timeline(None)


if __name__ == "__main__":
    unittest.main()
