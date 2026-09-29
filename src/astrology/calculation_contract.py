"""Provider-neutral contract for V2 astronomical calculations.

This module deliberately contains no ephemeris implementation. It defines the
minimum structured record required before astronomical values can feed Dasha,
transits, or career rules.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Mapping, Protocol, Sequence


@dataclass(frozen=True)
class CalculationRequest:
    birth_datetime_utc: datetime
    latitude: float
    longitude: float
    ayanamsha: str
    zodiac: str
    house_system: str


@dataclass(frozen=True)
class PlanetaryPosition:
    body: str
    longitude: float
    latitude: float
    distance_au: float


@dataclass(frozen=True)
class CalculationRecord:
    provider: str
    provider_version: str
    ephemeris: str
    request: CalculationRequest
    positions: Sequence[PlanetaryPosition]
    calculation_timestamp: datetime
    provenance: Mapping[str, str]


class CalculationProvider(Protocol):
    """Interface implemented by a certified astronomical provider."""

    name: str
    version: str

    def calculate(self, request: CalculationRequest) -> CalculationRecord:
        """Calculate positions using exactly the requested conventions."""
        ...
