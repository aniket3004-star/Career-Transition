# Priyanka Dalwani Dasha Reference Discrepancy

Status: open research discrepancy; no production calculation convention changed.

## Source facts

The Dharmayana Kundli supplied for Priyanka Dalwani states:

- Birth: 20 October 1989, 05:23, Sambalpur, Odisha, India.
- Ayanamsa: 23.795366°.
- Moon: 13°36′53.12″ Gemini, Nakshatra Ardra, Pada 3, lord Rahu.
- Mahadasha table: Rahu 30-May-1980 → 30-May-1998; Jupiter 30-May-1998 → 30-May-2014; Saturn 30-May-2014 → 30-May-2033.
- Saturn Antardasha endpoints are internally proportional to the source Saturn interval; Saturn/Moon ends 02-Dec-2026.

These are source observations, not values recomputed by this repository.

## Current engine result

The repository's Vimshottari implementation uses:

- 27 equal nakshatras of 13°20′.
- Standard Vimshottari lord order and durations.
- 365.2425 days per dasha year.
- Opening balance calculated from the Moon's fractional position within its nakshatra.

Using the Moon longitude printed by the PDF, the engine places the Rahu Mahadasha endpoint about **4.43 days later** than the source's 30-May-1998 endpoint when the source date is treated as a midnight UTC date marker.

Changing only the year length does not resolve this:

- 365.25 days/year moves the endpoint only slightly later.
- 365.0 days/year still places it about two days later.
- 360 days/year moves it substantially earlier.

Therefore the observed four-day difference cannot be responsibly attributed to ordinary 365.24/365.25 year-length rounding.

## Alternative balance-method check

There is another documented Vimshottari approach: calculate the fraction of the birth Nakshatra from the **time spent between Nakshatra ingress and egress**, rather than from the Moon's angular fraction at birth. Saravali explicitly describes this as a separate "Time Method":

https://saravali.github.io/astrology/dasa_balance.html

I tested that method independently with Swiss Ephemeris, using the birth instant and Lahiri sidereal Moon. For this chart:

- Birth Moon ≈ 73.615129° sidereal.
- Ardra ingress ≈ 19-Oct-1989 11:48 UTC.
- Next Nakshatra ingress ≈ 20-Oct-1989 11:10 UTC.
- The time-method opening balance produces a Rahu endpoint around **1-Jul-1998**, roughly **32 days later** than the Dharmayana 30-May-1998 endpoint.

So the time-method hypothesis does **not** explain the Dharmayana table under that independent ephemeris/convention.

This is an important negative result: we should not introduce a time-based balance method merely because it is a known alternative.

## Reverse diagnostic

If the source endpoint 30-May-1998 is combined with the printed birth time and the repository's 365.2425-day convention, the source endpoint implies an opening balance equivalent to a Moon longitude of approximately **73.623709°**, about **32.23 arcseconds** higher than the Moon longitude printed in the PDF.

This is a diagnostic only. It does **not** establish that Dharmayana internally used that longitude.

## External convention evidence

Independent published calculators document multiple conventions. For example:

- PanchangTime documents a 365.25-day Vimshottari year:
  https://panchangtime.com/methodology/vimshottari-dasha
- Vedic Proof documents a 365.2425-day convention:
  https://vedicproof.com/vimshottari-dasha-api
- Totally Tarot documents a 365.256364-day convention:
  https://totallytarot.net/library/tool/dasha

These differences are real implementation parameters, but they are not large enough in this case to explain the observed four-day opening-boundary discrepancy by themselves.

## Engineering decision

Do **not** change the production Dasha engine to fit this one Kundli.

The Priyanka case remains a real-world regression/reference case with an explicit five-day source-boundary tolerance. The discrepancy remains visible and documented rather than hidden.

Next validation target: obtain an independently reproducible Dasha calculation using the same birth data and determine whether the disagreement comes from the source's internal Moon longitude/ayanamsa/ephemeris or from its opening-balance convention. Only a demonstrated convention should be promoted into the engine.
