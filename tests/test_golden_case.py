import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from src.astrology.golden_case import GoldenCaseMetadata, load_golden_case


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


def payload(**overrides):
    values = dict(
        metadata={
            "case_id": "synthetic-loader-001",
            "reference_source": "synthetic-test-reference",
            "reference_version": "test-1",
            "reference_url": "https://example.invalid/reference",
            "source_timestamp": "2026-09-26T00:00:00+00:00",
            "timezone_id": "UTC",
            "zodiac": "sidereal",
            "ayanamsha": "test-convention",
            "ephemeris": "test-ephemeris",
            "coordinate_frame": "geocentric",
            "node_convention": "test-node",
        },
        expected_longitudes={"Sun": 10.0, "Moon": 20.0},
        tolerance_degrees=0.001,
    )
    values.update(overrides)
    return values


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


class GoldenCaseLoaderTests(unittest.TestCase):
    def write_json(self, data):
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
        with handle:
            json.dump(data, handle)
        return Path(handle.name)

    def test_loads_complete_provenance_bound_case(self):
        path = self.write_json(payload())
        try:
            loaded = load_golden_case(path)
            self.assertEqual(loaded.metadata.case_id, "synthetic-loader-001")
            self.assertEqual(loaded.expected_longitudes["Sun"], 10.0)
        finally:
            path.unlink()

    def test_missing_metadata_rejected(self):
        data = payload()
        del data["metadata"]["ayanamsha"]
        path = self.write_json(data)
        try:
            with self.assertRaises(ValueError):
                load_golden_case(path)
        finally:
            path.unlink()

    def test_invalid_longitude_rejected(self):
        data = payload(expected_longitudes={"Sun": 360.0})
        path = self.write_json(data)
        try:
            with self.assertRaises(ValueError):
                load_golden_case(path)
        finally:
            path.unlink()

    def test_invalid_tolerance_rejected(self):
        data = payload(tolerance_degrees=-0.1)
        path = self.write_json(data)
        try:
            with self.assertRaises(ValueError):
                load_golden_case(path)
        finally:
            path.unlink()


if __name__ == "__main__":
    unittest.main()
