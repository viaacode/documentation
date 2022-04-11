---
layout:       default
title:        SIP Structure
parent: SIP Specification 0.1
nav_order:    5
nav_exclude:  false
has_children: true
---

# SIP structure

The meemoo SIP consists of a hierarchical directory structure with 3 levels:

- the root directory `/` or the _bag level_;
- the `/data` directory inside the root directory or _package level_;
- the `/representations` directory inside the `/data` directory or _representation level_.

<figure class="mx-auto">
  <img src="../../../../../assets/images_spec/sip_structure.png" alt="meemoo SIP structure" /> 
  <figcaption>The directory structure of a meemoo SIP.</figcaption>
</figure>

The [_bag level_](/4_structure_bag) is a transport layer and contains essential information for checking the integrity of all files in the SIP.
It uses a manifest file listing every file in the SIP together with its checksum.

The [_package level_](/5_structure_package) contains descriptive and preservation information about the SIP's main subject, namely the different (sub)IE(s) of which digital representations are being delivered, and preservation information about the SIP as a whole (e.g. the software used to create the SIP).
In addition, a `mets.xml` file supplies information about the SIP's structure and administrative information about the SIP's submission (e.g. the organization that submits the SIP).

The [_representation level_](/6_structure_representation) contains the media files, grouped in representation folders.
Each representation folder also contains descriptive and preservation information about a specific representation of the (sub)IE(s) of the SIP situated at the _package level_ (cf. supra) and preservation information about the media files.

***Example***

```plaintext
root_directory
│──manifest-md5.txt
│──bagit.txt
│
└──data
   │--mets.xml
   │
   └──metadata
   │  │
   │  └──descriptive
   │  │      ...
   │  │
   │  └──preservation
   │         ... 
   │
   └──representations
      │
      └──representation_1
      │  │──mets.xml
      │  │
      │  └──data
      │  │      ...
      │  │
      │  └──metadata
      │     │
      │     └──descriptive
      │     │      ...
      │     │
      │     └──preservation
      │            ...
      │
      └──representation_*
         │   ...
```

## Running example

{: .note }
This section introduces a fictional scenario as a running example and is to be considered informative.
The examples in the upcoming sections are based on this scenario.

One of meemoo's content partners, the (fictional) Flemish Cat Museum (henceforth FCM), wishes to archive a number of rare digitised pictures of the Felis Catus Flamens (a cat species originating in Flanders and threatened with extinction).
More specifically, the FCM owns two pictures of the Felis Catus Flamens lying on a sofa and one picture of the Felis Catus Flamens on its cat tree.

The FCM views the Felis Catus Flamens itself as the IE of the SIP.
They furthermore consider the two different environments in which the cat appears, as two separate representations of subIEs (i.e. lying on a sofa and sitting on a cat tree) since they have different metadata about both environments available.
This therefore results in one main IE (i.e. the Felis Catus Flamens), two subIEs (i.e. the cat lying on a sofa and sitting on a cat tree) and two representations, each representing one of the subIEs.
One representation then consists of two pictures, while the other consists of one picture.