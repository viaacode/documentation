---
title: Licenses
nav_order: 5
---

# Licenses

On this page you will find an overview of all existing licenses in the _VIAA-metadata model_, the metadata model currently in use by meemoo, and more information about when each license becomes active.

## Overview of the Licenses

Below you will find an overview of all existing licenses in the _VIAA-metadata model_. For each license, the value it has in the meemoo archive and what the value means is indicated.

### Education 

| | |
| --- | --- |
| **MAM name** | `VIAA-ONDERWIJS` |
| **Default value** | ON |
| **Implication** | meemoo may use the content and metadata for opening towards education, for example on [education.hetarchief.be](https://education.hetarchief.be/). |

| | |
| --- | --- |
| **MAM name** | `ONDERWIJS-FRAGMENT` |
| **Default value** | OFF |
| **Implication** | meemoo may use the content and metadata of one or multiple fragments of the item for opening towards education, for example on [education.hetarchief.be](https://education.hetarchief.be/). |

### Scientific Research 

| | |
| --- | --- |
| **MAM name** | `VIAA-ONDERZOEK` |
| **Default value** | ON |
| **Implication** | meemoo may use the content and metadata for research purposes. There is currently no concrete application for this available. |

### Content Partners

#### Content

| | |
| --- | --- |
| **MAM name** | `VIAA-INTRA_CP-CONTENT` |
| **Default value** | ON |
| **Implication** | The low-resolution copy of the object may be shown between content partners. If this license is given, the license `VIAA-INTRA_CP-METADATA-ALL` will also be applied. This license is used on [hetarchief.be](https://hetarchief.be). |

#### Metadata

| | |
| --- | --- |
| **MAM name** | `VIAA-INTRA_CP-METADATA-ALL` |
| **Default value** | ON |
| **Implication** | A comprehensive set of metadata of the object may be shared between content partners. This license is used on [hetarchief.be](https://hetarchief.be). |

### Broad Public

#### Content

| | |
| --- | --- |
| **MAM name** | `VIAA-PUBLIEK-CONTENT` |
| **Default value** | OFF |
| **Implication** | The low-resolution copy of the object may be made available to the broad public. This license implies that either the `VIAA-PUBLIEK-METADATA-LTD` or `VIAA-PUBLIEK-METADATA-ALL` is given. This license is not yet in use. |

#### Metadata

**Limited Metadata Set**

| | |
| --- | --- |
| **MAM name** | `VIAA-PUBLIEK-METADATA-LTD` |
| **Default value** | ON |
| **Implication** | A limited set of metadata of the object may be shared with the broad public. This license is used on [hetarchief.be](https://hetarchief.be). |

**Extended Metadata Set**

| | |
| --- | --- |
| **MAM name** | `VIAA-PUBLIEK-METADATA-ALL` |
| **Default value** | OFF |
| **Implication** | A comprehensive set of metadata of the object may be shared with the broad public. This license is used on [hetarchief.be](https://hetarchief.be). |

### Visitor Tool of the Content Partner

#### Content

| | |
| --- | --- |
| **MAM name** | `BEZOEKERTOOL-CONTENT` |
| **Default value** | ON |
| **Implication** | The low-resolution copy of the object may be shared with users of the visitor tool. This license is used on [hetarchief.be](https://hetarchief.be). |

#### Metadata

| | |
| --- | --- |
| **MAM name** | `BEZOEKERTOOL-METADATA-ALL` |
| **Default value** | ON |
| **Implication** | A comprehensive set of metadata of the object may be shared with users of the visitor tool. This license is used on [hetarchief.be](https://hetarchief.be). |

### VIAA License Intra-muros

| | |
| --- | --- |
| **MAM name** | `VIAA-INTRAMUROS` |
| **Default value** | OFF |
| **Implication** | Currently not used and will remain so. It may be used in the future if material would be opened via applications within the meemoo walls. |

### Other Licenses

#### Content

| | |
| --- | --- |
| **MAM name** | `CC_BY-CONTENT`, `CC_BY-SA-CONTENT`, `CC0-CONTENT`, `CC_BY-NC-CONTENT`, `CC_BY-ND-CONTENT`, `CC_BY-NC-ND-CONTENT` |
| **Default value** | OFF |
| **Implication** | Naming in line with the licenses at [Creative Commons](https://creativecommons.org/). All metadata and the browse copy can be shared in line with the license as described by [Creative Commons](https://creativecommons.org/). |

#### Metadata

| **MAM name** | `CC_BY-METADATA`, `CC_BY-SA-METADATA`, `CC0-METADATA`, `CC_BY-NC-METADATA`, `CC_BY-ND-METADATA`, `CC_BY-NC-ND-METADATA` |
| | |
| **Default value** | OFF |
| **Implication** | Naming in line with the licenses at [Creative Commons](https://creativecommons.org/). All metadata and the browse copy can be shared in line with the license as described by [Creative Commons](https://creativecommons.org/). |

## When are the default values filled in?

For files from meemoo digitalization projects, the default licenses (see the table above) are automatically activated at the moment of import into the archive system. Note well: since the material is still in the ingest space or workspace at that moment, it will not be used. Content partners have six months to publish the material and, if necessary, to adjust the licenses. Only after publication does the license become truly active and the material can be opened according to the licenses.

For files from digital collections, the licenses are provided with the submission of the material. If no license was submitted, meemoo will activate the default licenses.

## Overview of Default Values

By default, meemoo will currently activate the following licenses:

  | | |
  | --- | --- |
  | VIAA-ONDERWIJS | ON |
  | ONDERWIJS-FRAGMENT | OFF |
  | VIAA-ONDERZOEK | ON |
  | VIAA-INTRAMUROS | OFF |
  | VIAA-INTRA_CP-CONTENT | ON |
  | VIAA-INTRA_CP-METADATA-ALL | ON |
  | VIAA-PUBLIEK-METADATA-LTD | ON |
  | VIAA-PUBLIEK-METADATA-ALL | OFF |
  | BEZOEKERTOOL-CONTENT | ON |
  | BEZOEKERTOOL-METADATA-ALL | ON |
  | All other licenses | OFF |

## Can I adjust the license?

Licenses can be adjusted at any time. At the same time, we would like to point out that these default settings are in line with the closed cooperation agreement and are normally only adjusted for certain reasons (such as exclusive rights with third parties, sensitive material, etc.). 

The opening platforms are designed to take the license into account and thus decide whether an item will be used or not. Please note that it may take (typically 24 hours, but depending on the platform) for the opening platform to be adjusted. For urgent cases, an update can be requested via <support@meemoo.be>.
