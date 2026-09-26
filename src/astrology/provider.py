"""Provider adapter boundary for V2 astronomy calculations.

Implementations must supply explicitly configured values. This interface contains
no fallback ephemeris, timezone, ayanamsha, or house-system defaults.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

from src.astrology.calculation_contract import CalculationRequest, CalculationResult


@dataclass(frozen=True)
class ProviderContext:
    request: CalculationRequest
    provider_version: str
    ephemeris_source: str


class AstronomyProvider(Protocol):
    def calculate(self, context: ProviderContext) -> CalculationResult:
        """Calculate a chart under the exact settings carried by context.

        Implementations must preserve provider provenance and must not silently
        substitute conventions. The returned result is not accuracy-verified
        merely because this method succeeds.
        """
        ...
