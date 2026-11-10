---
title: VIAA Metadatamodel
nav_order: 1
---
# VIAA Metadatamodel

Hier vind je alle informatie over het gebruiken van het _VIAA-metadatamodel_, het metadatamodel dat momenteel in gebruik is bij meemoo.

!!! note

    Wij werken momenteel aan [nieuwe metadatamodellen](../knowledge-graph/index.md) in kader van de [meemoo Knowledge Graph](https://meemoo.be/nl/publicaties/metadataroadmap-de-route-naar-een-verbeterde-metadatainfrastructuur). Het _VIAA-metadatamodel_ zal nog een aantal jaar ondersteund worden, maar wordt op termijn uitgefaseerd.

1. Velden in het metadatamodel:
   1. [Algemeen](algemeen.md)
   2. [Registratie van analoge dragers](registratie.md)
   3. [Digitaliseringsproces](digitalisering.md)
2. [Datatypes](datatypes.md)
3. [Licenties](licenties.md)

In het kader van de overeenkomst wordt uitgegaan van het invullen van minimaal volgende velden:

- [dc_identifier_localid](algemeen.md#dc_identifier_localid) of [dc_identifier_localids](algemeen.md#dc_identifier_localids): lokale ID('s)
- [dc_title](algemeen.md#dc_title)
  - Programma: reekstitel (indien materiaal deel is van reeks of coherent geheel van items)
  - Itemtitel: titel van te beschrijven archiefitem
- Datering: productiedatum ([dcterms_created](algemeen.md#dcterms_created)) en/of gebruiksdatum (bv. datum eerste uitzending; [dcterms_issued](algemeen.md#datum-uitgave--uitzending))
- [dc_creators](algemeen.md#dc_creators): producent / maker (indien gekend)
- Beschrijving: summiere beschrijving in tekst (tijdsgebaseerde annotatie optioneel; [dc_description](algemeen.md#dc_description)) of een minimum van 5 trefwoorden die de inhoud van het item beschrijven (onder te brengen in [dc_subjects](algemeen.md#dc_subjects))
- [dc_languages](algemeen.md#dc_languages): taal van het item
- [dc_rights_rightsOwners](algemeen.md#dc_rights_rightsOwners): rechthebbende (indien gekend)
- [dc_rights_comment](algemeen.md#dc_rights_comment): gebruiksbeperkingen indien van toepassing (afwijking van de standaard policy: mag gebruikt worden voor meemoo doelgroepen conform de overeenkomst)
