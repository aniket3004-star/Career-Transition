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

    def test_rejects_numeric_timezone_offset(self):
        payload = dict(VALID, timezone="+05:30")
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)
        self.assertTrue(any("IANA timezone" in error for error in result.errors))

    def test_rejects_out_of_range_coordinates(self):
        payload = dict(VALID, latitude=91)
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)

    def test_rejects_naive_calculation_timestamp(self):
        payload = dict(VALID, calculation_timestamp="2026-09-19T12:00:00")
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)

    def test_rejects_non_strict_birth_date_format(self):
        payload = dict(VALID, birth_date="1987-3-9")
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)

    def test_rejects_invalid_birth_date(self):
        payload = dict(VALID, birth_date="1987-02-30")
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)

    def test_rejects_invalid_birth_time(self):
        payload = dict(VALID, birth_time="25:17")
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)

    def test_rejects_nonexistent_local_birth_time(self):
        payload = dict(VALID, birth_date="2024-03-10", birth_time="02:30", timezone="America/New_York")
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)
        self.assertTrue(any("nonexistent" in error for error in result.errors))

    def test_rejects_ambiguous_local_birth_time(self):
        payload = dict(VALID, birth_date="2024-11-03", birth_time="01:30", timezone="America/New_York")
        result = validate_birth_input(payload)
        self.assertFalse(result.valid)
        self.assertTrue(any("ambiguous" in error for error in result.errors))

    def test_warns_when_source_record_id_is_absent(self):
        payload = dict(VALID)
        payload.pop("source_record_id")
        result = validate_birth_input(payload)
        self.assertTrue(result.valid, result.errors)
        self.assertTrue(result.warnings)


if __name__ == "__main__":
    unittest.main()
