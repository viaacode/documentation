---
title: Digital intake
nav_order: 1
---

# Digital intake

This page provides meemoo's content partners (CPs) with more insight into how metadata is structured in meemoo's MAM and how it must consequently be supplied for digital intake.

## Existing intake

CPs that have born digital or digitized material must supply metadata about this essence. This is done in the form of a sidecar XML file for each essence, e.g. test.xml + test.mxf. Meemoo's ingest process expects metadata that has already been mapped to meemoo's metadata model, as explained below. If you have any questions and/or comments, we would be happy to hear them via support@meemoo.be!

You can validate your mapped metadata using our XSD [`viaa_metadatamodel_xsd.xsd`](https://github.com/viaacode/documentation/blob/7bbe0323731bc180f0b5855b47245935ab8704c4/assets/legacy_born_digital/viaa_metadatamodel_van_cp_naar_viaa.xsd). A simple way to do this is with xmllint (part of [libxml](http://xmlsoft.org/)). Open a terminal and run the following command:

```bash
xmllint --noout --schema viaa_metadatamodel_voor_cp.xsd viaa_metadatamodel_voorbeeld_voor_cp.xml
```

See [`viaa_metadatamodel_voorbeeld_voor_cp.xml`](https://github.com/viaacode/documentation/blob/7bbe0323731bc180f0b5855b47245935ab8704c4/assets/legacy_born_digital/viaa_metadatamodel_voorbeeld_van_cp_naar_viaa.xml) for an example of a fully filled-in metadata file.


## Intake via meemoo SIP

Currently, meemoo is working on a uniform meemoo SIP for future projects. Read everything about the specification [here](sip/index.md).

These SIPs are supplied to meemoo via S3. You can read more about how this works in [Supplying SIPs](aanlevering-van-sips.md).

## Metadata model

See fields: [General](../metadata/viaa/algemeen.md) | [Digitization](../metadata/viaa/digitalisering.md)
