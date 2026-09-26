import unittest
from dataclasses import is_dataclass
from datetime import datetime, timezone

from src.astrology.calculation_contract import CalculationRequest
from src.astrology.provider import AstronomyProvider, ProviderContext


class ProviderBoundaryTests(unittest.TestCase):
    def test_provider_context_is_structured(self):
        self.assertTrue(is_dataclass(ProviderContext))
        self.assertTrue(hasattr(AstronomyProvider, "calculate"))

    def test_context_preserves_explicit_conventions(self):
        request = CalculationRequest(
            "case-001", "2000-01-15", "12:00", "exact", "Synthetic",
            20.0, 85.0,
            "Asia/Kolkata",
            datetime(2000, 1, 15, 6, 30, tzinfo=timezone.utc),
            "explicit-IANA",
            "Lahiri", "sidereal", "Whole Sign", "mean",
        )
        context = ProviderContext(request, "provider-1", "ephemeris-1")
        self.assertEqual(context.provider_version, "provider-1")
        self.assertEqual(context.ephemeris_source, "ephemeris-1")
        self.assertEqual(context.request.ayanamsha, "Lahiri")


if __name__ == "__main__":
    unittest.main()
