# V2 Active Status

**State:** V2 explicitly opened by human on 2026-09-29.

## Objective

Extend the accepted V1-alpha input/provenance boundary into a validated calculation pipeline for career-transition decision support.

## Non-negotiable gates

1. No user-facing career interpretation from uncertified calculations.
2. Every calculation layer must have independent validation evidence before downstream use.
3. Preserve V1 fail-closed input validation and provenance.
4. Do not fit calculation conventions to a single reference chart.
5. Keep deterministic career predictions out of the product.

## Execution order

1. Calculation-provider contract and licensing/precision review.
2. Planetary longitude / ayanamsha / timezone goldens.
3. Ascendant, houses and Nakshatra validation.
4. Vimshottari Dasha validation across multiple independent cases.
5. Transit calculations and regression cases.
6. Auditable career-rule engine.
7. Career-window and 12-month outlook layer.
8. Interpretation and safety gates.
9. End-to-end regression and V2 acceptance evidence.

## Existing research carried forward

The prior v2-calculation-foundation work contains an isolated Vimshottari implementation and a documented Priyanka Dalwani reference discrepancy. That discrepancy remains unresolved and must not be hidden or used to justify changing conventions without independent evidence.

## Current stop point

The first implementation gate is the calculation-provider contract and independent astronomy test harness. Dasha is downstream of a certified sidereal Moon longitude and therefore should not yet be wired into the production CLI.