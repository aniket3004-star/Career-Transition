import json
import unittest

from src.cli import main


class CliTests(unittest.TestCase):
    def test_valid_envelope_exits_zero(self):
        payload = {
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
        code = main(["--json", json.dumps(payload)])
        self.assertEqual(code, 0)

    def test_missing_ayanamsha_exits_nonzero(self):
        payload = {
            "birth_date": "1987-03-09",
            "birth_time": "10:17",
            "timezone": "Asia/Kolkata",
            "latitude": 20.4625,
            "longitude": 85.8828,
            "provider": "test-provider",
            "provider_version": "1.0",
            "zodiac": "sidereal",
            "house_system": "Whole Sign",
            "ephemeris": "Swiss Ephemeris (declared)",
            "calculation_timestamp": "2026-09-19T12:00:00Z",
            "provider_settings_verified": True,
        }
        code = main(["--json", json.dumps(payload)])
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
