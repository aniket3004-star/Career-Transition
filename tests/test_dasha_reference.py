import unittest
from datetime import datetime, timezone

from src.astrology.dasha_reference import (
    DashaReferenceCase,
    validate_dasha_reference_cases,
)
from src.astrology.reference_snapshot import ReferenceSnapshot


def snapshot(case_id, moon):
    return ReferenceSnapshot(
        case_id=case_id,
        reference_source="synthetic-test-fixture",
        reference_version="test-1",
        reference_url="https://example.com/reference",
        calculated_at_utc=datetime(2026, 1, 1, tzinfo=timezone.utc),
        timezone_id="UTC",
        zodiac="sidereal",
        sidereal_mode="Lahiri",
        ephemeris="synthetic",
        coordinate_frame="geocentric-ecliptic",
        node_convention="true",
        longitudes={"Moon": moon},
        ascendant_longitude=0.0,
    )


class DashaReferenceTests(unittest.TestCase):
    def test_single_reference_case_matches_starting_lord(self):
        case = DashaReferenceCase(
            case_id="case-ketu",
            birth_datetime=datetime(2000, 1, 1, tzinfo=timezone.utc),
            reference=snapshot("case-ketu", 0.0),
            expected_starting_lord="Ketu",
        )
        period = case.assert_matches()
        self.assertEqual(period.lord, "Ketu")

    def test_multiple_reference_cases_are_evaluated_independently(self):
        boundary = 360.0 / 27.0
        cases = (
            DashaReferenceCase(
                case_id="case-ketu",
                birth_datetime=datetime(2000, 1, 1, tzinfo=timezone.utc),
                reference=snapshot("case-ketu", 0.0),
                expected_starting_lord="Ketu",
            ),
            DashaReferenceCase(
                case_id="case-venus",
                birth_datetime=datetime(2001, 1, 1, tzinfo=timezone.utc),
                reference=snapshot("case-venus", boundary),
                expected_starting_lord="Venus",
            ),
            DashaReferenceCase(
                case_id="case-mercury",
                birth_datetime=datetime(2002, 1, 1, tzinfo=timezone.utc),
                reference=snapshot("case-mercury", 8 * boundary),
                expected_starting_lord="Mercury",
            ),
        )
        periods = validate_dasha_reference_cases(cases)
        self.assertEqual([p.lord for p in periods], ["Ketu", "Venus", "Mercury"])

    def test_missing_moon_is_rejected(self):
        ref = snapshot("missing-moon", 0.0)
        object.__setattr__(ref, "longitudes", {})
        case = DashaReferenceCase(
            case_id="missing-moon",
            birth_datetime=datetime(2000, 1, 1, tzinfo=timezone.utc),
            reference=ref,
            expected_starting_lord="Ketu",
        )
        with self.assertRaises(ValueError):
            case.assert_matches()

    def test_naive_birth_datetime_is_rejected(self):
        case = DashaReferenceCase(
            case_id="naive",
            birth_datetime=datetime(2000, 1, 1),
            reference=snapshot("naive", 0.0),
            expected_starting_lord="Ketu",
        )
        with self.assertRaises(ValueError):
            case.assert_matches()

    def test_wrong_expected_lord_is_rejected(self):
        case = DashaReferenceCase(
            case_id="wrong-lord",
            birth_datetime=datetime(2000, 1, 1, tzinfo=timezone.utc),
            reference=snapshot("wrong-lord", 0.0),
            expected_starting_lord="Venus",
        )
        with self.assertRaises(AssertionError):
            case.assert_matches()


if __name__ == "__main__":
    unittest.main()
