import unittest
from datetime import datetime, timezone

from src.astrology.golden_case import GoldenCaseMetadata


def case(**overrides):
    values = dict(
        case_id="case-001",
        reference_source="independent-reference",
        reference_version="1",
        reference_url="https://example.invalid/reference",
        source_timestamp=datetime(2026, 9, 26, tzinfo=timezone.utc),
        timezone_id="UTC",
        zodiac="sidereal",
        ayanamsha="explicit-convention",
        ephemeris="explicit-ephemeris",
        coordinate_frame="geocentric",
        node_convention="explicit-node-convention",
    )
    values.update(overrides)
    return GoldenCaseMetadata(**values)


class GoldenCaseMetadataTests(unittest.TestCase):
    def test_complete_metadata_validates(self):
        case().validate()

    def test_missing_text_field_rejected(self):
        with self.assertRaises(ValueError):
            case(ayanamsha="")

    def test_naive_source_timestamp_rejected(self):
        with self.assertRaises(ValueError):
            case(source_timestamp=datetime(2026, 9, 26))

    def test_reference_url_must_be_explicit(self):
        with self.assertRaises(ValueError):
            case(reference_url="reference-001")


if __name__ == "__main__":
    unittest.main()
