"""Strict external astronomy reference snapshot contract.

This module stores externally produced reference values; it never calculates
astronomy. It exists so a real Swiss Ephemeris/reference snapshot can be
validated and compared without silently inheriting library defaults.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import math
from typing import Mapping


@dataclass(frozen=True)
class ReferenceSnapshot:
    case_id: str
    reference_source: str
    reference_version: str
    reference_url: str
    calculated_at_utc: datetime
    timezone_id: str
    zodiac: str
    sidereal_mode: str
    ephemeris: str
    coordinate_frame: str
    node_convention: str
    longitudes: Mapping[str, float]
    ascendant_longitude: float

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        text_fields = {
            "case_id": self.case_id,
            "reference_source": self.reference_source,
            "reference_version": self.reference_version,
            "reference_url": self.reference_url,
            "timezone_id": self.timezone_id,
            "zodiac": self.zodiac,
            "sidereal_mode": self.sidereal_mode,
            "ephemeris": self.ephemeris,
            "coordinate_frame": self.coordinate_frame,
            "node_convention": self.node_convention,
        }
        if any(not isinstance(v, str) or not v.strip() for v in text_fields.values()):
            raise ValueError("reference snapshot contains a missing text field")
        if not self.reference_url.startswith(("https://", "http://")):
            raise ValueError("reference_url must be an explicit URL")
        if (not isinstance(self.calculated_at_utc, datetime)
                or self.calculated_at_utc.tzinfo is None
                or self.calculated_at_utc.utcoffset() is None):
            raise ValueError("calculated_at_utc must be timezone-aware")
        if not isinstance(self.longitudes, Mapping) or not self.longitudes:
            raise ValueError("longitudes must be a non-empty mapping")
        for body, longitude in self.longitudes.items():
            if not isinstance(body, str) or not body.strip():
                raise ValueError("body names must be non-empty strings")
            if (isinstance(longitude, bool)
                    or not isinstance(longitude, (int, float))
                    or not math.isfinite(longitude)
                    or not 0.0 <= longitude < 360.0):
                raise ValueError(f"longitude for {body!r} must be finite in [0, 360)")
        if (isinstance(self.ascendant_longitude, bool)
                or not isinstance(self.ascendant_longitude, (int, float))
                or not math.isfinite(self.ascendant_longitude)
                or not 0.0 <= self.ascendant_longitude < 360.0):
            raise ValueError("ascendant_longitude must be finite in [0, 360)")
