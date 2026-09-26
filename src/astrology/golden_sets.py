"""Set-level golden comparison helpers.

This module compares provider output with an independently supplied reference.
It never generates expected astronomy values itself.
"""
from __future__ import annotations

from datetime import datetime
from typing import Mapping

from src.astrology.golden import GoldenEvidence, GoldenObservation, compare_observation


def compare_longitude_sets(
    expected: Mapping[str, float],
    observed: Mapping[str, float],
    reference_source: str,
    reference_version: str,
    tolerance_degrees: float,
    case_id: str,
    compared_at: datetime | None = None,
) -> tuple[GoldenEvidence, ...]:
    """Compare matching named bodies without inventing missing observations."""
    if not expected:
        raise ValueError("expected must not be empty")
    if set(expected) != set(observed):
        missing = sorted(set(expected) - set(observed))
        extra = sorted(set(observed) - set(expected))
        raise ValueError(f"body sets differ; missing={missing}, extra={extra}")
    return tuple(
        compare_observation(
            GoldenObservation(
                case_id, body, expected[body], observed[body],
                tolerance_degrees, reference_source, reference_version,
            ),
            compared_at,
        )
        for body in sorted(expected)
    )
