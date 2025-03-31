---
layout:       default
title:        Film with 1 image reel
parent:       Use cases
grand_parent:  2.1
nav_order:    8
nav_exclude:  false
has_children: false
sip_profile:  Film
---
Editor's Draft
{: .label .label-yellow }
# Use Case: a digitization of a film with a single image reel

The following use case describes how to package a digitized film consisting of a single image reel.
The digitization contains a number of different representations of this film: a high-resolution master version, a medium-resolution mezzanine version and scans of the analog film container in both high- and low-resolution.
It includes:

- a MKV file;
- a JPG file;
- a PDF file;
- a MOV file;
- basic descriptive metadata about the content of the film;
- basic descriptive/preservation metadata about the analog carrier that was digitized;
- basic preservation metadata.

It uses the [**film SIP profile**]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/profiles/film.md %}).

A full sample SIP can be viewed [here](https://github.com/viaacode/documentation/tree/860cd24fab1875c581483ec266e90c76ff645d6c/assets/sip_samples/2.1/film_standard_mkv/uuid-2746e598-75cd-47b5-9a3e-8df18e98bb95).

## The content

The following content is provided for packaging:

| `master_dummy.mkv` | A high-resolution MKV file |
| `mezzanine_dummy.mov` | A medium-resolution MOV file |
| `dummy.pdf` | A high-resolution image scan of the analog film container |
| `dummy.jpg` | A low-resolution image scan of the analog film container |
| `metadata.xml` | A metadata record describing both the content of the film as well as the analog carrier that contained the film. |

The metadata record can contain the following information:

- the title of the film;
- a description of the film;
- the date the film was created;
- the genre of the film;
- the country where the film originated;
- any relevant creators and/or contributors of/to the film;
- a list of meemoo licenses;
- some keywords
- the md5 checksums of the media files;
- rights credits
- whether the film is silent or spoken;
- the original carrier format of the film;
- how many reels the analog film was made up of;
- any events prior to and following digitization;
- ...

Please note that the use case on this page merely serves as a possible example implementation of the film profile.
Metadata is also delivered, for example, in other formats than a single XML file.
In addition, it can also happen that the data is delivered by the service provider after digitization rather than by the content partner themselves.
In the latter case, it may be interesting to share the film profile specification with your service provider to handle or facilitate any necessary data transformation steps.

## Applying the core concepts

Since the metadata only describes a single film, we can consider it as the single Intellectual Entity in the SIP.

We can distinguish a couple of file sets that represent the film in some manner: a high-resolution copy mostly for archival purposes, a medium-resolution copy for dissemination and viewing purposes, and scans of the analog film container in both high- and low-resolution mostly for archival purposes as well.

Since each set of files can have a meaning on its own, they are split into separate representations. This results in the following application of the [core concepts]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/3_core-concepts.md %}):

|_Intellectual Entity_| the sculpture 'The Roman She-Wolf with Romulus and Remus' |
|_Representation 1_| the archive master: a high-resolution MKV file of the film |
|_Representation 2_| the mezzanine copy: a medium-resolution MOV file of the film |
|_Representation 3_| the low-resolution image scan of the analog film container |
|_Representation 4_| the high-resolution image scan of the analog film container |
|_Files (rep. 1)_| the MKV file: `master_dummy.mkv` |
|_Files (rep. 2)_| the MOV file: `mezzanine_dummy.mov` |
|_Files (rep. 3)_| the JPG file: `dummy.jpg` |
|_Files (rep. 4)_| the PDF file:  `dummy.pdf` |

This case relies on the film profile because:

- there is one IE and multiple representations containing one or more files;
- the film can be described using a combination of DCTERMS and a Schema.org;
- there is extensive descriptive metadata about the analog carrier itself that preceded the digitization.

## Directory structure

We package the content described earlier in a meemoo SIP named `uuid-2746e598-75cd-47b5-9a3e-8df18e98bb95`.
It has the following directory structure:

```plaintext
uuid-2746e598-75cd-47b5-9a3e-8df18e98bb95               # root directory
├── METS.xml
├── metadata
│   ├── descriptive
│   │   └── dc+schema.xml
│   └── preservation
│       └── premis.xml
└── representations
    ├── uuid-46b16a3e-3dbe-472d-9e9e-47c99457389d       # representation containing low-resolution image scan
    │   ├── METS.xml
    │   ├── data
    │   │   └── dummy.jpg
    │   └── metadata
    │       └── preservation
    │           └── premis.xml
    ├── uuid-5d7d4281-6a06-4b0e-ab88-cd430cb751ce       # representation containing high-resolution master copy
    │   ├── METS.xml
    │   ├── data
    │   │   └── master_dummy.mkv
    │   └── metadata
    │       └── preservation
    │           └── premis.xml
    ├── uuid-e2765c34-68dd-4f36-a230-5483c4bed076       # representation containing high-resolution image scan
    │   ├── METS.xml
    │   ├── data
    │   │   └── dummy.pdf
    │   └── metadata
    │       └── preservation
    │           └── premis.xml
    └── uuid-e3000091-b0c2-459b-9863-e5d2da8270c8       # representation containing medium-resolution mezzanine copy
        ├── METS.xml
        ├── data
        │   └── mezzanine_dummy.mov
        └── metadata
            └── preservation
                └── premis.xml
```

## The metadata

In total, the SIP contains 6 metadata files:

|`data/metadata/descriptive/dc+schema.xml`| Descriptive metadata about the IE residing at the _package level_ using the DCTERMS and Schema.org metadata schemas. |
|`data/metadata/preservation/premis.xml`| Preservation metadata about the IE residing at the _package level_, including any PREMIS events related to the SIP/package/representations + **descriptive metadata about the analog film carrier**. |
|`data/representations/uuid-*/metadata/preservation/premis.xml`| Preservation metadata about each of the 4 representations and 4 files residing at the _representation level_. |

Note the bold-faced descriptive metadata about the analog film carrier that can be present in the `premis.xml` file of the package level!
Contrary to other content profiles, the film profile allows an abstract 'carrier representation' inside this `premis.xml` file that makes it possible to capture descriptive metadata about the analog carrier, preceding any digitization events.
For more information about this 'carrier representation', please see the [film profile specification](../profiles/film.md).

### /data/metadata/descriptive/dc+schema.xml

The `dc+schema.xml` of the package level describes the IE using [the DCTERMS]((https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)) and the [Schema](schema.org/) metadata models.
It contains minimal metadata such as a title, a description, an identifier, a date of creation, and some additional metadata such as the genre and the country of origin of the film.

The identifier in the `dcterms:identifier` element is used to link the `dc+schema.xml` file to the corresponding PREMIS object in the `preservation/premis.xml` file of the package level (see [here]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/sip_structure/5_structure_package.md %}#shareduuidinfo) for more information).

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns="https://data.hetarchief.be/id/sip/2.1/film"
  xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xs="http://www.w3.org/2001/XMLSchema/"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:edtf="http://id.loc.gov/datatypes/edtf/" xmlns:schema="https://schema.org/">

  <!-- general title for the resource -->
  <dcterms:title xml:lang="nl">Katten in de tuin</dcterms:title>

  <!-- alternative title for the resource -->
  <dcterms:alternative xml:lang="nl">Ons katten in den hof</dcterms:alternative>

  <!-- general description for the resource -->
  <dcterms:description xml:lang="nl">Katten ravotten in de tuin</dcterms:description>

  <!-- linking id between dc and premis -->
  <dcterms:identifier>uuid-f9ef158c-f03c-4840-836e-8ffb8e8ebe04</dcterms:identifier>

  <!-- creationdate -->
  <dcterms:created xsi:type="edtf:EDTF-level1">XXXX-XX-XX</dcterms:created>

  <!-- genre of the resource -->
  <schema:genre>amateur recording</schema:genre>

  <!-- Country where the resource originated -->
  <schema:countryOfOrigin>BE</schema:countryOfOrigin>

  <!-- archiefvormer role -->
  <schema:creator schema:roleName="archiefvormer">
    <schema:name>Dummy privéarchief</schema:name>
  </schema:creator>

  <!-- rightsholder -->
  <dcterms:rightsHolder>© dummyorganisatie</dcterms:rightsHolder>

  <!-- IE type -->
  <dcterms:format>film</dcterms:format>

  <!-- VIAA licenses for the resource -->
  <dcterms:license>VIAA-ONDERWIJS</dcterms:license>
  <dcterms:license>VIAA-ONDERZOEK</dcterms:license>
  <dcterms:license>VIAA-INTRA-CP-CONTENT</dcterms:license>
  <dcterms:license>VIAA-INTRA_CP-METADATA-ALL</dcterms:license>
  <dcterms:license>VIAA-PUBLIEK-METADATA-LTD</dcterms:license>
  <dcterms:license>BEZOEKERTOOL-CONTENT</dcterms:license>
  <dcterms:license>BEZOEKERTOOL-METADATA-ALL</dcterms:license>

</metadata>
```

### data/metadata/preservation/premis.xml

The `premis.xml` of the package level describes the IE and the relationships with its representations.
It also contains relevant events that detail the digitization of the film, and its lifecycle up until the ingest of its digitized counterpart into meemoo's digital archives.

Note that the identifier in the `<premis:objectIdentifier>` element is shared with the `<dcterms:identifier/>` (in the `descriptive/dc+schema.xml` file) in order to link the PREMIS IE object to its description.

Finally, attention should be paid to the 'carrier representation' that was briefly introduced in the previous section.
This representation is a construct based on a `premis:representation` object that is entirely dedicated to the analog representation of the film (i.e. the image reel that was digitized).
Using a number of `<premis:significantProperties>` elements, this representation allows to describe the analog carrier in great detail and to use it as the source of a number of events (e.g. inspection, registration, digitization...).

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
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented
        by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-eb2175c9-56f9-4e7e-9192-0a11a297c1e2</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship with representation 1: mkv master -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="haObj"
        authorityURI="https://data.hetarchief.be/ns/object/"
        valueURI="https://data.hetarchief.be/ns/object/hasMasterCopy">has master</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-5defe23d-23b9-4819-a189-bc4793e7e60b</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship with representation 2: mov mezzanine -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="haObj"
        authorityURI="https://data.hetarchief.be/ns/object/"
        valueURI="https://data.hetarchief.be/ns/object/hasMezzanineCopy">has mezzanine</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-ed415625-bc4b-4ecc-b220-9c9d4400bde8</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship with representation 3: scans (pdf) -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented
        by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-d55d9a49-ac38-4849-8262-f978d36a3a24</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship with representation 4: scans (jpg) -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented
        by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-e2be2807-ba06-45a9-890d-4d275145aa9e</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>


  <!-- the object for the carrier representation is included here rather than in the representations
  directory, since it doesn't include any files -->
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
      <premis:significantPropertiesType>Number-of-reels</premis:significantPropertiesType>
      <premis:significantPropertiesValue>1</premis:significantPropertiesValue>
    </premis:significantProperties>
    <premis:significantProperties>
      <premis:significantPropertiesType>Preservation-problems</premis:significantPropertiesType>
      <premis:significantPropertiesValue>Base Scratching remarks: Light scratches, lines and
        stripes. Some cables.\nvinegar date: 2021-06-30 pH value:PH 4.8</premis:significantPropertiesValue>
    </premis:significantProperties>
    <premis:significantProperties>
      <premis:significantPropertiesType>Film-base</premis:significantPropertiesType>
      <premis:significantPropertiesValue>acetate</premis:significantPropertiesValue>
    </premis:significantProperties>
    <premis:significantProperties>
      <premis:significantPropertiesType>Subtitles-present</premis:significantPropertiesType>
      <premis:significantPropertiesValue>no</premis:significantPropertiesValue>
    </premis:significantProperties>
    <premis:significantProperties>
      <premis:significantPropertiesType>Silent-or-spoken-movie</premis:significantPropertiesType>
      <premis:significantPropertiesValue>Silent Movie</premis:significantPropertiesValue>
    </premis:significantProperties>
    <premis:significantProperties>
      <premis:significantPropertiesType>Color-or-Black-and-white</premis:significantPropertiesType>
      <premis:significantPropertiesValue>B/W and Color</premis:significantPropertiesValue>
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

    <!-- relationship between representation and its IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-f9ef158c-f03c-4840-836e-8ffb8e8ebe04</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

  <!-- events defined:
      - registration (source: carrier representation)
      - check-out (source: carrier representation)
      - inspection (source: carrier representation)
      - digitization (source: carrier representation; outcome: intermediate object representing DPXs or
  digitised sound)
      - compression (source: intermediate object representing DPXs; outcome: archive master MKV)
      - editing (source: archive master MKV; outcome: MOV mezzanine)
      - transfer (source: archive master MVK)
 -->

  <!-- registration event; performed by the CP -->
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

  <!-- check-out event; performed by the SP -->
  <premis:event>
    <premis:eventIdentifier>

      <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
      <premis:eventIdentifierValue>uuid-54c8c6f6-2981-41fd-bd02-edcb6e5b8871</premis:eventIdentifierValue>

    </premis:eventIdentifier>
    <premis:eventType valueURI="https://data.hetarchief.be/id/event-type/check-out">
      check-out
    </premis:eventType>
    <premis:eventDateTime>
      2021-12-28T00:00:00
    </premis:eventDateTime>
    <premis:eventOutcomeInformation>
      <premis:eventOutcome valueURI="http://id.loc.gov/vocabulary/preservation/eventOutcome/suc">success</premis:eventOutcome>
    </premis:eventOutcomeInformation>
    <!-- reference to the service provider -->
    <!-- organizations acting as agents have an additional implementer role -->
    <premis:linkingAgentIdentifier>
      <premis:linkingAgentIdentifierType>MEEMOO-OR-ID</premis:linkingAgentIdentifierType>
      <premis:linkingAgentIdentifierValue>OR-183420s</premis:linkingAgentIdentifierValue>
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

  <!-- inspection event; performed by the SP -->
  <premis:event>
    <premis:eventIdentifier>
      <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
      <premis:eventIdentifierValue>uuid-02411acf-e14f-49bb-9beb-f675dc2b351e</premis:eventIdentifierValue>
    </premis:eventIdentifier>
    <premis:eventType valueURI="https://data.hetarchief.be/id/event-type/inspection">inspection</premis:eventType>
    <premis:eventDateTime>2022-03-25T00:00:00</premis:eventDateTime>

    <premis:eventOutcomeInformation>
      <premis:eventOutcome valueURI="http://id.loc.gov/vocabulary/preservation/eventOutcome/suc">success</premis:eventOutcome>
      <premis:eventOutcomeDetail>
        <premis:eventOutcomeDetailNote>CEX / COLOR / MUTE</premis:eventOutcomeDetailNote>
      </premis:eventOutcomeDetail>
    </premis:eventOutcomeInformation>

    <!-- reference to the agent of the service provider -->
    <!-- people part of an organization acting as agent don't have a role assigned  -->
    <premis:linkingAgentIdentifier>
      <premis:linkingAgentIdentifierType>SP-AGENT</premis:linkingAgentIdentifierType>
      <premis:linkingAgentIdentifierValue>David</premis:linkingAgentIdentifierValue>
    </premis:linkingAgentIdentifier>

    <!-- reference to the service provider -->
    <!-- organizations acting as agents have an additional implementer role -->
    <premis:linkingAgentIdentifier>
      <premis:linkingAgentIdentifierType>MEEMOO-OR-ID</premis:linkingAgentIdentifierType>
      <premis:linkingAgentIdentifierValue>OR-183420s</premis:linkingAgentIdentifierValue>
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

  <!-- digitization event; performed by the SP -->
  <premis:event>
    <premis:eventIdentifier>
      <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
      <premis:eventIdentifierValue>uuid-652dd33d-367b-4a55-8e02-14f3e304d853</premis:eventIdentifierValue>
    </premis:eventIdentifier>
    <premis:eventType valueURI="https://data.hetarchief.be/id/event-type/digitization">digitization</premis:eventType>
    <premis:eventDateTime>2022-04-26T00:00:00</premis:eventDateTime>

    <premis:eventOutcomeInformation>
      <premis:eventOutcome valueURI="http://id.loc.gov/vocabulary/preservation/eventOutcome/suc">success</premis:eventOutcome>
      <premis:eventOutcomeDetail>
        <premis:eventOutcomeDetailNote>Abrasion marks, scratches, inlaid dust/dirt, important grain, apparent vignetting, slight instability, under/overexposure related to camera capture, slightly overscanned because of image between perfs or changing framing, dirty camera gate on some scenes</premis:eventOutcomeDetailNote>
      </premis:eventOutcomeDetail>
    </premis:eventOutcomeInformation>

    <!-- reference to the agent of the service provider -->
    <!-- people part of an organization acting as agent don't have a role assigned  -->
    <premis:linkingAgentIdentifier>
      <premis:linkingAgentIdentifierType>SP-AGENT</premis:linkingAgentIdentifierType>
      <premis:linkingAgentIdentifierValue>David/ScanStation</premis:linkingAgentIdentifierValue>
    </premis:linkingAgentIdentifier>

    <!-- reference to the service provider -->
    <!-- organizations acting as agents have an additional implementer role -->
    <premis:linkingAgentIdentifier>
      <premis:linkingAgentIdentifierType>MEEMOO-OR-ID</premis:linkingAgentIdentifierType>
      <premis:linkingAgentIdentifierValue>OR-183420s</premis:linkingAgentIdentifierValue>
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

    <!-- reference to an intermediary object that contains the digitized DPXs and/or sound -->
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-93199782-ab90-4ec4-ae43-92eb708a151d</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole
        valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>


  </premis:event>

  <!-- compression event; performed by the SP -->
  <premis:event>
    <premis:eventIdentifier>
      <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
      <premis:eventIdentifierValue>uuid-ddcd47c0-1967-475d-a3d4-e1d7fcc98729</premis:eventIdentifierValue>
    </premis:eventIdentifier>
    <premis:eventType valueURI="https://data.hetarchief.be/id/event-type/compression">compression</premis:eventType>
    <premis:eventDateTime>2022-04-28T00:00:00</premis:eventDateTime>
    <premis:eventDetailInformation>
      <premis:eventDetail>
        RAWcooked 23.09.20241109, FFmpeg 7.1
        Parameters used: --all -o Variation_Examples/AIP_VARIATION_3-M_image_0_sound_N_scans/rawcooked/t14th8df5w_001.mkv
        Package name: t14th8df5w_001_%06d.dpx
        Track 1:
        (000001 --> 000025)
        DPX/Raw/RGB/8bit/U/LE
        Info: Reversibility data created by RAWcooked 23.09.20241109.
        Info: Uncompressed file hashes (used by reversibility check) present.
        Info: Reversibility was checked, no issue detected.
      </premis:eventDetail>
    </premis:eventDetailInformation>
    <premis:eventOutcomeInformation>
      <premis:eventOutcome valueURI="http://id.loc.gov/vocabulary/preservation/eventOutcome/suc">success</premis:eventOutcome>
    </premis:eventOutcomeInformation>

    <!-- reference to the agent of the service provider -->
    <!-- people part of an organization acting as agent don't have a role assigned  -->
    <premis:linkingAgentIdentifier>
      <premis:linkingAgentIdentifierType>SP-AGENT</premis:linkingAgentIdentifierType>
      <premis:linkingAgentIdentifierValue>JulienS/RAWcooked 23.09.20241109, FFmpeg 7.1</premis:linkingAgentIdentifierValue>
    </premis:linkingAgentIdentifier>

    <!-- reference to the service provider -->
    <!-- organizations acting as agents have an additional implementer role -->
    <premis:linkingAgentIdentifier>
      <premis:linkingAgentIdentifierType>MEEMOO-OR-ID</premis:linkingAgentIdentifierType>
      <premis:linkingAgentIdentifierValue>OR-183420s</premis:linkingAgentIdentifierValue>
      <premis:linkingAgentRole
        valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
    </premis:linkingAgentIdentifier>

    <!-- reference to the source of the event -->
    <!-- reference to the intermediary premis:Representation object that contains the digitized DPXs
    and/or sound, created in digitization event above -->
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-93199782-ab90-4ec4-ae43-92eb708a151d</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole
        valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/sou">source</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>

    <!-- reference to the output of the event -->
    <!-- reference to the master representation that contains the MKV -->
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-5defe23d-23b9-4819-a189-bc4793e7e60b</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole
        valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>

  </premis:event>

  <!-- editing event; performed by the SP -->
  <premis:event>
    <premis:eventIdentifier>
      <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
      <premis:eventIdentifierValue>uuid-de489f24-98d1-4032-b39c-2f36e1cfcc63</premis:eventIdentifierValue>
    </premis:eventIdentifier>
    <premis:eventType valueURI="https://data.hetarchief.be/id/event-type/editing">editing</premis:eventType>
    <premis:eventDateTime>2022-04-28T00:00:00</premis:eventDateTime>

    <premis:eventOutcomeInformation>
      <premis:eventOutcome valueURI="http://id.loc.gov/vocabulary/preservation/eventOutcome/suc">success</premis:eventOutcome>
      <premis:eventOutcomeDetail>
        <premis:eventOutcomeDetailNote>Abrasion marks, scratches, inlaid dust/dirt, important grain, slight instability, under/overexposure related to camera capture, slight color fading/shift on some scenes. MUTE . Speed 16 fps. MIX COLOR/BW.</premis:eventOutcomeDetailNote>
      </premis:eventOutcomeDetail>
    </premis:eventOutcomeInformation>

    <!-- reference to the agent of the service provider -->
    <!-- people part of an organization acting as agent don't have a role assigned  -->
    <premis:linkingAgentIdentifier>
      <premis:linkingAgentIdentifierType>SP-AGENT</premis:linkingAgentIdentifierType>
      <premis:linkingAgentIdentifierValue>JulienS/Nucoda</premis:linkingAgentIdentifierValue>
    </premis:linkingAgentIdentifier>

    <!-- reference to the service provider -->
    <!-- organizations acting as agents have an additional implementer role -->
    <premis:linkingAgentIdentifier>
      <premis:linkingAgentIdentifierType>MEEMOO-OR-ID</premis:linkingAgentIdentifierType>
      <premis:linkingAgentIdentifierValue>OR-183420s</premis:linkingAgentIdentifierValue>
      <premis:linkingAgentRole
        valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
    </premis:linkingAgentIdentifier>

    <!-- reference to the premis:Representation object of the master representation -->
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-5defe23d-23b9-4819-a189-bc4793e7e60b</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole
        valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/sou">source</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>

    <!-- reference to the premis:Representation object that contains the MOV file (i.e. the
    mezzanine copy) -->
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-ed415625-bc4b-4ecc-b220-9c9d4400bde8</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole
        valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>


  </premis:event>

  <premis:event>
    <premis:eventIdentifier>

      <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
      <premis:eventIdentifierValue>uuid-019a16cf-9d35-469d-8c14-a8ed1564003d</premis:eventIdentifierValue>

    </premis:eventIdentifier>
    <premis:eventType valueURI="https://data.hetarchief.be/id/event-type/transfer">
      transfer
    </premis:eventType>
    <premis:eventDateTime>
      2022-05-07T00:00:00
    </premis:eventDateTime>
    <premis:eventDetailInformation>
      <premis:eventDetailExtension xmlns:schema="https://schema.org">
        <schema:name>lto_id</schema:name>
        <schema:value>I61842L6</schema:value>
      </premis:eventDetailExtension>
    </premis:eventDetailInformation>
    <premis:eventOutcomeInformation>
      <premis:eventOutcome valueURI="http://id.loc.gov/vocabulary/preservation/eventOutcome/suc">success</premis:eventOutcome>
    </premis:eventOutcomeInformation>
    <!-- reference to the service provider -->
    <!-- organizations acting as agents have an additional implementer role -->
    <premis:linkingAgentIdentifier>
      <premis:linkingAgentIdentifierType>MEEMOO-OR-ID</premis:linkingAgentIdentifierType>
      <premis:linkingAgentIdentifierValue>OR-183420s</premis:linkingAgentIdentifierValue>
      <premis:linkingAgentRole
        valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
    </premis:linkingAgentIdentifier>
    <!-- reference to the premis:Representation object that contains the archive master -->
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-5defe23d-23b9-4819-a189-bc4793e7e60b</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole
        valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/sou">source</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>
  </premis:event>

  <!-- reference to the content partner -->
  <premis:agent>
    <premis:agentIdentifier>
      <premis:agentIdentifierType>MEEMOO-OR-ID</premis:agentIdentifierType>
      <premis:agentIdentifierValue>OR-jw86m54</premis:agentIdentifierValue>
    </premis:agentIdentifier>
    <premis:agentName>FelixArchief</premis:agentName>
    <premis:agentType>CP-AGENT</premis:agentType>
  </premis:agent>

  <!-- reference to the service provider -->
  <premis:agent>
    <premis:agentIdentifier>
      <premis:agentIdentifierType>MEEMOO-OR-ID</premis:agentIdentifierType>
      <premis:agentIdentifierValue>OR-183420s</premis:agentIdentifierValue>
    </premis:agentIdentifier>
    <premis:agentName>Vectracom</premis:agentName>
    <premis:agentType>SP-AGENT</premis:agentType>
  </premis:agent>

</premis:premis>
```

### data/representations/uuid-46b16a3e-3dbe-472d-9e9e-47c99457389d/metadata/preservation/premis.xml

The `premis.xml` file of the first representation describes two PREMIS objects:

1. the representation;
2. the JPG file `dummy.jpg`.

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the JPG file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:premis="http://www.loc.gov/premis/v3"
  xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <!-- Create PREMIS object for the representation itself -->
    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-e2be2807-ba06-45a9-890d-4d275145aa9e</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files, detailed below -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-75d336db-603d-4795-b6cc-30bd7c583f8c</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-f9ef158c-f03c-4840-836e-8ffb8e8ebe04</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-75d336db-603d-4795-b6cc-30bd7c583f8c</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions"
          authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions"
          valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
          MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>b14d633a01600edabc450a0d0ae4390d</premis:messageDigest>
      </premis:fixity>
      <premis:size>5913</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/43</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="formatRegistryRole"
            authorityURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole"
            valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">
            specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>dummy.jpg</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-e2be2807-ba06-45a9-890d-4d275145aa9e</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```

### data/representations/uuid-5d7d4281-6a06-4b0e-ab88-cd430cb751ce/metadata/descriptive/dc+schema.xml

The `premis.xml` file of the second representation describes two PREMIS objects:

1. the representation;
2. the MKV file `master_dummy.mkv`.

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the MKV file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:premis="http://www.loc.gov/premis/v3"
  xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <!-- Create PREMIS object for the representation itself -->
    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-5defe23d-23b9-4819-a189-bc4793e7e60b</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files, detailed below -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-7df1ed59-40dd-4323-83c9-e730615eea34</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="haObj"
        authorityURI="https://data.hetarchief.be/ns/object/"
        valueURI="https://data.hetarchief.be/ns/object/isMasterCopyOf">is master of</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-f9ef158c-f03c-4840-836e-8ffb8e8ebe04</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-7df1ed59-40dd-4323-83c9-e730615eea34</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions"
          authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions"
          valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
          MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>a427d6f9dcf9d4db5145dc159fef7727</premis:messageDigest>
      </premis:fixity>
      <premis:size>6255</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/569</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="formatRegistryRole"
            authorityURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole"
            valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">
            specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>master_dummy.mkv</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-5defe23d-23b9-4819-a189-bc4793e7e60b</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```


### data/representations/uuid-e2765c34-68dd-4f36-a230-5483c4bed076/metadata/preservation/premis.xml

The `premis.xml` file of the third representation describes two PREMIS objects:

1. the representation;
2. the PDF file `dummy.pdf`.

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the PDF file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:premis="http://www.loc.gov/premis/v3"
  xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <!-- Create PREMIS object for the representation itself -->
    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-d55d9a49-ac38-4849-8262-f978d36a3a24</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files, detailed below -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-9e74d34e-f2ec-483f-b144-47f63307ecbe</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-f9ef158c-f03c-4840-836e-8ffb8e8ebe04</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-9e74d34e-f2ec-483f-b144-47f63307ecbe</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions"
          authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions"
          valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
          MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>b0dfa6f04e6056ecd953a2ad127820e3</premis:messageDigest>
      </premis:fixity>
      <premis:size>19933</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/18</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="formatRegistryRole"
            authorityURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole"
            valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">
            specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>dummy.pdf</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-d55d9a49-ac38-4849-8262-f978d36a3a24</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```

### data/representations/uuid-e3000091-b0c2-459b-9863-e5d2da8270c8/metadata/preservation/premis.xml

The `premis.xml` file of the fourth representation describes two PREMIS objects:

1. the representation;
2. the MOV file `mezzanine_dummy.mov`.

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the MOV file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:premis="http://www.loc.gov/premis/v3"
  xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <!-- Create PREMIS object for the representation itself -->
    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-ed415625-bc4b-4ecc-b220-9c9d4400bde8</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files, detailed below -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-b8e8db68-296b-4025-9dad-df966fe05b70</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="haObj"
        authorityURI="https://data.hetarchief.be/ns/object"
        valueURI="https://data.hetarchief.be/ns/object/isMezzanineCopyOf">is mezzanine of</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-f9ef158c-f03c-4840-836e-8ffb8e8ebe04</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-b8e8db68-296b-4025-9dad-df966fe05b70</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions"
          authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions"
          valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
          MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>04c2f9a43c2aa4d6f6975903bad69a67</premis:messageDigest>
      </premis:fixity>
      <premis:size>52574</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>x-fmt/384</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="formatRegistryRole"
            authorityURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole"
            valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">
            specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>mezzanine_dummy.mov</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType"
        authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
        valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-ed415625-bc4b-4ecc-b220-9c9d4400bde8</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```
