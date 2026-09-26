"""Auditable loading/validation boundary for astronomy golden cases.

Expected astronomical values are external data; this module never computes them.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import json
import math
from pathlib import Path
from typing import Any, Mapping

from src.astrology.golden_case import GoldenCaseMetadata


@dataclass(frozen=True)
class GoldenCase:
    metadata: GoldenCaseMetadata
    expected_longitudes: dict[str, float]
    tolerance_degrees: float

    def validate(self) -> None:
        self.metadata.validate()
        if not math.isfinite(self.tolerance_degrees) or self.tolerance_degrees < 0:
            raise ValueError("tolerance_degrees must be finite and non-negative")
        if not self.expected_longitudes:
            raise ValueError("expected_longitudes must not be empty")
        for body, longitude in self.expected_longitudes.items():
            if not isinstance(body, str) or not body.strip():
                raise ValueError("body names must be non-empty strings")
            if isinstance(longitude, bool) or not isinstance(longitude, (int, float)):
                raise ValueError(f"longitude for {body!r} must be numeric")
            if not math.isfinite(longitude) or not 0.0 <= longitude < 360.0:
                raise ValueError(f"longitude for {body!r} must be finite in [0, 360)")


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

    parsed_metadata = GoldenCaseMetadata(
        case_id=metadata["case_id"],
        reference_source=metadata["reference_source"],
        reference_version=metadata["reference_version"],
        reference_url=metadata["reference_url"],
        source_timestamp=datetime.fromisoformat(metadata["source_timestamp"]),
        timezone_id=metadata["timezone_id"],
        zodiac=metadata["zodiac"],
        ayanamsha=metadata["ayanamsha"],
        ephemeris=metadata["ephemeris"],
        coordinate_frame=metadata["coordinate_frame"],
        node_convention=metadata["node_convention"],
    )
    tolerance = root.get("tolerance_degrees")
    case = GoldenCase(parsed_metadata, dict(longitudes), tolerance)
    case.validate()
    return case
