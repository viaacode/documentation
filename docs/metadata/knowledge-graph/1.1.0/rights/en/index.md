---
layout: "default"
title: "Data model Rights"
parent: "Knowledge Graph"
nav_order: 1
nav_exclude: False
---
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;"><symbol id="svg-external-link" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title id="svg-external-link-title">(external link)</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line> </symbol></svg>

Data model Rights
====================

**Version:** 1.1.0

**Previous version:** 

**Created:** 2025-09-10

**Last modified:** 2025-09-10

**SHACL file:** [rights.shacl.ttl](rights.shacl.ttl)

**Other languages:**
[nl](../nl)
, [fr](../fr)

**Authors:**


Data model to describe rights and distribution policy.

<div id="zoom" class="table-wrapper">
None
</div>

## Namespaces

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

## Classes & Properties

**Classes:** 
 [//data.hetarchief.be/Motivation>](#%3Chttps%3A//data.hetarchief.be/Motivation%3E) |  [//data.hetarchief.be/UserGroup>](#%3Chttps%3A//data.hetarchief.be/UserGroup%3E) |  [//data.hetarchief.be/MetadataRange>](#%3Chttps%3A//data.hetarchief.be/MetadataRange%3E) |  [//data.hetarchief.be/ContentRange>](#%3Chttps%3A//data.hetarchief.be/ContentRange%3E) |  [Action](#odrl%3AAction) |  [Concept](#skos%3AConcept) |  [Constraint](#odrl%3AConstraint) |  [Digital representation](#haObj%3ADigitalRepresentation) |  [Intellectual entity](#premis%3AIntellectualEntity) |  [License](#premis%3ALicense) |  [Permission](#odrl%3APermission) |  [Policy](#odrl%3APolicy) |  [Prohibition](#odrl%3AProhibition) |  [Rights Statement](#dct%3ARightsStatement) |  [Rights status](#premis%3ARightsStatus) |  [public domain](#copyrightStatus%3Apub)
## <a id="%3Chttps%3A//data.hetarchief.be/Motivation%3E"></a>//data.hetarchief.be/Motivation> <small>[(<https://data.hetarchief.be/Motivation>)](https://data.hetarchief.be/Motivation)</small>





## <a id="%3Chttps%3A//data.hetarchief.be/UserGroup%3E"></a>//data.hetarchief.be/UserGroup> <small>[(<https://data.hetarchief.be/UserGroup>)](https://data.hetarchief.be/UserGroup)</small>





## <a id="%3Chttps%3A//data.hetarchief.be/MetadataRange%3E"></a>//data.hetarchief.be/MetadataRange> <small>[(<https://data.hetarchief.be/MetadataRange>)](https://data.hetarchief.be/MetadataRange)</small>





## <a id="%3Chttps%3A//data.hetarchief.be/ContentRange%3E"></a>//data.hetarchief.be/ContentRange> <small>[(<https://data.hetarchief.be/ContentRange>)](https://data.hetarchief.be/ContentRange)</small>





## <a id="odrl%3AAction"></a>Action <small>[(odrl:Action)](http://www.w3.org/ns/odrl/2/Action)</small>


An operation on an Asset.


## <a id="skos%3AConcept"></a>Concept <small>[(skos:Concept)](http://www.w3.org/2004/02/skos/core#Concept)</small>


**Subclasses:** 
[Local identifier](#haObj%3ALocalIdentifier)
, [Motivation](#%3Chttps%3A//data.hetarchief.be/ns/rights/Motivation%3E)
, [Organization type](#haOrg%3AOrganizationType)
, [Role](#org%3ARole)
, [Role name](#%3Chttps%3A//data.hetarchief.be/ns/description/RoleName%3E)

A SKOS concept can be viewed as an idea or notion; a unit of thought. However, what constitutes a unit of thought is subjective, and this definition is meant to be suggestive, rather than restrictive.


## <a id="odrl%3AConstraint"></a>Constraint <small>[(odrl:Constraint)](http://www.w3.org/ns/odrl/2/Constraint)</small>


A boolean expression that refines the semantics of an Action and Party/Asset Collection or declare the conditions applicable to a Rule.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3AleftOperand'></a>constraint name <br> <small>[(odrl:leftOperand)](http://www.w3.org/ns/odrl/2/leftOperand)</small> | The left operand in a constraint expression. | `1..1` | [`IRI`](https://www.rfc-editor.org/rfc/rfc3987.txt) <br>_Possible values: [`odrl:recipient`](http://www.w3.org/ns/odrl/2/recipient), [`<https://data.hetarchief.be/metadataRange>`](https://data.hetarchief.be/metadataRange), [`<https://data.hetarchief.be/contentRange>`](https://data.hetarchief.be/contentRange), [`odrl:dateTime`](http://www.w3.org/ns/odrl/2/dateTime), [`odrl:absoluteTemporalPosition`](http://www.w3.org/ns/odrl/2/absoluteTemporalPosition)_ |
| <a id='odrl%3ArightOperand'></a>constraint value <br> <small>[(odrl:rightOperand)](http://www.w3.org/ns/odrl/2/rightOperand)</small> | The value of the right operand in a constraint expression. | `1..1` | [//data.hetarchief.be/UserGroup>](#%3Chttps%3A//data.hetarchief.be/UserGroup%3E) _or_ [//data.hetarchief.be/MetadataRange>](#%3Chttps%3A//data.hetarchief.be/MetadataRange%3E) _or_ [//data.hetarchief.be/ContentRange>](#%3Chttps%3A//data.hetarchief.be/ContentRange%3E) <br>_Possible values: [`<https://data.hetarchief.be/extended>`](https://data.hetarchief.be/extended), [`<https://data.hetarchief.be/limited>`](https://data.hetarchief.be/limited), [`<https://data.hetarchief.be/full>`](https://data.hetarchief.be/full), [`<https://data.hetarchief.be/partial>`](https://data.hetarchief.be/partial), [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable), [`<https://data.hetarchief.be/between-partners>`](https://data.hetarchief.be/between-partners), [`<https://data.hetarchief.be/educational-public>`](https://data.hetarchief.be/educational-public), [`<https://data.hetarchief.be/intra-muros>`](https://data.hetarchief.be/intra-muros), [`<https://data.hetarchief.be/public>`](https://data.hetarchief.be/public), [`<https://data.hetarchief.be/research-public>`](https://data.hetarchief.be/research-public)_ |
| <a id='odrl%3Aoperator'></a>operator <br> <small>[(odrl:operator)](http://www.w3.org/ns/odrl/2/operator)</small> | The operator function applied to operands of a Constraint. | `1..1` | [`IRI`](https://www.rfc-editor.org/rfc/rfc3987.txt) <br>_Possible values: [`odrl:eq`](http://www.w3.org/ns/odrl/2/eq), [`odrl:lt`](http://www.w3.org/ns/odrl/2/lt)_ |

## <a id="haObj%3ADigitalRepresentation"></a>Digital representation <small>[(haObj:DigitalRepresentation)](https://data.hetarchief.be/ns/object/DigitalRepresentation)</small>


**Subclass of:** 
[Representation](#premis%3ARepresentation)

**Subclasses:** 
[Fragment representation](#haObj%3AFragmentRepresentation)

Digital representation of an archived intellectual entity.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3AhasPolicy'></a>Target Policy <br> <small>[(odrl:hasPolicy)](http://www.w3.org/ns/odrl/2/hasPolicy)</small> | Identifies an ODRL Policy for which the identified Asset is the target Asset to all the Rules. | `0..1` | [Policy](#odrl%3APolicy)  |
| <a id='dct%3Alicense'></a>condition for reuse <br> <small>[(dct:license)](http://purl.org/dc/terms/license)</small> | A legal document giving official permission to do something with the resource. | `0..1` | [License](#premis%3ALicense)  |
| <a id='premis%3ArightsStatus'></a>rights status <br> <small>[(premis:rightsStatus)](http://www.loc.gov/premis/rdf/v3/rightsStatus)</small> |  | `1..3` | [Rights status](#premis%3ARightsStatus)  |



## <a id="premis%3AIntellectualEntity"></a>Intellectual entity <small>[(premis:IntellectualEntity)](http://www.loc.gov/premis/rdf/v3/IntellectualEntity)</small>


**Subclass of:** 
[Object](#premis%3AObject)

**Subclasses:** 
[Audio](#%3Chttps%3A//data.hetarchief.be/ns/description/Audio%3E)
, [DVD](#%3Chttps%3A//data.hetarchief.be/ns/description/DVD%3E)
, [DVD chapter](#%3Chttps%3A//data.hetarchief.be/ns/description/DVDChapter%3E)
, [Film](#%3Chttps%3A//data.hetarchief.be/ns/description/Film%3E)
, [Image](#%3Chttps%3A//data.hetarchief.be/ns/description/Image%3E)
, [Material artwork](#%3Chttps%3A//data.hetarchief.be/ns/description/MaterialArtwork%3E)
, [Newspaper edition](#%3Chttps%3A//data.hetarchief.be/ns/description/NewspaperIssue%3E)
, [Newspaper issue page](#%3Chttps%3A//data.hetarchief.be/ns/description/NewspaperIssuePage%3E)
, [Video](#%3Chttps%3A//data.hetarchief.be/ns/description/Video%3E)

A set of content that is considered a single intellectual unit for purposes of management and description: for example, a particular book, map, photograph, database, or piece of hardware or software. An Intellectual Entity can include other Intellectual Entities; for example, a web site can include a web page; a web page can include an image. An Intellectual Entity may have one or more digital representations. An Intellectual Entity may also describe an environment, defined as technology supporting a digital object in some way (e.g. by rendering or executing it). Environments can consist of software, hardware, or a combination of both.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='dct%3Alicense'></a>condition for reuse <br> <small>[(dct:license)](http://purl.org/dc/terms/license)</small> | A legal document giving official permission to do something with the resource. | `0..1` | [License](#premis%3ALicense)  |
| <a id='dct%3Arights'></a>rights statement <br> <small>[(dct:rights)](http://purl.org/dc/terms/rights)</small> | Information about rights held in and over the resource. | `1..1` | [Rights Statement](#dct%3ARightsStatement)  |
| <a id='premis%3ArightsStatus'></a>rights status <br> <small>[(premis:rightsStatus)](http://www.loc.gov/premis/rdf/v3/rightsStatus)</small> |  | `1..3` | [Rights status](#premis%3ARightsStatus) _or_ [public domain](#copyrightStatus%3Apub)  |



## <a id="premis%3ALicense"></a>License <small>[(premis:License)](http://www.loc.gov/premis/rdf/v3/License)</small>


**Subclass of:** 
[Rights basis](#premis%3ARightsBasis)

A license agreement or other legal document that grants rights.




## <a id="odrl%3APermission"></a>Permission <small>[(odrl:Permission)](http://www.w3.org/ns/odrl/2/Permission)</small>


**Subclass of:** 
[Rule](#odrl%3ARule)

The ability to perform an Action over an Asset.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3Aaction'></a>None <br> <small>[(odrl:action)](http://www.w3.org/ns/odrl/2/action)</small> |  | `1..*` | [Action](#odrl%3AAction) <br>_Possible values: [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable)_ |
| <a id='odrl%3Aconstraint'></a>constraint <br> <small>[(odrl:constraint)](http://www.w3.org/ns/odrl/2/constraint)</small> | Constraint applied to a Rule. | `0..5` | [Constraint](#odrl%3AConstraint)  |
| <a id='premis%3AendDate'></a>end date <br> <small>[(premis:endDate)](http://www.loc.gov/premis/rdf/v3/endDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='premis%3Anote'></a>note <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> |  | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='premis%3AstartDate'></a>start date <br> <small>[(premis:startDate)](http://www.loc.gov/premis/rdf/v3/startDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |



## <a id="odrl%3APolicy"></a>Policy <small>[(odrl:Policy)](http://www.w3.org/ns/odrl/2/Policy)</small>


A non-empty group of Permissions and/or Prohibitions.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3Atarget'></a>doelrepresentatie <br> <small>[(odrl:target)](http://www.w3.org/ns/odrl/2/target)</small> | The target property indicates the Asset that is the primary subject to which the Rule action directly applies. | `1..*` | [Digital representation](#haObj%3ADigitalRepresentation)  |
| <a id='odrl%3Aprohibition'></a>limitation of access <br> <small>[(odrl:prohibition)](http://www.w3.org/ns/odrl/2/prohibition)</small> | Relates an individual Prohibition to a Policy. | `0..*` | [Prohibition](#odrl%3AProhibition)  |
| <a id='odrl%3Apermission'></a>ontsluitingstoestemming <br> <small>[(odrl:permission)](http://www.w3.org/ns/odrl/2/permission)</small> | Relates an individual Permission to a Policy. | `0..*` | [Permission](#odrl%3APermission)  |
| <a id='odrl%3Atarget'></a>représentation cible <br> <small>[(odrl:target)](http://www.w3.org/ns/odrl/2/target)</small> | The target property indicates the Asset that is the primary subject to which the Rule action directly applies. | `1..*` | [Digital representation](#haObj%3ADigitalRepresentation)  |
| <a id='odrl%3Atarget'></a>target representation <br> <small>[(odrl:target)](http://www.w3.org/ns/odrl/2/target)</small> | The target property indicates the Asset that is the primary subject to which the Rule action directly applies. | `1..*` | [Digital representation](#haObj%3ADigitalRepresentation)  |

## <a id="odrl%3AProhibition"></a>Prohibition <small>[(odrl:Prohibition)](http://www.w3.org/ns/odrl/2/Prohibition)</small>


**Subclass of:** 
[Rule](#odrl%3ARule)

The inability to perform an Action over an Asset.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3Aaction'></a>None <br> <small>[(odrl:action)](http://www.w3.org/ns/odrl/2/action)</small> |  | `1..*` | [Action](#odrl%3AAction) <br>_Possible values: [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable)_ |
| <a id='odrl%3Aconstraint'></a>constraint <br> <small>[(odrl:constraint)](http://www.w3.org/ns/odrl/2/constraint)</small> | Constraint applied to a Rule. | `0..5` | [Constraint](#odrl%3AConstraint)  |
| <a id='premis%3AendDate'></a>end date <br> <small>[(premis:endDate)](http://www.loc.gov/premis/rdf/v3/endDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='%3Chttps%3A//data.hetarchief.be/isMotivatedBy%3E'></a>is motivated by <br> <small>[(<https://data.hetarchief.be/isMotivatedBy>)](https://data.hetarchief.be/isMotivatedBy)</small> |  | `1..*` | [//data.hetarchief.be/Motivation>](#%3Chttps%3A//data.hetarchief.be/Motivation%3E)  |
| <a id='premis%3Anote'></a>note <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> |  | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='premis%3AstartDate'></a>start date <br> <small>[(premis:startDate)](http://www.loc.gov/premis/rdf/v3/startDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |



## <a id="dct%3ARightsStatement"></a>Rights Statement <small>[(dct:RightsStatement)](http://purl.org/dc/terms/RightsStatement)</small>


A statement about the intellectual property rights (IPR) held in or over a resource, a legal document giving official permission to do something with a resource, or a statement about access rights.


## <a id="premis%3ARightsStatus"></a>Rights status <small>[(premis:RightsStatus)](http://www.loc.gov/premis/rdf/v3/RightsStatus)</small>


**Subclasses:** 
[public domain](#copyrightStatus%3Apub)

Information about how a RightsBasis applies to a particular object.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='premis%3AendDate'></a>end date <br> <small>[(premis:endDate)](http://www.loc.gov/premis/rdf/v3/endDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='premis%3Anote'></a>note <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> |  | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='premis%3AstartDate'></a>start date <br> <small>[(premis:startDate)](http://www.loc.gov/premis/rdf/v3/startDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |

## <a id="copyrightStatus%3Apub"></a>public domain <small>[(copyrightStatus:pub)](http://id.loc.gov/vocabulary/preservation/copyrightStatus/pub)</small>


**Subclass of:** 
[Rights status](#premis%3ARightsStatus)

In the public domain and may used without copyright restriction.


_Properties from [Rights status](#premis%3ARightsStatus):_  [end date](#premis%3AendDate),  [note](#premis%3Anote),  [start date](#premis%3AstartDate)

[^1]: Unique language tags required
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
