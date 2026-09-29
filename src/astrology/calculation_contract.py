"""Provider-neutral contract for V2 astronomical calculations.

This module deliberately contains no ephemeris implementation. It defines the
minimum structured record required before astronomical values can feed Dasha,
transits, or career rules.
"""
from dataclasses import dataclass
from datetime import datetime, timedelta
import math
from typing import Mapping, Protocol, Sequence


@dataclass(frozen=True)
class CalculationRequest:
    birth_datetime_utc: datetime
    latitude: float
    longitude: float
    ayanamsha: str
    zodiac: str
    house_system: str

    def __post_init__(self) -> None:
        if self.birth_datetime_utc.tzinfo is None or self.birth_datetime_utc.utcoffset() != timedelta(0):
            raise ValueError("birth_datetime_utc must be timezone-aware UTC")
        for name, value, low, high in (
            ("latitude", self.latitude, -90.0, 90.0),
            ("longitude", self.longitude, -180.0, 180.0),
        ):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(f"{name} must be numeric")
            if not math.isfinite(value) or not low <= value <= high:
                raise ValueError(f"{name} must be finite and within [{low}, {high}]")
        for name, value in (
            ("ayanamsha", self.ayanamsha),
            ("zodiac", self.zodiac),
            ("house_system", self.house_system),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be nonblank text")


@dataclass(frozen=True)
class PlanetaryPosition:
    body: str
    longitude: float
    latitude: float
    distance_au: float

    def __post_init__(self) -> None:
        if not isinstance(self.body, str) or not self.body.strip():
            raise ValueError("body must be nonblank text")
        if isinstance(self.longitude, bool) or not isinstance(self.longitude, (int, float)):
            raise ValueError("longitude must be numeric")
        if not math.isfinite(self.longitude) or not 0.0 <= self.longitude < 360.0:
            raise ValueError("longitude must be finite and within [0, 360)")
        if isinstance(self.latitude, bool) or not isinstance(self.latitude, (int, float)):
            raise ValueError("latitude must be numeric")
        if not math.isfinite(self.latitude) or not -90.0 <= self.latitude <= 90.0:
            raise ValueError("latitude must be finite and within [-90, 90]")
        if isinstance(self.distance_au, bool) or not isinstance(self.distance_au, (int, float)):
            raise ValueError("distance_au must be numeric")
        if not math.isfinite(self.distance_au) or self.distance_au < 0:
            raise ValueError("distance_au must be finite and non-negative")


@dataclass(frozen=True)
class CalculationRecord:
    provider: str
    provider_version: str
    ephemeris: str
    request: CalculationRequest
    positions: Sequence[PlanetaryPosition]
    calculation_timestamp: datetime
    provenance: Mapping[str, str]

    def __post_init__(self) -> None:
        for name, value in (
            ("provider", self.provider),
            ("provider_version", self.provider_version),
            ("ephemeris", self.ephemeris),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be nonblank text")
        if self.calculation_timestamp.tzinfo is None or self.calculation_timestamp.utcoffset() != timedelta(0):
            raise ValueError("calculation_timestamp must be timezone-aware UTC")
        if not isinstance(self.provenance, Mapping):
            raise ValueError("provenance must be a mapping")


class CalculationProvider(Protocol):
    """Interface implemented by a certified astronomical provider."""

    name: str
    version: str

    def calculate(self, request: CalculationRequest) -> CalculationRecord:
        """Calculate positions using exactly the requested conventions."""
        ...
