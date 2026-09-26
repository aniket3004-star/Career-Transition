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

## Next gates for any later calculation phase

1. Treat `V1_ACCEPTANCE.md` and `PROJECT_STATUS.md` as the authoritative record of the already-completed V1-alpha acceptance.
2. Before any calculation phase, require a human to explicitly open V2 and independently validate the calculation/provider layer.
3. Keep Dasha, transits, career rules, forecasts, deployment, payments, and recovery of missing historical ZIPs outside V1-alpha until that authorization.
4. Preserve the fail-closed input/provenance boundary and do not represent the alpha as an astrology or career-forecasting product.

## Acceptance status

V1-alpha acceptance evidence is complete as recorded in `V1_ACCEPTANCE.md` and `PROJECT_STATUS.md`. The calculation layer remains uncertified and V2 remains unopened.