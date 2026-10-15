# Datatypes

Datatypes are common formats for writing a date, a time, or a language.

## ISO 8601

<a id="iso8601"></a>

The [ISO 8601](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=40874) standard is a widely used format for noting date and time.
This format is used when the moment is _known_ and _exact_ (e.g., the moment of intake).

There are three common notations:
- Date (`YYYY-MM-DD`): `2001-02-03`
- Time (`hh:mm:ss`): `09:30:01`
- Date and time (`YYYY-MM-DDThh:mm:ss`): `2001-02-03T09:30:01`

A time zone can be indicated by the hour difference with GMT appended with a `+`: `2004-01-01T10:10:10+05:00`

More info can be found on the [wikipedia page about ISO 8601](https://nl.wikipedia.org/wiki/ISO_8601)

## Extended Date Time Format (EDTF)

<a id="edtf"></a>

To allow for refinement and approximate values, the [Extended Date Time Format (EDTF)](https://www.loc.gov/standards/datetime/) is used.
The EDTF standard adds various forms of refinement, generalization, and approximate values to the [ISO 8601](#iso8601) notation.
This format is therefore used when the moment is _unknown_ or _inexact_ (e.g., the recording of an old film).

The EDTF standard is built from several levels; a Level 0 EDTF string consists of 1 of 3 features (date, date/time, or interval).
A Level 1 EDTF string consists of the same features but supports uncertain, unknown, and approximate dates.
Level 2 supports even more options for uncertain, unknown, and approximate date components.
Extended time intervals, and scientific notation of dates also fall under Level 2.

Since MediaHaven version 22.1, date/time strings are validated against the EDTF standard.
These strings must therefore conform to the features defined in the standard or else the items will not be processed.
Full support for Levels 0 and 1 is available.
Level 2 is partially supported but may be expanded in the future.

A non-exhaustive list of EDTF features supported in MediaHaven 22.1:

|Date notation|Example|Notes|
|:----|:----|:----|
|[Empty date]| | |
|Unknown date|XXXX-XX-XX| |
|Full date|1988-10-27| |
|Full date with time|1988-10-27T15:35:54|T indicates time|
|Full date with time (UTC)|1988-10-27T15:35:54Z|Z indicates coordinated world time (UTC)|
|Full date with time and shift|1988-10-27T15:35:54+1:00|+1:00 indicates time zone UTC+1|
|Year|1988| |
|Year and month|1988-10| |
|Year and season|1988-23|21 = spring, 22 = summer, 23 = fall, 24 = winter|
|Negative calendar year|-1988| |
|Letter-prefixed year|Y170000002|Dates for the year -9999 and after the year 9999|
|Approximate date|1988-10~|Tilde ~ as last character|
|Uncertain date|1988-10?|Question mark ? as last character|
|Uncertain and approximate date|1988-10%|Percent sign % as last character|
|Non-specific century|19XX| |
|Non-specific decade|198X| |
|Non-specific month|1988-XX| |
|Non-specific day in month|1988-10-XX| |
|Non-specific day in year|1988-XX-XX| |
|Time interval|1988-10/1989|The oldest date must always come first. Unknown values are not allowed (e.g., 1988-XX-XX/1989 is not allowed)|
|Interval with unknown start|/1988-10-27| |
|Interval with unknown end|1988-10-27/| |
|Interval with open start|../1988-10-27| |
|Interval with open end|1988-10-27/..| |
|Interval with approximate date|1988-10%/1989| |

To check if a date/time string can be validated in the EDTF standard, you can use the [Extended Date Time Format Levels 0,1 and 2 Validation Service](https://digital2.library.unt.edu/edtf/).
The page explains how to manually validate a string (see below), or you can use API requests to, for example, build an automatic check.

- To determine if a date conforms to EDTF Level 0-2, enter the date in the input field at the bottom of [this page](https://digital2.library.unt.edu/edtf/) and click “Submit”.
- The result is `Valid EDTF date` if the date is accepted, or `Invalid EDTF date` if the date is invalid.
- MediaHaven will not accept an invalid EDTF date.
