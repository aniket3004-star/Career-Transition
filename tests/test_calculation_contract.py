import unittest
from datetime import datetime, timezone

from src.astrology.calculation_contract import (
    CalculationRecord,
    CalculationRequest,
    PlanetaryPosition,
)


class CalculationContractTests(unittest.TestCase):
    def test_request_requires_timezone_aware_utc_datetime_by_convention(self):
        request = CalculationRequest(
            birth_datetime_utc=datetime(2000, 1, 15, 6, 30, tzinfo=timezone.utc),
            latitude=20.0,
            longitude=85.0,
            ayanamsha="Lahiri",
            zodiac="sidereal",
            house_system="whole_sign",
        )
        self.assertEqual(request.birth_datetime_utc.tzinfo, timezone.utc)

    def test_position_is_structured_and_unit_explicit(self):
        position = PlanetaryPosition(
            body="Moon",
            longitude=73.6,
            latitude=-1.2,
            distance_au=0.0027,
        )
        self.assertEqual(position.body, "Moon")
        self.assertGreaterEqual(position.longitude, 0.0)
        self.assertLess(position.longitude, 360.0)

    def test_record_preserves_provider_and_provenance(self):
        request = CalculationRequest(
            birth_datetime_utc=datetime(2000, 1, 15, 6, 30, tzinfo=timezone.utc),
            latitude=20.0,
            longitude=85.0,
            ayanamsha="Lahiri",
            zodiac="sidereal",
            house_system="whole_sign",
        )
        record = CalculationRecord(
            provider="test-provider",
            provider_version="1",
            ephemeris="synthetic",
            request=request,
            positions=(),
            calculation_timestamp=datetime(2026, 9, 29, tzinfo=timezone.utc),
            provenance={"source_record_id": "synthetic-001"},
        )
        self.assertEqual(record.provider, "test-provider")
        self.assertEqual(record.provenance["source_record_id"], "synthetic-001")


if __name__ == "__main__":
    unittest.main()
