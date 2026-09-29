import json
import unittest
from pathlib import Path


FIXTURE = Path(__file__).parent / "fixtures" / "astronomy_goldens.json"


class AstronomyGoldenRegistryTests(unittest.TestCase):
    def test_registry_schema_requires_reproducible_reference_metadata(self):
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))

        self.assertEqual(payload["schema_version"], 1)
        self.assertEqual(payload["status"], "REFERENCE_PENDING")
        self.assertGreaterEqual(len(payload["cases"]), 1)

        for case in payload["cases"]:
            self.assertIsInstance(case.get("case_id"), str)
            self.assertTrue(case["case_id"].strip())
            self.assertIn(case["status"], {"REFERENCE_PENDING", "CERTIFIED"})

            for field in (
                "target",
                "center",
                "input_time",
                "time_scale",
                "calendar_convention",
                "reference_frame",
                "reference_plane",
                "treatment",
                "quantity",
                "units",
                "source",
                "query_settings",
                "provenance_url",
                "captured_value",
                "tolerance",
                "capture_date",
                "notes",
            ):
                self.assertIn(field, case)

            for endpoint in ("target", "center"):
                self.assertIsInstance(case[endpoint], dict)
                self.assertTrue(str(case[endpoint].get("id", "")).strip())
                self.assertTrue(str(case[endpoint].get("name", "")).strip())

            self.assertIsInstance(case["query_settings"], dict)
            self.assertTrue(case["query_settings"])
            self.assertTrue(case["provenance_url"].startswith("https://"))
            self.assertTrue(case["source"]["url"].startswith("https://"))
            self.assertTrue(case["source"]["api_documentation"].startswith("https://"))
            self.assertTrue(str(case["source"].get("name", "")).strip())
            self.assertTrue(str(case["source"].get("version", "")).strip())

            if case["status"] == "REFERENCE_PENDING":
                self.assertIsNone(case["captured_value"])
                self.assertIsNone(case["tolerance"])
                self.assertIsNone(case["capture_date"])
            else:
                self.assertIsNotNone(case["captured_value"])
                self.assertIsNotNone(case["tolerance"])
                self.assertIsNotNone(case["capture_date"])


if __name__ == "__main__":
    unittest.main()
