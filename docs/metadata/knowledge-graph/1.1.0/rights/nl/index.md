---
layout: "default"
title: "Datamodel Rechten"
parent: "Knowledge Graph"
nav_order: 1
nav_exclude: True
---
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;"><symbol id="svg-external-link" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title id="svg-external-link-title">(external link)</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line> </symbol></svg>

Datamodel Rechten
====================

**Versie:** 1.1.0

**Vorige versie:** 

**Aangemaakt op:** 2025-09-10

**Laatst gewijzigd op:** 2025-09-10

**SHACL-bestand:** [rights.shacl.ttl](rights.shacl.ttl)

**Andere talen:**
[en](../en)
, [fr](../fr)

**Auteurs:**


Datamodel om rechten en distributiebeleid te beschrijven.

<div id="zoom" class="table-wrapper">
None
</div>

## Naamruimten

| Prefix | URI      |
| :----- | :------- |
| copyrightStatus     | [http://id.loc.gov/vocabulary/preservation/copyrightStatus/](http://id.loc.gov/vocabulary/preservation/copyrightStatus/) |
| dct     | [http://purl.org/dc/terms/](http://purl.org/dc/terms/) |
| edtf     | [http://id.loc.gov/datatypes/edtf/](http://id.loc.gov/datatypes/edtf/) |
| foaf     | [http://xmlns.com/foaf/0.1/](http://xmlns.com/foaf/0.1/) |
| haObj     | [https://data.hetarchief.be/ns/object/](https://data.hetarchief.be/ns/object/) |
| haOrg     | [https://data.hetarchief.be/ns/organization/](https://data.hetarchief.be/ns/organization/) |
| odrl     | [http://www.w3.org/ns/odrl/2/](http://www.w3.org/ns/odrl/2/) |
| org     | [http://www.w3.org/ns/org#](http://www.w3.org/ns/org#) |
| owl     | [http://www.w3.org/2002/07/owl#](http://www.w3.org/2002/07/owl#) |
| pav     | [http://purl.org/pav/](http://purl.org/pav/) |
| premis     | [http://www.loc.gov/premis/rdf/v3/](http://www.loc.gov/premis/rdf/v3/) |
| rdf     | [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#) |
| rdfs     | [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#) |
| schema     | [https://schema.org/](https://schema.org/) |
| sh     | [http://www.w3.org/ns/shacl#](http://www.w3.org/ns/shacl#) |
| skos     | [http://www.w3.org/2004/02/skos/core#](http://www.w3.org/2004/02/skos/core#) |
| vann     | [http://purl.org/vocab/vann/](http://purl.org/vocab/vann/) |
| xsd     | [http://www.w3.org/2001/XMLSchema#](http://www.w3.org/2001/XMLSchema#) |

## Klassen & Eigenschappen

**Klassen:** 
 [//data.hetarchief.be/Motivation>](#%3Chttps%3A//data.hetarchief.be/Motivation%3E) |  [//data.hetarchief.be/UserGroup>](#%3Chttps%3A//data.hetarchief.be/UserGroup%3E) |  [//data.hetarchief.be/MetadataRange>](#%3Chttps%3A//data.hetarchief.be/MetadataRange%3E) |  [//data.hetarchief.be/ContentRange>](#%3Chttps%3A//data.hetarchief.be/ContentRange%3E) |  [Actie](#odrl%3AAction) |  [Beleid](#odrl%3APolicy) |  [Beperking](#odrl%3AConstraint) |  [Concept](#skos%3AConcept) |  [Digitale representatie](#haObj%3ADigitalRepresentation) |  [Intellectuele entiteit](#premis%3AIntellectualEntity) |  [Licentie](#premis%3ALicense) |  [Rechtenstatus](#premis%3ARightsStatus) |  [Rechtenverklaring](#dct%3ARightsStatement) |  [Toestemming](#odrl%3APermission) |  [Verbod](#odrl%3AProhibition) |  [publiek domein](#copyrightStatus%3Apub)
## <a id="%3Chttps%3A//data.hetarchief.be/Motivation%3E"></a>//data.hetarchief.be/Motivation> <small>[(<https://data.hetarchief.be/Motivation>)](https://data.hetarchief.be/Motivation)</small>





## <a id="%3Chttps%3A//data.hetarchief.be/UserGroup%3E"></a>//data.hetarchief.be/UserGroup> <small>[(<https://data.hetarchief.be/UserGroup>)](https://data.hetarchief.be/UserGroup)</small>





## <a id="%3Chttps%3A//data.hetarchief.be/MetadataRange%3E"></a>//data.hetarchief.be/MetadataRange> <small>[(<https://data.hetarchief.be/MetadataRange>)](https://data.hetarchief.be/MetadataRange)</small>





## <a id="%3Chttps%3A//data.hetarchief.be/ContentRange%3E"></a>//data.hetarchief.be/ContentRange> <small>[(<https://data.hetarchief.be/ContentRange>)](https://data.hetarchief.be/ContentRange)</small>





## <a id="odrl%3AAction"></a>Actie <small>[(odrl:Action)](http://www.w3.org/ns/odrl/2/Action)</small>


Een handeling uitgevoerd op een middel.


## <a id="odrl%3APolicy"></a>Beleid <small>[(odrl:Policy)](http://www.w3.org/ns/odrl/2/Policy)</small>


Een niet-lege groep toestemmingen en/of verboden.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3Atarget'></a>Doel <br> <small>[(odrl:target)](http://www.w3.org/ns/odrl/2/target)</small> | De doel-eigenschap geeft het middel aan waarop de regelactie rechtstreeks van toepassing is. | `1..*` | [Digitale representatie](#haObj%3ADigitalRepresentation)  |
| <a id='odrl%3Apermission'></a>access permission <br> <small>[(odrl:permission)](http://www.w3.org/ns/odrl/2/permission)</small> | Verbindt een individuele toestemming aan een beleid. | `0..*` | [Toestemming](#odrl%3APermission)  |
| <a id='odrl%3Aprohibition'></a>ontsluitingsbeperking <br> <small>[(odrl:prohibition)](http://www.w3.org/ns/odrl/2/prohibition)</small> | Verbindt een individueel verbod aan een beleid. | `0..*` | [Verbod](#odrl%3AProhibition)  |

## <a id="odrl%3AConstraint"></a>Beperking <small>[(odrl:Constraint)](http://www.w3.org/ns/odrl/2/Constraint)</small>


Een booleaanse uitdrukking die de betekenis van een actie en partij-/middelenverzameling verfijnt of de voorwaarden bepaalt die op een regel van toepassing zijn.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3AleftOperand'></a>beperkingsnaam <br> <small>[(odrl:leftOperand)](http://www.w3.org/ns/odrl/2/leftOperand)</small> | De linkeroperand in een beperkingsuitdrukking. | `1..1` | [`IRI`](https://www.rfc-editor.org/rfc/rfc3987.txt) <br>_Mogelijke waarden: [`odrl:recipient`](http://www.w3.org/ns/odrl/2/recipient), [`<https://data.hetarchief.be/metadataRange>`](https://data.hetarchief.be/metadataRange), [`<https://data.hetarchief.be/contentRange>`](https://data.hetarchief.be/contentRange), [`odrl:dateTime`](http://www.w3.org/ns/odrl/2/dateTime), [`odrl:absoluteTemporalPosition`](http://www.w3.org/ns/odrl/2/absoluteTemporalPosition)_ |
| <a id='odrl%3ArightOperand'></a>beperkingswaarde <br> <small>[(odrl:rightOperand)](http://www.w3.org/ns/odrl/2/rightOperand)</small> | De waarde van de rechteroperand in een beperkingsuitdrukking. | `1..1` | [//data.hetarchief.be/UserGroup>](#%3Chttps%3A//data.hetarchief.be/UserGroup%3E) _of_ [//data.hetarchief.be/MetadataRange>](#%3Chttps%3A//data.hetarchief.be/MetadataRange%3E) _of_ [//data.hetarchief.be/ContentRange>](#%3Chttps%3A//data.hetarchief.be/ContentRange%3E) <br>_Mogelijke waarden: [`<https://data.hetarchief.be/extended>`](https://data.hetarchief.be/extended), [`<https://data.hetarchief.be/limited>`](https://data.hetarchief.be/limited), [`<https://data.hetarchief.be/full>`](https://data.hetarchief.be/full), [`<https://data.hetarchief.be/partial>`](https://data.hetarchief.be/partial), [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable), [`<https://data.hetarchief.be/between-partners>`](https://data.hetarchief.be/between-partners), [`<https://data.hetarchief.be/educational-public>`](https://data.hetarchief.be/educational-public), [`<https://data.hetarchief.be/intra-muros>`](https://data.hetarchief.be/intra-muros), [`<https://data.hetarchief.be/public>`](https://data.hetarchief.be/public), [`<https://data.hetarchief.be/research-public>`](https://data.hetarchief.be/research-public)_ |
| <a id='odrl%3Aoperator'></a>operator <br> <small>[(odrl:operator)](http://www.w3.org/ns/odrl/2/operator)</small> | De operatorfunctie toegepast op de operanden van een beperking. | `1..1` | [`IRI`](https://www.rfc-editor.org/rfc/rfc3987.txt) <br>_Mogelijke waarden: [`odrl:eq`](http://www.w3.org/ns/odrl/2/eq), [`odrl:lt`](http://www.w3.org/ns/odrl/2/lt)_ |

## <a id="skos%3AConcept"></a>Concept <small>[(skos:Concept)](http://www.w3.org/2004/02/skos/core#Concept)</small>


**Subklassen:** 
[Lokale identificatie](#haObj%3ALocalIdentifier)
, [Motivatie](#%3Chttps%3A//data.hetarchief.be/ns/rights/Motivation%3E)
, [Organisatietype](#haOrg%3AOrganizationType)
, [Rol](#org%3ARole)
, [Rolnaam](#%3Chttps%3A//data.hetarchief.be/ns/description/RoleName%3E)

Een SKOS-concept kan als idee of begrip worden gezien; een gedachte-eenheid. Echter, wat  een gedachte-eenheid is, is subjectief, en deze definitie is eerder suggestief dan beperkend bedoeld.


## <a id="haObj%3ADigitalRepresentation"></a>Digitale representatie <small>[(haObj:DigitalRepresentation)](https://data.hetarchief.be/ns/object/DigitalRepresentation)</small>


**Subklasse van:** 
[Representatie](#premis%3ARepresentation)

**Subklassen:** 
[Fragment representatie](#haObj%3AFragmentRepresentation)

Digitale representatie van een gearchiveerde intellectuele entiteit (Intellectual Entity).

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3AhasPolicy'></a>Doelbeleid <br> <small>[(odrl:hasPolicy)](http://www.w3.org/ns/odrl/2/hasPolicy)</small> | Identificeert een ODRL-beleid waarvoor het middel het doelmiddel is van alle regels. | `0..1` | [Beleid](#odrl%3APolicy)  |
| <a id='dct%3Alicense'></a>hergebruikvoorwaarde <br> <small>[(dct:license)](http://purl.org/dc/terms/license)</small> | Een juridisch document dat officiële toestemming geeft om iets met de entiteit te doen. | `0..1` | [Licentie](#premis%3ALicense)  |
| <a id='premis%3ArightsStatus'></a>rechtenstatus <br> <small>[(premis:rightsStatus)](http://www.loc.gov/premis/rdf/v3/rightsStatus)</small> |  | `1..3` | [Rechtenstatus](#premis%3ARightsStatus)  |



## <a id="premis%3AIntellectualEntity"></a>Intellectuele entiteit <small>[(premis:IntellectualEntity)](http://www.loc.gov/premis/rdf/v3/IntellectualEntity)</small>


**Subklasse van:** 
[Object](#premis%3AObject)

**Subklassen:** 
[Afbeelding](#%3Chttps%3A//data.hetarchief.be/ns/description/Image%3E)
, [Audio](#%3Chttps%3A//data.hetarchief.be/ns/description/Audio%3E)
, [Dvd](#%3Chttps%3A//data.hetarchief.be/ns/description/DVD%3E)
, [Dvd-hoofdstuk](#%3Chttps%3A//data.hetarchief.be/ns/description/DVDChapter%3E)
, [Film](#%3Chttps%3A//data.hetarchief.be/ns/description/Film%3E)
, [Kranteneditie](#%3Chttps%3A//data.hetarchief.be/ns/description/NewspaperIssue%3E)
, [Kranteneditiepagina](#%3Chttps%3A//data.hetarchief.be/ns/description/NewspaperIssuePage%3E)
, [Materieel kunstwerk](#%3Chttps%3A//data.hetarchief.be/ns/description/MaterialArtwork%3E)
, [Video](#%3Chttps%3A//data.hetarchief.be/ns/description/Video%3E)

Set van inhoud die beschouwd wordt als één enkele intellectuele eenheid met als doeleinden beheer en beschrijving.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='dct%3Alicense'></a>hergebruikvoorwaarde <br> <small>[(dct:license)](http://purl.org/dc/terms/license)</small> | Een juridisch document dat officiële toestemming geeft om iets met de entiteit te doen. | `0..1` | [Licentie](#premis%3ALicense)  |
| <a id='premis%3ArightsStatus'></a>rechtenstatus <br> <small>[(premis:rightsStatus)](http://www.loc.gov/premis/rdf/v3/rightsStatus)</small> |  | `1..3` | [Rechtenstatus](#premis%3ARightsStatus) _of_ [publiek domein](#copyrightStatus%3Apub)  |
| <a id='dct%3Arights'></a>rechtenverklaring <br> <small>[(dct:rights)](http://purl.org/dc/terms/rights)</small> | Informatie over rechten in en over de bron. | `1..1` | [Rechtenverklaring](#dct%3ARightsStatement)  |



## <a id="premis%3ALicense"></a>Licentie <small>[(premis:License)](http://www.loc.gov/premis/rdf/v3/License)</small>


**Subklasse van:** 
[Rechtenbasis](#premis%3ARightsBasis)

Een licentieovereenkomst of ander juridisch document dat rechten verleent.




## <a id="premis%3ARightsStatus"></a>Rechtenstatus <small>[(premis:RightsStatus)](http://www.loc.gov/premis/rdf/v3/RightsStatus)</small>


**Subklassen:** 
[publiek domein](#copyrightStatus%3Apub)

Informatie over hoe een rechtenbasis van toepassing is op een bepaald object.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='premis%3AendDate'></a>einddatum <br> <small>[(premis:endDate)](http://www.loc.gov/premis/rdf/v3/endDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='premis%3Anote'></a>notitie <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> |  | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='premis%3AstartDate'></a>startdatum <br> <small>[(premis:startDate)](http://www.loc.gov/premis/rdf/v3/startDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |

## <a id="dct%3ARightsStatement"></a>Rechtenverklaring <small>[(dct:RightsStatement)](http://purl.org/dc/terms/RightsStatement)</small>


Een verklaring over de intellectuele eigendomsrechten (IPR) van toepassing op of over een entiteit, een juridisch document dat officiële toestemming geeft om iets te doen met een entiteit, of een verklaring over toegangsrechten.


## <a id="odrl%3APermission"></a>Toestemming <small>[(odrl:Permission)](http://www.w3.org/ns/odrl/2/Permission)</small>


**Subklasse van:** 
[Regel](#odrl%3ARule)

De mogelijkheid om een actie uit te voeren op een middel.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3Aaction'></a>access action <br> <small>[(odrl:action)](http://www.w3.org/ns/odrl/2/action)</small> |  | `1..*` | [Actie](#odrl%3AAction) <br>_Mogelijke waarden: [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable)_ |
| <a id='odrl%3Aaction'></a>action d'accès <br> <small>[(odrl:action)](http://www.w3.org/ns/odrl/2/action)</small> |  | `1..*` | [Actie](#odrl%3AAction) <br>_Mogelijke waarden: [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable)_ |
| <a id='odrl%3Aconstraint'></a>beperking <br> <small>[(odrl:constraint)](http://www.w3.org/ns/odrl/2/constraint)</small> | Beperking toegepast op een regel. | `0..5` | [Beperking](#odrl%3AConstraint)  |
| <a id='premis%3AendDate'></a>einddatum <br> <small>[(premis:endDate)](http://www.loc.gov/premis/rdf/v3/endDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='premis%3Anote'></a>notitie <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> |  | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='odrl%3Aaction'></a>ontsluitingsactie <br> <small>[(odrl:action)](http://www.w3.org/ns/odrl/2/action)</small> |  | `1..*` | [Actie](#odrl%3AAction) <br>_Mogelijke waarden: [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable)_ |
| <a id='premis%3AstartDate'></a>startdatum <br> <small>[(premis:startDate)](http://www.loc.gov/premis/rdf/v3/startDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |



## <a id="odrl%3AProhibition"></a>Verbod <small>[(odrl:Prohibition)](http://www.w3.org/ns/odrl/2/Prohibition)</small>


**Subklasse van:** 
[Regel](#odrl%3ARule)

De onmogelijkheid om een actie uit te voeren op een middel.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3Aaction'></a>access action <br> <small>[(odrl:action)](http://www.w3.org/ns/odrl/2/action)</small> |  | `1..*` | [Actie](#odrl%3AAction) <br>_Mogelijke waarden: [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable)_ |
| <a id='odrl%3Aaction'></a>action d'accès <br> <small>[(odrl:action)](http://www.w3.org/ns/odrl/2/action)</small> |  | `1..*` | [Actie](#odrl%3AAction) <br>_Mogelijke waarden: [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable)_ |
| <a id='odrl%3Aconstraint'></a>beperking <br> <small>[(odrl:constraint)](http://www.w3.org/ns/odrl/2/constraint)</small> | Beperking toegepast op een regel. | `0..5` | [Beperking](#odrl%3AConstraint)  |
| <a id='premis%3AendDate'></a>einddatum <br> <small>[(premis:endDate)](http://www.loc.gov/premis/rdf/v3/endDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='premis%3Anote'></a>notitie <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> |  | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='odrl%3Aaction'></a>ontsluitingsactie <br> <small>[(odrl:action)](http://www.w3.org/ns/odrl/2/action)</small> |  | `1..*` | [Actie](#odrl%3AAction) <br>_Mogelijke waarden: [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable)_ |
| <a id='premis%3AstartDate'></a>startdatum <br> <small>[(premis:startDate)](http://www.loc.gov/premis/rdf/v3/startDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='%3Chttps%3A//data.hetarchief.be/isMotivatedBy%3E'></a>wordt gemotiveerd door <br> <small>[(<https://data.hetarchief.be/isMotivatedBy>)](https://data.hetarchief.be/isMotivatedBy)</small> |  | `1..*` | [//data.hetarchief.be/Motivation>](#%3Chttps%3A//data.hetarchief.be/Motivation%3E)  |



## <a id="copyrightStatus%3Apub"></a>publiek domein <small>[(copyrightStatus:pub)](http://id.loc.gov/vocabulary/preservation/copyrightStatus/pub)</small>


**Subklasse van:** 
[Rechtenstatus](#premis%3ARightsStatus)

In het publieke domein en kan zonder auteursrechtbeperking worden gebruikt.


_Eigenschappen van [Rechtenstatus](#premis%3ARightsStatus):_  [einddatum](#premis%3AendDate),  [notitie](#premis%3Anote),  [startdatum](#premis%3AstartDate)

[^1]: Unieke taallabels vereist
<style>
#zoom {
  height: 60vh;
  padding: 5px;
}

#zoom > svg {
    width: 100%;
    height: 100%;
}

.svg-external-link {
  width: 16px;
  height: 16px;
}
</style>

<script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.5.0/dist/svg-pan-zoom.min.js"></script>
<script>
window.onload = (event) => {
  svgPanZoom('#zoom > svg', {controlIconsEnabled: true})
};
</script>
