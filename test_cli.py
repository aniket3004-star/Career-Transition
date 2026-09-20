import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from cli import main


# Synthetic fixture only; never use real birth details in repository tests.
VALID = {
    "birth_date": "1990-06-15", "birth_time": "14:30", "timezone": "Asia/Kolkata",
    "latitude": 12.9716, "longitude": 77.5946, "provider": "test-provider",
    "provider_version": "1.0", "ayanamsha": "Lahiri", "zodiac": "sidereal",
    "house_system": "Whole Sign", "ephemeris": "Swiss Ephemeris (declared)",
    "calculation_timestamp": "2026-09-19T12:00:00Z", "provider_settings_verified": True,
    "source_record_id": "fixture-001",
}


class CliTests(unittest.TestCase):
    def invoke(self, args):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = main(args)
        return code, json.loads(stream.getvalue())

    def test_valid_envelope_exits_zero_and_never_enables_career_rules(self):
        code, output = self.invoke(["--json", json.dumps(VALID)])
        self.assertEqual(code, 0)
        self.assertTrue(output["schema_valid"])
        self.assertFalse(output["career_rules_eligible"])
        self.assertIsNone(output["career_outlook"])

    def test_missing_ayanamsha_exits_nonzero(self):
        payload = {key: value for key, value in VALID.items() if key != "ayanamsha"}
        code, output = self.invoke(["--json", json.dumps(payload)])
        self.assertEqual(code, 1)
        self.assertFalse(output["schema_valid"])

    def test_malformed_json_returns_structured_error_without_traceback(self):
        code, output = self.invoke(["--json", "{"])
        self.assertEqual(code, 2)
        self.assertFalse(output["schema_valid"])
        self.assertIn("valid JSON", output["errors"][0])

    def test_missing_file_returns_structured_error(self):
        code, output = self.invoke(["--file", "/path/that/does/not/exist.json"])
        self.assertEqual(code, 2)
        self.assertIn("could not be read", output["errors"][0])

    def test_non_object_json_is_rejected(self):
        code, output = self.invoke(["--json", "[]"])
        self.assertEqual(code, 2)
        self.assertIn("JSON object", output["errors"][0])

    def test_save_is_opt_in_and_writes_only_under_gitignored_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            previous = Path.cwd()
            try:
                import os
                os.chdir(directory)
                target = Path("outputs") / "nested" / "result.json"
                code, output = self.invoke(["--json", json.dumps(VALID), "--save", str(target)])
                self.assertEqual(code, 0)
                self.assertEqual(json.loads(target.read_text(encoding="utf-8")), output)
            finally:
                os.chdir(previous)

    def test_save_outside_gitignored_outputs_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "unsafe.json"
            code, output = self.invoke(["--json", json.dumps(VALID), "--save", str(target)])
            self.assertEqual(code, 2)
            self.assertFalse(output["schema_valid"])
            self.assertIn("gitignored outputs", output["errors"][0])

    def test_json_and_file_are_mutually_exclusive(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "input.json"
            target.write_text("{}", encoding="utf-8")
            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit):
                    main(["--json", "{}", "--file", str(target)])


if __name__ == "__main__":
    unittest.main()
