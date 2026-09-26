import unittest
from dataclasses import is_dataclass

from src.astrology.provider import AstronomyProvider, ProviderContext


class ProviderBoundaryTests(unittest.TestCase):
    def test_provider_context_is_structured(self):
        self.assertTrue(is_dataclass(ProviderContext))
        self.assertTrue(hasattr(AstronomyProvider, "__protocol_attrs__") or hasattr(AstronomyProvider, "calculate"))


if __name__ == "__main__":
    unittest.main()
