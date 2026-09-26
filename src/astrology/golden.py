"""Independent-comparison primitives for V2 astronomy validation.

No provider is implemented here. The module only defines reproducible comparison
math and evidence records so provider output cannot be marked verified by
self-comparison.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
import math


@dataclass(frozen=True)
class GoldenObservation:
    case_id: str
    body: str
    expected_longitude: float
    observed_longitude: float
    tolerance_degrees: float
    reference_source: str
    reference_version: str


@dataclass(frozen=True)
class GoldenEvidence:
    case_id: str
    body: str
    delta_degrees: float
    tolerance_degrees: float
    passed: bool
    reference_source: str
    reference_version: str
    compared_at: datetime


def circular_difference_degrees(a: float, b: float) -> float:
    """Shortest signed angular difference in [-180, 180)."""
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x)
           for x in (a, b)):
        raise ValueError("angles must be finite numeric values")
    return ((a - b + 180.0) % 360.0) - 180.0


def compare_observation(observation: GoldenObservation,
                        compared_at: datetime | None = None) -> GoldenEvidence:
    if not observation.case_id.strip():
        raise ValueError("case_id is required")
    if not observation.body.strip():
        raise ValueError("body is required")
    if not observation.reference_source.strip():
        raise ValueError("reference_source is required")
    if not observation.reference_version.strip():
        raise ValueError("reference_version is required")
    if not math.isfinite(observation.tolerance_degrees) or observation.tolerance_degrees < 0:
        raise ValueError("tolerance_degrees must be finite and non-negative")
    delta = circular_difference_degrees(
        observation.observed_longitude, observation.expected_longitude
    )
    timestamp = compared_at or datetime.now(timezone.utc)
    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise ValueError("compared_at must be timezone-aware")
    return GoldenEvidence(
        case_id=observation.case_id,
        body=observation.body,
        delta_degrees=delta,
        tolerance_degrees=observation.tolerance_degrees,
        passed=abs(delta) <= observation.tolerance_degrees,
        reference_source=observation.reference_source,
        reference_version=observation.reference_version,
        compared_at=timestamp.astimezone(timezone.utc),
    )
