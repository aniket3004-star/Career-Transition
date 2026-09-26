"""Auditable metadata contract for independently sourced astronomy goldens.

This module stores provenance only; it deliberately does not contain expected
astronomical values. A case becomes usable only when its source/convention
metadata is explicit.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class GoldenCaseMetadata:
    case_id: str
    reference_source: str
    reference_version: str
    reference_url: str
    source_timestamp: datetime
    timezone_id: str
    zodiac: str
    ayanamsha: str
    ephemeris: str
    coordinate_frame: str
    node_convention: str

    def validate(self) -> None:
        required = {
            "case_id": self.case_id,
            "reference_source": self.reference_source,
            "reference_version": self.reference_version,
            "reference_url": self.reference_url,
            "timezone_id": self.timezone_id,
            "zodiac": self.zodiac,
            "ayanamsha": self.ayanamsha,
            "ephemeris": self.ephemeris,
            "coordinate_frame": self.coordinate_frame,
            "node_convention": self.node_convention,
        }
        if any(not isinstance(v, str) or not v.strip() for v in required.values()):
            raise ValueError("golden-case metadata contains a missing text field")
        if self.source_timestamp.tzinfo is None or self.source_timestamp.utcoffset() is None:
            raise ValueError("source_timestamp must be timezone-aware")
        if not self.reference_url.startswith(("https://", "http://")):
            raise ValueError("reference_url must be an explicit URL")
