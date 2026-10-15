---
title: VIAA Metadata Model
nav_order: 1
---
# VIAA Metadata Model

Here you will find all information on using the _VIAA Metadata Model_, the metadata model currently in use at meemoo.

!!! note

    We are currently working on [new metadata models](../knowledge-graph/index.md) as part of the [meemoo Knowledge Graph](https://meemoo.be/nl/publicaties/metadataroadmap-de-route-naar-een-verbeterde-metadatainfrastructuur). The _VIAA Metadata Model_ will continue to be supported for a number of years but will eventually be phased out.

1. Fields in the metadata model:
   1. [General](algemeen.md)
   2. [Registration of analogue carriers](registratie.md)
   3. [Digitisation process](digitalisering.md)
2. [Data types](datatypes.md)
3. [Licences](licenties.md)

In the context of the agreement, it is assumed that the following fields are filled in at minimum:
- [dc_identifier_localid](algemeen.md#dc_identifier_localid) or [dc_identifier_localids](algemeen.md#dc_identifier_localids): local IDs
- [dc_title](algemeen.md#dc_title)
  - Program: series title (if the material is part of a series or coherent whole of items)
  - Item title: title of the archival item to be described
- Dating: production date ([dcterms_created](algemeen.md#dcterms_created)) and/or use date (e.g., date of first broadcast; [dcterms_issued](algemeen.md#datum-uitgave--uitzending))
- [dc_creators](algemeen.md#dc_creators): producer / maker (if known)
- Description: summary description in text (temporal annotation optional; [dc_description](algemeen.md#dc_description)) or a minimum of 5 keywords describing the content of the item (to be placed in [dc_subjects](algemeen.md#dc_subjects))
- [dc_languages](algemeen.md#dc_languages): language of the item
- [dc_rights_rightsOwners](algemeen.md#dc_rights_rightsOwners): rights holders (if known)
- [dc_rights_comment](algemeen.md#dc_rights_comment): usage restrictions if applicable (deviation from the standard policy: may be used for meemoo target audiences in accordance with the agreement)
