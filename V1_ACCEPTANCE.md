# V1-alpha acceptance (agent stop condition)

Status: **NOT DONE**

An agent may mark V1-alpha done only when every item below has evidence in the repo (test name, CI run, or file path). Unchecked items mean keep working. Do not start V2.

## Product scope for V1-alpha
A local CLI (and optional tiny local web form) that:
1. Collects birth details.
2. Validates them with the fail-closed input contract.
3. Returns either a structured **quarantined** envelope or a **schema_valid + provenance_complete** envelope.
4. Does **not** calculate planetary longitudes, Dasha, transits, or career outlook yet.
5. Prints a clear "calculation layer not certified" status.

This is intentional. The charter forbids unvalidated astrology driving user-facing advice.

## Checklist

### A. Repository hygiene
- [x] `requirements.txt` or `pyproject.toml` documents the test/runtime dependency policy and pins any third-party test dependencies actually used. If tests use only the Python standard library, explicitly state that no third-party test dependency needs pinning.
  Evidence: `pyproject.toml` declares Python >=3.11, zero runtime dependencies, and `test-dependencies = "stdlib-only"`.
- [x] `README.md` has exact local run commands
  Evidence: `README.md` documents `python cli.py --help`, unittest discovery, and `python -m unittest -v test_cli`.
- [x] `.gitignore` excludes secrets, venv, real birth data, ZIP dumps
  Evidence: `.gitignore` excludes `.env*`, key/certificate files, birth/private/local data, outputs, birth/chart JSON, ZIP and log dumps.
- [x] No personal birth charts in git
  Evidence: `docs/PUBLIC_BIRTH_DATA_AUDIT.md` records the complete tracked-tree review and repository-content searches for known personal birth markers; no matches were returned. The root CLI fixture is synthetic.

### B. Input contract (already started)
- [x] `src/validation/input_contract.py` rejects missing/malformed date, time, coords, timezone
  Evidence: `tests/test_input_contract.py` covers invalid dates/times, unknown timezone, coordinate range/type/finite checks, and DST-local-time failures.
- [x] Numeric timezone offset alone is rejected; an IANA timezone identifier is required in the `timezone` field (the implementation's canonical key; do not silently accept numeric offsets)
  Evidence: `tests/test_input_contract.py::test_rejects_numeric_timezone_offset`.
- [x] Implicit ayanamsha/zodiac/house/node defaults cannot set `accuracy_verified` or `career_rules_eligible`
  Evidence: `tests/test_input_contract.py::test_rejects_missing_configuration_instead_of_defaulting`; `cli.py` hard-codes `accuracy_verified=false` and `career_rules_eligible=false`.
- [x] Status flags cannot skip prerequisites (`career_rules_eligible` stays false in V1-alpha)
  Evidence: `cli.py` always emits `career_rules_eligible: false` and `career_outlook: null`.
- [x] `tests/test_input_contract.py` covers happy path + fail-closed cases
  Evidence: `tests/test_input_contract.py` contains the complete explicit-metadata happy path plus rejection cases.
- [x] GitHub Actions workflow on `main` and PRs runs those tests
  Evidence: `.github/workflows/python-tests.yml` triggers on pushes and pull requests to `main` and runs unittest discovery plus `test_cli`.

### C. App shell
- [x] `src/` has a CLI entrypoint, e.g. `python -m src.cli` or `python src/cli.py`
  Evidence: `src/cli.py` exists and `tests/test_cli.py` contains the src-entrypoint regression coverage documented in `PROJECT_STATUS.md`.
- [x] CLI accepts JSON or flags for the input envelope
  Evidence: `cli.py` accepts mutually exclusive `--json` and `--file` sources.
- [x] CLI writes JSON to stdout and a non-zero exit code on reject
  Evidence: `cli.py` renders structured JSON and returns exit code 1 for validation rejection and 2 for input/IO errors.
- [x] CLI never prints career advice or planet longitudes in V1-alpha
  Evidence: `cli.py` uses an explicit input-only message and does not calculate or emit planetary positions, Dasha, transits, or career advice.
- [ ] Optional: one-page local form that posts to the same validator

### D. Privacy
- [x] Default is in-memory only
  Evidence: `cli.py` only calls `_save_output` when `--save` is explicitly supplied.
- [x] Persistence is off unless `--save` is explicitly passed
  Evidence: `cli.py` gates persistence on `args.save`; `tests/test_cli.py` covers opt-in saving.
- [x] Saved files go to a gitignored directory
  Evidence: `_save_output` rejects paths outside `outputs/`; `.gitignore` excludes `outputs/`.
- [x] Logs do not include raw birth data in issue titles or public docs
  Evidence: repository workflow/status documentation uses synthetic examples and does not include raw birth-data logging; public fixture guidance explicitly prohibits real birth data.

### E. Evidence
- [ ] `PROJECT_STATUS.md` lists the commit SHA that satisfies this checklist
- [x] `V1_HANDOFF.md` exists with run commands, limitations, and V2 next gates
  Evidence: `V1_HANDOFF.md` contains local run commands, alpha boundaries, privacy cautions, and next gates.
- [ ] CI is green on that commit

## Explicitly out of V1-alpha
Do not implement these until a human opens V2:
- Swiss Ephemeris / provider chart calculation
- Independent astronomy goldens
- Vimshottari Dasha / transits
- Career rule engine and 12-month outlook
- Deploy / domain / payments
- Recovering missing historical ZIPs (user must supply them)

## How to check a box
Replace `- [ ]` with `- [x]` and add a one-line evidence note under the item. Do not mark a box complete based only on a claim in the status document; inspect the cited file/test/CI evidence first.
