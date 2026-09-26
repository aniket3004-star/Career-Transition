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
    expected_mahadasha_end_dates: Tuple[datetime, ...] | None = None
    boundary_tolerance_days: float = 0.0

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
        if self.expected_mahadasha_end_dates is not None:
            if not self.expected_mahadasha_end_dates:
                raise ValueError("expected_mahadasha_end_dates must be non-empty when supplied")
            if any(
                not isinstance(value, datetime)
                or value.tzinfo is None
                or value.utcoffset() is None
                for value in self.expected_mahadasha_end_dates
            ):
                raise ValueError("expected_mahadasha_end_dates must contain timezone-aware datetimes")
        if (isinstance(self.boundary_tolerance_days, bool)
                or not isinstance(self.boundary_tolerance_days, (int, float))
                or not math.isfinite(self.boundary_tolerance_days)
                or self.boundary_tolerance_days < 0):
            raise ValueError("boundary_tolerance_days must be finite and non-negative")

    def assert_mahadasha_boundaries(self, mahadasha_count: int | None = None) -> Tuple[DashaPeriod, ...]:
        """Validate source-published Mahadasha boundaries without hiding convention drift."""
        self.validate()
        if self.expected_mahadasha_end_dates is None:
            raise ValueError("expected_mahadasha_end_dates are required for boundary validation")
        count = mahadasha_count or len(self.expected_mahadasha_end_dates)
        if count != len(self.expected_mahadasha_end_dates):
            raise ValueError("mahadasha_count must match expected boundary count")
        periods = vimshottari_timeline(
            self.birth_datetime,
            self.reference.longitudes["Moon"],
            mahadasha_count=count,
        )
        tolerance_seconds = self.boundary_tolerance_days * 86400.0
        for period, expected_end in zip(periods, self.expected_mahadasha_end_dates):
            difference = abs((period.end - expected_end).total_seconds())
            if difference > tolerance_seconds:
                raise AssertionError(
                    f"{self.case_id}: {period.lord} end differs from source by "
                    f"{difference / 86400.0:.6f} days"
                )
        return periods

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
