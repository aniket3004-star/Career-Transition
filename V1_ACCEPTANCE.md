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
- [ ] `requirements.txt` or `pyproject.toml` documents the test/runtime dependency policy and pins any third-party test dependencies actually used. If tests use only the Python standard library, explicitly state that no third-party test dependency needs pinning.
- [ ] `README.md` has exact local run commands
- [ ] `.gitignore` excludes secrets, venv, real birth data, ZIP dumps
- [ ] No personal birth charts in git

### B. Input contract (already started)
- [ ] `src/validation/input_contract.py` rejects missing/malformed date, time, coords, timezone
- [ ] Numeric timezone offset alone is rejected; an IANA timezone identifier is required in the `timezone` field (the implementation's canonical key; do not silently accept numeric offsets)
- [ ] Implicit ayanamsha/zodiac/house/node defaults cannot set `accuracy_verified` or `career_rules_eligible`
- [ ] Status flags cannot skip prerequisites (`career_rules_eligible` stays false in V1-alpha)
- [ ] `tests/test_input_contract.py` covers happy path + fail-closed cases
- [ ] GitHub Actions workflow on `main` and PRs runs those tests

### C. App shell
- [ ] `src/` has a CLI entrypoint, e.g. `python -m src.cli` or `python src/cli.py`
- [ ] CLI accepts JSON or flags for the input envelope
- [ ] CLI writes JSON to stdout and a non-zero exit code on reject
- [ ] CLI never prints career advice or planet longitudes in V1-alpha
- [ ] Optional: one-page local form that posts to the same validator

### D. Privacy
- [ ] Default is in-memory only
- [ ] Persistence is off unless `--save` is explicitly passed
- [ ] Saved files go to a gitignored directory
- [ ] Logs do not include raw birth data in issue titles or public docs

### E. Evidence
- [ ] `PROJECT_STATUS.md` lists the commit SHA that satisfies this checklist
- [ ] `V1_HANDOFF.md` exists with run commands, limitations, and V2 next gates
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
