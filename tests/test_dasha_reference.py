import unittest
from datetime import datetime, timedelta, timezone

from src.astrology.dasha import antardasha_timeline, vimshottari_timeline
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


def priyanka_dharmayana_snapshot():
    return ReferenceSnapshot(
        case_id="priyanka-dalwani-dharmayana-1989-10-20",
        reference_source="Dharmayana Kundli PDF",
        reference_version="kundli-pdf-pages-2-4-50-51",
        reference_url="https://www.dharmayana.in/",
        calculated_at_utc=datetime(2026, 9, 27, tzinfo=timezone.utc),
        timezone_id="Asia/Kolkata",
        zodiac="sidereal",
        sidereal_mode="Lahiri",
        ephemeris="source-kundli",
        coordinate_frame="geocentric-ecliptic",
        node_convention="true",
        longitudes={"Moon": 73.61472222222222},
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

    def test_priyanka_dharmayana_case_matches_dasha_sequence_and_boundaries(self):
        birth = datetime(1989, 10, 20, 5, 23, tzinfo=timezone(timedelta(hours=5, minutes=30)))
        reference = priyanka_dharmayana_snapshot()
        case = DashaReferenceCase(
            case_id=reference.case_id,
            birth_datetime=birth,
            reference=reference,
            expected_starting_lord="Rahu",
        )
        first = case.assert_matches()

        # The PDF prints Moon longitude to arc-second precision. Its displayed
        # Mahadasha transition dates are therefore treated as source observations,
        # with a five-day comparison tolerance rather than false sub-day precision.
        source_transition_dates = (
            datetime(1998, 5, 30, tzinfo=timezone.utc),
            datetime(2014, 5, 30, tzinfo=timezone.utc),
            datetime(2033, 5, 30, tzinfo=timezone.utc),
        )
        case_with_boundaries = DashaReferenceCase(
            case_id=reference.case_id,
            birth_datetime=birth,
            reference=reference,
            expected_starting_lord="Rahu",
            expected_mahadasha_end_dates=source_transition_dates,
            boundary_tolerance_days=5.0,
        )
        periods = case_with_boundaries.assert_mahadasha_boundaries(3)

        self.assertEqual(first.lord, "Rahu")

        saturn = periods[2]
        antardashas = antardasha_timeline(saturn)
        self.assertEqual(
            [period.lord for period in antardashas],
            ["Saturn", "Mercury", "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter"],
        )

        # The source PDF lists Antardasha end dates. Saturn/Moon ends on
        # 2 Dec 2026, so on 27 Sep 2026 the active Antardasha is Moon.
        validation_date = datetime(2026, 9, 27, tzinfo=timezone.utc)
        active = next(
            period for period in antardashas
            if period.start <= validation_date < period.end
        )
        self.assertEqual(active.lord, "Moon")

        source_moon_end = datetime(2026, 12, 2, tzinfo=timezone.utc)
        difference = abs((active.end - source_moon_end).total_seconds())
        self.assertLessEqual(difference, 5 * 86400)

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
