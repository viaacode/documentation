---
layout: default
title: Licenties
parent: VIAA Metadatamodel
nav_order: 5
---

# Licenties

Op deze pagina vind je een overzicht van alle bestaande licenties in het _VIAA-metadatamodel_, het metadatamodel dat momenteel in gebruik is bij meemoo, en meer informatie over het moment waarop welke licentie actief wordt.

## Overzicht van de licenties

Hieronder vind je een overzicht van alle bestaande licenties in het _VIAA-metadatamodel_. Per licentie wordt aangegeven wat de waarde is in het meemoo archief en wat de waarde betekent.

### Onderwijs 

| **MAM-naam** | `VIAA-ONDERWIJS` |
| **Defaultwaarde**|  AAN |
| **Implicatie** | meemoo mag de content en metadata gebruiken voor ontsluiting richting het onderwijs, bijvoorbeeld op [onderwijs.hetarchief.be](https://onderwijs.hetarchief.be/). |

| **MAM-naam** | `ONDERWIJS-FRAGMENT` |
| **Defaultwaarde**|  UIT |
| **Implicatie** | meemoo mag de content en metadata van één dan wel meerdere fragmenten van het item gebruiken voor ontsluiting richting het onderwijs, bijvoorbeeld op [onderwijs.hetarchief.be](https://onderwijs.hetarchief.be/). |

### Wetenschappelijk onderzoek 

| **MAM-naam** | `VIAA-ONDERZOEK` |
| **Defaultwaarde** | AAN |
| **Implicatie** | meemoo mag de content en metadata gebruiken voor research doeleinden. Hier is nog geen concrete applicatie voor beschikbaar. |

### Contentpartners

#### Content

| **MAM-naam** |  `VIAA-INTRA_CP-CONTENT` |
| **Defaultwaarde** | AAN |
| **Implicatie** | De lage resolutiekopie van het object mag getoond worden tussen contentpartners. Indien deze licentie gegeven wordt, zal ook de licentie `VIAA-INTRA_CP-METADATA-ALL` van toepassing worden. Deze licentie wordt gebruikt op [hetarchief.be](https://hetarchief.be). |

#### Metadata

| **MAM-naam** | `VIAA-INTRA_CP-METADATA-ALL` |
| **Defaultwaarde** | AAN |
| **Implicatie** | Een uitgebreide set aan metadata van het object mag gedeeld worden tussen contentpartners. Deze licentie wordt gebruikt op [hetarchief.be](https://hetarchief.be) |

### Brede publiek

#### Content

| **MAM-naam** | `VIAA-PUBLIEK-CONTENT` |
| **Defaultwaarde** | UIT |
| **Implicatie** | De lage resolutiekopie van het object mag beschikbaar gemaakt worden aan het brede publiek. Deze licentie impliceert dat ook de `VIAA-PUBLIEK-METADATA-LTD` of `VIAA-PUBLIEK-METADATA-ALL` gegeven wordt. Deze licentie is nog niet in gebruik. |

#### Metadata

**Beperkte metadataset**

| **MAM-naam** | `VIAA-PUBLIEK-METADATA-LTD` |
| **Defaultwaarde** | AAN |
| **Implicatie** | Een beperkte set aan metadata van het object mag gedeeld worden aan het brede publiek. Deze licentie wordt gebruikt op [hetarchief.be](https://hetarchief.be). |

**Uitgebreide metadataset**

| **MAM-naam** | `VIAA-PUBLIEK-METADATA-ALL` |
| **Defaultwaarde** | UIT |
| **Implicatie** | Een uitgebreide set aan metadata van het object mag gedeeld worden aan het brede publiek. Deze licentie wordt gebruikt op [hetarchief.be](https://hetarchief.be). |

### Bezoekertool van de contentpartner

#### Content

| **MAM-naam** | `BEZOEKERTOOL-CONTENT` |
| **Defaultwaarde** | AAN |
| **Implicatie** | De lage resolutiekopie van het object mag gedeeld worden aan gebruikers van de bezoekertool. Deze licentie wordt gebruikt op [hetarchief.be](https://hetarchief.be) |

#### Metadata

| **MAM-naam** | `BEZOEKERTOOL-METADATA-ALL` |
| **Defaultwaarde** | AAN |
| **Implicatie** | Een uitgebreide set aan metadata van het object mag gedeeld worden aan gebruikers van de bezoekertool. Deze licentie wordt gebruikt op [hetarchief.be](https://hetarchief.be) |

### VIAA-licentie intra-muros

| **MAM naam** | `VIAA-INTRAMUROS` |
| **Default waarde** | UIT |
| **Implicatie** | wordt momenteel nog niet gebruikt en zal uitstaan. Kan in de toekomst gebruikt worden indien materiaal via applicaties binnen de meemoo-muren ontsloten zou worden. |

### Andere licenties

#### Content

| **MAM-naam** | `CC_BY-CONTENT`, `CC_BY-SA-CONTENT`, `CC0-CONTENT`, `CC_BY-NC-CONTENT`, `CC_BY-ND-CONTENT`, `CC_BY-NC-ND-CONTENT` |
| **Defaultwaarde** | UIT |
| **Implicatie** | naamgeving in lijn met de licenties bij [Creative Commons](https://creativecommons.org/). Alle metadata en de browsekopie kunnen gedeeld worden in lijn met de licentie zoals omschreven door [Creative Commons](https://creativecommons.org/). |

#### Metadata

| **MAM-naam** | `CC_BY-METADATA`, `CC_BY-SA-METADATA`, `CC0-METADATA`, `CC_BY-NC-METADATA`, `CC_BY-ND-METADATA`, `CC_BY-NC-ND-METADATA`
| **Defaultwaarde** | UIT |
| **Implicatie** | naamgeving in lijn met de licenties bij [Creative Commons](https://creativecommons.org/). Alle metadata en de browsekopie kunnen gedeeld worden in lijn met de licentie zoals omschreven door [Creative Commons](https://creativecommons.org/). |

## Wanneer worden de standaardwaardes ingevuld?

Voor bestanden uit meemoo-digitaliseringsprojecten worden de standaardlicenties (zie tabel hierboven) automatisch actief op het moment van import in het archiefsysteem. Let wel: aangezien het materiaal zich op dat moment nog in de ingest-ruimte of workspace bevindt, zal het niet gebruikt worden. Contentpartners hebben zes maanden de tijd om het materiaal te publiceren en indien nodig de licenties aan te passen. Pas na publicatie wordt de licentie echt actief en kan het materiaal dus ontsloten worden volgens de licenties.

Voor bestanden uit digitale collecties worden de licenties meegegeven bij de aanlevering van het materiaal. Indien geen licentie aangeleverd werd, zal meemoo de standaardlicenties activeren.

## Overzicht standaardwaardes

Standaard zal meemoo op dit moment onderstaande licenties activeren:

  | VIAA-ONDERWIJS  |    AAN |
  | ONDERWIJS-FRAGMENT  |    UIT |
  | VIAA-ONDERZOEK   |   AAN |
  | VIAA-INTRAMUROS  |   UIT |
  | VIAA-INTRA_CP-CONTENT  |  AAN |
  | VIAA-INTRA_CP-METADATA-ALL | AAN |
  | VIAA-PUBLIEK-METADATA-LTD  | AAN |
  | VIAA-PUBLIEK-METADATA-ALL |  UIT |
  | BEZOEKERTOOL-CONTENT | AAN |
  | BEZOEKERTOOL-METADATA-ALL | AAN |
  | Alle andere licenties  | UIT |

## Kan ik de licentie nog aanpassen?

Licenties kunnen ten allen tijde aangepast worden. Tegelijkertijd wensen we er op te wijzen dat deze defaultsettings conform de afgesloten samenwerkingsovereenkomst zijn en er normaal gezien enkel wegens bepaalde redenen (zoals exclusieve rechten met derden, gevoelig materiaal, ...) aanpassingen nodig zijn.  

Ontsluitingsplatformen zijn zo ontworpen dat ze rekening houden met de licentie en op basis hiervan een item al dan niet zullen gebruiken. Hou er wel rekening mee dat het even (typisch 24u, maar afhankelijk van platform tot platform) kan duren eer het ontsluitingsplatform aangepast is. Voor dringende gevallen kan een update gevraagd worden via <support@meemoo.be>.
