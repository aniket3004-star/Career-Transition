"""Reference-case validation for the Vimshottari Dasha layer.

This module does not calculate astronomy. It validates the Dasha layer against
externally supplied sidereal Moon longitudes that carry explicit provenance.
"""
from dataclasses import dataclass
from datetime import datetime
import math
from typing import Tuple

from .dasha import DashaPeriod, vimshottari_timeline, DAYS_PER_YEAR
from .reference_snapshot import ReferenceSnapshot


@dataclass(frozen=True)
class DashaReferenceCase:
    """One externally sourced Moon-position case for Dasha validation."""

    case_id: str
    birth_datetime: datetime
    reference: ReferenceSnapshot
    expected_starting_lord: str
    expected_opening_balance_years: float | None = None
    opening_balance_tolerance_years: float = 1e-6

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
        if self.expected_opening_balance_years is not None:
            if (isinstance(self.expected_opening_balance_years, bool)
                    or not isinstance(self.expected_opening_balance_years, (int, float))
                    or not math.isfinite(self.expected_opening_balance_years)
                    or self.expected_opening_balance_years < 0):
                raise ValueError("expected_opening_balance_years must be finite and non-negative")
        if (isinstance(self.opening_balance_tolerance_years, bool)
                or not isinstance(self.opening_balance_tolerance_years, (int, float))
                or not math.isfinite(self.opening_balance_tolerance_years)
                or self.opening_balance_tolerance_years < 0):
            raise ValueError("opening_balance_tolerance_years must be finite and non-negative")

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
        if self.expected_opening_balance_years is not None:
            actual_years = (
                (period.end - period.start).total_seconds()
                / (DAYS_PER_YEAR * 86400.0)
            )
            if abs(actual_years - self.expected_opening_balance_years) > self.opening_balance_tolerance_years:
                raise AssertionError(
                    f"{self.case_id}: expected opening balance "
                    f"{self.expected_opening_balance_years}, got {actual_years}"
                )
        return period


def validate_dasha_reference_cases(
    cases: Tuple[DashaReferenceCase, ...],
) -> Tuple[DashaPeriod, ...]:
    if not cases:
        raise ValueError("cases must be non-empty")
    return tuple(case.assert_matches() for case in cases)
