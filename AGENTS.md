# Agent instructions — Career Transition V1

You are an implementation agent for this repository.
Do not wait for the user to type "continue".
Do not ask what to do next if the next task is already defined.

## Mission
Ship **V1-alpha** only. Then stop and wait for a human to start V2.

V1-alpha is the smallest testable product shell that:
- accepts birth details under the fail-closed input contract
- records explicit calculation provenance
- refuses to invent chart math or career advice
- has tests + CI green
- can be demoed locally

Full validated astrology (independent ephemeris goldens, Dasha, transits, career rules) is **V2+**. Do not start V2 in this run.

## Read first, in this order
1. `V1_ACCEPTANCE.md` — stop condition
2. `AUTONOMY_CHARTER.md` — guardrails
3. `PROJECT_STATUS.md` — current state
4. `specs/INPUT_PROVENANCE_CONTRACT.md`
5. Existing `src/` and `tests/`

## Loop
Repeat until `V1_ACCEPTANCE.md` is fully checked and CI is green:

1. Pick the next unchecked V1-alpha item.
2. Make the smallest code change.
3. Add or update tests.
4. If you can run tests, run them. If you cannot, say so; do not claim pass.
5. Update `PROJECT_STATUS.md` with evidence (commit SHA, files, what was / was not run).
6. Commit in small slices.
7. If blocked only by a user-only item (secrets, paid API, ZIP artifacts, release approval), write the blocker in `PROJECT_STATUS.md` and continue any unblocked V1-alpha work.

## Hard stop
Stop the run when ALL of these are true:
- Every box in `V1_ACCEPTANCE.md` is checked with evidence
- You have written `V1_HANDOFF.md`
- You have not enabled career-rule advice

Then tell the human: "V1-alpha complete. Ready for V2 after review."

## Never do
- Fabricate task register #1–#45
- Claim ZIP artifacts exist in this repo (they are not in the git tree)
- Silently default ayanamsha / timezone / house system
- Emit Favorable/Mixed/Challenging career periods
- Deploy, spend money, or request production secrets
- Commit real birth data or API keys
- Write more planning docs instead of code when code is unblocked
