# OAI-PMH

## OAI-PMH Overview

OAI-PMH is a standardized protocol that operates on the basis of 'Providers' and 'Harvesters'. A provider is an application that makes metadata available to third-party applications. A harvester is a user of this metadata. OAI-PMH enables users to:

* Provide metadata of items or collections on the web (as 'provider')
* Consume metadata (as 'harvester')

The meemoo archive behaves as a data **provider** and can thus make your archived collections available in whole or in part via this standard. For use cases, refer to [the integration page](https://portaal.meemoo.be/nl/portaal/support-category/item/hoe-bouw-ik-een-integratie-met-meemoo) on our website.

OAI-PMH is a standardized protocol. The meemoo implementation complies with version 2 of this standard. For the technical documentation, refer to the documentation of the standard itself: [https://www.openarchives.org/OAI/openarchivesprotocol.html](https://www.openarchives.org/OAI/openarchivesprotocol.html).

## Authentication

The meemoo OAI-PMH implementation is not publicly available: only users who have the right to view certain items or collections will be able to do so via OAI-PMH. The user's rights determine the visibility via OAI-PMH.

Authentication currently only occurs via OAuth 2.0, as with the REST API v2. You will first need to register the application. Instructions can be found [here](https://developer.meemoo.be/docs/integratie/).

### Users

Every user of the meemoo archive also has access to the OAI-PMH API. This can be handy for quick testing, but for specific applications, we strongly recommend creating a dedicated account. You can request such an account by contacting [support@meemoo.be](mailto:support@meemoo.be). You only need to provide a valid email address so the password for this user can be set.

### Rights

By default, all items that are part of your meemoo archive and published will be available via OAI-PMH. If only part of the records are needed in the harvesting application, there are two options:

* The harvesting application itself filters the items.
* An OAI user is created that only provides a part of your material.

For the first option, no further configuration is needed: the harvesting application decides which items should be shown and which not. For the second option, a specific account with limited rights must be created, and items must be assigned to this account.

For assistance and advice regarding this configuration, you can always contact [support@meemoo.be](mailto:support@meemoo.be).

## Endpoint and Verbs

The meemoo OAI-PMH endpoint is available at: [https://archief.meemoo.be/mediahaven-oai/oai](https://archief-meemoo.be/mediahaven-oai/oai)

Implemented verbs include:

* **```Identify```** - Displays information about the meemoo archive.
  * Example: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=Identify](https://archief-meemoo.be/mediahaven-oai/oai?verb=Identify)"
* **```ListMetadataFormats```** - Lists the supported metadata formats.
  * Example: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=ListMetadataFormats](https://archief-meemoo.be/mediahaven-oai/oai?verb=ListMetadataFormats)"
  * Meemoo currently supports the following metadata formats:
    * oai_dc - Provides only descriptive metadata and the header.
    * mediahaven - Provides the main technical and content metadata, and links to browse copies.
    * mets - Provides all metadata as in mediahaven, including PREMIS metadata and links to browse copies.
* **```ListIdentifiers```** - Lists all identifiers in the archive. Only the headers of the records are given.
  * Example: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=ListIdentifiers&metadataPrefix=mets](https://archief-meemoo.be/mediahaven-oai/oai?verb=ListIdentifiers&metadataPrefix=mets)"
* **```ListRecords```** - Lists all records in the archive. Alongside the header, all metadata is provided.
  * Example: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=oai_dc](https://archief-meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=oai_dc)"
* **```ListSets```** - Lists all defined sets.
  * Example: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=ListSets](https://archief-meemoo.be/mediahaven-oai/oai?verb=ListSets)"
* **```GetRecord```** - Retrieves all metadata for a specific record. The record ID and metadata format must be specified. The meemoo identifier ("noid:7940r9mw4c") is the unique identifier of the record.
  * Example: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=noid:7940r9mw4c](https://archief-meemoo.be/mediahaven-oai/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=noid:7940r9mw4c)"

## Use Case

### General

In this paragraph, a use case is described where items stored in the meemoo archive need to be shown on an external platform, such as the website of a content partner. The metadata and essence (audio, video, or photo) are stored locally on the external platform's CMS.

If the metadata in the archive is updated, or new items are added to the collection, they must also be shown on the external website.

For this use case, we assume:

1. The items to be disclosed belong to a specific collection.
2. There is a user and password available with access to this collection.

The use case is worked out in the following steps:

1. To achieve an initial synchronization, all records are retrieved using ```ListRecords```. The records contain both metadata and links to browse copies that can be used to display audio, video, or photo or to download them.

2. Once this synchronization is complete, updated records are requested periodically via OAI-PMH. In this example, we assume updates occur every 24 hours. During the update, both newly added items are harvested and updates to existing items are harvested.

## Step 1: Initial Synchronization

### ListRecords

In this step, all records are retrieved. We choose to retrieve all metadata records in METS format:

**REQUEST:**

``` shell
https://archief.meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=mets
```

* We use ```listRecords```, which retrieves a list of all metadata records from the archive.
* As metadata schema, we use ```mets```, which immediately provides all metadata, including links to audio/video or photo files.

**RESPONSE:** The response contains several records, of which we show the first few:

``` xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
    <responseDate>2018-01-12T13:52:04Z</responseDate>
    <request metadataPrefix="mets" verb="ListRecords">https://archief.viaa.be/mediahaven-oai/oai</request>
    <ListRecords>
        <record>
            <header>
                <identifier>umid:aa7e5487751b441acad0a1a9cb212d390660082e630d4f543755f5dd164a0a8e308ddb84c28fc7f034c6</identifier>
                <datestamp>2017-07-16T16:26:14Z</datestamp>
                <setSpec>cp_name</setSpec>
            </header>
            <metadata>
                <mets:mets xmlns:mets="http://www.loc.gov/METS/" xmlns:premis="info:lc/xmlns/premis-v2" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd info:lc/xmlns/premis-v2 http://www.loc.gov/standards/premis/premis.xsd">
                    <mets:metsHdr CREATEDATE="2017-07-16T16:17:35Z" ID="MEDIAHAVEN" LASTMODDATE="2014-07-16T16:26:14Z">
                        <mets:agent ROLE="CREATOR" TYPE="ORGANIZATION">
                            <mets:name>MEDIAHAVEN</mets:name>
                        </mets:agent>
                        <mets:agent ROLE="CUSTODIAN" TYPE="ORGANIZATION">
                            <mets:name>viaa</mets:name>
                        </mets:agent>
                        <mets:agent ROLE="IPOWNER" TYPE="ORGANIZATION">
                            <mets:name>tvbxl</mets:name>
                        </mets:agent>
                    </mets:metsHdr>
                    <mets:dmdSec ID="METADATA">
                        <mets:mdWrap MDTYPE="OTHER" OTHERMDTYPE="MediaHAVEN_external_metadata">
                            <mets:xmlData>
                                <MediaHAVEN_external_metadata>
                                    <title>8938w0w54.mxf.xml</title>
                                    <description/>
                                    <OriginalFilename>8938w0w54.mxf.xml</OriginalFilename>
                                    <Administrative>
                                        <OrganisationName>tvbxl</OrganisationName>
                                        <LastModifiedDate>2014-07-16T16:26:14Z</LastModifiedDate>
                                        <ArchiveDate>2014:07:16 18:17:35</ArchiveDate>
                                        <UploadedBy>BulkUpload tvbxl</UploadedBy>
                                        <Type>document</Type>
                                        <DepartmentName>cp_name</DepartmentName>
                                    </Administrative>
                                    <Technical>
                                        <OriginalFilename>8938w0w54.mxf.xml</OriginalFilename>
                                        <FileSize>7488</FileSize>
                                        <Md5>a9dc62020c2f638a3c07aa4289462a88</Md5>
                                        <MimeType>application/xml</MimeType>
                                        <DurationTimeCode>00:00:00.000</DurationTimeCode>
                                        <StartTimeCode>00:00:00.000</StartTimeCode>
                                        <EndTimeCode>00:00:00.000</EndTimeCode>
                                        <FragmentDurationTimeCode>00:00:00.000</FragmentDurationTimeCode>
                                        <FragmentStartTimeCode>00:00:00.000</FragmentStartTimeCode>
                                        <FragmentEndTimeCode>00:00:00.000</FragmentEndTimeCode>
                                        <FragmentDurationFrames>0</FragmentDurationFrames>
                                        <FragmentStartFrames>0</FragmentStartFrames>
                                        <FragmentEndFrames>0</FragmentEndFrames>
                                    </Technical>
                                    <Internal>
                                        <MediaObjectId>cbe630d4afa8e308ddb84c971212d3906b60082a7e5487751b441acad0a1a9c5</MediaObjectId>
                                        <FragmentId>cbe630d4afa8e308ddb84c971212d3906b60082a7e5487751b441acad0a1a9c5cbe630d4afa8e308ddb84c971212d3906b60082a7e5487751b441acad0a1a9c5</FragmentId>
                                        <TransferStatus>1016</TransferStatus>
                                        <ArchiveStatus>on_tape</ArchiveStatus>
                                        <OrganisationId>123</OrganisationId>
                                        <IngestSpaceId>-51d6-bf44-41db-aa126fe7-b085a4464c22</IngestSpaceId>
                                        <IsInIngestSpace>0</IsInIngestSpace>
                                        <DepartmentId></DepartmentId>
                                        <IsFragment>0</IsFragment>
                                        <HasKeyframes>0</HasKeyframes>
                                        <ContainsGeoData>0</ContainsGeoData>
                                        <PathToKeyframe>http://server.net/viaa/no-preview.png</PathToKeyframe>
                                        <PathToKeyframeThumb>http://server.net/viaa/no-preview.png</PathToKeyframeThumb>
                                        <Browses>
                                            <Browse>
                                                <PathToKeyframe>http://server.net.viaa.be/viaa/no-preview.png</PathToKeyframe>
                                                <PathToKeyframeThumb>http://server.net.viaa.be/viaa/no-preview.png</PathToKeyframeThumb>
                                            </Browse>
                                        </Browses>
                                    </Internal>
                                    <MDProperties>
                                        <CreationDate>2014:07:16 14:35:23+02:00</CreationDate>
                                        <rights_owner>© Copyright cp_name</rights_owner>
                                    </MDProperties>
                                </MediaHAVEN_external_metadata>
                            </mets:xmlData>
                        </mets:mdWrap>
                    </mets:dmdSec>
                    <mets:amdSec ID="PREMIS">
                        <mets:digiprovMD ID="MEDIAHAVEN_EVENT-54322396">
                            <mets:mdWrap MDTYPE="PREMIS:EVENT">
                                <mets:xmlData>
                                    <premis:event>
                                        <premis:eventIdentifier>
                                            <premis:eventIdentifierType>MEDIAHAVEN_EVENT</premis:eventIdentifierType>
                                            <premis:eventIdentifierValue>54322396</premis:eventIdentifierValue>
                                        </premis:eventIdentifier>
                                        <premis:eventType>UPDATE</premis:eventType>
                                        <premis:eventDateTime>2017-07-06 08:30:56.066243</premis:eventDateTime>
                                        <premis:eventDetail/>
                                        <premis:eventOutcomeInformation>
                                            <premis:eventOutcome>OK</premis:eventOutcome>
                                        </premis:eventOutcomeInformation>
                                        <premis:linkingAgentIdentifier>
                                            <premis:linkingAgentIdentifierType>MEDIAHAVEN_USER</premis:linkingAgentIdentifierType>
                                            <premis:linkingAgentIdentifierValue>cp_name</premis:linkingAgentIdentifierValue>
                                        </premis:linkingAgentIdentifier>
                                        <premis:linkingObjectIdentifier>
                                            <premis:linkingObjectIdentifierType>MEDIAHAVEN_ID</premis:linkingObjectIdentifierType>
                                            <premis:linkingObjectIdentifierValue>a7e5487751b441acad0a1a9cb212d3906b60082e630d4afa8e308ddb84c971c543755f5dd164a0f7e1b6028fc7f034c6</premis:linkingObjectIdentifierValue>
                                        </premis:linkingObjectIdentifier>
                                    </premis:event>
                                </mets:xmlData>
                            </mets:mdWrap>
                        </mets:digiprovMD>
                        <mets:digiprovMD ID="MEDIAHAVEN_EVENT-54321572">
                            <mets:mdWrap MDTYPE="PREMIS:EVENT">
                                <mets:xmlData>
                                    <premis:event>
                                        <premis:eventIdentifier>
                                            <premis:eventIdentifierType>MEDIAHAVEN_EVENT</premis:eventIdentifierType>
                                            <premis:eventIdentifierValue>54321572</premis:eventIdentifierValue>
                                        </premis:eventIdentifier>
                                        <premis:eventType>PUBLISH</premis:eventType>
                                        <premis:eventDateTime>2017-07-06 08:15:34.59108</premis:eventDateTime>
                                        <premis:eventDetail/>
                                        <premis:eventOutcomeInformation>
                                            <premis:eventOutcome>OK</premis:eventOutcome>
                                        </premis:eventOutcomeInformation>
                                        <premis:linkingAgentIdentifier>
                                            <premis:linkingAgentIdentifierType>MEDIAHAVEN_USER</premis:linkingAgentIdentifierType>
                                            <premis:linkingAgentIdentifierValue>cp_name</premis:linkingAgentIdentifierValue>
                                        </premis:linkingAgentIdentifier>
                                        <premis:linkingObjectIdentifier>
                                            <premis:linkingObjectIdentifierType>MEDIAHAVEN_ID</premis:linkingObjectIdentifierType>
                                            <premis:linkingObjectIdentifierValue>a7e5487751b441acad0a1a9cb212d3906b60082e630d4afa8e308ddb84c971c543755f5dd164a0f7e1b6028fc7f034c6</premis:linkingObjectIdentifierValue>
                                        </premis:linkingObjectIdentifier>
                                    </premis:event>
                                </mets:xmlData>
                            </mets:mdWrap>
                        </mets:digiprovMD>
                    </mets:amdSec>
                    <mets:fileSec>
                        <mets:fileGrp>
                            <mets:file CHECKSUM="a300283c0c2f6a9daa4c62728948862a" CHECKSUMTYPE="MD5" CREATED="2014-07-16T16:17:35Z" ID="umid-a7e5487751b441acad0a1a9cb212d3906b60082e630d4afa8e308ddb84c971c5" MIMETYPE="application/xml" USE="PRESERVATION">
                                <mets:FLocat LOCTYPE="URL" xlink:href="http://server.net/path/file.xml"/>
                            </mets:file>
                            <mets:file ID="umid-browse" MIMETYPE="image/png" USE="ACCESS">
                                <mets:FLocat LOCTYPE="URL" xlink:href="http://server.net/path/file.xml"/>
                            </mets:file>
                        </mets:fileGrp>
                    </mets:fileSec>
                </mets:mets>
            </metadata>
        </record>
```

(!) Note that the response will include all files the user has rights to access. This means not only audio, video, or photo will be returned but also (if present) XML files containing quality control reports, subtitles, etc. Filtering in the call is not possible, so the harvesting application must implement the filtering. This can be done based on the type field (e.g., by ignoring documents).

A response is paginated and defaults to returning 25 records per request. If additional records are available, the following will be indicated at the bottom of the response:

* A ```resumptionToken``` is provided, which must be included in the next request to retrieve the next page.
* The ```completeListSize``` attribute indicates the total number of records.
* The ```cursor``` attribute indicates the number of records already retrieved.

In this example, the next request should look like this. The response will contain records 26 to 49:

``` shell
https://archief.meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=mets&resumptionToken=UMDA6MDA6MDBaLCB1bnRpbD0yMTAwLTEyLTMwVDIzOjU5OjU5WiwgdG9rZW5TdGFydD0yNX0=
```

To loop through the entire list until the ```resumptionToken``` is empty, the harvesting application must perform this pagination. In this example, we have retrieved 200 records (8 pages), and there are 7 records left on the last page.

``` xml
<resumptionToken completeListSize="207" cursor="200"></resumptionToken>
```

### Storing Retrieved Data

It is up to the harvesting application to process the response and store the metadata and/or links to browse copies in the target database, such as the CMS or DMS of the external website.

## Step 2: Periodic Updates

### 'Selective Harvesting'

To perform periodic updates, you can use ```from``` and ```until``` date fields as additional query parameters. Suppose you want to retrieve all records added or modified since January 1, 2018, at 10:00:00, you would use this request:

**REQUEST:**

``` shell
https://archief.meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=mets&from=2018-01-01T10:00:00Z
```

The response format will be identical to that in Step 1 but will typically contain fewer records. Only records added or modified since the specified date will be returned. Pagination is also handled via a ```resumptionToken``` if the complete list contains more than 25 records.

To keep your data up-to-date, this type of request should be executed at scheduled intervals, with the ```from``` datestamp being the date of the last periodic update.

To retrieve data for a specific day only, you can add an ```until``` parameter, for example:

**REQUEST:**

``` shell
https://archief.meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=mets&from=2018-01-01T00:00:00Z&until=2019-01-01T00:00:00Z
```

## Advanced Concepts

### Use of Sets

The meemoo implementation supports sets. Currently, sets are defined at the level of content providers.

### Handling Deleted Items

Currently, there is limited support for deleted items. Records that have been removed from the meemoo archive will not be visible through ```ListIdentifiers``` and ```ListRecords```. A ```GetRecord``` request will return an error indicating that the record has been deleted.

Organizations that delete items in the archive and want to ensure their harvested data remains in sync can compare the list of IDs obtained via a ```ListIdentifiers``` request with the list of IDs in their own database.

In the future, if there is sufficient demand from content partners, support for deleted records can be increased to persistent or transient. [See: http://www.openarchives.org/OAI/2.0/openarchivesprotocol.htm#DeletedRecords](http://www.openarchives.org/OAI/2.0/openarchivesprotocol.htm#DeletedRecords)

Contact [support@meemoo.be](mailto:support@meemoo.be) if you are interested in this feature.
