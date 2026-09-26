import unittest
from datetime import datetime, timezone

from src.astrology.calculation_contract import (
    CalculationResult,
    ProviderMetadata,
    validate_result_gates,
)


def result(**overrides):
    values = dict(
        provider=ProviderMetadata("synthetic", "0", "not-an-ephemeris", False),
        calculated_at=datetime(2026, 9, 22, tzinfo=timezone.utc),
        raw_response_digest=None,
        sidereal_longitudes={},
        ascendant_longitude=None,
        schema_valid=True,
        provenance_complete=False,
        calculation_reproduced=False,
        accuracy_verified=False,
        career_rules_eligible=False,
    )
    values.update(overrides)
    return CalculationResult(**values)


class CalculationGateTests(unittest.TestCase):
    def test_schema_only_result_is_allowed(self):
        validate_result_gates(result())

    def test_each_downstream_state_requires_previous_gate(self):
        for field in ("provenance_complete", "calculation_reproduced",
                      "accuracy_verified", "career_rules_eligible"):
            with self.subTest(field=field):
                with self.assertRaises(ValueError):
                    validate_result_gates(result(**{field: True}))

    def test_full_chain_is_allowed(self):
        validate_result_gates(result(
            provenance_complete=True,
            calculation_reproduced=True,
            accuracy_verified=True,
            career_rules_eligible=True,
        ))

    def test_raw_digest_is_not_enough_for_accuracy(self):
        validate_result_gates(result(
            raw_response_digest="abc",
            provenance_complete=True,
            accuracy_verified=False,
        ))


if __name__ == "__main__":
    unittest.main()
