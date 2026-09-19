# Career Transition Astrology V1

A local, fail-closed input-validation prototype for a future Vedic astrology career-transition decision-support tool. **This repository is not yet a career forecasting product.** It does not calculate a chart, Dasha, transits, or career outlook.

## Current status

The current CLI validates an explicitly sourced birth-input envelope and emits a JSON status. The calculation layer is not certified; `career_outlook` is always `null`, and the CLI must not be used to make career decisions. `src/astrology/dasha.py` is an isolated experimental calculation module, not wired into the V1-alpha CLI and not independently certified.

## Requirements

- Python 3.11+
- No third-party runtime/test dependencies; tests use Python's standard-library `unittest`.

## Run locally

From the repository root:

```bash
python cli.py --help
python -m unittest discover -s tests -p 'test_*.py' -v
python -m unittest -v test_cli
```

To exercise the CLI, create a local JSON file (do not use real personal birth details in public examples). Example fixture below is synthetic and demonstrates the required envelope shape, not a verified chart:

```json
{
  "birth_date": "2000-01-15",
  "birth_time": "12:00",
  "timezone": "Asia/Kolkata",
  "latitude": 20.0,
  "longitude": 85.0,
  "provider": "synthetic-fixture",
  "provider_version": "1.0",
  "ayanamsha": "Lahiri",
  "zodiac": "sidereal",
  "house_system": "Whole Sign",
  "ephemeris": "declared-only-not-run",
  "calculation_timestamp": "2026-09-20T12:00:00Z",
  "provider_settings_verified": true,
  "source_record_id": "synthetic-001"
}
```

Save it as `input.synthetic.json`, then run:

```bash
python cli.py --file input.synthetic.json
```

A valid schema is **not** proof that the provider values are accurate. The `--save PATH` option explicitly persists the resulting JSON to the path you specify; use a local gitignored location and never commit real birth data or reports. Persistence is off unless `--save` is supplied.

## V1-alpha acceptance boundary

V1-alpha is intentionally limited to a local CLI that validates input and returns a structured status. It must not calculate planetary longitudes, Dasha, transits, or career advice. See [`V1_ACCEPTANCE.md`](V1_ACCEPTANCE.md) for the acceptance checklist and evidence requirements.

## Intended eventual product (not implemented/certified)

- User-controlled birth-data handling and provenance.
- Validated chart positions, Ascendant, Nakshatra, Vimshottari Dasha and relevant transits.
- Explicit, auditable career rules and uncertainty.
- A career-focused 12-month outlook with Favorable, Mixed, and Challenging periods, without numeric scores.

Astrology interpretations are decision-support content, not guarantees. Users make their own career decisions.

## Privacy and security

Do not commit credentials, API keys, personal birth details, private reports, or real user data. Use synthetic fixtures. Review provider licensing and limitations before integration. Human approval is required before any release.
