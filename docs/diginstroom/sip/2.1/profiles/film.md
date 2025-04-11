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

The film profile supports the ingest of digitised film stored on one or more image and/or audio reels. 
This profile dictates how the media files (in file formats such as MKV, MOV, JPEG and PDF), their metadata, and the relationships between them, should be expressed and organized.

It mainly applies the [DCTERMS metadata schema](https://www.dublincore.org/schemas/xmls/qdc/dcterms.xsd) for descriptive metadata and allows extensions using [Schema.org](https://schema.org), thereby resembling the [Basic profile](https://data.hetarchief.be/id/sip/2.1/basic). 

Its additions lie in the introduction of a separate PREMIS representation to denote the physical carrier(s) (a so-called 'carrier representation') and custom film-specific metadata (using `<premis:significantProperties>` elements in the package PREMIS file) to describe physical aspects of this/these carrier(s).

This carrier representation was added to facilitate the description of the physical carrier(s), since the PREMIS metadata schema itself doesn't offer this possibility directly.
Please note that, as a result, the carrier representation as such is not reflected by a representation folder in the `representations` directory, given that it is used purely for the addition of descriptive metadata about the carrier(s) and does not contain any files itself.

**Permalink:** <https://data.hetarchief.be/id/sip/2.1/film>

## Example Directory structure

```plaintext
root_directory
├── METS.xml
├── metadata
│   ├── descriptive
│   │   └── dc+schema.xml                               # descriptive metadata about the content of the film
│   └── preservation
│       └── premis.xml                                  # package PREMIS
│
└── representations
    │
    ├── representation_1
    │   ├── METS.xml
    │   ├── data
    │   │   └── master.mkv                              # archive master
    │   └── metadata
    │       └── preservation
    │           └── premis.xml
    │
    ├── representation_2
    │   ├── METS.xml
    │   ├── data
    │   │   └── mezzanine.mov                           # mezzanine
    │   └── metadata
    │       └── preservation
    │           └── premis.xml
    │
    ├── representation_3
    │   ├── METS.xml
    │   ├── data
    │   │   └── scan.jpeg                               # scan(s) of the reel's container (if present) in JPEG
    │   └── metadata
    │       └── preservation
    │           └── premis.xml
    │
    └── representation_4
        ├── METS.xml
        ├── data
        │   └── scan.pdf                                # scan(s) of the reel's container (if present) in PDF
        └── metadata
            └── preservation
                └── premis.xml
```

## Requirements

### General

- A SIP MUST contain content of exactly one digitised film, consisting of one or more image and/or audio reels.
- Each MKV, MOV, or set of scans (either in JPG and/or in PDF) contained in their respective representation directories MUST represent exactly one image or audio reel.
- There MUST be exactly one IE present in the SIP, i.e. the digitised film.
- There MUST be preservation metadata at the package level in the `preservation/premis.xml` file.
- There MUST be preservation metadata at the representation level in the respective `preservation/premis.xml` files.
- Preservation metadata in the SIP MUST be limited to the PREMIS metadata schema.
- Fixity MUST be calculated using the MD5 hashing algorithm, thus:
  - The value of element `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm` MUST be set to `MD5`.
  - The value of attribute `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm/@valueURI` MUST be set to `"http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5"`.
  - The value of all `//*/@CHECKSUMTYPE` attributes in the `METS.xml` files MUST be set to `MD5`.
- Descriptive metadata about the IE MUST be specified at the package level in the `dc+schema.xml` file.
- Descriptive metadata about the carrier(s) (i.e. the reel(s)) MUST be specified at the package level in the `preservation/premis.xml` file.

### Package METS

- The `/mets/@TYPE` attribute MUST be set to `Video – File-based and Physical Media`.
- The `csip:CONTENTINFORMATIONTYPE` attribute MUST be set to `OTHER` and the `csip:OTHERCONTENTINFORMATIONTYPE` attribute MUST be set to `https://data.hetarchief.be/id/sip/2.1/film`.
- The `mets/dmdSec/mdRef/@MDTYPE` attribute MUST be set to `OTHER` and the `mets/dmdSec/mdRef/@OTHERMDTYPE` MUST be set to `dc+schema`.

### Package Descriptive Metadata

- A descriptive metadata file `descriptive/dc+schema.xml` describing the IE  MUST be present at the package level.
- Descriptive metadata in the `descriptive/dc+schema.xml` MUST be limited to the DCTERMS and SCHEMA elements outlined in the [basic profile](https://developer.meemoo.be/docs/diginstroom/sip/2.1/profiles/basic.html#dc-requirements).
- The DCTERMS and SCHEMA metadata in the `descriptive/dc+schema.xml` file MUST follow the [basic profile requirements](https://developer.meemoo.be/docs/diginstroom/sip/2.1/profiles/basic.html#dc-requirements) regarding the use of elements and attributes.
- In addition to the elements and requirements outlined in the basic profile, the film profile allows the use of the elements outlined below:

| Element | `metadata/schema:countryOfOrigin` |
|-----------------------|-----------|
| Name | Country of origin |
| Description | The country of origin of the film, i.e. where the film was created. |
| Datatype | [ISO 3166]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/2_terminology.md %}#iso3166) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/schema:genre` |
|-----------------------|-----------|
| Name | Genre |
| Description | Genre of the film. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/2_terminology.md %}#string) |
| Vocabulary | Amateuropname<br>Andere<br>Animatiefilm<br>Bedrijfsfilm<br>Biografie<br>Burlesque<br>Cinemagazine<br>Compilatie<br>Dierenfilm<br>Documentaire<br>Educatieve film<br>Erotics<br>Ethnografische film<br>Experimentele film<br>Familiefilm<br>Feeërie<br>Filmbrief<br>Fragmenten<br>Gefilmd Spektakel<br>Griezelfilm<br>Historische film<br>Industriefilm<br>Journaal<br>Kinderfilm<br>Komedie<br>Kunstfilm<br>Medische film<br>Melodrama<br>Militange film<br>Montagefilm<br>Muzikale film<br>Natuurfilm<br>Onafgewerkte film<br>Onbekend<br>Oorlogsfilm<br>Opdrachtfilm<br>Overheidsvoorlichting<br>Parodie<br>Pornografische film<br>Poëtische film<br>Promotiefilm<br>Propagandafilm<br>Reclamefilm<br>Reisverslag<br>Reportage<br>Rushes<br>Televisie Programma<br>Televisiefilm<br>Toeristische Film<br>Trailer<br>Westerns<br>Wetenschappelijke Film |
| Cardinality | 0..* |
| Obligation | MAY |

### Package Preservation Metadata

The addition of a separate PREMIS representation for the carrier(s) (i.e. the carrier representation) leads to a number of additional requirements in the package `premis.xml` file.
The section below outlines the high level requirements, while the section [Describing a carrier within the carrier representation](#describing-a-carrier-within-the-carrier-representation) contains a more detailed discussion of the possibilities offered by the carrier representation, divided into [a general intro](#introduction) and [a normative summary of requirements](#normative-summary).

- The following relationships MUST be present between the `<premis:object>` of the intellectual entity and that of the carrier representation (see also [Overview of relevant PREMIS relationships]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/sip_structure/5_structure_package.md %}#premis-relationships) for more information):
  - A structural `<premis:relationship>`  of type 'has carrier copy';
  - A structural `<premis:relationship>`  of type 'is carrier copy of'.

_Example 1: an example `<premis:object>` of a carrier representation together the relationships between the Intellectual Entity and the carrier representation_

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:premis="http://www.loc.gov/premis/v3" xmlns:haObj="https://data.hetarchief.be/ns/object/"
  xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <!-- IE for the film as a whole -->
  <premis:object xsi:type="premis:intellectualEntity">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-f9ef158c-f03c-4840-836e-8ffb8e8ebe04</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>MEEMOO-LOCAL-ID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>2891#422</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>MEEMOO-PID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>kiodik2z9x</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship with the (abstract) carrier representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="haObj"
        authorityURI="https://data.hetarchief.be/ns/object/"
        valueURI="https://data.hetarchief.be/ns/object/hasCarrierCopy">has carrier copy</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-eb2175c9-56f9-4e7e-9192-0a11a297c1e2</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    </premis:object>

    <!-- PREMIS object for the carrier representation itself -->
    <premis:object xsi:type="premis:representation">

    <!-- Create PREMIS object for the representation itself -->
    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-eb2175c9-56f9-4e7e-9192-0a11a297c1e2</premis:objectIdentifierValue>
    </premis:objectIdentifier>
    <premis:objectIdentifier>
      <premis:objectIdentifierType>Batch-ID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>FLMB20</premis:objectIdentifierValue>
    </premis:objectIdentifier>
    <premis:objectIdentifier>
      <premis:objectIdentifierType>Barcode-image-reels</premis:objectIdentifierType>
      <premis:objectIdentifierValue>AFLM_FEL_001392</premis:objectIdentifierValue>
    </premis:objectIdentifier>

        <!-- relationship between the carrier representation and its IE -->
        <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="haObj"
        authorityURI="https://data.hetarchief.be/ns/object/"
        valueURI="https://data.hetarchief.be/ns/object/isCarrierCopyOf">is carrier copy of</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-f9ef158c-f03c-4840-836e-8ffb8e8ebe04</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    </premis:object>

</premis:premis>
```

#### Describing a carrier within the carrier representation

##### Introduction

The carrier representation lends itself to the addition of descriptive metadata about the carriers themselves.
This can be achieved by using `<premis:significantProperties>` elements nested inside of the `<premis:object>` of the carrier representation.
In turn each of these elements consists of either a `<premis:significantPropertiesType>` element (for the metadata field name) and a `<premis:significantPropertiesValue>` element (for the metadata field value), or a `<premis:significantPropertiesExtension>` element that allows the use of external metadata schemas inside the element.

In addition to the use outlined above, we require that a carrier representation specifies the carrier type of the digitised reel(s) the SIP contains. 
It is currently impossible to add other descriptive metadata at this finer grained level, meaning that other descriptive metadata about the reels must be added via one of the the constructions outlined in the previous paragraph.

Finally, the carrier representation is also used in relevant events related to the handling of the real-life, physical carrier (e.g. registration, check-out, digitization...).

_Example 2: hierarchical listing of a package `premis.xml` file with an Intellectual Entity and a Carrier Representation consisting of 2 pieces of descriptive metadata and the carrier type of its reel_

```text
premis:premis
│
├── premis:object xsi:type="premis:intellectualEntity"    # Intellectual Entity
│
└── premis:object xsi:type="premis:representation"        # Carrier Representation
    │
    ├── premis:significantProperties                      # Descriptive metadata
    │   ├── premis:significantPropertiesType
    │   └── premis:significantPropertiesValue
    │
    ├── premis:significantProperties                      # Descriptive metadata
    │   ├── premis:significantPropertiesType
    │   └── premis:significantPropertiesValue
    │
    ├── premis:significantProperties                      # Descriptive metadata
    │   └── premis:significantPropertiesExtension
    │
    └── premis:storage                                    # Carrier type of reel 1
        └── premis:storageMedium
```

##### Normative summary

- There MUST be a carrier representation in the package premis.xml, reflected by a `<premis:object>`;
- Any descriptive metadata about the physical film's reel(s) MUST be included as part of the carrier representation `<premis:object>`;
- Any descriptive metadata in the carrier representation `<premis:object>` MUST be placed in separate `<premis:significantProperties>` elements;
- Each `<premis:significantProperties>` element MUST either contain a combination of a `<premis:significantPropertiesType>` element (for the metadata field name) and a `<premis:significantPropertiesValue>` element (for the metadata field value), or a `<premis:significantPropertiesExtension>` element with the use of external metadata schemas;
- If a `<premis:significantPropertiesExtension>` element is used, it MUST declare the namespaces of the external metadata schemas using the `@xmlns` attribute;
- Each digitized reel in the SIP MUST be reflected in the carrier representation `<premis:object>` by using separate `<premis:storageMedium>` elements;
- Each `<premis:storageMedium>` element MUST contain a `<premis:storage>` element with the specific carrier type of a reel;
- Any events related to the handling of the real-life, physical carrier(s) MUST refer to the carrier representation `<premis:object>` with a `<premis:linkingObjectIdentifier>` element (see [Adding provenance of representations](https://developer.meemoo.be/docs/diginstroom/sip/2.1/sip_structure/5_structure_package.html#adding-provenance-of-representations);

_Example 4_ below contains an illustration of a simplified carrier representation (preceded by its intellectual entity) and a registration event involving the carrier representation in the package `premis.xml` file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:premis="http://www.loc.gov/premis/v3" xmlns:haObj="https://data.hetarchief.be/ns/object/"
  xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <!-- IE for the film as a whole -->
  <premis:object xsi:type="premis:intellectualEntity">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-f9ef158c-f03c-4840-836e-8ffb8e8ebe04</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>MEEMOO-LOCAL-ID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>2891#422</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>MEEMOO-PID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>kiodik2z9x</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship with the (abstract) carrier representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="haObj"
        authorityURI="https://data.hetarchief.be/ns/object/"
        valueURI="https://data.hetarchief.be/ns/object/hasCarrierCopy">has carrier copy</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-eb2175c9-56f9-4e7e-9192-0a11a297c1e2</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    </premis:object>

    <!-- PREMIS object for the carrier representation itself -->
    <premis:object xsi:type="premis:representation">

    <!-- Create PREMIS object for the representation itself -->
    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-eb2175c9-56f9-4e7e-9192-0a11a297c1e2</premis:objectIdentifierValue>
    </premis:objectIdentifier>
    <premis:objectIdentifier>
      <premis:objectIdentifierType>Batch-ID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>FLMB20</premis:objectIdentifierValue>
    </premis:objectIdentifier>
    <premis:objectIdentifier>
      <premis:objectIdentifierType>Barcode-image-reels</premis:objectIdentifierType>
      <premis:objectIdentifierValue>AFLM_FEL_001392</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:significantProperties>
      <premis:significantPropertiesType>Projection-speed</premis:significantPropertiesType>
      <premis:significantPropertiesValue>18 f/s</premis:significantPropertiesValue>
    </premis:significantProperties>
    <premis:significantProperties>
      <premis:significantPropertiesType>CP-evaluation</premis:significantPropertiesType>
      <premis:significantPropertiesValue>4 interesting, HR digitisation</premis:significantPropertiesValue>
    </premis:significantProperties>
    <premis:significantProperties>
      <premis:significantPropertiesType>Image-or-sound</premis:significantPropertiesType>
      <premis:significantPropertiesValue>image</premis:significantPropertiesValue>
    </premis:significantProperties>
    <premis:significantProperties>
      <premis:significantPropertiesType>Aspect-ratio</premis:significantPropertiesType>
      <premis:significantPropertiesValue>1:37</premis:significantPropertiesValue>
    </premis:significantProperties>
    <premis:significantProperties>
      <premis:significantPropertiesExtension xmlns:schema='https://schema.org'>
        <schema:duration>0:04:55</schema:duration>
        <schema:material>Original positive</schema:material>
        <schema:size>
          <schema:unitCode>MTR</schema:unitCode>
          <schema:QuantitativeValue>135</schema:QuantitativeValue>
        </schema:size>
      </premis:significantPropertiesExtension>
    </premis:significantProperties>

    <premis:storage>
      <premis:storageMedium>8mmfilm</premis:storageMedium>
    </premis:storage>


        <!-- relationship between the carrier representation and its IE -->
        <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="haObj"
        authorityURI="https://data.hetarchief.be/ns/object/"
        valueURI="https://data.hetarchief.be/ns/object/isCarrierCopyOf">is carrier copy of</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-f9ef158c-f03c-4840-836e-8ffb8e8ebe04</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    </premis:object>

</premis:premis>

    <!-- registration event -->
    <premis:event>
    <premis:eventIdentifier>

      <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
      <premis:eventIdentifierValue>uuid-e435a1eb-fa72-4221-b673-3cc9289d0904</premis:eventIdentifierValue>

    </premis:eventIdentifier>
    <premis:eventType valueURI="https://data.hetarchief.be/id/event-type/registration">
      registration
    </premis:eventType>
    <premis:eventDateTime>
      2021-04-02T09:04:04
    </premis:eventDateTime>

    <premis:eventOutcomeInformation>
      <premis:eventOutcome valueURI="http://id.loc.gov/vocabulary/preservation/eventOutcome/suc">success</premis:eventOutcome>
    </premis:eventOutcomeInformation>
    <!-- reference to the content partner -->
    <!-- organizations acting as agents have an additional implementer role -->
    <premis:linkingAgentIdentifier>
      <premis:linkingAgentIdentifierType>MEEMOO-OR-ID</premis:linkingAgentIdentifierType>
      <premis:linkingAgentIdentifierValue>OR-jw86m54</premis:linkingAgentIdentifierValue>
      <premis:linkingAgentRole
        valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
    </premis:linkingAgentIdentifier>
    <!-- reference to the premis:Representation object of the carrier representation -->
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-eb2175c9-56f9-4e7e-9192-0a11a297c1e2</premis:linkingObjectIdentifierValue>
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
