---
layout: default
title: Datatypes
parent: VIAA Metadatamodel
nav_order: 4
---

# Datatypes

{: .fw-300 }
Datatypes zijn gangbare formaten voor het neerschrijven van een datum, een tijdstip of een taal.

## ISO 8601
{: #iso8601}

De [ISO 8601](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=40874) standaard is een wijdverspreid formaat om datum en tijd te noteren.
Dit formaat wordt gebruikt wanneer het moment _gekend_ en _exact_ is (bv. het moment van instroom).

Er zijn drie gangbare notaties:
- Datum (`YYYY-MM-DD`): `2001-02-03`
- Tijd (`hh:mm:ss`): `09:30:01`
- Datum en tijd (`YYYY-MM-DDThh:mm:ss`) : `2001-02-03T09:30:01`

Een tijdzone kan worden aangeduid door het uurverschil met GMT achteraan met een `+` toe te voegen: `2004-01-01T10:10:10+05:00`

Meer info vind je op de [wikipedia pagina over ISO 8601](https://nl.wikipedia.org/wiki/ISO_8601)
## Extended Date Time Format (EDTF)
{: #edtf}

Om verfijning en benaderende waarden toe te staan wordt [Extended Date Time Format (EDTF)](https://www.loc.gov/standards/datetime/) gebruikt.
De EDTF-standaard voegt verschillende vormen van verfijning, veralgemening en benaderende waarden toe aan de [ISO 8601](#iso8601) notatie.
Dit formaat wordt dus gebruikt wanneer het moment _ongekend_ of _inexact_ is (bv. de opname van een oude film).

De EDTF-standaard is opgebouwd uit verschillende levels; een Level 0 EDTF string bestaat uit 1 van 3 features (datum, datum/tijd, of interval).
Een Level 1 EDTF string bestaat uit dezelfde features, maar ondersteunt onzekere, onbekende, en datums bij benadering.
Level 2 ondersteunt nog meer opties voor onzekere, onbekende, en onderdelen van een datum bij benadering.
Ook uitgebreide tijdsintervallen, en wetenschappelijke notatie van datums vallen onder Level 2.

Sinds MediaHaven versie 22.1 worden datum/tijd-strings bij ingest gevalideerd tegen de EDTF-standaard.
Deze strings moeten dus voldoen aan de features gedefineerd in de standaard anders worden de items niet verwerkt.
Er is volledige ondersteuning voor de Levels 0 en 1.
Level 2 is beperkt ondersteund, maar wordt mogelijks in de toekomst nog verder uitgebreid.

Een niet-exhaustieve lijst van EDTF features die ondersteund worden in MediaHaven 22.1:

|Datumnotatie|Voorbeeld|Opmerkingen|
|:----|:----|:----|
|[Lege datum]| | |
|Onbekende datum|XXXX-XX-XX| |
|Volledige datum|1988-10-27| |
|Volledige datum met tijdstip|1988-10-27T15:35:54|T duid tijdstip aan|
|Volledige datum met tijdstip (UTC)|1988-10-27T15:35:54Z|Z duidt gecoördineerde wereldtijd (UTC) aan|
|Volledige datum met tijdstip en shift|1988-10-27T15:35:54+1:00|+1:00 duidt aan dat de tijdszone UTC+1 is|
|Jaartal|1988| |
|Jaartal en maand|1988-10| |
|Jaartal en seizoen|1988-23|21 = lente, 22 = zomer, 23 = herfst, 24 = winter|
|Negatief kalender jaar|-1988| |
|Letter prefixed jaartal|Y170000002|Datums voor het jaar -9999 en na het jaar 9999|
|Datum bij benadering|1988-10~|Tilde ~ als laatste karakter|
|Datum onzeker|1988-10?|Vraagteken ? als laatste karakter|
|Datum onzeker en bij benadering|1988-10%|Procentteken % als laatste karakter|
|Niet specifieke eeuw|19XX| |
|Niet specifiek decennium|198X| |
|Niet specifieke maand|1988-XX| |
|Niet specifieke dag in de maand|1988-10-XX| |
|Niet specifieke dag in het jaar|1988-XX-XX| |
|Tijdsinterval|1988-10/1989|De oudste datum moet altijd eerst staan. Onbekende waardes zijn niet toegestaan (bv. 1988-XX-XX/1989 mag niet)|
|Interval met onbekend begin|/1988-10-27| |
|Interval met onbekend einde|1988-10-27/| |
|Interval met open begin|../1988-10-27| |
|Interval met open einde|1988-10-27/..| |
|Interval met één datum bij benadering|1988-10%/1989| |

Om te controleren of een datum/tijd string gevalideerd kan worden in de EDTF-standaard kan je gebruik maken van de [Extended Date Time Format Levels 0,1 and 2 Validation Service](https://digital2.library.unt.edu/edtf/).
De pagina legt uit hoe je manueel een string kan valideren (zie ook hieronder), of gebruik kan maken van API requests om bv. een automatische controle in te bouwen.

- Om te bepalen of een datum conform is aan EDTF Level 0-2, vul je de datum in onderaan [deze pagina](https://digital2.library.unt.edu/edtf/) in het invoerveld. Klik daarna op “Submit”.
- Het resultaat is `Valid EDTF date` wanneer de datum aanvaard wordt, of `Invalid EDTF date` wanneer de datum ongeldig is.
- MediaHaven zal een ongeldige EDTF-datum niet aanvaarden.
