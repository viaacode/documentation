---
layout:       default
title:        Single file
parent:       Use cases
grand_parent:  2.1
nav_order:    1
nav_exclude:  false
has_children: false
sip_profile: Basic
---
Editor's Draft
{: .label .label-yellow }
# Use Case: a single image

The following use case describes how to package a single image file with some basic descriptive metadata.
It illustrates the most minimal implementation that conforms to meemoo's SIP specification and the [**Basic content profile**]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/profiles/basic.md %}).

A full sample SIP can be downloaded [here](https://github.com/viaacode/documentation/tree/main/assets/sip_samples/basic_deec5d89-3024-4cbd-afcd-e18af4ad33ec/).

## The content

The following content is provided for packaging:

| `D523F963.jpg` | The media file: an image in the JPEG media format containing a photo taken in January 2022 depicting a cat lying on a sofa. |
| `metadata.xml` | A metadata record describing the contents of the essence. |

The metadata record contains the following information:

- the title of the photo
- three keywords

## Applying the core concepts

Since the metadata record is only about one thing (i.e. the photograph), we can appoint it as the sole Intellectual Entity present.
Only one version of the image was supplied (i.e. the media file in the JPEG media format), hence there is only one representation.
This representation contains the `D523F963.jpg` file.

| _Intellectual Entity_ | photograph taken in January 2022 depicting a cat  |
| _Representation_ | the archive master |
| _File_ | the media file `D523F963.jpg` |

This case uses the Basic content profile because:

- there is only one IE and one Representation;
- the metadata can be mapped entirely to the Dublin Core and PREMIS metadata vocabularies.

## Directory structure

We package the above in a meemoo SIP named `basic_deec5d89-3024-4cbd-afcd-e18af4ad33ec.zip`.
It has the following directory structure:

```plaintext
basic_deec5d89-3024-4cbd-afcd-e18af4ad33ec
│── METS.xml
│── metadata
|   |── descriptive
|   |   └── dc+schema.xml
|   └── preservation
|       └── premis.xml
│
└── representations
    └──representation_1
       │── METS.xml
       └──data
       |  └── D523F963.jpg
       │
       └──metadata
          └──preservation
             └── premis.xml
```

## The metadata

In total, the SIP contains 3 metadata files:

| `/data/metadata/descriptive/dc+schema.xml` | Descriptive metadata about the IE residing on _Package level_. |
| `/data/metadata/preservation/premis.xml` | Preservation metadata about the IE residing on _Package level_. |
| `/data/representations/representation_1/metadata/preservation/premis.xml` | Preservation metadata about the representation and files residing on _Representation level_. |

### /data/metadata/descriptive/dc+schema.xml

The `dc+schema.xml` of the package level describes the IE using the DCTERMS metadata schema.
It contains minimal metadata such as a title, an identifier, a creation datetime (set to unknown) and a number of keywords.

Note that the identifier is used to link the `dc+schema.xml` file to the corresponding PREMIS object in the `preservation/premis.xml` file of the package level (see [here]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/sip_structure/5_structure_package.md %}#shareduuidinfo)).

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns="https://data.hetarchief.be/id/sip/2.1/basic" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:edtf="http://id.loc.gov/datatypes/edtf/">

  <!-- general title for the resource -->
  <dcterms:title xml:lang="nl">Felis Catus Flamens sitting on a cat tree</dcterms:title>

  <!-- linking id between dc and premis -->
  <dcterms:identifier>uuid-a0a5329c-4ad1-4607-9f6e-ce980d90b992</dcterms:identifier>

  <!-- date unknown -->
  <dcterms:created xsi:type="edtf:EDTF-level1">XXXX</dcterms:created>

  <!-- multiple keywords about the resource -->
  <dcterms:subject xml:lang="nl">Cat</dcterms:subject>
  <dcterms:subject xml:lang="nl">Felis Catus Flamens</dcterms:subject>
  <dcterms:subject xml:lang="nl">Cat tree</dcterms:subject>

</metadata>  
```

### /data/metadata/preservation/premis.xml

The `premis.xml` of the package level describes the IE and its relationship with its representation.

Note that the identifier in the `<premis:objectIdentifier>` element is shared with the `<dcterms:identifier>` in the `descriptive/dc+schema.xml` file in order to link the two files together.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <!-- IE about the Felis Catus Flamens -->
  <premis:object xsi:type="premis:intellectualEntity">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-a0a5329c-4ad1-4607-9f6e-ce980d90b992</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-4e475706-2752-4f77-9069-1f71c0e22572</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```

### /data/representations/representation_1/metadata/preservation/premis.xml

The `premis.xml` of the representation level describes two PREMIS objects:

1. the representation
2. the media file `D523F963.jpg`

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the media file;

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-4e475706-2752-4f77-9069-1f71c0e22572</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-945a16cd-eeb6-4a4c-95bb-4656a9f0909d</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE/subIE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-a0a5329c-4ad1-4607-9f6e-ce980d90b992</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-945a16cd-eeb6-4a4c-95bb-4656a9f0909d</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>18513a8d61c6f2cbaaeeedd754b01d6b</premis:messageDigest>
      </premis:fixity>
      <premis:size>1735648</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/1507</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="formatRegistryRole" authorityURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
        <premis:formatNote></premis:formatNote>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>D523F963.jpg</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-4e475706-2752-4f77-9069-1f71c0e22572</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```

<small>
Continue to [Video file with subtitles]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/usecases/video-with-subtitles.md %}).
</small>
