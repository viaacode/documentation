---
layout:       default
title:        Film
parent:       Profiles
grand_parent:  2.1
nav_order:    4
nav_exclude:  false
---
Editor's Draft
{: .label .label-yellow }
# Profile: Film 

The film profile supports the ingest of digitised film consisting of one or more image and/or audio reels. 
This profile dictates how the media files (in file formats such as ZIP, MOV and DPX), their metadata, and the relationships between them, should be expressed and organized.

It mainly applies the [DCTERMS metadata schema](https://www.dublincore.org/schemas/xmls/qdc/dcterms.xsd) for descriptive metadata and allows extensions using [Schema.org](https://schema.org), thereby resembling the [Material Artwork profile](https://data.hetarchief.be/id/sip/2.1/material-artwork). 

Its additions lie in the introduction of a separate representation to denote the physical carrier(s) (a so-called 'carrier representation') and custom film-specific metadata (using `<premis:significantProperties>` elements in the package PREMIS file) to describe physical aspects of this/these carrier(s).
This carrier representation was added to facilitate the description of the physical carrier(s), since the PREMIS metadata schema itself doesn't offer this possibility. 

**Permalink:** <https://data.hetarchief.be/id/sip/2.1/film>

## Example Directory structure

```plaintext
root_directory
├── METS.xml
├── metadata
│   ├── descriptive
│   │   └── dc+schema.xml
│   └── preservation
│       └── premis.xml                                  # package PREMIS
│
└── representations
    │
    ├── representation_1
    │   ├── METS.xml
    │   ├── data
    │   │   └── master.zip                              # ZIP containing DPX files
    │   └── metadata
    │       └── preservation
    │           └── premis.xml
    │
    ├── representation_2
    │   ├── METS.xml
    │   ├── data
    │   │   └── mezzanine.mov                           # Playable mezzanine
    │   └── metadata
    │       └── preservation
    │           └── premis.xml
    │
    └── representation_3
        ├── METS.xml
        ├── data
        │   └── QC.dpx                                  # DPX for QC
        └── metadata
            └── preservation
                └── premis.xml
```

## Requirements

### General

- A SIP MUST contain content of exactly one digitised film, consisting of one or more image and/or audio reels.
- <mark> The content MUST be digitised per reel, i.e. each ZIP and/or MOV and/or DPX file contained in their respective representation directories MUST represent exactly one film consisting of one or more image and/or audio reels.</mark>
- There MUST be exactly one IE present in the SIP, i.e. the digitised film.
- There MUST be preservation metadata at the package level in the `preservation/premis.xml` file.
- There MUST be preservation metadata at the representation level in the respective `preservation/premis.xml` files.
- Preservation metadata in the SIP MUST be limited to the PREMIS metadata schema.
- Fixity MUST be calculated using the MD5 hashing algorithm, thus:
  - The value of element `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm` MUST be set to `MD5`.
  - The value of attribute `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm/@valueURI` MUST be set to `"http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5"`.
  - The value of all `//*/@CHECKSUMTYPE` attributes in the `METS.xml` files MUST be set to `MD5`.
- <mark>There MAY be descriptive metadata at the representation level (e.g. information about the representations, such as a title or a description).</mark>

### Package METS

- The `/mets/@TYPE` attribute MUST be set to `Video – File-based and Physical Media`.
- The `csip:CONTENTINFORMATIONTYPE` attribute MUST be set to `OTHER` and the `csip:OTHERCONTENTINFORMATIONTYPE` attribute MUST be set to `https://data.hetarchief.be/id/sip/2.1/film`.
- The `mets/dmdSec/mdRef/@MDTYPE` attribute MUST be set to `OTHER` and the `mets/dmdSec/mdRef/@OTHERMDTYPE` MUST be set to `DC+SCHEMA`.

### Package Descriptive Metadata

- A descriptive metadata file `descriptive/dc+schema.xml` describing the IE  MUST be present at the package level.
- Descriptive metadata in the `descriptive/dc+schema.xml` MUST be limited to the DCTERMS and SCHEMA elements outlined in the [basic profile](https://developer.meemoo.be/docs/diginstroom/sip/2.1/profiles/basic.html#dc-requirements).
- The DCTERMS and SCHEMA metadata in the `descriptive/dc+schema.xml` file MUST follow the [basic profile requirements](https://developer.meemoo.be/docs/diginstroom/sip/2.1/profiles/basic.html#dc-requirements) regarding the use of elements and attributes.

### Package Preservation Metadata

- If the SIP needs to contain descriptive metadata about the carrier and its reels themselves, the package `preservation/premis.xml` MUST contain a `<premis:object>` for the carrier representation;
- If a carrier representation is present, a structural `<premis:relationship>`  of type 'is represented by' MUST exist between the `<premis:object>` of the intellectual entity and the `<premis:object>` of the carrier representation (see [Overview of relevant PREMIS relationships]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/sip_structure/5_structure_package.md %}#premis-relationships) for more information);
- If a carrier representation is present, a structural `<premis:relationship>`  of type 'represents' MUST exist between the `<premis:object>` of the carrier representation and the `<premis:object>` of the intellectual entity (see [Overview of relevant PREMIS relationships]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/sip_structure/5_structure_package.md %}#premis-relationships) for more information);
- Any descriptive metadata about the physical film's reel(s) MUST be included as part of the carrier representation `<premis:object>` in separate `<premis:significantProperties>` elements;
- If descriptive metadata about the reel(s) is included, the metadata field name MUST be placed in a `<premis:significantPropertiesType>` element with the corresponding metadata field value in a `<premis:significantPropertiesValue>` element (both nested in one of the aforementioned `<premis:significantProperties>` elements);
- The carrier representation `<premis:object>` MUST contain the carrier type in a `<premis:storageMedium>` element, nested inside a `<premis:storage>` element;
- If the SIP contains a `<premis:object>` for the carrier representation, any events related to the handling of the real-life, physical carrier (e.g. registration, check-out, digitization...) MUST refer to the `<premis:object>` of the carrier representation with the use of a `<premis:linkingObjectIdentifier>` element (see [Adding provenance of representations](https://developer.meemoo.be/docs/diginstroom/sip/2.1/sip_structure/5_structure_package.html#adding-provenance-of-representations) for more information regarding the use of PREMIS events in the SIP).

The example below contains an illustration of a simplified carrier representation (preceded by its intellectual entity) and a registration event involving the carrier representation in PREMIS:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:premis="http://www.loc.gov/premis/v3" xmlns:haObj="https://data.hetarchief.be/ns/object/"
    xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

    <!-- IE for the film as a whole -->
    <premis:object
        xsi:type="premis:intellectualEntity">

        <premis:objectIdentifier>
            <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
            <premis:objectIdentifierValue>uuid-b1c5fa36-6bb6-460b-836b-ade5541fe89e</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <!-- relationship between the IE and its carrier representation -->
        <premis:relationship>
            <premis:relationshipType authority="relationshipType"
                authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
                valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
            <premis:relationshipSubType authority="relationshipSubType"
                authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
                valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is
                represented
                by</premis:relationshipSubType>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-e2f092de-f800-486c-a291-3160ce740544</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
        </premis:relationship>

    </premis:object>

    <!-- PREMIS object for the carrier representation itself -->
    <premis:object xsi:type="premis:representation">

        <premis:objectIdentifier>
            <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
            <premis:objectIdentifierValue>uuid-e2f092de-f800-486c-a291-3160ce740544</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <!-- descriptive metadata in several <premis:significantProperties> elements -->
        <premis:significantProperties>
            <premis:significantPropertiesType>barcode_image_reels</premis:significantPropertiesType>
            <premis:significantPropertiesValue>AFLM_FEL_001392</premis:significantPropertiesValue>
        </premis:significantProperties>
        <premis:significantProperties>
            <premis:significantPropertiesType>material_type</premis:significantPropertiesType>
            <premis:significantPropertiesValue>Original positive</premis:significantPropertiesValue>
        </premis:significantProperties>
        <premis:significantProperties>
            <premis:significantPropertiesType>num_reels</premis:significantPropertiesType>
            <premis:significantPropertiesValue>1</premis:significantPropertiesValue>
        </premis:significantProperties>
        <premis:significantProperties>
            <premis:significantPropertiesType>film_base</premis:significantPropertiesType>
            <premis:significantPropertiesValue>acetate</premis:significantPropertiesValue>
        </premis:significantProperties>

        <!-- indication of the carrier type -->
        <premis:storage>
            <premis:storageMedium>
                super8mmfilm
            </premis:storageMedium>
        </premis:storage>

        <!-- relationship between the carrier representation and its IE -->
        <premis:relationship>
            <premis:relationshipType authority="relationshipType"
                authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
                valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
            <premis:relationshipSubType authority="relationshipSubType"
                authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
                valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">
                represents</premis:relationshipSubType>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-b1c5fa36-6bb6-460b-836b-ade5541fe89e</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
        </premis:relationship>

    </premis:object>

    <!-- registration event -->
    <premis:event>
        <premis:eventIdentifier>

            <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
            <premis:eventIdentifierValue>uuid-aba62b7b-dd7a-43cf-b077-45f8b96deae8</premis:eventIdentifierValue>

        </premis:eventIdentifier>
        <premis:eventType valueURI="https://data.hetarchief.be/id/event-type/registration">
      registration
    </premis:eventType>
        <premis:eventDateTime>
      2021-04-02T09:04:04
    </premis:eventDateTime>
        <premis:eventDetailInformation>
            <premis:eventDetail>Base Scratching remarks: Light scratches, lines and stripes. Some cables. vinegar date: 2021-06-30 pH value:PH 4.8</premis:eventDetail>
            <premis:eventDetailExtension xmlns:schema="https://schema.org/">
                <schema:name>estimate_preparation_time_for_digitisation</schema:name>
                <schema:value>1:30:00</schema:value>
            </premis:eventDetailExtension>
            <premis:eventDetailExtension xmlns:schema="https://schema.org/">
                <schema:name>estimate_manual_cleaning_time</schema:name>
                <schema:value>0:00:00</schema:value>
            </premis:eventDetailExtension>
            <premis:eventDetailExtension xmlns:schema="https://schema.org/">
                <schema:name>physical_state_film</schema:name>
                <schema:value>film in good state</schema:value>
            </premis:eventDetailExtension>
        </premis:eventDetailInformation>

        <premis:eventOutcomeInformation>
            <premis:eventOutcome
                valueURI="http://id.loc.gov/vocabulary/preservation/eventOutcome/suc">success</premis:eventOutcome>
        </premis:eventOutcomeInformation>
        
        <premis:linkingAgentIdentifier>
            <premis:linkingAgentIdentifierType>MEEMOO-OR-ID</premis:linkingAgentIdentifierType>
            <premis:linkingAgentIdentifierValue>OR-jw86m54</premis:linkingAgentIdentifierValue>
            <premis:linkingAgentRole
                valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
        </premis:linkingAgentIdentifier>

        <!-- reference to the premis:Representation object of the carrier representation -->
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-e2f092de-f800-486c-a291-3160ce740544</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole
                valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/sou">source</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
    </premis:event>

</premis:premis>
```

### Validation

The XML files that are required by this profile can be validated using the following XML schema definitions:

| File | Format | XML Schema |
| `METS.xml` | METS v1.12.1 | [mets.xsd](https://www.loc.gov/standards/mets/mets.xsd) |
| `premis.xml` | PREMIS v3.0 | [premis-v3-0.xsd](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd) |
| `dc+schema.xml` | Dublin Core with Schema.org | dc+schema.xsd (not yet available) |

## Use Cases

Some use cases that implement this profile are:

{% include _usecases.liquid  %}