# Career Transition Astrology V1

A decision-support project exploring Vedic astrology-based career timing. It is intended to provide transparent interpretations and supporting evidence—not to make career decisions for users or provide deterministic guarantees.

## Project status

Repository bootstrap. Existing project artifacts (rules, validators, audits, and test packs) are maintained separately and must be reviewed and integrated deliberately. No prior artifact is considered verified merely because it has been reported as created.

## V1 objectives

- Accept user-provided birth details with clear validation and privacy choices.
- Calculate and validate geocentric planetary positions, Ascendant, Nakshatra, Vimshottari Mahadasha/Antardasha, and relevant transits.
- Apply an explicit, auditable career-rule engine.
- Explain conclusions in plain language with traceable evidence and uncertainty.
- Present a career-focused outlook over the next 12 months, including Favorable, Mixed, and Challenging periods without numeric scores.
- Keep the system in decision-support mode: users make their own career choices.

## Scope and guardrails

- Primary timing: Vimshottari Mahadasha and Antardasha. Pratyantardasha is considered only after validation.
- Career houses: 2nd, 6th, 10th, and 11th; 7th when examining a transition from employment to entrepreneurship.
- Transit focus: Jupiter, Saturn, Rahu, and Ketu.
- AI may explain validated calculations and rules; it must not independently invent or recalculate astrology data.
- In-memory processing by default. Persist chart data only with explicit opt-in.
- No payments in the initial data-collection period.
- Human approval is required before any release.

## Planned architecture

1. Birth-details input and validation.
2. Calculation layer for chart positions, Ascendant, Nakshatra, Dasha, and transits.
3. Validated career-rule engine with evidence references and confidence/uncertainty handling.
4. AI interpretation layer restricted to explaining supplied calculations and rules.
5. Quality, safety, regression, and incident gates.
6. Career report with executive summary, monthly outlook, notable windows, and expandable reasoning.

## Development workflow

Backlog → scoped task → implementation branch → automated tests and evidence → independent review → merge candidate → human release approval.

Failures block dependent work and create tracked defects. Tests should run on changes; broader regression and audit checks should run before release. Never represent an unrun test as passing.

## Repository organization (planned)

- `docs/` — product requirements, architecture, decisions, and task register
- `src/` — application and calculation code (to be added after artifact audit)
- `tests/` — automated and offline validation tests
- `data/` — non-sensitive fixtures only; never commit personal birth charts or secrets
- `reports/` — validation and audit evidence

## Immediate next steps

1. Inventory and inspect the existing ZIP artifacts.
2. Recover and verify the original task register before marking tasks complete.
3. Establish the canonical engine and validator interfaces.
4. Add reproducible setup, tests, and CI.
5. Integrate the validated core in small, reviewable changes.

## Privacy and security

Do not commit credentials, API keys, personal birth details, private reports, or real user data. Use synthetic fixtures for tests. Document any external data provider and its licensing/limitations before integration.
