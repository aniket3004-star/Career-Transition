"""Explicit tropical-to-sidereal conversion primitives.

This module deliberately does not calculate an ayanamsha. A provider/reference
must supply the ayanamsha offset for the exact instant and named convention.
That separation prevents a fixed or hidden Lahiri-style offset from being
mistaken for an astronomical calculation.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Mapping


@dataclass(frozen=True)
class SiderealConversion:
    ayanamsha_name: str
    ayanamsha_degrees: float
    tropical_longitudes: Mapping[str, float]
    sidereal_longitudes: Mapping[str, float]


def _validate_angle(value: float, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{name} must be a finite numeric value")


def tropical_to_sidereal(longitude: float, ayanamsha_degrees: float) -> float:
    """Subtract an explicitly supplied ayanamsha and normalize to [0, 360)."""
    _validate_angle(longitude, "longitude")
    _validate_angle(ayanamsha_degrees, "ayanamsha_degrees")
    return (longitude - ayanamsha_degrees) % 360.0


def convert_longitudes(
    tropical_longitudes: Mapping[str, float],
    ayanamsha_name: str,
    ayanamsha_degrees: float,
) -> SiderealConversion:
    """Convert a complete longitude mapping using one explicit offset."""
    if not isinstance(ayanamsha_name, str) or not ayanamsha_name.strip():
        raise ValueError("ayanamsha_name is required")
    _validate_angle(ayanamsha_degrees, "ayanamsha_degrees")
    if not tropical_longitudes:
        raise ValueError("tropical_longitudes must not be empty")

    converted = {
        body: tropical_to_sidereal(longitude, ayanamsha_degrees)
        for body, longitude in tropical_longitudes.items()
    }
    return SiderealConversion(
        ayanamsha_name=ayanamsha_name,
        ayanamsha_degrees=ayanamsha_degrees,
        tropical_longitudes=dict(tropical_longitudes),
        sidereal_longitudes=converted,
    )
