---
layout:       default
title:        Bag level
parent:         SIP Structure
grand_parent: SIP Specification 0.1
nav_order:    5
nav_exclude:  false
---
Status: WIP
{: .label .label-yellow }
# Structure of a meemoo SIP: bag level
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

<mark class="miel">Afkorting CP is nog niet geintroduceerd?</mark>

The bag is the top level of the meemoo SIP and is in essence as a wrapper around a SIP submitted by a CP for ingest in the meemoo archive.
It is a compressed directory that conforms to the [BagIt 1.0 specification (RFC 8493)](https://www.rfc-editor.org/rfc/rfc8493.html).

A bag has a sole practical purpose as a transfer container between a CP's archive and meemoo's ingest space.
Therefore, it will be unpacked during ingest and is deleted after processing.
As such it will not appear in the meemoo archive as a separate entity.

***Requirements***

- A bag MUST be a compressed archive file.
- A bag MUST contain a `bagit.txt` file.
- A bag MUST contain a `manifest-md5.txt` file.

<mark class="miel">Deze hieronder is zinloos als requirement, of toch hier, want je kan dat toch niet controleren. Beperk je tot wat software wel of niet nodig heeft. Hard constrainst dus. En gaat dit niet over de SIP ipv de Bag? Lijkt mij wel nuttig om informatief te vermelden, bv. in de intro of de directory structure. </mark>

- A bag MUST contain content from only one particular CP and MUST NOT contain content from different CPs.
- A bag MUST contain a `/data` directory.
- The contents of a bag MUST be character-encoded according to UTF-8.
- A bag SHOULD be a ZIP or TAR file.
- A bag MAY contain a `bag-info.txt` file.

***Example***

```plaintext
root_directory
│── manifest-md5.txt
│── bagit.txt
│
└──data
   │   ...
```

## manifest-md5.txt (file)

The `manifest-md5.txt` file lists all files in the bag across the different directories together with their corresponding checksums created with the MD5 message-digest algorithm.
It is used during processing of the bag to allow for data integrity checking.

***Requirements***

- The `manifest-md5.txt` file MUST list all files contained in the bag.
- The `manifest-md5.txt` file MUST NOT list any directories.
- The `manifest-md5.txt` file MUST NOT list any files outside of the bag.
- Each line of the `manifest-md5.txt` file MUST be of the form *checksum filepath*, where *filepath* is the pathname of a file relative to the bag-lelvel directory, and *checksum* is a hex-encoded checksum calculated by the MD5 message-digest algorithm.
- The slash ('/') character MUST be used as a path separator in *filepath*.
- One or more linear whitespace characters (spaces or tabs) MUST separate each *checksum* from each *filepath*.
- Each line of the `manifest-md5.txt` file MUST be terminated with an LF, a CR or a CRLF.

***Example***

```plaintext
9675dc6350af621ebd4b3ddd05b33eeb  ./data/mets.xml
3d800edcf9c5535c52ec8e0d6a160ccb  ./data/representations/representation_2/mets.xml
18513a8d61c6f2cbaaeeedd754b01d6b  ./data/representations/representation_2/data/D523F963.jpg
d59060b8b471627a74b12bacca878543  ./data/representations/representation_2/metadata/preservation/premis.xml
ed2d03c274c9ce0521531d6d2c269e94  ./data/representations/representation_2/metadata/descriptive/dc.xml
158dd1571df41274b0a349a0e54b5f81  ./data/representations/representation_1/mets.xml
d4985ba4b67ff067a0e84c53b6d35355  ./data/representations/representation_1/data/1450.jpeg
b7ae37f6094794e313402b9d064978e8  ./data/representations/representation_1/data/1445.jpeg
d49ec67f6cf9194e3cee47f125e2b0fb  ./data/representations/representation_1/metadata/preservation/premis.xml
05bfa303741e01fee4d151464c933e29  ./data/representations/representation_1/metadata/descriptive/dc.xml
f95e7df37dfdfa5174388598aa901164  ./data/metadata/preservation/premis.xml
409e895924d354ef4ace1330a962ebbf  ./data/metadata/descriptive/dc_ie.xml
5ade81b44c26f1020d1f6fcc8ec0b420  ./data/metadata/descriptive/dc_subie_1.xml
1f263443332dcd49ae428c067d180ebe  ./data/metadata/descriptive/dc_subie_2.xml
eaa2c609ff6371712f623f5531945b44  ./bagit.txt
2ec9403539086d7447dd91361d3c5456  ./manifest-md5.txt
```

## bagit.txt (file)

The `bagit.txt` file contains exactly two lines in the exact order specified in the example below.
The first line specifies to which version of the [BagIt specification](https://www.rfc-editor.org/rfc/rfc8493.html) the bag conforms, while the second line identifies the character set encoding of the bag and its files.

***Requirements***

- The first line of the `bagit.txt` file MUST specify the exact version of the BagIt standard.
- The second line of the `bagit.txt` file MUST specify the character set encoding of the bag and its files.

***Example***

```plaintext
BagIt-Version: 1.0
Tag-File-Character-Encoding: UTF-8
```

## /data (directory)

<mark class="miel">Ga je hier niet te diep? De requirements lijken mij al grotendeels over het package level te gaan, dus ik heb ze naar daar verhuisd.</mark>

The `/data` directory contains the content of the bag divided across a number of different files and directories.
Each `/data` directory MUST contain exactly one package, consisting of the combination of a `mets.xml` file, a `/metadata` directory and a `/representations` directory.
See the [package level](../5_structure_package) for more information and the requirements of the `/data` directory.

***Example***

```plaintext
root_directory
│   ...
│
└──data
   │   mets.xml
   │
   └──metadata
   │      ...
   └──representations
   │      ...
```