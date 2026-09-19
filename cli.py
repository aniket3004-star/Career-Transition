"""V1-alpha CLI: validate birth-input envelopes. No chart or career calculation."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from src.validation.input_contract import validate_birth_input


def _load_payload(args: argparse.Namespace) -> dict[str, Any]:
    if args.json:
        payload = json.loads(args.json)
    elif args.file:
        payload = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        raise SystemExit("Provide --json or --file")
    if not isinstance(payload, dict):
        raise SystemExit("Input must be a JSON object")
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Career Transition V1-alpha input validator. Does not calculate astrology."
    )
    parser.add_argument("--json", help="Inline JSON envelope")
    parser.add_argument("--file", help="Path to JSON envelope")
    parser.add_argument("--save", help="Opt-in persist path. Off by default.")
    args = parser.parse_args(argv)

    payload = _load_payload(args)
    result = validate_birth_input(payload)
    output = {
        "schema_valid": result.valid,
        "provenance_complete": result.valid and not result.warnings,
        "calculation_reproduced": False,
        "accuracy_verified": False,
        "career_rules_eligible": False,
        "calculation_layer": "not_certified",
        "evidence_label": result.evidence_label,
        "errors": list(result.errors),
        "warnings": list(result.warnings),
        "career_outlook": None,
        "message": "V1-alpha validates input only. No planetary positions, dashas, transits, or career advice.",
    }
    print(json.dumps(output, indent=2))
    if args.save:
        path = Path(args.save)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    return 0 if result.valid else 1


if __name__ == "__main__":
    sys.exit(main())
