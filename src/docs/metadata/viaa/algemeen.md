---
layout: default
title:  "Velden: Algemeen"
parent: VIAA Metadatamodel
nav_order: 1
---

{: .fw-300 }
Deze velden zijn van toepassing op gedigitaliseerd als *digital born* materiaal.

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


# Administratieve en beschrijvende metadata

## CP Naam

De naam van de Content Partner (CP).

| **XML element**        | `<CP>`                                 |
| **Datatype**           | Vrije tekst                            |
| **Verplichting**       | Verplicht                              |
| **Herhaalbaar**        | Nee                                    |

```xml
<CP>MHKA</CP>
```

## CP ID

De unieke identifier van de Content Partner.

| **XML element**        | `<CP_id>`                                      |
| **Datatype**           | ID                                             |
| **Verplichting**       | Verplicht                                      |
| **Herhaalbaar**        | Nee                                            |

```xml
<CP_id>OR-1245</CP_id>
```

## Sub CP naam

{: .important }
Dit veld is verouderd en wordt niet langer gebruikt.

De naam van de sub CP die gekoppeld is aan de hoofd CP (enkel van toepassing indien uw organisatie onderverdeeld is in suborganisaties).

| **XML element**        | `<Sub_CP>`                           |
| **Datatype**           | Vrije tekst                          |
| **Verplichting**       | Verplicht indien van toepassing (VA) |
| **Herhaalbaar**        | Nee                                  |

```xml
<Sub_CP>Faculteit Letterkunde</Sub_CP>
```

## Hoofd lokale CP ID

{: #dc_identifier_localid}

De hoofd ID van de oorspronkelijke drager of het *born digital* item. Dit is de registratiecode die het meest courant wordt gebruikt door de CP binnen ***het eigen*** archief- of collectiemanagementsysteem.

Dit is de unieke ID van de content partner die de linkt vormt naar het eigen collectiebeheerssysteem. Dit kan later gebruikt worden om metadata te koppelen in het meemoo archiefsysteem. Voor digitalisering door meemoo is deze ID al in Mediahaven aanwezig, indien deze mee wordt gegeven in de [registratietool](http://registratie.meemoo.be) `<original_carrier_id/>`.

Het kan gebeuren dat voor sommige objecten de CP geen relevante ID of registratienummer bijhoudt (ook al raadt meemoo aan om vóór registratie in de [registratietool](http://registratie.meemoo.be) dit alsnog toe te kennen). In dat geval blijft dit veld leeg.

| **XML element**            | `<dc_identifier_localid>`                                                                        |
| **Data type**              | ID                                                                                               |
| **Verplichting**           | Verplicht indien van toepassing (VA)                                                             |
| **Herhaalbaar**            | Nee                                                                                              |

```xml
<dc_identifier_localid>audiocassette 365</dc_identifier_localid>
```

## Overige lokale CP ID

{: #dc_identifier_localids}

Eventuele alternatieve ID's van de oorspronkelijke drager of het *born digital* item, gebruikt door de CP binnen het eigen archief- of collectiebeheerssysteem.

| **XML element**            | `<dc_identifier_localids type="list"><ARDOME/><priref/>...</dc_identifier_localids>`             |
| **Data type**              | Vrije tekst                                                             |
| **Verplichting**           | Optioneel                                                                                        |
| **Herhaalbaar**            | Ja                                                                                               |


**Voorbeeld VRT:**

```xml
<dc_identifier_localids type="list">
    <ARDOME>ABC135</ARDOME>
</dc_identifier_localids>
```

**Voorbeeld AMSAB**:

```xml
<dc_identifier_localids type="list">
    <reproduction.reference>audiocassette_420</reproduction.reference>
    <acquisition.number>S/2005/051</acquisition.number>
    <alternative_number>MG/05/051-102/1</alternative_number>
</dc_identifier_localids>
```

### Mogelijke sleutels

{: .no_toc }

| `<Acquisition_number />`       | |
| `<Alternative_number />`       | |
| `<Analoge_drager />`           | |
| `<Api />`                      | |
| `<Ardome />`                   | |
| `<Basis />`                    | |
| `<Bestandsnaam />`             | De orignele bestandsnaam van het item. |
| `<DataPID />`                  | |
| `<Historical_carrier />`       | |
| `<Historical_record_number />` | |
| `<Inventarisnummer />`         | Unieke identifier bij bv. musea die gelinkt is aan een fysiek object uit de collectie.|
| `<MEDIA_ID />`                 | |
| `<Object_number />`            | Het Axiell Adlib object number.  |
| `<Pdf />`                      | |
| `<PersistenteURI_Record />`    | Persistente URI die verwijst naar de lokale record bij de contentpartner. |
| `<PersistenteURI_VKC_Record />`    | Persistente URI die verwijst naar de lokale record bij de Vlaamse Kunstencollectie. |
| `<PersistenteURI_VKC_Werk />`      | Persistente URI die verwijst naar het werk dat wordt afgebeeld bij de Vlaamse Kunstencollectie. |
| `<PersistenteURI_Werk />`      | Persistente URI die verwijst naar het werk dat wordt afgebeeld. |
| `<Priref />`                   | |
| `<Vaf_ID />`                   | Unieke identifier binnen het VAF (Vlaams Audiovisueel Fonds). |
| `<Topstuk_ID />`               | Het topstuk ID, toegekend door het Departement Cultuur, Jeugd en Media, tijdens de erkenning van het topstuk. |
| `<Word_ID />`                  | |
| `<WorkPID />`                  | |

## Batch ID

De ID van de batch waarin de drager van de contentpartner naar de Service Provider of meemoo werd verstuurd. 

| **XML element**        | `<batch_id/>`                                                                                                     |
| **Datatype**           | ID                                                                                                                |
| **Verplichting**       | Verplicht indien gekend |
| **Herhaalbaar**        | Nee                                                                                                               |

```xml
<batch_id>BMXMJPGB01</batch_id>
```

## Batch Naam

De naam van de batch waarin de drager van de contentpartner naar de Service Provider of meemoo werd verstuurd. 

| **XML element**        | `<batch_name/>`                                                                                                     |
| **Datatype**           | Vrije tekst                                                                                                               |
| **Verplichting**       | Optioneel |
| **Herhaalbaar**        | Nee                                                                                                               |

```xml
<batch_name>GPLB06</batch_name>
```


# Relaties 

De relatiemetadatavelden in het meemoo datamodel worden gebruikt om de formele relaties aan te duiden tussen verschillende digitale objecten. De definitie van deze relaties beperkt zich tot 4 verschillende types (_is deel van_, _bevat_, _is verwant aan_ en _is versie van_).

## (Dit digitaal object) is deel van

\"Is_deel_van\" geeft aan van welk digitale object (parent file) het beschreven bestand deel uitmaakt.


| **XML element**        | `<dc_relations type="list"><is_deel_van/></dc_relations>`                                                |
| **Datatype**           | [PID](#pid) of [dc_identifier_localid](#dc_identifier_localid) in de vorm `dc_identifier_localid:<id>`                                                                              |
| **Verplichting**       | Automatisch ingevuld door meemoo mapping (born digital)                                                    |
| **Herhaalbaar**        | Ja                                                                                                       |

## (Dit digitaal object) bevat

\"bevat\" geeft aan welke digitale objecten deel uit maken van het beschreven bestand.


| **XML element**        | `<dc_relations type="list"><bevat/></dc_relations>`                                    |
| **Datatype**           | [PID](#pid) of [dc_identifier_localid](#dc_identifier_localid) in de vorm `dc_identifier_localid:<id>`                                                                                 |
| **Verplichting**       | Automatisch ingevuld door meemoo mapping (born digital)                                  |
| **Herhaalbaar**        | Ja                                                                                     |

## (Dit digitaal object) is verwant aan

In dit veld worden verwante digitale objecten (PIDs) aangegeven.


| **XML element**        | `<dc_relations type="list"><is_verwant_aan/></dc_relations>`       |
| **Datatype**           | [PID](#pid) of [dc_identifier_localid](#dc_identifier_localid) in de vorm `dc_identifier_localid:<id>`                                                               |
| **Verplichting**       | Automatisch ingevuld door meemoo mapping (born digital)              |
| **Herhaalbaar**        | Ja                                                                 |

## (Dit digitaal object) is versie van

In dit veld worden versies van digitale objecten (PIDs) aangegeven. (vb. Dubbele kopieën)


| **XML element**        | `<dc_relations type="list"><is_versie_van/></dc_relations>`                                 |
| **Datatype**           | [PID](#pid) of [dc_identifier_localid](#dc_identifier_localid) in de vorm `dc_identifier_localid:<id>`                                                                                         |
| **Verplichting**       | Automatisch ingevuld door meemoo mapping (born digital)                                       |
| **Herhaalbaar**        | Ja                                                                                          |

# Titels

## Hoofdtitel

De algemene benaming of hoofdtitel.

_Voor andere versies (lange titels, vertalingen) kan het veld 'Alternatieve Titel' worden gebruikt._

| **XML element**            | `<dc_title/>`                                                                                           |
| **Datatype**               | Vrije tekst                                                                                          |
| **Verplichting**           | Verplicht                                                                                            |
| **Herhaalbaar**            | Nee                                                                                                  |

```xml
<dc_title>nieuws 19-09-94</dc_title>
```

## Secundaire titel: Serie

De serietitel. Dit is de titel van de serie waar het item deel van uitmaakt.

| **XML element**        | `<dc_titles type="list"><serie/></dc_titles>`                                  |
| **Datatype**           | Vrije tekst                                                                    |
| **Verplichting**       | Optioneel                                                                      |
| **Herhaalbaar**        | Ja                                                                             |

 ```xml
 <dc_titles type="list">
    <serie>Het Journaal</serie>
</dc_titles>
 ```

## Secundaire titel: Episode

De titel van de episode waar het item deel van uitmaakt.


| **XML element**        | `<dc_titles type="list"><episode/></dc_titles>`            |
| **Datatype**           | Vrije tekst                                                |
| **Verplichting**       | Optioneel                                                  |
| **Herhaalbaar**        | Ja                                                         |

```xml
<dc_titles type="list">
    <epsiode>Het Journaal</episode>
</dc_titles>
```

## Secundaire titel: Aflevering

Dit is de titel van de aflevering waar het item deel van uitmaakt.

| **XML element**        | `<dc_titles type="list"><aflevering/></dc_titles>`                   |
| **Datatype**           | Vrije tekst                                                          |
| **Verplichting**       | Optioneel                                                            |
| **Herhaalbaar**        | Ja                                                                   |

## Secundaire titel: Alternatief

De alternatieve titel. Dit is een alternatieve titel voor het digitale object. Een alternatieve titel kan bijvoorbeeld een vertaling van de originele (hoofd)titel zijn.


| **XML element**        | `<dc_titles type="list"><alternatief/></dc_titles>`         |
| **Datatype**           | Vrije tekst                                                 |
| **Verplichting**       | Optioneel                                                   |
| **Herhaalbaar**        | Ja                                                          |

## Secundaire titel: Programma

De programmatitel. Dit is de titel van het programma waarvan het item deel uitmaakt. Hiermee wordt een specifieke aflevering of episode van een serie bedoeld.

| **XML element**        | `<dc_titles type="list"><programma/></dc_titles>` |
| **Datatype**           | Vrije tekst                                       |
| **Verplichting**       | Optioneel                                         |
| **Herhaalbaar**        | Ja                                                |

## Secundaire titel: Serienummer

Het nummer van de serie waarvan het item deel uitmaakt.


| **XML element**        | `<dc_titles type="list"><serienummer/></dc_titles>`       |
| **Datatype**           | Vrije tekst                                               |
| **Verplichting**       | Optioneel                                                 |
| **Herhaalbaar**        | Ja                                                        |

## Secundaire titel: Seizoen

Het seizoen/jaargang van de serie waarvan het item deel uitmaakt.


| **XML element**        | `<dc_titles type="list"><seizoen></dc_titles>`                      |
| **Datatype**           | Vrije tekst                                                         |
| **Verplichting**       | Optioneel                                                           |
| **Herhaalbaar**        | Ja                                                                  |

## Secundaire titel: Seizoennummer

Het nummer van het seizoen waarvan het item deel uitmaakt.


| **XML element**        | `<dc_titles type="list"><seizoennummer></dc_titles>`         |
| **Datatype**           | Vrije tekst                                                  |
| **Verplichting**       | Optioneel                                                    |
| **Herhaalbaar**        | Ja                                                           |

## Secundaire titel: Archief

Het hoogste beschrijvingsniveau: het archief waar het object deel van uitmaakt.


| **XML element**        | `<dc_titles type="list"><archief/></dc_titles>`                                   |
| **Datatype**           | Vrije tekst                                                                       |
| **Verplichting**       | Optioneel                                                                         |
| **Herhaalbaar**        | Ja                                                                                |

```xml
<dc_titles type="list">
<archief>Archief Gezinsbond`</archief>
</dc_titles>
```

## Secundaire titel: Deelarchief

Een deel van een archief dat bestaat uit een geheel van onderling gerelateerde archiefstukken.

| **XML element**        | `<dc_titles type="list"><deelarchief/></dc_titles>`                                             |
| **Datatype**           | Vrije tekst                                                                                     |
| **Verplichting**       | Optioneel                                                                                       |
| **Herhaalbaar**        | Ja                                                                                              |

```xml
<deelarchief>Groene Omroep (deelarchief Agalev)</deelarchief>
</dc_titles>
```

## Secundaire titel: Reeks

Documenten gerangschikt volgens een ordeningsplan of beheerd als een eenheid omdat ze het resultaat zijn van een zelfde proces van archiefvorming of opslag, of van eenzelfde activiteit, of omdat ze een bepaalde vorm hebben, of wegens enige andere samenhang die voortkomt uit creatie, ontvangst of gebruik.

| **XML element**        | `<dc_titles type="list"><reeks/></dc_titles>` |
| **Datatype**           | Vrije tekst                                   |
| **Verplichting**       | Optioneel                                     |
| **Herhaalbaar**        | Ja                                            |

```xml
<dc_titles type="list">
<reeks>Mondelinge Bronnen</reeks>
</dc_titles>
```

## Secundaire titel: Deelreeks

Een reeks, een onderdeel van een bovenliggende reeks zoals hierboven omschreven.

| **XML element**        | `<dc_titles type="list"><deelreeks/></dc_titles>`                                  |
| **Datatype**           | Vrije tekst                                                                        |
| **Verplichting**       | Optioneel                                                                          |
| **Herhaalbaar**        | Ja                                                                                 |

```xml
<dc_titles type="list">
    <deelreeks>Over bloemetjes en bijtjes: seksuele voorlichting in en rond het socialistisch milieu</deelreeks>
</dc_titles>
```

## Secundaire titel: Registratie

Dit is de registratie-titel zoals ingegeven in de [registratietool](http://registratie.meemoo.be).

_Bij het verrijken van de metadata kan het voorvallen dat de titel die tijdens de registratie werd ingegeven in dede [registratietool](http://registratie.meemoo.be) registratiesoftware opgeschoond dient te worden maar tegelijk ook interessante informatie bevat. Op dat moment kan de registratietitel bewaard worden onder de secundaire titel 'registratie' en kan de hoofdtitel vervangen worden door een opgeschoonde titel._

| **XML element**        | `<dc_titles type="list"><registratie/></dc_titles>` |
| **Datatype**           | Vrije tekst                                         |
| **Verplichting**       | Optioneel                                           |
| **Herhaalbaar**        | Ja                                                  |

```xml
<dc_titles type="list">
<registratie>landbouwbeleid: interview Willy De Clercq; mensenrechten: interview Karel De Gucht; LVZ: interview Louis Bril; sfeerbeelden</registratie>
</dc_titles>
```

# Datum

## Datum creatie

{: #dcterms_created}

De datum waarop de inhoud van het object werd gecreëerd.

_Bij de mapping naar het meemoo datamodel wordt de creatiedatum ook gemapt naar het veld `<date>`. Dit metadataveld verwacht een exacte datum om zo ook een facet toe te kunnen voegen in de zoekinterface. Bijkomend wordt hierdoor het item ook zichtbaar op de tijdslijn in de meemoo archiefwebsite._

_Indien onbekend wordt de datum van de creatie van de analoge drager (verplicht bij registratie in de [registratietool](http://registratie.meemoo.be)) gekozen, aangezien deze doorgaans met de datum van de creatie van de originele inhoud samenvalt of er toch dicht bij aansluit. Het is evenwel mogelijk dat de intellectuele inhoud ('content') vastgelegd op de drager een latere kopie is van een ouder origineel (bijvoorbeeld een kopie van een film op Umatic). In dit geval verschillen de datum van creatie van de datum van de originele drager._


| **XML element**            | `<dcterms_created/>`                                                                             |
| **Datatype**               | [Extended Date Time Format (EDTF)]({{ site.baseurl }}{% link docs/metadata/viaa/datatypes.md %}#edtf)                                                             |
| **Verplichting**           | Verplicht (indien 'datum uitgave' niet is ingevuld).                                             |
| **Herhaalbaar**            | Nee                                                                                              |


```xml
<dcterms_created>192u</dcterms_created>
```

## Datum uitgave / uitzending

{: #dcterms_issued}

De datum waarop het item is uitgegeven of uitgezonden.


| **XML element**            | `<dcterms_issued/>`                                                                             |
| **Datatype**               | [Extended Date Time Format (EDTF)]({{ site.baseurl }}{% link docs/metadata/viaa/datatypes.md %}#edtf)                                                                      |
| **Verplichting**           | Verplicht (indien 'datum creatie' niet is ingevuld).                                            |
| **Herhaalbaar**            | Nee                                                                                             |

```xml
<dcterms_issued>2016-01-27T13:00</dcterms_issued>
```

# Productie

## Maker

{: #dc_creators}

De persoon of instelling die (in hoofdzaak) verantwoordelijk is voor de creatie van de inhoud van het item.


| **XML element**            | `<dc_creators type="list"><Maker /><Regisseur /></Archiefvormer>...</dc_creators>` |
| **Datatype**               | Vrije tekst                                                                                     |
| **Verplichting**           | Verplicht indien gekend (VA)                                                                                                        |
| **Herhaalbaar**            | Ja                                                                                                                                  |

```xml
<dc_creators type="list">
    <Maker>Paul de Vree</Maker>
    <Archiefvormer>Jef van Hoof</Archiefvormer>
</dc_creators>
```

### Mogelijke sleutels

{: .no_toc }

Aan de hand van een gecontroleerde lijst kan de rol van de maker worden gespecificeerd. meemoo biedt een standaard lijst van rollen aan. Deze kan afhankelijk van de partner worden aangepast. Indien geen van de rollen van toepassing is, kan het generieke 'maker' worden gebruikt, ofwel kan in overleg met meemoo de gecontroleerde lijst worden uitgebreid.

| `<Maker />` | |
| `<Archiefvormer />` | |
| `<Architect>` | De architect van het afgebeelde gebouw. |
| `<Auteur />` | |
| `<Acteur />` | |
| `<Cineast />` | |
| `<Componist />` | |
| `<Choreograaf />` | |
| `<Danser />` | |
| `<Documentairemaker />` | |
| `<Fotograaf />` | |
| `<Geïnterviewde />` | |
| `<Interviewer />` | |
| `<Kunstenaar />` | |
| `<Muzikant />` | |
| `<Performer />` | |
| `<Producer />` | |
| `<Productiehuis />` | |
| `<Regisseur />` | |
| `<Schrijver />` | |
| `<Opdrachtgever />` | |

## Bijdrager

De persoon of instelling die een substantiële creatieve bijdrage tot de inhoud van het item heeft geleverd.

| **XML element**            | `<dc_contributors type="list"><Bijdrager /><Auteur /><Cameraman />...</dc_contributors>` |
| **Datatype**               | Vrije tekst                                                                  |
| **Verplichting**           | Optioneel                                                                                                                 |
| **Herhaalbaar**            | Ja                                                                                                                        |

```xml
<dc_contributors type="list">
    <Bijdrager />
    <Auteur />
    <Cameraman />
</dc_contributors>
```

### Mogelijke sleutels

{: .no_toc }

Aan de hand van een gecontroleerde lijst kan de rol van de bijdrager worden gespecificeerd. meemoo biedt een standaard lijst van rollen aan.

| `<Aanwezig />` | |
| `<Adviseur />` | |
| `<Afwezig />` | |
| `<Archivaris />` | |
| `<Arrangeur />` | |
| `<ArtistiekDirecteur />` | |
| `<Assistent />` | |
| `<Auteur />` | |
| `<Belichting />` | |
| `<Bijdrager />` | |
| `<Cameraman />` | |
| `<Co-producer />` | |
| `<Commentator />` | |
| `<Componist />` | |
| `<DecorOntwerper />` | |
| `<Digitaliseringspartner />` | |
| `<Dirigent />` | |
| `<Dramaturg />` | |
| `<Fabrikant />` | Bedrijf dat het afgebeelde goed of product geproduceerd heeft. |
| `<Fotografie />` | |
| `<Geluid />` | |
| `<Geluidsman />` | |
| `<GrafischOntwerper />` | |
| `<KostuumOntwerper />` | |
| `<Kunstenaar />` | |
| `<Make-up />` | |
| `<Muzikant />` | |
| `<Monteur />` | Iemand verantwoordelijk voor de ordening van beeld en/of geluid in audiomateriaal of audiovisueel materiaal. |
| `<Nieuwsanker />` | |
| `<Omroeper />` | |
| `<Onderzoeker />` | |
| `<Post-productie />` | |
| `<Producer />` | |
| `<Reporter />` | |
| `<Scenarist />` | |
| `<Soundtrack />` | |
| `<Sponsor />` | |
| `<TechnischAdviseur />` | |
| `<Uitvoerder />` | |
| `<Verontschuldigd />` | |
| `<Vertaler />` | |
| `<Verteller />` | |
| `<Voorzitter />` | |
| `<Afgebeelde />` | De entiteiten (bv. objecten, plaatsen of personen) die worden afgebeeld op het materiaal. |
| `<Ontvanger />` | De entiteit (bv. organisatie of persoon) die het materiaal origineel heeft ontvangen, zoals bij een brief of postkaart. |

## Publisher

{: #publisher}

De entiteit in hoofdzaak verantwoordelijk voor het verdelen en het toegankelijk maken van een item voor derden door omroep, verkoop, verhuur,...

| **XML element**            | `<dc_publishers type="list"><Publisher /><Distributeur />...</dc_publishers>` |
| **Datatype**               | Vrije tekst                                                                  |
| **Verplichting**           | Optioneel                                                                                                                |
| **Herhaalbaar**            | Ja                                                                                                                       |

```xml
<dc_publishers type="list"/>
    <Publisher>VRT</Publisher>
</dc_publishers>
```

### Mogelijke sleutels

{: .no_toc }

Aan de hand van een gecontroleerde lijst kan de rol van de publisher worden gespecificeerd. meemoo biedt een standaard lijst van rollen aan. Deze kan afhankelijk van de partner worden aangepast.

Indien geen van de rollen van toepassing is, kan het generieke 'Publisher' worden gebruikt, ofwel kan in overleg met meemoo de gecontroleerde lijst worden uitgebreid.

| `<Distributeur />` | |
| `<Exposant />` | |
| `<Persagentschap />` | |
| `<Publisher />` | |

# Inhoud

## Hoofdbeschrijving

{: #dc_description }

Een korte, algemene omschrijving van de intellectuele inhoud van een item.


| **XML element**            | `<dc_description/>`                                                                                                                                             |
| **Datatype**               | Vrije tekst                                                                                                                                                  |
| **Verplichting**           | Verplicht indien geen minimum van vijf trefwoorden.                                                                                                          |
| **Herhaalbaar**            | Nee                                                                                                                                                          |

```xml
<dc_description>Deze interviews zijn ingericht door het Universiteitsarchief en vormen een basis voor een onderzoek. Het eindresultaat is de publicatie \'Meisjestudenten aan de RUG</dc_description>
```

## Lange beschrijving

{: #dc_description_lang }

Een gedetailleerde beschrijving van de inhoud van het object. Dit kan bijvoorbeeld door puntsgewijs de voornaamste scènes, stock-shots, aparte items... te beschrijven. Voor ondertitels is een apart veld voorzien.


| **XML element**            | `<dc_description_lang/>`                                                                                                                                                       |
| **Datatype**               | Vrije tekst                                                                                                                                                                    |
| **Verplichting**           | Optioneel                                                                                                                                                                      |
| **Herhaalbaar**            | Nee                                                                                                                                                                            |

```xml
<dc_description_lang>
    Deze interviews zijn ingericht door het Universiteitsarchief en vormen een basis voor een onderzoek. 
    
    Het eindresultaat is de publicatie \'Meisjestudenten aan de RUG
</dc_description_lang>
```

## Programmabeschrijving

{: #dc_description_programme }

Een korte beschrijving van het programma waar het item een onderdeel van vormt.


| **XML element**        | `<dc_description_programme/>`                                                     |
| **Datatype**           | Vrije tekst                                                                       |
| **Verplichting**       | Optioneel                                                                         |
| **Herhaalbaar**        | Nee                                                                               |

## Cast

{: #dc_description_cast }

Een oplijsting van de voornaamste acteurs/performers en hun respectievelijke rol.


| **XML element**        | `<dc_description_cast/>`                                                                                      |
| **Datatype**           | Vrije tekst                                                                                                   |
| **Verplichting**       | Optioneel                                                                                                     |
| **Herhaalbaar**        | Ja                                                                                                            |

```xml
<dc_description_cast>Julien Schoenaert (Oedipus), Aafke Bruyninckx (Antigone)</dc_description_cast>
```

## Ondertitels

Een weergave van de ondertitels die bij het digitale object horen.

| **XML element**            | `<dc_description_ondertitels/>`                                                                                                                                                |
| **Datatype**               | Vrije tekst                                                                                                                                                                    |
| **Verplichting**           | Optioneel                                                                                                                                                                      |
| **Herhaalbaar**            | Nee                                                                                                                                                                            |

## Transcriptie

Een weergave van de transcriptie van het digitale object.

_De transcriptie kan eventueel in de toekomst ook automatisch aangemaakt worden door een speech to text engine._

| **XML element**            | `<dc_description_transcriptie/>`                                                                                                                                               |
| **Datatype**               | Vrije tekst                                                                                                                                                                    |
| **Verplichting**           | Optioneel                                                                                                                                                                      |
| **Herhaalbaar**            | Nee                                                                                                                                                                            |

## Genre

{: #genre}

Omschrijving van de aard, het genre van het item adhv een gecontroleerde lijst die door meemoo beheerd wordt.

| **XML element**            | `<dc_types type="list"><multiselect/></dc_types>`                                                                   |
| **Datatype**               | Gecontroleerde lijst                                                           |
| **Verplichting**           | Optioneel                                                                                                     |
| **Herhaalbaar**            | Ja                                                                                                            |

```xml
<dc_types type="list">
    <multiselect>Sport</multiselect>
</dc_types>
```

### Mogelijke waarden

{: .no_toc }

| `Actualiteit` | Een verslag van de gebeurtenissen van de dag of van het ogenblik; het nieuws dat op dat moment aan de orde is. |
| `Animatie` | Een film of video met getekende of andere levenloze figuren, waarbij animatie toegepast is. |
| `Concert` | Een voorstelling waar muziek gespeeld wordt voor publiek. |
| `Dans` | Een voorstelling voor publiek waar ritmisch bewogen wordt op muziek. |
| `Docudrama` | Een combinatie van documentaire en drama; een soort verslag van een historische of actuele gebeurtenis, waarbij uitgaande van feitelijke gegevens historische gebeurtenissen worden nagespeeld. |
| `Documentaire` | Een non-fictieve film of programma op televisie of radio over dingen die echt gebeurd zijn. Ze bevatten scènes of opnames uit de werkelijkheid die een beeld proberen te geven van een bepaalde situatie.  |
| `Documentatie` | Materiaal dat een bepaald onderwerp om- en beschrijft. |
| `Drama` | Een toneelstuk of met een slechte afloop. |
| `Educatief` | Materiaal dat bedoeld is om van te leren of opvoedkundige waarde heeft. |
| `Entertainment` | Materiaal met een amusementsfunctie en heeft als hoofddoel het vertier, vermaak of amusement van het publiek. |
| `Fictie` | Een verhaal of tekst, dat niet op de werkelijkheid is gebaseerd. Het wordt geschreven vanuit de fantasie van de schrijver.  |
| `Interview` | Een georganiseerd gesprek waarbij iemand vragen stelt en een ander antwoordt. |
| `Komedie` | Dramatisch werk waarin op amusante wijze over gewone mensen in alledaagse situaties gehandeld wordt. |
| `Kortfilm` | Een film met een voor films relatief korte speelduur. |
| `Kunstwerk` | Een voortbrengsel van het creatief en origineel tot uiting of voorstelling brengen van gedachten of gevoelens, bijvoorbeeld een schilderij, een muziekstuk of een beeldhouwwerk; voortbrengsel van de kunst |
| `Magazine` | Een periodieke publicatie die per aflevering bestaat uit een bundeling van artikelen. |
| `Muziekopname` | Een geluidsopname die bestaat uit muziek. |
| `Nieuws` | Berichten over belangrijke dingen die kortgeleden gebeurd zijn. |
| `Non-fictie` | Een verhaal of tekst, dat op de werkelijkheid is gebaseerd. De schrijver beschrijft feiten. |
| `Opera` | De opera is een toneelstuk met orkestbegeleiding waarin voornamelijk gezongen wordt in poëzievorm.  |
| `Performance` | Een theatrale voorstelling van een podiumkunstenaar of beeldend kunstenaar |
| `Speelfilm` | Een film waarin acteurs spelen. |
| `Sport` | Een televisie- of radioprogramma waar verslag wordt gedaan van sportwedstrijden, uitslagen van sportwedstrijden worden gegeven of een wedstrijd wordt besproken. |
| `Wetenschap` | Een televisie- of radioprogramma met wetenschap als hoofdonderwerp. |
| `Praatprogramma` | Een televisieprogramma of radioprogramma waarbij het hoofdaandeel uit spreken bestaat; een talkshow. |
| `Theater` | Theater is een verzamelnaam voor kunstvormen waarbij acteurs levende voorstellingen maken voor een publiek, opgevoerd op een scène, waarbij het hoofdaandeel uit spreken bestaat. |
| `Podcast` | Een podcast is een audio-'uitzending' waarbij het geluidsbestand op aanvraag beschikbaar is door middel van webfeeds. |
| `Bladmuziek` | Muziek die op papier genoteerd is. |

## Object type

{: #ebu_objectType }

Het type uitzending (programma of item).

| **XML element**            | `<ebu_objectType/>`                                                                                                                                             |
| **Datatype**               | Vrije tekst                                                                                                                                                  |
| **Verplichting**           | Nee                                                                                                                                                            |
| **Herhaalbaar**            | Nee                                                                                                                                                          |

```xml
<ebu_objectType>item</ebu_objectType>
<ebu_objectType>programma</ebu_objectType>
```

## Coverage (ruimtelijk)

Een beschrijvende afbakening van het geografisch gebied (straat, stad, land, continent) waar de inhoud van het item betrekking op heeft.

| **XML element**        | `<dc_coverages type="list"><ruimte/></dc_coverages>` |
| **Datatype**           | Vrije tekst                                          |
| **Verplichting**       | Optioneel                                            |
| **Herhaalbaar**        | Ja                                                   |

```xml
<dc_coverages type="list">
    <ruimte>Parijs</ruimte>
    <ruimte>provincie Antwerpen</ruimte>
</dc_coverages>
```

## Coverage (tijd)

Een beschrijvende afbakening van de tijdsperiode waar de inhoud van het item betrekking op heeft.

Let wel: het betreft hier de tijdsperiode waar het item *inhoudelijk* betrekking op heeft, niet de datum van creatie. Een documentaire uit de jaren 1950 over de Gulden Sporenslag heeft dus bijvoorbeeld als temporele coverage 'middeleeuwen'.


| **XML element**        | `<dc_coverages type="list"><tijd/></dc_coverages>`                  |
| **Datatype**           | Vrije tekst                                                         |
| **Verplichting**       | Optioneel                                                           |
| **Herhaalbaar**        | Ja                                                                  |

```xml
<dc_coverages type="list">
    <tijd>interbellum</tijd>
    <tijd>jaren 1920</tijd>
</dc_coverages>
```

## Trefwoorden

{: #dc_subjects}

Thematische trefwoorden met betrekking tot de inhoud van het item.

| **XML element**            | `<dc_subjects type="list"><Trefwoord/></dc_subjects>`                                                                                                          |
| **Datatype**               | Vrije tekst                                                                                                                                                      |
| **Verplichting**           | Verplicht (minimaal 5 trefwoorden) indien geen (korte) beschrijving                                                                                              |
| **Herhaalbaar**            | Ja                                                                                                                                                               |

```xml
<dc_subjects type="list">
    <Trefwoord>seksuele voorlichting</Trefwoord>
    <Trefwoord>socialistische beweging</Trefwoord>
</dc_subjects>
```

## Taal

{: #dc_languages }

De (belangrijkste) taal/talen die in het item worden gesproken of gebruikt.

Het betreft de gesproken of gezongen taal, niet de taal van eventuele ondertitels. In het geval van een stomme film, is de taal van de eventuele tussentitels indicatief.

| **XML element**            | `<dc_languages type="list"><multiselect/></dc_languages>`                                                                                                               |
| **Datatype**               | [ISO 639-1](https://nl.wikipedia.org/wiki/Lijst_van_ISO_639-codes) ("nl" = Nederlands; "fr" = Frans; "de" = Duits; "it" = Italiaans; "en" = Engels; "es" = Spaans; ...) |
| **Verplichting**           | Verplicht                                                                                                                                                               |
| **Herhaalbaar**            | Ja                                                                                                                                                                      |

```xml
<dc_languages type="list">
    <multiselect>nl</multiselect>
    <multiselect>fr</multiselect>
</dc_languages>
```

# Rechten

## Licentie

{: #licentie}

Het type licentie waaronder de exploitatie (het gebruik, de reproductie en bewerking) van het item wordt bepaald. De licenties zijn zo opgesteld dat er een onderscheid gemaakt kan worden tussen het hergebruik van het object en de metadata.

| **XML element**            | `<dc_rights_licenses type="list"><multiselect/></dc_rights_licences>`        |
| **Datatype**               | Gecontroleerde lijst |
| **Verplichting**           | Verplicht                                                                 |
| **Herhaalbaar**            | Ja                                                                        |

```xml
<dc_rights_licenses type="list">
    <multiselect>CC_BY-SA-METADATA</multiselect>
</dc_rights_licenses>
```

### Mogelijke waarden

{: .no_toc }

- VIAA-ONDERWIJS
- VIAA-ONDERZOEK
- VIAA-INTRAMUROS
- VIAA-INTRA_CP-CONTENT
- VIAA-INTRA_CP-METADATA-ALL
- VIAA-PUBLIEK-METADATA-LTD
- VIAA-PUBLIEK-METADATA-ALL
- VIAA-PUBLIEK-CONTENT
- Publiek-Domein
- CC0-METADATA
- CC0-CONTENT
- CC_BY-METADATA
- CC_BY-CONTENT
- CC_BY-SA-METADATA
- CC_BY-SA-CONTENT
- CC_BY-ND-METADATA
- CC_BY-ND-CONTENT
- CC_BY-NC-METADATA
- CC_BY-NC-CONTENT
- CC_BY-NC-SA-METADATA
- CC_BY-NC-SA-CONTENT
- CC_BY-NC-ND-METADATA
- CC_BY-NC-ND-CONTENT
- BEZOEKERTOOL-CONTENT
- BEZOEKERTOOL-METADATA-ALL

Zie de [detailpagina]({{ site.baseurl }}{% link docs/metadata/viaa/licenties.md %}) over licenties voor meer informatie over de betekenis van de verschillende waarden.

## Auteursrechthouder

{: #dc_rights_rightsOwners}

De persoon of organisatie die de auteursrechten bezit. Dit kan de eigenlijke auteur zijn, zijn erfgenamen of een derde partij aan wie de rechten zijn overgedragen.

| **XML element**            | `<dc_rights_rightsOwners type="list"><Auteursrechthouder/></dc_rights_rightsOwners>`             |
| **Datatype**               | Vrije tekst                                                                                      |
| **Verplichting**           | Verplicht (indien gekend)                                                                        |
| **Herhaalbaar**            | Ja                                                                                               |

```xml
<dc_rights_rightsOwners>
    <Auteursrechthouder>Etienne Tordoir</Auteursrechthouder>
    <Auteursrechthouder>KADOC</Auteursrechthouder>
</dc_rights_rightsOwner>
```

## Licentiehouder

De persoon of organisatie die eigenaar is van de resource of de rechten beheert.

Soms wordt de het toezicht op het correcte gebruik, evenals het beheer van de inkomsten gegenereerd uit het gebruik van auteursrechtelijk beschermde werken uitbesteed aan een externe persoon of organisatie (een zogenaamd auteursrechtvennootschappen zoals SABAM, SEMU,...).


| **XML element**        | `<dc_rights_rightsHolders type="list"><Licentiehouder/></dc_rights_rightsHolders>`                   |
| **Datatype**           | Vrije tekst                                                                                          |
| **Verplichting**       | Optioneel                                                                                            |
| **Herhaalbaar**        | Ja                                                                                                   |

```xml
<dc_rights_rightsHolders>
    <Licentiehouder>SABAM</Licentiehouder>
</dc_rights_rightsHolders>
```

## Credit

Tekst van de attributie of kennisgeving die bij het beeld moet verschijnen.

| **XML element**        | `<dc_rights_credit/>` |
| **Datatype**           | Vrije tekst           |
| **Verplichting**       | Optioneel             |
| **Herhaalbaar**        | Nee                    |

```xml
<dc_rights_credit>Copyright AMSAB. Onder de licentie Creative Commons CC-PD</dc_rights_credit/>
<dc_rights_credit>Copyright SMAK. Alle rechten voorbehouden</dc_rights_credit>
<dc_rights_credit>Alle rechten voorbehouden. Gelieve contact op te nemen met reproductie\@uu.be</dc_rights_credit>
```

## Opmerkingen rechten

{: #dc_rights_comment}

Hier kunnen bijkomende opmerkingen en voorwaarden met betrekking tot de gebruiksrechten van toepassing op het item worden vastgelegd.

| **XML element**            | `<dc_rights_comment/>`                                                                                                                             |
| **Datatype**               | Vrije tekst                                                                                                                                        |
| **Verplichting**           | Optioneel                                                                                                                                          |
| **Herhaalbaar**            | Nee                                                                                                                                                 |

```xml
<dc_rights_comment>Gelieve contact op te nemen met reproductie\@uu.be</dc_rights_comment>
```

# Technische metadata

De technische metadata wordt automatisch uitgelezen uit de header van de archiefmaster.

## Video formaat

Het videoformaat waarin de master copy van het digitale item bewaard wordt.


| **XML element**        | `<VideoFormat/>`                                                              |
| **Datatype**           | Vrije tekst                                                                   |
| **Herhaalbaar**        | Nee                                                                           |

```xml
<VideoFormat>JPEG2000</VideoFormat>
```

## Video technisch

Dit is de videotechnische metadata van de archiefmaster die uit de header van de mxf wordt opgehaald.

| **XML element**        | `<VideoTechnical/>` |
| **Datatype**           | Vrije tekst         |
| **Herhaalbaar**        | Nee                 |

```xml
<VideoTechnical>jpeg2000 (JPEG 2000 codestream restriction 0) 720x288 50.0fps 122815000bps</VideoTechnical>
```

## Audio technisch

Dit is de audiotechnische metadata van de archiefmaster die uit de header van de mxf wordt opgehaald.

| **XML element**        | `<AudioTechnical/>`                                                                                     |
| **Datatype**           | Vrije tekst                                                                                             |
| **Herhaalbaar**        | Nee                                                                                                     |

```xml
<AudioTechnical>pcm_s24le 8ch 48000HZ 9216000bps</AudioTechnical>
```

## TC IN

Dit zijn de tijdscodes die overgenomen zijn van de analoge drager in de digitale kopie.

| **XML element**        | `<TcInTimecode/>`                                                                         |
| **Herhaalbaar**        | Nee                                                                                       |

## TC OUT

Dit zijn de tijdscodes die overgenomen zijn van de analoge drager in de digitale kopie.


| **XML element**        | `<TcOutTimecode/>`                                                                        |
| **Herhaalbaar**        | Nee                                                                                       |

## Duur

De totale duur van het digitale item.

| **XML element**        | `<DurationTimecode/>`                                                  |
| **Datatype**           | Duur (`hh:mm:ss:sss`) |
| **Herhaalbaar**        | Nee                                                                    |

```xml
<DurationTimecode>00:14:14.920</DurationTimecode>
```

## Image size

De dimensie van het beeld, uitgedrukt in pixels.


| **XML element**        | `<ImageSize/>`                                     |
| **Datatype**           | Breedte x Hoogte (in pixels)                       |
| **Herhaalbaar**        | Nee                                                |

```xml
<ImageSize>1920x1080</ImageSize>
```

## MD5

MD5 (Message Digest Algorithm 5) is een veelgebruikte standaard om de integriteit van digitale bestanden te controleren.

| **XML element**        | `<md5/>`                                                      |
| **Datatype**           | [MD5 Checksum](https://nl.wikipedia.org/wiki/MD5#MD5-hashes) |
| **Herhaalbaar**        | Nee                                                           |

```xml
<MD5>69c64bcb374c5dd7bd5fa0b3bb76758f</MD5>
```
