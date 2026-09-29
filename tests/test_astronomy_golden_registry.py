import json
import unittest
from pathlib import Path


FIXTURE = Path(__file__).parent / "fixtures" / "astronomy_goldens.json"


class AstronomyGoldenRegistryTests(unittest.TestCase):
    def test_registry_is_explicitly_pending_until_reference_values_are_captured(self):
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))

        self.assertEqual(payload["schema_version"], 1)
        self.assertEqual(payload["status"], "REFERENCE_PENDING")
        self.assertGreaterEqual(len(payload["cases"]), 1)

        for case in payload["cases"]:
            self.assertIn("case_id", case)
            self.assertIn(case["status"], {"REFERENCE_PENDING", "CERTIFIED"})
            self.assertIn("target", case)
            self.assertIn("center", case)
            self.assertIn("input_time", case)
            self.assertIn("time_scale", case)
            self.assertIn("reference_frame", case)
            self.assertIn("reference_plane", case)
            self.assertIn("treatment", case)
            self.assertIn("quantity", case)
            self.assertIn("units", case)
            self.assertIn("source", case)
            self.assertIn("url", case["source"])

            if case["status"] == "REFERENCE_PENDING":
                self.assertIsNone(case["captured_value"])
                self.assertIsNone(case["tolerance"])
            else:
                self.assertIsNotNone(case["captured_value"])
                self.assertIsNotNone(case["tolerance"])


if __name__ == "__main__":
    unittest.main()
