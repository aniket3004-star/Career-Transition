import unittest
from datetime import datetime, timezone

from src.astrology.reference_snapshot import ReferenceSnapshot


def snapshot(**overrides):
    values = dict(
        case_id="ref-001",
        reference_source="Swiss Ephemeris",
        reference_version="2.10",
        reference_url="https://www.astro.com/swisseph/",
        calculated_at_utc=datetime(2026, 9, 26, tzinfo=timezone.utc),
        timezone_id="Asia/Kolkata",
        zodiac="sidereal",
        sidereal_mode="Lahiri ICRC",
        ephemeris="Swiss Ephemeris",
        coordinate_frame="geocentric-ecliptic-of-date",
        node_convention="true-node",
        longitudes={"Sun": 100.0, "Moon": 200.0},
        ascendant_longitude=150.0,
    )
    values.update(overrides)
    return ReferenceSnapshot(**values)


class ReferenceSnapshotTests(unittest.TestCase):
    def test_complete_snapshot_validates(self):
        snapshot().validate()

    def test_requires_explicit_sidereal_mode(self):
        with self.assertRaises(ValueError):
            snapshot(sidereal_mode="")

    def test_requires_timezone_aware_timestamp(self):
        with self.assertRaises(ValueError):
            snapshot(calculated_at_utc=datetime(2026, 9, 26))

    def test_rejects_invalid_longitude(self):
        with self.assertRaises(ValueError):
            snapshot(longitudes={"Moon": 360.0})

    def test_rejects_invalid_ascendant(self):
        with self.assertRaises(ValueError):
            snapshot(ascendant_longitude=-0.1)

    def test_requires_explicit_reference_url(self):
        with self.assertRaises(ValueError):
            snapshot(reference_url="Swiss Ephemeris")


if __name__ == "__main__":
    unittest.main()
