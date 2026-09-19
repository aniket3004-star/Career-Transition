"""Vimshottari dasha timeline utilities (research prototype).

This module calculates the conventional 120-year Vimshottari sequence from a
sidereal Moon longitude and birth instant. It is not an ephemeris: callers must
supply a correctly computed Moon longitude and explicitly document the
ayanamsha, timezone conversion, and source. Results are symbolic timelines,
not career predictions or recommendations.

Conventions: 27 equal nakshatras of 13°20'; lords cycle Ketu, Venus, Sun,
Moon, Mars, Rahu, Jupiter, Saturn, Mercury; years use 365.2425 days.
"""
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import math
from typing import Tuple

NAKSHATRA_DEGREES = 360.0 / 27.0
DASHA_YEARS = {
    "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7,
    "Rahu": 18, "Jupiter": 16, "Saturn": 19, "Mercury": 17,
}
LORDS = tuple(DASHA_YEARS)
TOTAL_YEARS = sum(DASHA_YEARS.values())
DAYS_PER_YEAR = 365.2425

@dataclass(frozen=True)
class DashaPeriod:
    lord: str
    start: datetime
    end: datetime


def _utc(dt: datetime) -> datetime:
    if not isinstance(dt, datetime) or dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError("birth_datetime must be timezone-aware")
    return dt.astimezone(timezone.utc)


def vimshottari_timeline(birth_datetime: datetime, sidereal_moon_longitude: float,
                         mahadasha_count: int = 9) -> Tuple[DashaPeriod, ...]:
    """Return sequential Mahadasha periods beginning at birth.

    Moon longitude must be a finite real number in [0, 360). The first period
    begins at birth and has only the remaining fraction of its lord's full
    duration; subsequent periods use full durations. `mahadasha_count` is 1..108.
    """
    if (isinstance(sidereal_moon_longitude, bool)
            or not isinstance(sidereal_moon_longitude, (int, float))
            or not math.isfinite(sidereal_moon_longitude)
            or not 0 <= sidereal_moon_longitude < 360):
        raise ValueError("sidereal_moon_longitude must be finite and in [0, 360)")
    if (isinstance(mahadasha_count, bool) or not isinstance(mahadasha_count, int)
            or not 1 <= mahadasha_count <= 108):
        raise ValueError("mahadasha_count must be an integer between 1 and 108")
    birth = _utc(birth_datetime)
    nak_index = int(sidereal_moon_longitude / NAKSHATRA_DEGREES)
    fraction_elapsed = (sidereal_moon_longitude % NAKSHATRA_DEGREES) / NAKSHATRA_DEGREES
    first_lord_index = nak_index % len(LORDS)
    first_lord = LORDS[first_lord_index]
    remaining_years = DASHA_YEARS[first_lord] * (1.0 - fraction_elapsed)
    periods = []
    start = birth
    for i in range(mahadasha_count):
        lord = LORDS[(first_lord_index + i) % len(LORDS)]
        years = remaining_years if i == 0 else DASHA_YEARS[lord]
        end = start + timedelta(days=years * DAYS_PER_YEAR)
        periods.append(DashaPeriod(lord, start, end))
        start = end
    return tuple(periods)


def antardasha_timeline(mahadasha: DashaPeriod) -> Tuple[DashaPeriod, ...]:
    """Return the nine proportional Antardashas within one Mahadasha."""
    if (not isinstance(mahadasha, DashaPeriod)
            or mahadasha.lord not in DASHA_YEARS
            or not isinstance(mahadasha.start, datetime)
            or not isinstance(mahadasha.end, datetime)
            or mahadasha.end <= mahadasha.start):
        raise ValueError("invalid Mahadasha period")
    lord_index = LORDS.index(mahadasha.lord)
    total_seconds = (mahadasha.end - mahadasha.start).total_seconds()
    periods = []
    start = mahadasha.start
    for i in range(9):
        lord = LORDS[(lord_index + i) % 9]
        fraction = DASHA_YEARS[lord] / TOTAL_YEARS
        end = (mahadasha.end if i == 8 else
               start + timedelta(seconds=total_seconds * fraction))
        periods.append(DashaPeriod(lord, start, end))
        start = end
    return tuple(periods)
