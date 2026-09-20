import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import cli


class CliTests(unittest.TestCase):
    def _run(self, *args):
        stream = io.StringIO()
        with redirect_stdout(stream):
            code = cli.main(list(args))
        return code, json.loads(stream.getvalue())

    def test_valid_json_returns_schema_only_result(self):
        payload = {
            "birth_date": "2000-01-15",
            "birth_time": "12:00:00",
            "timezone": "Asia/Kolkata",
            "latitude": 20.0,
            "longitude": 85.0,
            "provider": "synthetic-fixture",
            "provider_version": "1",
            "ayanamsha": "Lahiri",
            "zodiac": "sidereal",
            "house_system": "whole_sign",
            "ephemeris": "synthetic-test-ephemeris",
            "calculation_timestamp": "2026-09-19T10:00:00+00:00",
            "provider_settings_verified": True,
            "source_record_id": "synthetic-test-record",
        }
        code, output = self._run("--json", json.dumps(payload))
        self.assertEqual(code, 0)
        self.assertTrue(output["schema_valid"])
        self.assertTrue(output["provenance_complete"])
        self.assertFalse(output["calculation_reproduced"])
        self.assertFalse(output["accuracy_verified"])
        self.assertFalse(output["career_rules_eligible"])
        self.assertIsNone(output["career_outlook"])
        self.assertIn("No planetary positions", output["message"])

    def test_invalid_json_is_rejected(self):
        code, output = self._run("--json", "not-json")
        self.assertEqual(code, 2)
        self.assertFalse(output["schema_valid"])
        self.assertFalse(output["accuracy_verified"])
        self.assertEqual(output["evidence_label"], "quarantined")
        self.assertIn("valid JSON", output["errors"][0])

    def test_save_must_remain_under_outputs(self):
        payload = {"not": "a valid birth envelope"}
        with tempfile.TemporaryDirectory() as temp:
            previous = Path.cwd()
            try:
                import os
                os.chdir(temp)
                code, output = self._run(
                    "--json", json.dumps(payload), "--save", "../escape.json"
                )
            finally:
                os.chdir(previous)
        self.assertEqual(code, 2)
        self.assertFalse(output["schema_valid"])
        self.assertIn("outputs/", output["errors"][0])


if __name__ == "__main__":
    unittest.main()
