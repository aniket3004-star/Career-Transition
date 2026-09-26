"""Reference-case validation for the Vimshottari Dasha layer.

This module does not calculate astronomy. It validates the Dasha layer against
externally supplied sidereal Moon longitudes that carry explicit provenance.
"""
from dataclasses import dataclass
from datetime import datetime
import math
from typing import Tuple

from .dasha import DashaPeriod, vimshottari_timeline
from .reference_snapshot import ReferenceSnapshot


@dataclass(frozen=True)
class DashaReferenceCase:
    """One externally sourced Moon-position case for Dasha validation."""

    case_id: str
    birth_datetime: datetime
    reference: ReferenceSnapshot
    expected_starting_lord: str

    def validate(self) -> None:
        if not self.case_id.strip():
            raise ValueError("case_id must be non-empty")
        if not isinstance(self.birth_datetime, datetime):
            raise ValueError("birth_datetime must be a datetime")
        if self.birth_datetime.tzinfo is None or self.birth_datetime.utcoffset() is None:
            raise ValueError("birth_datetime must be timezone-aware")
        self.reference.validate()
        if "Moon" not in self.reference.longitudes:
            raise ValueError("reference must contain Moon longitude")
        if self.expected_starting_lord not in {
            "Ketu", "Venus", "Sun", "Moon", "Mars",
            "Rahu", "Jupiter", "Saturn", "Mercury",
        }:
            raise ValueError("expected_starting_lord is not a Vimshottari lord")

    def assert_matches(self) -> DashaPeriod:
        self.validate()
        moon = self.reference.longitudes["Moon"]
        period = vimshottari_timeline(
            self.birth_datetime,
            moon,
            mahadasha_count=1,
        )[0]
        if period.lord != self.expected_starting_lord:
            raise AssertionError(
                f"{self.case_id}: expected starting lord "
                f"{self.expected_starting_lord}, got {period.lord}"
            )
        return period


def validate_dasha_reference_cases(
    cases: Tuple[DashaReferenceCase, ...],
) -> Tuple[DashaPeriod, ...]:
    if not cases:
        raise ValueError("cases must be non-empty")
    return tuple(case.assert_matches() for case in cases)
