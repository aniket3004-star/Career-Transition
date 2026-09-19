# V1-alpha handoff

## State

**V1-alpha is an input-validation prototype, not a certified astrology or career-forecasting product.** The acceptance checklist in `V1_ACCEPTANCE.md` remains authoritative; do not mark V1-alpha complete unless every checklist item has evidence.

## Run locally

Requirements: Python 3.11+; no third-party runtime or test dependencies.

From the repository root:

```bash
python cli.py --help
python -m unittest discover -s tests -p 'test_*.py' -v
python -m unittest -v test_cli
```

For a CLI example, prepare a **synthetic** JSON envelope following the example in `README.md`, then run:

```bash
python cli.py --file input.synthetic.json
```

Optional persistence must be explicitly requested and saved only under the gitignored `outputs/` directory:

```bash
python cli.py --file input.synthetic.json --save outputs/result.json
```

## Current boundaries and cautions

- The CLI validates input/provenance and emits structured status; it does not provide career advice.
- `career_outlook` remains null. A schema-valid envelope does not establish astronomical accuracy.
- The calculation layer is not certified. The isolated `src/astrology/dasha.py` module is not integrated into the alpha CLI or independently certified.
- Do not commit real birth details, reports, credentials, or API keys. Use synthetic fixtures.
- Do not use this prototype to make career decisions.

## Next gates before calling V1-alpha accepted

1. Audit every unchecked item in `V1_ACCEPTANCE.md` against the current repository and record evidence beside each checked item.
2. Verify input-contract edge cases, privacy behavior, CLI exit/output behavior, and CI on the exact candidate commit.
3. Complete independent calculation validation and provider/licensing review only after a human explicitly opens the later calculation phase; these are outside V1-alpha.
4. Keep Dasha, transits, career rules, forecasts, deployment, payments, and recovery of missing historical ZIPs out of this alpha scope.
5. Update `PROJECT_STATUS.md` with the exact acceptance commit and green CI evidence only when the checklist is genuinely complete.

## Acceptance status

This handoff does not certify acceptance. Consult `V1_ACCEPTANCE.md` and `PROJECT_STATUS.md` for the current evidence and outstanding items.