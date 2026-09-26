"""Provider-neutral contracts for the V2 calculation layer.

This module deliberately performs no astronomy. It defines the data and
dependency gates that a real ephemeris provider must satisfy before results
can enter Dasha/transit/career logic.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class CalculationRequest:
    request_id: str
    birth_date: str
    birth_time: str
    birth_time_precision: str
    birthplace_label: str
    latitude: float
    longitude: float
    timezone_id: str
    utc_instant: datetime
    timezone_resolution: str
    ayanamsha: str
    zodiac: str
    house_system: str
    node_convention: str


@dataclass(frozen=True)
class ProviderMetadata:
    provider_name: str
    provider_version: str
    ephemeris_source: str
    settings_verified: bool


@dataclass(frozen=True)
class CalculationResult:
    provider: ProviderMetadata
    calculated_at: datetime
    raw_response_digest: Optional[str]
    sidereal_longitudes: dict[str, float]
    ascendant_longitude: Optional[float]
    schema_valid: bool
    provenance_complete: bool
    calculation_reproduced: bool
    accuracy_verified: bool
    career_rules_eligible: bool


def validate_result_gates(result: CalculationResult) -> None:
    """Raise when a downstream certification state violates its prerequisites."""
    if result.career_rules_eligible and not result.accuracy_verified:
        raise ValueError("career_rules_eligible requires accuracy_verified")
    if result.accuracy_verified and not result.calculation_reproduced:
        raise ValueError("accuracy_verified requires calculation_reproduced")
    if result.calculation_reproduced and not result.provenance_complete:
        raise ValueError("calculation_reproduced requires provenance_complete")
    if result.provenance_complete and not result.schema_valid:
        raise ValueError("provenance_complete requires schema_valid")
