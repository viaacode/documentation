---
layout: default
title: OAI-PMH
parent: Een integratie ontwikkelen
has_children: false
has_toc: true
nav_order: 2
last_modified_date: 2020-10-08 12:30:00 +0200
---

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Over OAI-PMH

OAI-PMH is een gestandaardiseerd protocol dat werkt op basis van 'Providers' en 'Harvesters'. Een provider is een applicatie die metadata ter beschikking stelt aan derde applicaties. Een harvester is een gebruiker van deze metadata. OAI-PMH stelt de gebruikers in staat om:

* De metadata van items of collecties aan te bieden op het web (als 'provider')
* De metadata te verbruiken (als 'harvester')

Het meemoo-archief gedraagt zich als data **provider** en kan dus jouw gearchiveerde collecties geheel of gedeeltelijk ter beschikking stellen via deze standaard. Voor use cases verwijzen we door naar [de integratie pagina](https://portaal.meemoo.be/nl/portaal/support-category/item/hoe-bouw-ik-een-integratie-met-meemoo) op onze website.

OAI-PMH is een gestandaardiseerd protocol. De meemoo-implementatie voldoet aan versie 2 van deze standaard. Voor de technische documentatie verwijzen we dan ook naar de documentatie van de standaard zelf: [https://www.openarchives.org/OAI/openarchivesprotocol.html](https://www.openarchives.org/OAI/openarchivesprotocol.html).

In dit document worden de voor meemoo specifieke implementatiedetails besproken zoals authenticatie, het gebruik van sets en de afhandeling van files die verwijderd werden in het meemoo-archief. Verder wordt op deze pagina een typisch scenario uitgewerkt aan de hand van het meemoo-archief.

## Authenticatie

De meemoo-implementatie van OAI-PMH is niet publiek beschikbaar: enkel gebruikers die het recht hebben om bepaalde items of collecties te zien, zullen die ook kunnen raadplegen via OAI-PMH. De rechten van de gebruiker bepalen de zichtbaarheid via OAI-PMH.

Net zoals bij de REST API v2 verloopt de authenticatie tegenwoordig enkel via OAuth 2.0. Je zal dus eerst de applicatie moeten registeren. Hoe je dit doet vind je [hier](https://developer.meemoo.be/docs/integratie/) terug.

### Gebruikers

Elke gebruiker van het meemoo-archief heeft meteen ook toegang tot de OAI-PMH API. Dit kan handig zijn om snel zaken te testen, maar voor specifieke applicaties raden we sterk aan een gebruiker te laten aanmaken voor dit doel. Het aanmaken van een dergelijk account gebeurt op eenvoudige vraag bij [support@meemoo.be](mailto:support@meemoo.be). Je hoeft enkel een geldig e-mailadres te voorzien, zodat het wachtwoord van deze gebruiker ingesteld kan worden.

### Rechten

Standaard zullen alle items die zich in jouw meemoo-archief bevinden en die gepubliceerd zijn, beschikbaar zijn via OAI-PMH. Indien slechts een deel van de records nodig zijn in de harvestende applicatie, zijn er twee opties:

* De harvestende applicatie staat zelf in voor de filtering
* Er wordt een OAI-gebruiker aangemaakt die maar een deel van jouw materiaal ter beschikking stelt.

Voor de eerste optie is geen verdere configuratie nodig: de harvestende applicatie beslist zelf welke items getoond moeten worden en welke niet. Voor de tweede optie moet een specifiek account aangemaakt worden met beperkte rechten en moeten items aan dit account toegekend worden.

Voor hulp en advies omtrent deze configuratie kan je steeds terecht bij [support@meemoo.be](mailto:support@meemoo.be).

## Endpoint en verbs

Het meemoo OAI-PMH endpoint is hier terug te vinden: [https://archief.meemoo.be/mediahaven-oai/oai](https://archief.meemoo.be/mediahaven-oai/oai)

Volgende verbs zijn geïmplementeerd:

* **```Identify```** geeft informatie over het meemoo-archief weer
    * Voorbeeld: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=Identify](https://archief-qas.meemoo.be/mediahaven-oai/oai?verb=Identify)”
* **```ListMetadataFormats```** geeft een lijst van de ondersteunde metadataformaten.
    * Voorbeeld: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=ListMetadataFormats](https://archief-qas.meemoo.be/mediahaven-oai/oai?verb=ListMetadataFormats)"
    * Meemoo ondersteunt momenteel de volgende metadataformaten:
        * oai_dc: geeft enkel de beschrijvende metadata en de header.
        * mediahaven: geeft de belangrijkste technische en inhoudelijke metadata, en links naar de browsekopies.
        * mets: geeft alle metadata als in mediahaven, inclusief de PREMIS-metadata en links naar de browsekopies.
* **```ListIdentifiers```** geeft een lijst van alle identifiers in het archief. Enkel de headers van de records worden gegeven.
    * Voorbeeld: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=ListIdentifiers&metadataPrefix=mets](https://archief.meemoo.be/mediahaven-oai/oai?verb=ListIdentifiers&metadataPrefix=mets)"
* **```ListRecords```** geeft een lijst van alle records in het archief. Naast de header wordt hier ook alle metadata meegegeven.
    * Voorbeeld: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=oai_dc](https://archief.meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=oai_dc)"
* **```ListSets```** geeft een lijst van alle gedefinieerde sets.
    * Voorbeeld: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=ListSets](https://archief.meemoo.be/mediahaven-oai/oai?verb=ListSets)"
* **```GetRecord```** geeft alle metadata voor één specifieke record. De ID van het record en het metadataformat moeten meegegeven worden. De meemoo identifier ("noid:7940r9mw4c") is hier de unieke identifier van het record.
    * Voorbeeld: "[https://archief.meemoo.be/mediahaven-oai/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=noid:7940r9mw4c](https://archief.meemoo.be/mediahaven-oai/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=noid:7940r9mw4c)"

# Use case

## Algemeen

In deze paragraaf wordt een use case omschreven waarbij items die in het meemoo-archief opgeslagen zijn getoond moeten worden op een extern platform, bvb. de website van een content partner. De metadata en essence (audio, video of foto) worden hierbij lokaal opgeslagen, bijvoorbeeld in het CMS van het extern platform.

Indien de metadata in het archief geüpdatet wordt, of indien nieuwe items aan de collectie toegevoegd worden, moeten ze ook getoond worden op de externe website.

Voor deze use case gaan we ervan uit dat:

1. de items die we willen ontsluiten tot een bepaalde collectie behoren
2. er een user en paswoord beschikbaar is met toegang tot deze collectie

De use case wordt uitgewerkt in de volgende stappen:

1.  Om een initiële synchronisatie te realiseren wordt aan de hand van listrecords alle records opgehaald. De records bevatten zowel metadata als links naar de browse kopies die gebruikt kunnen worden om audio, video of foto weer te geven of te downloaden.

2.  Eens deze synchronisatie gelopen heeft worden via OAI-PMH periodiek de geüpdatete records opgevraagd. In dit voorbeeld gaan we ervan uit dat dit elke 24u gebeurt. Tijdens de update worden zowel nieuw toegevoegde items ‘geharvest’ als updates van reeds bestaande items.

## Stap 1: Initiële synchronisatie

### ListRecords

In deze stap worden alle records opgehaald. We kiezen ervoor om alle metadata van de records op te halen in mets formaat:

**REQUEST:**

``` shell
https://archief.meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=mets
```

* we gebruiken ```listRecords```, waarmee we een lijst van alle metadata records opvragen uit het archief.
* als metadataschema gebruiken we ```mets```, wat meteen alle metadata weergeeft, inclusief links naar de audio/foto of video bestanden.

**RESPONSE:** De response bevat een aantal records, waarvan we hier de eerste tonen:

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

(!) Let op dat de response alle bestanden zal weergeven waar de user recht op heeft. Dat betekent dat niet alleen audio, foto of video zal teruggegeven worden maar ook (indien aanwezig) xml bestanden met rapporten omtrent kwaliteitscontrole, ondertitels, etc. Filteren in de call is niet mogelijk, dus de harvestende applicatie moet instaan voor de filtering. Dat kan op basis van het veld type (bvb. door documenten te negeren worden alle

Een response is gepagineerd en geeft per default 25 records terug per request. Indien extra records beschikbaar zijn wordt dit aangegeven onderaan de response:

* Er wordt onderin de XML response een ```resumptionToken``` meegegeven. Om de volgende pagina op te halen, moet dit token aan de volgende request worden meegegeven.
* Het ```completeListSize``` attribuut geeft het totaal aantal records aan.
* Het ```cursor``` attribuut geeft het aantal reeds teruggegeven records weer.

In dit voorbeeld zal de volgende request er dus als volgt uit moeten zien. De response hierop zal records 25 t.e.m. 49 bevatten:

``` shell
https://archief.meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=mets&resumptionToken=UMDA6MDA6MDBaLCB1bnRpbD0yMTAwLTEyLTMwVDIzOjU5OjU5WiwgdG9rZW5TdGFydD0yNX0=
```

Op deze manier kan de volledige lijst overlopen worden tot de ```resumptionToken``` leeg is. Dat wil zeggen dat je op de laatste pagina bent. In onderstaand voorbeeld zijn we aangekomen op de laatste pagina van in totaal 9 pagina's. We hebben reeds 200 reocrds opgehaald (8*25), de laatste pagina bevat dus nog 7 records.

``` xml
<resumptionToken completeListSize="207" cursor="200"></resumptionToken>
```

### De opgehaalde gegevens bewaren

Het is aan de harvestende applicatie om de response te verwerken en voor elke ```record``` in de XML de metadata en/of de link naar de browsekopies op te slaan in de doeldatabase, bv. het CMS of DMS van de externe website.

## Stap 2: Periodieke updates

### 'Selective harvesting'

Om periodieke updates te realiseren kan gewerkt worden met ```from``` en ```until``` datumvelden als bijkomende query parameter. Stel dat je bijvoorbeeld alle records wil opvragen die sinds 1 januari 2018 om 10:00:00 toegevoegd of aangepast werden, dan gebruik je deze request:

**REQUEST:**

``` shell
https://archief.meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=mets&from=2018-01-01T10:00:00Z
```

Het formaat van de response zal identiek zijn aan deze uit stap 1 maar zal typisch minder records bevatten. Namelijk enkel de records die sinds de opgegeven datum toegevoegd of gewijzigd zijn. Ook hier wordt overigens gewerkt met paginering via een resumptionToken in het geval de complete lijst meer dan 25 records bevat.

Om de eigen data up-to-date te houden wordt dit type request best op gezette tijdstippen uitgevoerd, waarbij de from datestamp de datum van de laatste periodieke update is.

Wil je enkel de data van 1 bepaalde dag ophalen dan kan dat door ook een ```until``` parameter mee te sturen, bijvoorbeeld:

**REQUEST:**

``` shell
https://archief.meemoo.be/mediahaven-oai/oai?verb=ListRecords&metadataPrefix=mets&from=2018-01-01T00:00:00Z&until=2019-01-01T00:00:00Z
```

# Geavanceerde concepten

## Gebruik van sets

De meemoo-implementatie ondersteunt sets. Op dit moment worden sets gedefinieerd op het niveau van content providers.

## Omgaan met verwijderde items

Op dit moment is er beperkte support voor verwijderde items. Records die uit het meemoo-archief verwijderd werden, zullen niet meer zichtbaar zijn met de verbs ListIdentifiers en ListRecords. Een GetRecord-request zal een foutmelding opleveren waaruit afgeleid kan worden dat het record gedeletet werd.

Organisaties die records deleten in het archiefsysteem en willen controleren of hun geharveste data nog "in sync" is, kunnen bijvoorbeeld alle items id's opvragen aan de hand van een ```ListIdentifiers``` request en de lijst in de response vergelijken met de lijst van id's in de eigen database.

In de toekomst en indien er voldoende vraag is vanuit de CP's kan het delete-support verhoogd worden naar persistent of transient. [Zie: http://www.openarchives.org/OAI/2.0/openarchivesprotocol.htm#DeletedRecords](http://www.openarchives.org/OAI/2.0/openarchivesprotocol.htm#DeletedRecords)

Contacteer [support@meemoo.be](mailto:support@meemoo.be) indien je hier vragende partij voor bent.
