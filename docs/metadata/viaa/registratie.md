---
layout: default
title: "Velden: Registratie dragers"
parent: VIAA Metadatamodel
nav_order: 2
---

{: .fw-300 }
Deze velden worden ingevuld door contentpartners tijdens de registratie van analoog materiaal, met oog op een digitaliseringsproject uitgevoerd door meemoo. Deze informatie wordt standaard automatisch overgenomen uit de registratieinformatie in de [registratietool](http://registratie.meemoo.be).

{: .important }
Deze pagina dient louter ter documentatie van de relevante velden bij registratie. Onderstaande velden kunnen dus niet gebruikt worden bij bv. een digitaal instroomproces.

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>
                                                                                                                          
# Dragerinformatie

## Bestandstype

Type drager (onderverdeeld in `audio`, `video`, `film`, en `paper`).


| **XML element**            | `<type/>`                                                                                                                                           |
| **Datatype**               | Gecontroleerde lijst: zie onze pagina over [drager registratie in de registratietool](https://portaal.meemoo.be/nl/portaal/support-category/item/hoe-registreer-ik-een-nieuwe-drager-in-ams) |
| **Verplichting**           | Verplicht indien gekend                                   |
| **Herhaalbaar**            | Nee                                                                                                                                                 |

```xml
<type>video</type>
```

## Formaat

Een omschrijving van het type materiële drager waarop het item oorspronkelijk is vastgelegd.


| **XML element**        | `<format/>`                                                                                                                                         |
| **Datatype**           | Gecontroleerde lijst: zie onze pagina over [drager registratie in de registratietool](https://portaal.meemoo.be/nl/portaal/support-category/item/hoe-registreer-ik-een-nieuwe-drager-in-ams) |
| **Verplichting**       | Verplicht indien gekend                                   |
| **Herhaalbaar**        | Nee                                                                                                                                                 |

```xml
<format>Betacam SP</format>
```

## Formaatversie

Een specifieke formaatversie, die voor sommige dragerformaten wordt gevraagd, zoals voor VHS of DVCPRO.


| **XML element**        | `<format_version/>`                                                                                                                                         |
| **Datatype**           | Gecontroleerde lijst: zie onze pagina over [drager registratie in de registratietool](https://portaal.meemoo.be/nl/portaal/support-category/item/hoe-registreer-ik-een-nieuwe-drager-in-ams) |
| **Verplichting**       | Verplicht                                   |
| **Herhaalbaar**        | Nee                                                                                                                                                 |

```xml
<format_version>DVCPRO HD</format_version>
```

## Barcode drager

Dit is de barcode van meemoo die op de materiële drager werd aangebracht.


| **XML element**        | `<carrier_barcode/>`                                                                                              |
| **Datatype**           | ID                                                                                                                |
| **Verplichting**       | Verplicht |
| **Herhaalbaar**        | Nee                                                                                                               |

```xml
<carrier_barcode>AACC_AMS_000540</carrier_barcode>
```

## Originele locatie

Dit is de standplaats van de originele materiële drager. Dit kan een lokaal- of reknummer, een plaatskenmerk of de naam van een collectie zijn.


| **XML element**        | `<original_location/>`                                                                                            |
| **Datatype**           | Vrije tekst                                                                                                       |
| **Verplichting**       | Optioneel |
| **Herhaalbaar**        | Nee                                                                                                               |

```xml
<original_location>10A</original_location>
<original_location>rek 12, plank 3</original_location>
<original_location>Erfenis Amaat Burssens</original_location>
```

## Merk

Dit is het merk of de fabrikant van de materiële drager.


| **XML element**        | `<brand/>`                                                                                                                                          |
| **Datatype**           | Gecontroleerde lijst: zie onze pagina over [drager registratie in de registratietool](https://portaal.meemoo.be/nl/portaal/support-category/item/hoe-registreer-ik-een-nieuwe-drager-in-ams) |
| **Verplichting**       | Verplicht                                   |
| **Herhaalbaar**        | Nee                                                                                                                                                 |

```xml
<brand>Philips</brand>
```

## Productiedatum drager

Dit is de (geschatte) productiedatum van de materiële drager.


| **XML element**        | `<date/>`                                                                                                          |
| **Datatype**           | [Extended Date Time Format (EDTF)]({{ site.baseurl }}{% link docs/metadata/viaa/datatypes.md %}#edtf)                                                                                |
| **Verplichting**       | Verplicht |
| **Herhaalbaar**        | Nee                                                                                                                |

```xml
<date>1937-09-07</date>
```

## Kern/Spoel

In dit veld kan worden aangegeven of de tape op een kern dan wel op een open spoel is bevestigd.


| **XML element**        | `<core_reel/>`                                                                                                                                                        |
| **Datatype**           | "Kern" / "Spoel" (zie ook onze pagina over [drager registratie in de registratietool](https://portaal.meemoo.be/nl/portaal/support-category/item/hoe-registreer-ik-een-nieuwe-drager-in-ams)) |
| **Verplichting**       | Verplicht indien gekend                                                    |
| **Herhaalbaar**        | Nee                                                                                                                                                                   |

```xml
<core_reel>Spoel</core_reel>
```

## Deterioratiefenomenen

Fenomenen -- doorgaans onder invloed van fysische of chemische factoren -- die mogelijks de integriteit en raadpleegbaarheid van de gegevens op de drager in gevaar kunnen brengen.


| **XML element**        | `<preservation_problems/>`                                                                                                                           |
| **Datatype**           | Gecontroleerde lijst: zie onze pagina over [drager registratie in de registratietool](https://portaal.meemoo.be/nl/portaal/support-category/item/hoe-registreer-ik-een-nieuwe-drager-in-ams)) |
| **Verplichting**       | Optioneel                                   |
| **Herhaalbaar**        | Ja                                                                                                                                                   |

```xml
<preservation_problems>disc rot</preservation_problems>
```

## Bijbehorende documenten/dragers aanwezig?

Bijbehorende documenten/dragers die de contentpartner niet apart kan bewaren. Bij registratie wordt dus aangeduid dat er bij de verpakte drager andere dragers zitten. Deze bijbehorende documenten/dragers worden dus niet mee gedigitaliseerd, maar wel gesignaleerd aan de Service Provider, o.m. om verlies tegen te gaan.

| **XML element**            | `<related_documents />`                                                                   |
| **Datatype**               | "0" of "1"                                                           |
| **Verplichting**           | Verplicht                                                                                                     |
| **Herhaalbaar**            | Nee                                                                                                            |

```xml
<related_documents>0</related_documents>
```

## Kleur

De kleur van de inhoud van de drager. Dit duidt bijvoorbeeld het verschil tussen zwart-wit en kleur fotografie of film.

| **XML element**            | `<color />`                                                                   |
| **Datatype**               | Gecontroleerde lijst                                                         |
| **Verplichting**           | Verplicht                                                                                                     |
| **Herhaalbaar**            | Nee                                                                                                            |

```xml
<color>Color</color>
```

### Mogelijke waarden

- `Black-white`
- `Color`
- `Coloured`

## Label aanwezig?

Het al dan niet aanwezig zijn van een label op de drager.

| **XML element**            | `<label_present/>`                                                                   |
| **Datatype**               | "0" of "1"                                                          |
| **Verplichting**           | Verplicht                                                                                                     |
| **Herhaalbaar**            | Nee                                                                                                            |

```xml
<label_present>1</label_present>
```

## Opschrift originele doos

Een kopie van eventuele opschriften op de originele bewaardoos van de drager.

| **XML element**            | `<inscription_original_carrier_box/>`                                                                   |
| **Datatype**               | Vrije tekst                                                          |
| **Verplichting**           | Optioneel                                                                                                     |
| **Herhaalbaar**            | Nee                                                                                                            |

```xml
<inscription_original_carrier_box>1234</inscription_original_carrier_box>
```

## Abraham ID

Identifier van de krantentitel die ervoor zorgt dat de link met Abraham - Catalogus van Belgische kranten, een databank van de Vlaamse Erfgoedbibliotheek waarin het krantenbezit van bijna honderd bewaarinstellingen in Vlaanderen en Brussel is opgenomen - blijft bewaard.

| **XML element**            | `<abraham_ID/>`                                                                   |
| **Datatype**               | ID                                                          |
| **Verplichting**           | Verplicht                                                                                                     |
| **Herhaalbaar**            | Ja                                                                                                            |

```xml
<abraham_ID>c:bnc:5224</abraham_ID>
```

## Editie
	
Hierbij gaat het om de soort uitgave van de editie. Een krant kent meerdere soorten edities: ochtend-, middag-, avond- of weekendeditie.

| **XML element**            | `<edition />`                                                                   |
| **Datatype**               | Gecontroleerde lijst _of_ Vrije tekst                                                          |
| **Verplichting**           | Verplicht indien gekend                                                                                                    |
| **Herhaalbaar**            | Ja                                                                                                            |

```xml
<edition>Afternoon</edition>
```

### Mogelijke waarden

- `Morning`
- `Afternoon`
- `Evening`
- `Weekend`

## Jaargang en volumenummer

Een krant verschijnt serieel. Via jaargangen en volumenummers wordt aangegeven om welke uitgave van een langlopende titel het gaat. 

| **XML element**            | `<number />`                                                                   |
| **Datatype**               | Tekst die een numerieke waarde, gevolgd met een punt als onderscheidingsteken en opnieuw een numerieke waarde bevat. Als onbekende kan een 'x' worden gebruikt.                                                           |
| **Verplichting**           | Verplicht indien gekend                                                                                                     |
| **Herhaalbaar**            | Ja                                                                                                            |

```xml
<number>1.6</number>
```

## Teksttype

Hoe het voornaamste deel van de tekst van deze drager is weergegeven: gedrukt, getypt of handgeschreven.

| **XML element**            | `<text_type />`                                                                   |
| **Datatype**               | Gecontroleerde lijst                                                      |
| **Verplichting**           | Verplicht                                                                                            |
| **Herhaalbaar**            | Ja                                                                                                            |

```xml
<text_type>Printed</text_type>
<text_type>Typed</text_type>
<text_type>Handwritten</text_type>
```

### Mogelijke waarden

- `Handwritten`
- `Typed`
- `Printed`
	

## Aantal pagina’s

Het aantal pagina's waaruit de drager bestaat.

| **XML element**            | `<number_of_pages/>`                                                                   |
| **Datatype**               | Numeriek                                                      |
| **Verplichting**           | Verplicht                                                                                            |
| **Herhaalbaar**            | Ja                                                                                                            |

```xml
<number_of_pages>2</number_of_pages>
```

## Afmetingen van papier 

De omvang van het papier volgens hoogte x breedte (in cm).

| **XML element**            | `<dimensions/>`                                                                   |
| **Datatype**               | hoogte x breedte                                                       |
| **Verplichting**           | Verplicht                                                                                            |
| **Herhaalbaar**            | Ja                                                                                                            |

```xml
<dimensions>46 x 30</dimensions>
```	

## Dragereenheid

De dragereenheid toont aan hoe de drager bijeen wordt gehouden.

| **XML element**            | `<carrier_unity/>`                                                                   |
| **Datatype**               | Gecontroleerde lijst |
| **Verplichting**           | Verplicht                                                                                            |
| **Herhaalbaar**            | Ja                                                                                                            |

```xml
<carrier_unity>Bound - 180° opening</carrier_unity>
```

### Mogelijke waarden

- `Bound - 180° opening`
- `Bound - not 180° opening` 
- `Stapled`
- `Loose`


## Staat van band en bindingen

Evaluatie in welke staat de band zich bevindt. 

| **XML element**            | `<cover_and_bindings/>`                                                                   |
| **Datatype**               | Gecontroleerde lijst |
| **Verplichting**           | Verplicht indien van toepassing (VA) is enkel van toepassing indien de dragereenheid Gebonden - 180° of Gebonden - niet 180° te openen is.                                                                                             |
| **Herhaalbaar**            | Ja                                                                                                            |

```xml
<cover_and_bindings>Poor</cover_and_bindings>
<cover_and_bindings>Bad</cover_and_bindings>
<cover_and_bindings>Reasonable</cover_and_bindings>
<cover_and_bindings>Good</cover_and_bindings>
```

### Mogelijke waarden

- `Poor`
- `Bad`
- `Reasonable`
- `Good`

## Staat van papier

Evaluatie in welke staat het papier zich bevindt. 

| **XML element**            | `<paper/>`                                                                   |
| **Datatype**               | Gecontroleerde lijst |
| **Verplichting**           | Verplicht indien van toepassing (VA) is enkel van toepassing indien de dragereenheid Gebonden - 180° of Gebonden - niet 180° te openen is.                                                                                             |
| **Herhaalbaar**            | Ja                                                                                                            |

### Mogelijke waarden

- `Poor`
- `Bad`
- `Reasonable`
- `Good`

```xml
<paper>Good</paper>
<paper>Reasonable</paper>
<paper>Poor</paper>
<paper>Bad</paper>
```

## Tekstkwaliteit voor OCR

Verschijnselen die een uitdaging kunnen vormen voor een geautomatiseerde optische tekstherkenning.

| **XML element**            | `<text_quality_for_ocr><multiselect/></text_quality_for_ocr>`                                                                   |
| **Datatype**               | Gecontroleerde lijst |
| **Verplichting**           | Verplicht                                                                                             |
| **Herhaalbaar**            | Ja                                                                                                            |
	
```xml
<text_quality_for_ocr>
  <multiselect>Creases</multiselect>
  <multiselect>Folds</multiselect>
  <multiselect>Imprints</multiselect>
  <multiselect>Repairs</multiselect>
  <multiselect>Stains</multiselect>
  <multiselect>Tears</multiselect>
  <multiselect>Text Loss</multiselect>
</text_quality_for_ocr>
```

### Mogelijke waarden

- `No problems`
- `Imprints`
- `Folds`
- `Faded ink`
- `Creases`
- `Text loss`
- `Repairs`
- `Tears`
- `Stains`
- `Vertically printed text`


## Aantal folio’s

Het aantal folio’s van een handschrift of manuscript. Eén folio zijn twee opeenvolgende pagina’s. De rectozijde is de voorkant, de versozijde de achterkant.

| **XML element**        | `<number_of_folios/>`                                                                                                     |
| **Datatype**           | Numeriek                                                                                                            |
| **Verplichting**       | Optioneel     |
| **Herhaalbaar**        | Nee                                                                                                                |

```xml
<number_of_folios>174</number_of_folios>
```

## Materiaal

Het materiaal waaruit het object bestaat.

| **XML element**        | `<materials><material /></materials>`                                                                                                     |
| **Datatype**           | Vrije tekst                                                                                                            |
| **Verplichting**       | Optioneel     |
| **Herhaalbaar**        | Ja                                                                                                                |

```xml
<materials type="list">
	<material>papier</material>
	<material>perkament</material>
</materials>
```

## Herkomst object

Neerslag van de herkomst van dit exemplaar van het object in kwestie, of de opeenvolging van eigenaars of beheerders, die verantwoordelijk zijn voor het creëeren, ontvangen of accumuleren van het object.

| **XML element**        | `<dc_provenances><dc_provenance /></dc_provenances>`                                                                                                     |
| **Datatype**           | Vrije tekst                                                                                                            |
| **Verplichting**       | Optioneel     |
| **Herhaalbaar**        | Ja                                                                                                                |

```xml
<dc_provenances type="list">
  <dc_provenance>Abdij van Averbode</object_provenance>
  <dc_provenance>Archief Grootseminarie Ten Duinen</object_provenance>
</dc_provenances>
```

## Afmetingen - hoogte, breedte, dikte

De afmetingen van het object in mm, volgens hoogte x breedte x (indien driedimensionaal) dikte.

| **XML element**        | `<dimensions type="list"></height_in_mm></dimensions>`                                                                                                    |
| **Datatype**           | Numeriek                                                                                                            |
| **Verplichting**       | Optioneel     |
| **Herhaalbaar**        | Nee                                                                                                                |

| **XML element**        | `<dimensions type="list"></width_in_mm></dimensions>`                                                                                                    |
| **Datatype**           | Numeriek                                                                                                            |
| **Verplichting**       | Optioneel     |
| **Herhaalbaar**        | Nee                                                                                                                |

| **XML element**        | `<dimensions type="list"></depth_in_mm></dimensions>`                                                                                                    |
| **Datatype**           | Numeriek                                                                                                            |
| **Verplichting**       | Optioneel     |
| **Herhaalbaar**        | Nee                                                                                                                |

```xml
<dimensions type="list">
	<height_in_mm>310</height_in_mm>
	<width_in_mm>210</width_in_mm>
	<depth_in_mm>35</depth_in_mm>
</dimensions>
```


# Logistieke informatie

## Registratiedatum drager

De datum waarop de drager in de registratietool werd geregistreerd.


| **XML element**        | `<created_on/>`                                                                                                   |
| **Datatype**           | [ISO 8601](https://nl.wikipedia.org/wiki/ISO_8601) Datum en tijd (`YYYY-MM-DDThh:mm:ss`)                          |
| **Verplichting**       | Verplicht indien gekend |
| **Herhaalbaar**        | Nee                                                                                                               |

```xml
<created_on>2014-11-27T14:11:11</created_on>
```

## Barcode verzameldoos

De barcode van meemoo die werd bevestigd op de verzameldoos waarin de drager zich bevindt.


| **XML element**        | `<collection_box_barcode/>`                                                                                       |
| **Datatype**           | ID                                                                                                                |
| **Verplichting**       | Verplicht indien gekend |
| **Herhaalbaar**        | Nee                                                                                                               |

```xml
<collection_box_barcode>BBMX_AMS_000007</collection_box_barcode>
```

## Barcode transportbak

De barcode van meemoo die werd bevestigd op de transportbak waarin de verzameldozen zich bevinden.


| **XML element**        | `<transport_box_barcode/>`                                                                                       |
| **Datatype**           | ID                                                                                                                |
| **Verplichting**       | Verplicht indien gekend |
| **Herhaalbaar**        | Nee                                                                                                               |

```xml
<transport_box_barcode>VIAA-AKF-0022</transport_box_barcode>
```

## Status

Status van de shipment om het logistieke proces te monitoren.


| **XML element**        | `<status/>` |
| **Datatype**           | Gecontroleerde lijst |
| **Verplichting**       | Optioneel |
| **Herhaalbaar**        | Nee |

```xml
<status>Pending</status>
```

### Mogelijke waarden

- `Pending`
- `Ready for shipment at CP`
- `Checked out at CP`
- `Checked in at SP`
- `Checked in at VIAA`
- `Checked out at VIAA`
- `Checked out at SP`
- `Checked in at CP`

## Shipment ID

De ID van de verzending waarin de drager van de contentpartner naar de Service Provider werd verstuurd. Deze is vooral van belang voor de Service Provider en meemoo.


| **XML element**        | `<shipment_id/>`                                                                                                  |
| **Datatype**           | ID                                                                                                                |
| **Verplichting**       | Verplicht indien gekend |
| **Herhaalbaar**        | Nee                                                                                                               |

```xml
<shipment_id>14314364782</shipment_id>
```

# Quality Control (QC)

## Resultaat manuele QC

Na het uitvoeren van de manuele kwaliteitscontrole wordt de contentpartner gevraagd de kwaliteit van het digitale bestand te beoordelen. Dit kan door aan te geven of de kwaliteit 'ok' is of 'not ok'. Hierbij kan de dropdownlijst onder het veld 'Resultaat manuele kwaliteitscontrole' geraadpleegd worden. De waarden in de lijst 'audio' en 'video' geven aan wat er visueel en auditief gedetecteerd kan worden. Deze lijsten zullen verder uitgebreid worden. Indien er vragen of feedback zijn, kan dit steeds gemeld worden via [support@meemoo.be](mailto:support@meemoo.be)].


| **XML element**        | `<QCoutcome/>`                                                                                                                                       |
| **Datatype**           | "OK" / "NOT OK"                                                                                                                                      |
| **Verplichting**       | Optioneel (enkel van toepassing op de statistische selectie van een volledige batch, meemoo adviseert om een statistische selectie van 10% te maken) |
| **Herhaalbaar**        | Neen                                                                                                                                                 |

## QC Audio

Indien de kwaliteit van de audio in het digitaal object niet ok is dan kan in deze dropdownlijst een waarde geselcteerd worden die aangeeft wat de reden is voor het afkeuren van de kwaliteit. Indien de oorzaak niet in de dropdownlijst aanwezig is kan het opmerkingenveld gebruikt worden.


| **XML element**        | `<QCaudio/>`                                                                                                                                       |
| **Datatype**           | "OK" / "NOT OK"                                                                                                                                    |
| **Verplichting**       | Optioneel (enkel van toepassing op de statistische selectie van een volledige batch, meemoo adviseert om een statistische selectie van 10% te maken) |
| **Herhaalbaar**        | Neen                                                                                                                                               |

## QC Video

Indien de kwaliteit van de video in het digitaal object niet ok is dan kan in deze dropdownlijst een waarde geselcteerd worden die aangeeft wat de reden is voor het afkeuren van de kwaliteit. Indien de oorzaak niet in de dropdownlijst aanwezig is kan het opmerkingenveld gebruikt worden.


| **XML element**        | `<QCvideo/>`                                                                                                                                       |
| **Datatype**           | "OK" / "NOT OK"                                                                                                                                    |
| **Verplichting**       | Optioneel (enkel van toepassing op de statistische selectie van een volledige batch, meemoo adviseert om een statistische selectie van 10% te maken) |
| **Herhaalbaar**        | Neen                                                                                                                                               |

## QC Opmerkingen

Dit is een vrij tekstveld dat gebruikt kan worden om alle bijkomende opmerkingen rond de uitgevoerde kwaliteitscontrole te bewaren.


| **XML element**        | `<QCcomment/>`                                                                                                                                     |
| **Datatype**           | Vrij tekstveld                                                                                                                                     |
| **Verplichting**       | Optioneel (enkel van toepassing op de statistische selectie van een volledige batch, meemoo adviseert om een statistische selectie van 10% te maken) |
| **Herhaalbaar**        | Neen                    
