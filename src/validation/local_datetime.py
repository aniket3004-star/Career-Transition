"""DST-aware validation for local birth date/time inputs.

This checks timezone interpretation only; it does not calculate a natal chart.
Ambiguous and nonexistent local times are returned explicitly rather than guessed.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, time, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


@dataclass(frozen=True)
class LocalDateTimeResult:
    status: str  # VALID, AMBIGUOUS, NONEXISTENT, INVALID
    candidates_utc: tuple[datetime, ...] = ()
    message: str = ""


def resolve_local_datetime(birth_date: str, birth_time: str, timezone_name: str) -> LocalDateTimeResult:
    """Resolve a strict local wall time without silently choosing a DST fold.

    A valid ordinary time yields one UTC instant. A repeated clock time yields
    two distinct UTC instants (AMBIGUOUS); a spring-forward gap yields none.
    """
    try:
        if not isinstance(birth_date, str) or date.fromisoformat(birth_date).isoformat() != birth_date:
            raise ValueError("date must use YYYY-MM-DD")
        if not isinstance(birth_time, str) or len(birth_time) not in (5, 8):
            raise ValueError("time must use HH:MM or HH:MM:SS")
        fmt = "%H:%M:%S" if len(birth_time) == 8 else "%H:%M"
        parsed_time = datetime.strptime(birth_time, fmt).time()
        zone = ZoneInfo(timezone_name)
    except (ValueError, TypeError, ZoneInfoNotFoundError):
        return LocalDateTimeResult("INVALID", message="Invalid date, time, or IANA timezone")

    wall = datetime.combine(date.fromisoformat(birth_date), time(
        parsed_time.hour, parsed_time.minute, parsed_time.second
    ))
    candidates: set[datetime] = set()
    for fold in (0, 1):
        local = wall.replace(tzinfo=zone, fold=fold)
        utc_value = local.astimezone(timezone.utc)
        round_trip = utc_value.astimezone(zone).replace(tzinfo=None)
        if round_trip == wall:
            candidates.add(utc_value)

    ordered = tuple(sorted(candidates))
    if not ordered:
        return LocalDateTimeResult("NONEXISTENT", message="Local time falls in a timezone clock-change gap")
    if len(ordered) > 1:
        return LocalDateTimeResult("AMBIGUOUS", ordered, "Local time occurs twice; explicit fold/offset is required")
    return LocalDateTimeResult("VALID", ordered)
