---
layout: default
title: "Velden: Digitaliseringsproces"
parent: VIAA Metadatamodel
nav_order: 3
---

{: .fw-300 }
Deze velden worden gebruikt door de digitaliseringspartners van meemoo in kader van het digitaliseringsproject.

{: .important }
Deze pagina dient louter ter documentatie van de relevante velden bij digitalisering. Onderstaande velden kunnen dus niet gebruikt worden bij bv. een digitaal instroomproces.

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Digitaliseringspartner

## Service Provider

De naam van de Service Provider aan wie de digitalisering van de originele drager werd uitbesteed.


| **XML element**        | `<sp_name/>`                                                                                                                                   |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<sp_name>Vectracom</sp_name>
```

## Service Provider ID

De unieke ID van de Service Provider aan wie de digitalisering van de originele drager werd uitbesteed.


| **XML element**        | `<sp_id/>`                                                                                                                                     |
| **Datatype**           | ID                                                                                                                                             |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<sp_id>OR-183420s</sp_id>
```

# Digitaliseringsproces

## Datum inspectie analoge drager

De datum waarop de materiële drager door de Service Provider visueel werd geïnspecteerd.


| **XML element**        | `<inspection_date/>`                                                                                                                           |
| **Datatype**           | [ISO 8601](https://nl.wikipedia.org/wiki/ISO_8601) Datum (`YYYY-MM-DD`)                                                                                                                                         |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<inspection_date>2015-04-21</inspection_date>
```

## Uitkomst inspectie analoge drager

De uitkomst van de visuele inspectie van de drager door de Service Provider. Met andere woorden is deze geslaagd (y) of niet geslaagd (n).

| **XML element**        | `<inspection_outcome/>`                                                                                                                       |
| **Datatype**           | y/n                                                                                                                                            |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<inspection_outcome>y</inspection_outcome>
```

## Opmerking inspectie analoge drager

Eventuele opmerkingen van de Service Provider naar aanleiding van de visuele inspectie van de analoge drager (denk aan schade, ontbrekende elementen).

| **XML element**        | `<inspection_note/>`                                                                                                                          |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<inspection_note >Beschadiging cassette</inspection_note>
```

## Datum herstel analoge dragger

De datum waarop de Service Provider herstellende ingrepen op de drager heeft toegepast.

| **XML element**        | `<repair_date/>`                                                                                                                               |
| **Datatype**           | [ISO 8601](https://nl.wikipedia.org/wiki/ISO_8601) Datum (`YYYY-MM-DD`)                                                                        |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<repair_date>2015-10-03`</repair_date>
```

## Uitkomst herstel analoge drager

De uitkomst van de door de Service Provider ondernomen herstelacties. Met andere woorden is deze geslaagd (y) of niet geslaagd (n).


| **XML element**        | `<repair_outcome/>`                                                                                                                            |
| **Datatype**           | y/n                                                                                                                                            |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<repair_outcome>y</repair_outcome>
```

## Opmerking herstel analoge drager

Bijkomende opmerkingen met betrekking tot de herstelactie.

| **XML element**        | `<repair_note/>`                                                                                                                               |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

## Datum reiniging analoge drager

De datum waarop de materiële drager werd gereinigd.

| **XML element**        | `<cleaning_date/>`                                                                                                                             |
| **Datatype**           | [ISO 8601](https://nl.wikipedia.org/wiki/ISO_8601) Datum (`YYYY-MM-DD`)                                                                        |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

## Uitkomst reiniging analoge drager

De uitkomst van de reinigingsactie van de materiële drager. Met andere woorden is deze geslaagd (y) of niet geslaagd (n).

| **XML element**        | `<cleaning_outcome/>`                                                                                                                          |
| **Datatype**           | y/n                                                                                                                                            |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<cleaning_outcome>y</cleaning_outcome>
```

## Opmerking reiniging analoge drager

Eventuele opmerking m.b.t. de reiniging van de materiële drager.

| **XML element**        | `<cleaning_note/>`                                                                                                                             |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

## Datum bakken analoge drager

De datum waarop de analoge drager werd gebakken.

| **XML element**        | `<baking_date/>`                                                                                                                               |
| **Datatype**           | [ISO 8601](https://nl.wikipedia.org/wiki/ISO_8601) Datum (`YYYY-MM-DD`)                                                                        |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

## Uitkomst bakken analoge drager

De uitkomst van het bakproces van de analoge drager. Met andere woorden is deze geslaagd (y) of niet geslaagd (n).

| **XML element**        | `<baking_outcome/>`                                                                                                                            |
| **Datatype**           | y/n                                                                                                                                            |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<baking_outcome>y</baking_outcome>
```

## Digitaliseringsdatum

De datum waarop de digitalisering van de analoge drager plaatsvond.

| **XML element**        | `<digitization_date/>`                                                                                                                         |
| **Datatype**           | [ISO 8601](https://nl.wikipedia.org/wiki/ISO_8601) Datum (`YYYY-MM-DD`)                                                                         |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<digitization_date>2015-10-03</digitization_date>
```

## Tijdstip digitalisering

Het tijdstip waarop de digitalisering van de analoge drager plaatsvond.

| **XML element**        | `<digitization_time/>`                                                                                                                        |
| **Datatype**           | [ISO 8601](https://nl.wikipedia.org/wiki/ISO_8601) Tijd (`hh:mm:ss`)                                                                             |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

## Uitkomst digitalisering

De uitkomst van de digitalisering. Met andere woorden is deze geslaagd (y) of niet geslaagd (n).

| **XML element**        | `<digitization_outcome/>`                                                                                                                      |
| **Datatype**           | y/n                                                                                                                                            |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<digitization_outcome>y</digitization_outcome>
```

## Opmerking digitalisering

Een eventuele opmerking bij de digitalisering van een analoge drager.

| **XML element**        | `<digitization_note/>`                                                                                                                         |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

## Datum kwaliteitscontrole SP

De datum waarop door de Service Provider een kwaliteitscontrole van het digitale item is uitgevoerd.


| **XML element**        | `<qc_date/>`                                                                                                                                   |
| **Datatype**           | [ISO 8601](https://nl.wikipedia.org/wiki/ISO_8601) Datum (`YYYY-MM-DD`)                                                                          |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

## Uitkomst kwaliteitscontrole SP

De uitkomst van de kwaliteitscontrole door de Service Provider. Is deze positief (y) of negatief (n)?


| **XML element**        | `<qc_outcome/>`                                                                                                                                |
| **Datatype**           | "y" / "n"                                                                                                                                      |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<qc_outcome>y</qc_outcome>
```

## Opmerking kwaliteitscontrole SP

Een eventuele opmerking bij de kwaliteitscontrole door de Service Provider.


| **XML element**        | `<qc_note/>`                                                                  |
| **Datatype**           | Vrije tekst                                                                   |
| **Verplichting**       | Optioneel                                                                     |
| **Herhaalbaar**        | Nee                                                                           |

## Agent kwaliteitscontrole SP

Dit is een verwijzing naar de persoon bij de Service Provider die de kwaliteitscontrole heeft uitgevoerd.


| **XML element**        | `<qc_by/>`                                                                                                                                     |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<qc_by>User001</qc_by>
```

## Datum transfer naar LTO tape

De datum waarop het digitale item bij de Service Provider naar LTO tape werd geschreven.


| **XML element**        | `<transfer_lto_date/>`                                                                                                                         |
| **Datatype**           | [ISO 8601](https://nl.wikipedia.org/wiki/ISO_8601) Datum (`YYYY-MM-DD`)                                                                          |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<transfer_lto_date>2015-10-03</transfer_lto_date>
```

## LTO ID

De unieke ID van de LTO tape waarop het digitale item wordt aangeleverd door de Service Provider.


| **XML element**        | `<lto_id/>`                                                                                                                                    |
| **Datatype**           | ID                                                                                                                                             |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<lto_id>IM0180L5</lto_id>
```

## OTC start

Het startpunt van de tijdscodering zoals die op de originele drager wordt bijgehouden.


| **XML element**        | `<OTC_start/>`                                                                                                     |
| **Datatype**           | Tijdscode (`uu:mm:ss:SS`)                                                                                          |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de registratieinformatie in de [registratietool](http://registratie.meemoo.be). |
| **Herhaalbaar**        | Nee                                                                                                                |

```xml
<OTC_start>01:00:00:00</OTC_start>
```

## Duur

De gekende of geschatte duur van de inhoud van de originele drager.


| **XML element**        | `<file_duration/>`                                                                                                 |
| **Datatype**           | Duur (`uu:mm:ss.SS`)                                                                                               |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de registratieinformatie in de [registratietool](http://registratie.meemoo.be). |
| **Herhaalbaar**        | Nee                                                                                                                |

```xml
<file_duration>00:30:14.10</file_duration>
```

## Recording speed

De opnamesnelheid van de drager. Dit is hoofdzakelijk van toepassing voor openspoelaudiotapes.


| **XML element**        | `<audio_carrier_speed/>`                                                                                          |
| **Datatype**           | `x.xx cm/s`                                                                                                         |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de registratieinformatie in de [registratietool](http://registratie.meemoo.be). |
| **Herhaalbaar**        | Nee                                                                                                               |

```xml
<audio_carrier_speed>4.75 cm/s</audio_carrier_speed>
```

## Audio noise reduction

De bij audiocassettes gebruikte technologie van ruisonderdrukking.


| **XML element**        | `<audio_noise_reduction/>`                                                                                        |
| **Datatype**           | Vrije tekst                                                                                                       |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de registratieinformatie in de [registratietool](http://registratie.meemoo.be). |
| **Herhaalbaar**        | Nee                                                                                                               |

```xml
<audio_noise_reduction>Dolby A</audio_noise_reduction>
```

## Audio IEC type

Het type magnetische coating gebruikt voor de tape van een audiocassette.


| **XML element**        | `<audio_iec_type/>`                                                                                                                                                   |
| **Datatype**           | I-IV (IEC 60094) (zie ook onze pagina over [drager registratie in de registratietool](https://portaal.meemoo.be/nl/portaal/support-category/item/hoe-registreer-ik-een-nieuwe-drager-in-ams)) |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de registratieinformatie in de [registratietool](http://registratie.meemoo.be).                                                    |
| **Herhaalbaar**        | Nee                                                                                                                                                                   |

```xml
<audio_iec_type>II</audio_iec_type>
```

## Audio tracks

Het aantal geluidssporen dat op de drager werd vastgelegd.


| **XML element**        | `<audio_tracks/>`                                                                                                  |
| **Datatype**           | Integer                                                                                                            |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de registratieinformatie in de [registratietool](http://registratie.meemoo.be). |
| **Herhaalbaar**        | Nee                                                                                                                |

```xml
<audio_tracks>2</audio_tracks>
```

## PID

{: #pid}

De *Persistent Identifier*. Een door meemoo toegekende unieke naam.

Elk digitaal object in het meemoo archief heeft een unieke PID.

| **XML element**        | `<PID>`                                                             |
| **Datatype**           | PID                                                                 |
| **Verplichting**       | Verplicht (automatisch)                                             |
| **Herhaalbaar**        | Nee                                                                 |

```xml
<PID>294805325</PID>
```

# Digitaliseringsketen

## Digitaliseringsformaat

Het formaat waarin de archiefmaster van het digitale item werd geproduceerd door de Service Provider.


| **XML element**        | `<digitization_format/>`                                                                                                                       |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<digitization_format>WAV</digitization_format>
```

## Player fabrikant

De fabrikant van de tijdens het digitaliseringsproces gebruikte afspeelapparatuur.


| **XML element**        | `<player_manufacturer/>`                                                                                                                       |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<player_manufacturer>Sony</player_manufacturer>
```

## Player serienummer

Het serienummer van de tijdens het digitaliseringsproces gebruikte afspeelapparatuur.


| **XML element**        | `<player_serial_number/>`                                                                                                                      |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<player_serial_number>33418</player_serial_number>
```

## Player model

Het model van de tijdens het digitalliseringsproces gebruikte afspeelapparatuur.


| **XML element**        | `<player_model/>`                                                                                                                              |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<player_model>BVH-2000PS</player_model>
```

## Timebase corrector fabrikant

Naam van de fabrikant van de timebase corrector (TBC). Dit is een toestel dat storingen en vervormingen van het beeldsignaal op een videotape buffert en corrigeert.

| **XML element**        | `<timebase_corrector_manufacturer/>`                                                                                                           |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<timebase_corrector_manufacturer>Leitch</timebase_corrector_manufacturer>
```

## Timebase corrector serienummer

Het serienummer van de timebase corrector (TBC) gebruikt om storingen in het beeldsignaal van een videotape te corrigeren.


| **XML element**        | `<timebase_corrector_serial_number/>`                                                                                                          |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<timebase_corrector_serial_number>LTHI0123706032\#9315</timebase_corrector_serial_number>
```

## Timebase corrector model

Het model van de timebase corrector (TBC) gebruikt om storingen in het beeldsignaal van een videotape te corrigeren. 


| **XML element**        | `<timebase_corrector_model/>`                                                                                                                  |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<timebase_corrector_model>DPS-575</timebase_corrector_model>
```

## AD fabrikant

Naam van de fabrikant van de analoog-digitaalomzetter. De AD-omzetter zet een analoog signaal om in een digitaal.


| **XML element**        | `<AD_manufacturer/>`                                                                                                                           |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<AD_manufacturer>Realtek</AD_manufacturer>
```

## AD serienummer

Het serienummer van de AD-omzetter.


| **XML element**        | `<AD_serial_number/>`                                                                                                                          |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<AD_serial_number>1</AD_serial_number>
```

## AD model

Het model van de AD-omzetter.


| **XML element**        | `<AD_model/>`                                                                                                                                  |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<AD_model>Alc887</AD_model>
```

## Encoder fabrikant

De fabrikant van de tijdens het digitaliseringproces gebruikte encoder. Dit zijn de hardware of software die gebruikt worden voor het transcoderen van informatie van het ene formaat (of code) naar de andere.


| **XML element**        | `<encoder_manufacturer/>`                                                                                                                      |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<encoder_manufacturer>EVS</encoder_manufacturer>
```

## Encoder serienummer

Het serienummer van de tijdens het digitaliseringproces gebruikte encoder.


| **XML element**        | `<encoder_serial_number/>`                                                                                                                     |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<encoder_serial_number>41130319</encoder_serial_number>
```

## Encoder model

Het specifieke model van de tijdens het digitaliseringproces gebruikte encoder.

| **XML element**        | `<encoder_model/>`                                                                                                                             |
| **Datatype**           | Vrije tekst                                                                                                                                    |
| **Verplichting**       | Deze informatie wordt automatisch overgenomen uit de digitaliseringsmetadata die door de Service Provider wordt aangeleverd na digitalisering. |
| **Herhaalbaar**        | Nee                                                                                                                                            |

```xml
<encoder_model>Open Cube</encoder_model>
```
