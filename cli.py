"""V1-alpha CLI: validate birth-input envelopes. No chart or career calculation."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from src.validation.input_contract import validate_birth_input


_ERROR_MESSAGE = "V1-alpha validates input only. No planetary positions, dashas, transits, or career advice."


def _error_output(message: str) -> dict[str, Any]:
    return {
        "schema_valid": False,
        "provenance_complete": False,
        "calculation_reproduced": False,
        "accuracy_verified": False,
        "career_rules_eligible": False,
        "calculation_layer": "not_certified",
        "evidence_label": "quarantined",
        "errors": [message],
        "warnings": [],
        "career_outlook": None,
        "message": _ERROR_MESSAGE,
    }


def _load_payload(args: argparse.Namespace) -> dict[str, Any]:
    try:
        raw = args.json if args.json is not None else Path(args.file).read_text(encoding="utf-8")
        payload = json.loads(raw)
    except json.JSONDecodeError:
        raise ValueError("Input is not valid JSON.") from None
    except OSError:
        raise ValueError("Input file could not be read.") from None
    if not isinstance(payload, dict):
        raise ValueError("Input must be a JSON object.")
    return payload


def _save_output(rendered: str, requested_path: str) -> None:
    path = Path(requested_path)
    output_root = Path("outputs").resolve()
    resolved = path.resolve()
    try:
        resolved.relative_to(output_root)
    except ValueError:
        raise ValueError("--save must target the gitignored outputs/ directory.") from None
    resolved.parent.mkdir(parents=True, exist_ok=True)
    resolved.write_text(rendered + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Career Transition V1-alpha input validator. Does not calculate astrology."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--json", help="Inline JSON envelope")
    source.add_argument("--file", help="Path to JSON envelope")
    parser.add_argument("--save", help="Opt-in persistence under the gitignored outputs/ directory.")
    args = parser.parse_args(argv)

    try:
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
            "message": _ERROR_MESSAGE,
        }
        exit_code = 0 if result.valid else 1
    except ValueError as exc:
        output = _error_output(str(exc))
        exit_code = 2

    rendered = json.dumps(output, indent=2)
    if args.save:
        try:
            _save_output(rendered, args.save)
        except (OSError, ValueError) as exc:
            output = _error_output(str(exc))
            rendered = json.dumps(output, indent=2)
            exit_code = 2
    print(rendered)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
