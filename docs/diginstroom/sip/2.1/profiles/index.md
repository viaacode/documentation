---
layout:       default
title:        Profiles
parent:       2.1
grand_parent:  SIP Specification 
nav_order:    5
nav_exclude:  false
has_children: true
---
Editor's Draft
{: .label .label-yellow }
# SIP content profiles

SIP content profiles define specific configurations of the meemoo SIP specification that are supported by the meemoo ingest pipeline.
They group different types of content that share a similar structure (e.g., there is only one representation or one file) and/or have the same metadata demands (e.g. all of the supplied metadata fits in the DCTERMS vocabulary).

A profile adds extra restrictions or extensions on top of the SIP specification.
Hence, the SIP validation process depends on both.
A delivered SIP MUST indicate which profile it adheres to in the package `METS.xml` through the [`mets/@csip:OTHERCONTENTINFORMATIONTYPE` attribute]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/sip_structure/5_structure_package.md %}#OTHERCONTENTINFORMATIONTYPE). Note that the `csip:CONTENTINFORMATIONTYPE` attribute must always be set to `OTHER`.

<small>
Continue to [Basic profile]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/profiles/basic.md %}).
</small>