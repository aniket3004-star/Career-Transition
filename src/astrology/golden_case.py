"""Auditable metadata and loading boundary for astronomy golden cases.

Expected astronomical values are external data; this module never computes them.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import json
import math
from pathlib import Path
from typing import Mapping

from src.astrology.golden import GoldenObservation


@dataclass(frozen=True)
class GoldenCaseMetadata:
    case_id: str
    reference_source: str
    reference_version: str
    reference_url: str
    source_timestamp: datetime
    timezone_id: str
    zodiac: str
    ayanamsha: str
    ephemeris: str
    coordinate_frame: str
    node_convention: str

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        required = {
            "case_id": self.case_id,
            "reference_source": self.reference_source,
            "reference_version": self.reference_version,
            "reference_url": self.reference_url,
            "timezone_id": self.timezone_id,
            "zodiac": self.zodiac,
            "ayanamsha": self.ayanamsha,
            "ephemeris": self.ephemeris,
            "coordinate_frame": self.coordinate_frame,
            "node_convention": self.node_convention,
        }
        if any(not isinstance(v, str) or not v.strip() for v in required.values()):
            raise ValueError("golden-case metadata contains a missing text field")
        if not isinstance(self.source_timestamp, datetime):
            raise ValueError("source_timestamp must be a datetime")
        if self.source_timestamp.tzinfo is None or self.source_timestamp.utcoffset() is None:
            raise ValueError("source_timestamp must be timezone-aware")
        if not self.reference_url.startswith(("https://", "http://")):
            raise ValueError("reference_url must be an explicit URL")


@dataclass(frozen=True)
class GoldenCase:
    metadata: GoldenCaseMetadata
    expected_longitudes: dict[str, float]
    tolerance_degrees: float

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        self.metadata.validate()

    def assert_compatible(
        self,
        *,
        timezone_id: str,
        zodiac: str,
        ayanamsha: str,
        ephemeris: str,
        coordinate_frame: str,
        node_convention: str,
    ) -> None:
        """Reject comparison when calculation conventions differ from the case."""
        actual = {
            "timezone_id": timezone_id,
            "zodiac": zodiac,
            "ayanamsha": ayanamsha,
            "ephemeris": ephemeris,
            "coordinate_frame": coordinate_frame,
            "node_convention": node_convention,
        }
        expected = {
            "timezone_id": self.metadata.timezone_id,
            "zodiac": self.metadata.zodiac,
            "ayanamsha": self.metadata.ayanamsha,
            "ephemeris": self.metadata.ephemeris,
            "coordinate_frame": self.metadata.coordinate_frame,
            "node_convention": self.metadata.node_convention,
        }
        mismatches = [
            key for key in expected
            if actual[key] != expected[key]
        ]
        if mismatches:
            raise ValueError(f"golden-case conventions differ: {mismatches}")
        if (isinstance(self.tolerance_degrees, bool)
                or not isinstance(self.tolerance_degrees, (int, float))
                or not math.isfinite(self.tolerance_degrees)
                or self.tolerance_degrees < 0):
            raise ValueError("tolerance_degrees must be finite and non-negative numeric")
        if not self.expected_longitudes:
            raise ValueError("expected_longitudes must not be empty")
        for body, longitude in self.expected_longitudes.items():
            if not isinstance(body, str) or not body.strip():
                raise ValueError("body names must be non-empty strings")
            if isinstance(longitude, bool) or not isinstance(longitude, (int, float)):
                raise ValueError(f"longitude for {body!r} must be numeric")
            if not math.isfinite(longitude) or not 0.0 <= longitude < 360.0:
                raise ValueError(f"longitude for {body!r} must be finite in [0, 360)")

    def observations(self, observed: Mapping[str, float]) -> tuple[GoldenObservation, ...]:
        """Return typed comparison records carrying this case's provenance."""
        if set(self.expected_longitudes) != set(observed):
            missing = sorted(set(self.expected_longitudes) - set(observed))
            extra = sorted(set(observed) - set(self.expected_longitudes))
            raise ValueError(f"body sets differ; missing={missing}, extra={extra}")
        return tuple(
            GoldenObservation(
                case_id=self.metadata.case_id,
                body=body,
                expected_longitude=self.expected_longitudes[body],
                observed_longitude=observed[body],
                tolerance_degrees=self.tolerance_degrees,
                reference_source=self.metadata.reference_source,
                reference_version=self.metadata.reference_version,
            )
            for body in sorted(self.expected_longitudes)
        )


def _required_mapping(value: Any, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{name} must be an object")
    return value


def load_golden_case(path: str | Path) -> GoldenCase:
    """Load one provenance-bound golden case from JSON and fail closed."""
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    root = _required_mapping(payload, "root")
    metadata = _required_mapping(root.get("metadata"), "metadata")
    longitudes = _required_mapping(root.get("expected_longitudes"), "expected_longitudes")

    required_metadata = (
        "case_id", "reference_source", "reference_version", "reference_url",
        "source_timestamp", "timezone_id", "zodiac", "ayanamsha", "ephemeris",
        "coordinate_frame", "node_convention",
    )
    missing = [key for key in required_metadata if key not in metadata]
    if missing:
        raise ValueError(f"metadata missing required fields: {missing}")

    try:
        source_timestamp = datetime.fromisoformat(metadata["source_timestamp"])
    except (TypeError, ValueError) as exc:
        raise ValueError("source_timestamp must be an ISO-8601 datetime") from exc

    parsed_metadata = GoldenCaseMetadata(
        case_id=metadata["case_id"],
        reference_source=metadata["reference_source"],
        reference_version=metadata["reference_version"],
        reference_url=metadata["reference_url"],
        source_timestamp=source_timestamp,
        timezone_id=metadata["timezone_id"],
        zodiac=metadata["zodiac"],
        ayanamsha=metadata["ayanamsha"],
        ephemeris=metadata["ephemeris"],
        coordinate_frame=metadata["coordinate_frame"],
        node_convention=metadata["node_convention"],
    )
    case = GoldenCase(parsed_metadata, dict(longitudes), root.get("tolerance_degrees"))
    case.validate()
    return case
