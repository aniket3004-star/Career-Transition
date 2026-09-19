"""Fail-closed input contract checks for Career Transition Astrology V1.

This module validates shape and declared metadata only. It does not calculate
charts, verify a provider's claims, or establish astronomical accuracy.
Python 3.9+ (zoneinfo) is required.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
import math
import re
from typing import Any, Mapping
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_TIME_RE = re.compile(r"^\d{2}:\d{2}(?::\d{2})?$")


@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()
    evidence_label: str = "INPUT_SCHEMA_ONLY"


def _nonblank(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_strict_date(value: Any) -> bool:
    if not isinstance(value, str) or not _DATE_RE.fullmatch(value):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def _valid_local_time(value: Any) -> bool:
    if not isinstance(value, str) or not _TIME_RE.fullmatch(value):
        return False
    try:
        datetime.strptime(value, "%H:%M:%S" if len(value) == 8 else "%H:%M")
        return True
    except ValueError:
        return False


def validate_birth_input(payload: Mapping[str, Any]) -> ValidationResult:
    """Validate required birth details and explicit calculation provenance.

    Required keys: birth_date (strict YYYY-MM-DD), birth_time (HH:MM[:SS]),
    timezone (IANA zone), latitude, longitude, provider, provider_version,
    ayanamsha, zodiac, house_system, ephemeris, and calculation_timestamp.
    No defaults are silently supplied.
    """
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(payload, Mapping):
        return ValidationResult(False, ("payload must be a mapping",))

    required_text = (
        "timezone", "provider", "provider_version", "ayanamsha",
        "zodiac", "house_system", "ephemeris",
    )
    for key in required_text:
        if not _nonblank(payload.get(key)):
            errors.append(f"{key} must be explicitly supplied as nonblank text")

    if not _valid_strict_date(payload.get("birth_date")):
        errors.append("birth_date must be a valid YYYY-MM-DD date")

    if not _valid_local_time(payload.get("birth_time")):
        errors.append("birth_time must be a valid local HH:MM or HH:MM:SS time")

    tz = payload.get("timezone")
    if _nonblank(tz):
        try:
            ZoneInfo(tz)
        except (ZoneInfoNotFoundError, ValueError, TypeError):
            errors.append("timezone must be a recognized IANA timezone identifier")

    for key, low, high in (("latitude", -90.0, 90.0), ("longitude", -180.0, 180.0)):
        value = payload.get(key)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            errors.append(f"{key} must be a numeric value")
        elif not math.isfinite(value) or not low <= value <= high:
            errors.append(f"{key} must be finite and within [{low}, {high}]")

    timestamp = payload.get("calculation_timestamp")
    if not _nonblank(timestamp):
        errors.append("calculation_timestamp must be an explicit ISO-8601 timestamp")
    else:
        try:
            normalized = timestamp[:-1] + "+00:00" if timestamp.endswith("Z") else timestamp
            parsed = datetime.fromisoformat(normalized)
            if parsed.tzinfo is None or parsed.utcoffset() is None:
                errors.append("calculation_timestamp must include an explicit UTC offset or Z")
        except ValueError:
            errors.append("calculation_timestamp must be a valid ISO-8601 timestamp")

    # This is an attestation, not proof. Absence or falsehood blocks comparison.
    if payload.get("provider_settings_verified") is not True:
        errors.append("provider_settings_verified must be true before provider output is treated as configured")
    if not _nonblank(payload.get("source_record_id")):
        warnings.append("source_record_id absent: provenance cannot be traced to a retained source record")

    return ValidationResult(not errors, tuple(errors), tuple(warnings))
