# V2 Provider Licensing Review

**Reviewed:** 2026-09-29

## Swiss Ephemeris / Pyswisseph

Swiss Ephemeris is a technically relevant candidate for the astronomical calculation layer, but it is not license-neutral.

The current Swiss Ephemeris documentation states that the library is offered under a dual licensing model:
- GNU Affero General Public License (AGPL); or
- Swiss Ephemeris Professional License.

The documentation states that the licensing choice must be made before distributing software containing Swiss Ephemeris or activating a public service using it.

The Pyswisseph project is itself AGPL-3.0 and incorporates Swiss Ephemeris. Its documentation also notes that the required ephemeris files must be supplied separately.

## Engineering decision

Do not add Pyswisseph as a runtime dependency yet.

Instead:
1. define a provider-neutral calculation interface;
2. validate the interface with standard-library tests;
3. establish independent astronomy goldens;
4. select the final provider/licensing route before public/commercial integration.

This avoids silently creating an incompatible licensing obligation.

## Sources reviewed

- Swiss Ephemeris programmer documentation: https://www.astro.com/swisseph/swephprg.htm
- Swiss Ephemeris documentation: https://www.astro.com/swisseph-download/doc/swisseph.pdf
- Pyswisseph documentation/repository: https://github.com/astrorigin/pyswisseph

This document records engineering research, not legal advice.
