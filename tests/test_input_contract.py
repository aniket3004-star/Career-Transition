"""Unit tests for input schema checks; these do not validate astrology math."""
import unittest

from src.validation.input_contract import validate_birth_input


VALID = {
    "birth_date": "1987-03-09",
    "birth_time": "10:17",
    "timezone": "Asia/Kolkata",
    "latitude": 20.4625,
    "longitude": 85.8828,
    "provider": "test-provider",
    "provider_version": "1.0",
    "ayanamsha": "Lahiri",
    "zodiac": "sidereal",
    "house_system": "Whole Sign",
    "ephemeris": "Swiss Ephemeris (declared)",
    "calculation_timestamp": "2026-09-19T12:00:00Z",
    "provider_settings_verified": True,
    "source_record_id": "fixture-001",
}


class InputContractTests(unittest.TestCase):
    def test_accepts_complete_explicit_metadata(self):
        result = validate_birth_input(VALID)
        self.assertTrue(result.valid, result.errors)
        self.assertEqual(result.evidence_label, "INPUT_SCHEMA_ONLY")

    def test_rejects_missing_configuration_instead_of_defaulting(self):
        payload = dict(VALID)
        payload.pop("ayanamsha")
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)
        self.assertTrue(any("ayanamsha" in error for error in result.errors))

    def test_rejects_unverified_provider_settings(self):
        payload = dict(VALID, provider_settings_verified=False)
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)

    def test_rejects_unknown_timezone(self):
        payload = dict(VALID, timezone="Mars/Olympus")
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)

    def test_rejects_out_of_range_coordinates(self):
        payload = dict(VALID, latitude=91)
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)

    def test_rejects_naive_calculation_timestamp(self):
        payload = dict(VALID, calculation_timestamp="2026-09-19T12:00:00")
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)

    def test_warns_when_source_record_id_is_absent(self):
        payload = dict(VALID)
        payload.pop("source_record_id")
        result = validate_birth_input(payload)
        self.assertTrue(result.valid, result.errors)
        self.assertTrue(result.warnings)


if __name__ == "__main__":
    unittest.main()
