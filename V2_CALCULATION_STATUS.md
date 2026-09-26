# V2 Calculation Status

## Current state

V2 has been explicitly opened by the human on 2026-09-26.

The first implementation slice is on branch `v2-calculation-foundation`:
- calculation result contract
- provider metadata contract
- dependency-enforced validation gates
- unit tests for the gate chain

No planetary position is currently calculated or certified.

## Validation gates

`schema_valid -> provenance_complete -> calculation_reproduced -> accuracy_verified -> career_rules_eligible`

A downstream state cannot be true while an upstream state is false.

## Provider decision

A real ephemeris provider is the next dependency. Swiss Ephemeris is a technically viable candidate, but its official documentation describes dual AGPL/professional licensing and requires the developer to choose the licensing model before distribution/public service. No paid license has been purchased and no licensing decision has been made.

Therefore:
- do not add Swiss Ephemeris as a mandatory dependency yet;
- do not claim any chart calculation is verified;
- do not use a synthetic provider as an accuracy reference;
- evaluate an independent reference/calculation path before certification.

## Next executable gate

Implement the provider adapter boundary and a reproducible golden-case harness that can compare planetary longitudes/Ascendant under explicitly recorded conventions and predeclared tolerances.

Only after that harness has an independent reference source should real birth-data validation begin.

## Not started

- real ephemeris calculation
- independent astronomy goldens
- Dasha integration
- transit engine
- career rules
- career outlook/UI
- deployment

## Safety boundary

No real personal birth data, credentials, paid services, production deployment, or career classifications are to be introduced without the appropriate approval/evidence.
