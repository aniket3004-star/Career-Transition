# Canonical Engine & Career Rules Review

Audit date: 2026-09-19

## Files inspected
- `career-transition-v1-canonical-engine.zip`
- `career-transition-v1-career-rules-v35.zip`
- `career-transition-v1-backtest-v36.zip`
- `career-transition-v1-critical-audit-v37.zip`
- `career-transition-v1-validation-harness.zip`

## Canonical architecture
The canonical layer defines a provider-neutral schema and adapter contract. It expects raw longitudes plus calculation metadata, derives sign/Nakshatra/pada/Whole Sign houses, and uses a fail-closed validation sequence: input → provider configuration → astronomy → Vedic derivations → Dasha → transits → calculation validated → rules → AI explanation.

## Rule registry status
The v35 registry explicitly lists all seven candidate families as `BLOCKED`: active MD/AD connections to the 10th, 6th, 11th, and entrepreneurship-specific 7th/10th; plus Jupiter, Saturn, and Mean Rahu/Ketu transit activations. D10 is excluded from the primary classifier pending its own validation. Fast planets cannot change primary classification.

## Backtest and audit interpretation
- v36 defines provenance-first evidence and promotion gates; it does not promote any rule.
- v37 reports 5/5 exploratory associations for one candidate rule family, but explicitly flags selection bias, coarse event dates, and lack of blinded controls; decision: no primary rule promoted.
- v37 labels a number of foundations implemented/local-testable and others internally tested but uncertified. It separately identifies missing live provider comparisons, independent engine comparisons, real Dasha checks, transit tests, blinded controls, production classification, AI report generation, online environment, and privacy implementation.
- These statements are artifact-reported findings. This review has not independently reproduced the underlying five-chart calculations.

## Harness code concerns / verification limits
The inspected harness contains a Dasha helper that advances dates using a fixed 365.2425-day year approximation and a runner that reads a fixed fixture path and hardcodes a birth timestamp. The v37 critical audit itself warns this approximation is a sanity aid, not authoritative production Dasha timing. The harness README/plan and code require a careful reproducibility review before being treated as executable validation evidence.

The harness includes a Swiss-reference calculation layer, canonical validator, Dasha validator, and a Supabase function scaffold. Their presence alone does not establish that dependencies install, the function deploys, provider calls succeed, or expected values match independent references.

## Disposition
**Do not promote rules or call the product production-ready.** Preserve the fail-closed gates. Next, inspect the full harness source and fixtures, run tests in a reproducible environment, reconcile Dasha dates independently, then build controlled provider comparisons and blinded backtests.

## Task register dependency
The original numbered tasks #1–#45 have not been recovered from their authoritative source in this audit. Do not fabricate a replacement or mark task completion against guessed numbering.