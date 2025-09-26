---
layout: "default"
title: "Modèle de données Droits"
parent: "Knowledge Graph"
nav_order: 1
nav_exclude: True
---
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;"><symbol id="svg-external-link" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title id="svg-external-link-title">(external link)</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line> </symbol></svg>

Modèle de données Droits
====================

**Version:** 1.1.0

**Version précédente:** 

**Créé:** 2025-09-10

**Dernière mise à jour:** 2025-09-10

**Fichier SHACL:** [rights.shacl.ttl](rights.shacl.ttl)

**Autres langues:**
[en](../en)
, [nl](../nl)

**Auteurs:**


Modèle de données pour décrire les droits et la politique de distribution.

<div id="zoom" class="table-wrapper">
None
</div>

## Espaces de noms

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

## Classes & Propriétés

**Classes:** 
 [//data.hetarchief.be/Motivation>](#%3Chttps%3A//data.hetarchief.be/Motivation%3E) |  [//data.hetarchief.be/UserGroup>](#%3Chttps%3A//data.hetarchief.be/UserGroup%3E) |  [//data.hetarchief.be/MetadataRange>](#%3Chttps%3A//data.hetarchief.be/MetadataRange%3E) |  [//data.hetarchief.be/ContentRange>](#%3Chttps%3A//data.hetarchief.be/ContentRange%3E) |  [Action](#odrl%3AAction) |  [Autorisation](#odrl%3APermission) |  [Concept](#skos%3AConcept) |  [Contrainte](#odrl%3AConstraint) |  [Déclaration des droits](#dct%3ARightsStatement) |  [Entité intellectuelle](#premis%3AIntellectualEntity) |  [Interdiction](#odrl%3AProhibition) |  [Licence](#premis%3ALicense) |  [Politique](#odrl%3APolicy) |  [Représentation digitale](#haObj%3ADigitalRepresentation) |  [Statut de droits](#premis%3ARightsStatus) |  [domaine public](#copyrightStatus%3Apub)
## <a id="%3Chttps%3A//data.hetarchief.be/Motivation%3E"></a>//data.hetarchief.be/Motivation> <small>[(<https://data.hetarchief.be/Motivation>)](https://data.hetarchief.be/Motivation)</small>





## <a id="%3Chttps%3A//data.hetarchief.be/UserGroup%3E"></a>//data.hetarchief.be/UserGroup> <small>[(<https://data.hetarchief.be/UserGroup>)](https://data.hetarchief.be/UserGroup)</small>





## <a id="%3Chttps%3A//data.hetarchief.be/MetadataRange%3E"></a>//data.hetarchief.be/MetadataRange> <small>[(<https://data.hetarchief.be/MetadataRange>)](https://data.hetarchief.be/MetadataRange)</small>





## <a id="%3Chttps%3A//data.hetarchief.be/ContentRange%3E"></a>//data.hetarchief.be/ContentRange> <small>[(<https://data.hetarchief.be/ContentRange>)](https://data.hetarchief.be/ContentRange)</small>





## <a id="odrl%3AAction"></a>Action <small>[(odrl:Action)](http://www.w3.org/ns/odrl/2/Action)</small>


Une opération effectuée sur une ressource.


## <a id="odrl%3APermission"></a>Autorisation <small>[(odrl:Permission)](http://www.w3.org/ns/odrl/2/Permission)</small>


**Sous-classe de:** 
[Règle](#odrl%3ARule)

La capacité d’exécuter une action sur une ressource.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3Aaction'></a>None <br> <small>[(odrl:action)](http://www.w3.org/ns/odrl/2/action)</small> |  | `1..*` | [Action](#odrl%3AAction) <br>_Valeurs possibles: [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable)_ |
| <a id='odrl%3Aconstraint'></a>contrainte <br> <small>[(odrl:constraint)](http://www.w3.org/ns/odrl/2/constraint)</small> | Contrainte appliquée à une règle. | `0..5` | [Contrainte](#odrl%3AConstraint)  |
| <a id='premis%3AstartDate'></a>date de début <br> <small>[(premis:startDate)](http://www.loc.gov/premis/rdf/v3/startDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='premis%3AendDate'></a>fin <br> <small>[(premis:endDate)](http://www.loc.gov/premis/rdf/v3/endDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='premis%3Anote'></a>note <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> |  | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |



## <a id="skos%3AConcept"></a>Concept <small>[(skos:Concept)](http://www.w3.org/2004/02/skos/core#Concept)</small>


**Sous-classes:** 
[Identifiant local](#haObj%3ALocalIdentifier)
, [Motivation](#%3Chttps%3A//data.hetarchief.be/ns/rights/Motivation%3E)
, [Nom de rôle](#%3Chttps%3A//data.hetarchief.be/ns/description/RoleName%3E)
, [Rôle](#org%3ARole)
, [Type de organisation](#haOrg%3AOrganizationType)

Un concept SKOS peut être considéré comme une idée ou une notion, une unité de pensée. Cependant, ce qui constitue une unité de pensée est subjectif, et cette définition se veut suggestive, plutôt que restrictive.


## <a id="odrl%3AConstraint"></a>Contrainte <small>[(odrl:Constraint)](http://www.w3.org/ns/odrl/2/Constraint)</small>


Une expression booléenne qui affine la signification d’une action et d’un ensemble de parties/ressources ou qui déclare les conditions applicables à une règle.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3AleftOperand'></a>nom de la contrainte <br> <small>[(odrl:leftOperand)](http://www.w3.org/ns/odrl/2/leftOperand)</small> | L’opérande gauche dans une expression de contrainte. | `1..1` | [`IRI`](https://www.rfc-editor.org/rfc/rfc3987.txt) <br>_Valeurs possibles: [`odrl:recipient`](http://www.w3.org/ns/odrl/2/recipient), [`<https://data.hetarchief.be/metadataRange>`](https://data.hetarchief.be/metadataRange), [`<https://data.hetarchief.be/contentRange>`](https://data.hetarchief.be/contentRange), [`odrl:dateTime`](http://www.w3.org/ns/odrl/2/dateTime), [`odrl:absoluteTemporalPosition`](http://www.w3.org/ns/odrl/2/absoluteTemporalPosition)_ |
| <a id='odrl%3Aoperator'></a>opérateur <br> <small>[(odrl:operator)](http://www.w3.org/ns/odrl/2/operator)</small> | La fonction opérateur appliquée aux opérandes d’une contrainte. | `1..1` | [`IRI`](https://www.rfc-editor.org/rfc/rfc3987.txt) <br>_Valeurs possibles: [`odrl:eq`](http://www.w3.org/ns/odrl/2/eq), [`odrl:lt`](http://www.w3.org/ns/odrl/2/lt)_ |
| <a id='odrl%3ArightOperand'></a>valeur de contrainte <br> <small>[(odrl:rightOperand)](http://www.w3.org/ns/odrl/2/rightOperand)</small> | La valeur de l’opérande droit dans une expression de contrainte. | `1..1` | [//data.hetarchief.be/UserGroup>](#%3Chttps%3A//data.hetarchief.be/UserGroup%3E) _ou_ [//data.hetarchief.be/MetadataRange>](#%3Chttps%3A//data.hetarchief.be/MetadataRange%3E) _ou_ [//data.hetarchief.be/ContentRange>](#%3Chttps%3A//data.hetarchief.be/ContentRange%3E) <br>_Valeurs possibles: [`<https://data.hetarchief.be/extended>`](https://data.hetarchief.be/extended), [`<https://data.hetarchief.be/limited>`](https://data.hetarchief.be/limited), [`<https://data.hetarchief.be/full>`](https://data.hetarchief.be/full), [`<https://data.hetarchief.be/partial>`](https://data.hetarchief.be/partial), [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable), [`<https://data.hetarchief.be/between-partners>`](https://data.hetarchief.be/between-partners), [`<https://data.hetarchief.be/educational-public>`](https://data.hetarchief.be/educational-public), [`<https://data.hetarchief.be/intra-muros>`](https://data.hetarchief.be/intra-muros), [`<https://data.hetarchief.be/public>`](https://data.hetarchief.be/public), [`<https://data.hetarchief.be/research-public>`](https://data.hetarchief.be/research-public)_ |

## <a id="dct%3ARightsStatement"></a>Déclaration des droits <small>[(dct:RightsStatement)](http://purl.org/dc/terms/RightsStatement)</small>


Une déclaration sur les droits de propriété intellectuelle (DPI) a été maintenue dans ou au-dessus d'une ressource, un document légal donnant l'autorisation officielle de faire quelque chose avec une ressource ou une déclaration sur les droits d'accès.


## <a id="premis%3AIntellectualEntity"></a>Entité intellectuelle <small>[(premis:IntellectualEntity)](http://www.loc.gov/premis/rdf/v3/IntellectualEntity)</small>


**Sous-classe de:** 
[Objet](#premis%3AObject)

**Sous-classes:** 
[Audio](#%3Chttps%3A//data.hetarchief.be/ns/description/Audio%3E)
, [Chapitre DVD](#%3Chttps%3A//data.hetarchief.be/ns/description/DVDChapter%3E)
, [DVD](#%3Chttps%3A//data.hetarchief.be/ns/description/DVD%3E)
, [Edition de journal](#%3Chttps%3A//data.hetarchief.be/ns/description/NewspaperIssue%3E)
, [Film](#%3Chttps%3A//data.hetarchief.be/ns/description/Film%3E)
, [Image](#%3Chttps%3A//data.hetarchief.be/ns/description/Image%3E)
, [Page d'édition de journal](#%3Chttps%3A//data.hetarchief.be/ns/description/NewspaperIssuePage%3E)
, [Vidéo](#%3Chttps%3A//data.hetarchief.be/ns/description/Video%3E)
, [Œuvres d'art matérielles](#%3Chttps%3A//data.hetarchief.be/ns/description/MaterialArtwork%3E)

Ensemble de contenu qui est considéré comme une unité intellectuelle pour des objectifs de gestion et de description.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='dct%3Alicense'></a>condition de réutilisation <br> <small>[(dct:license)](http://purl.org/dc/terms/license)</small> | Un document juridique permettant à l'autorisation officielle de faire quelque chose avec la ressource. | `0..1` | [Licence](#premis%3ALicense)  |
| <a id='dct%3Arights'></a>déclaration des droits <br> <small>[(dct:rights)](http://purl.org/dc/terms/rights)</small> | Informations sur les droits maintenus dans et au-dessus de la ressource. | `1..1` | [Déclaration des droits](#dct%3ARightsStatement)  |
| <a id='premis%3ArightsStatus'></a>statut de droit <br> <small>[(premis:rightsStatus)](http://www.loc.gov/premis/rdf/v3/rightsStatus)</small> |  | `1..3` | [Statut de droits](#premis%3ARightsStatus) _ou_ [domaine public](#copyrightStatus%3Apub)  |



## <a id="odrl%3AProhibition"></a>Interdiction <small>[(odrl:Prohibition)](http://www.w3.org/ns/odrl/2/Prohibition)</small>


**Sous-classe de:** 
[Règle](#odrl%3ARule)

L’impossibilité d’exécuter une action sur une ressource.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3Aaction'></a>None <br> <small>[(odrl:action)](http://www.w3.org/ns/odrl/2/action)</small> |  | `1..*` | [Action](#odrl%3AAction) <br>_Valeurs possibles: [`<https://data.hetarchief.be/available-for-consultation>`](https://data.hetarchief.be/available-for-consultation), [`<https://data.hetarchief.be/downloadable>`](https://data.hetarchief.be/downloadable)_ |
| <a id='odrl%3Aconstraint'></a>contrainte <br> <small>[(odrl:constraint)](http://www.w3.org/ns/odrl/2/constraint)</small> | Contrainte appliquée à une règle. | `0..5` | [Contrainte](#odrl%3AConstraint)  |
| <a id='premis%3AstartDate'></a>date de début <br> <small>[(premis:startDate)](http://www.loc.gov/premis/rdf/v3/startDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='%3Chttps%3A//data.hetarchief.be/isMotivatedBy%3E'></a>est motivé par <br> <small>[(<https://data.hetarchief.be/isMotivatedBy>)](https://data.hetarchief.be/isMotivatedBy)</small> |  | `1..*` | [//data.hetarchief.be/Motivation>](#%3Chttps%3A//data.hetarchief.be/Motivation%3E)  |
| <a id='premis%3AendDate'></a>fin <br> <small>[(premis:endDate)](http://www.loc.gov/premis/rdf/v3/endDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='premis%3Anote'></a>note <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> |  | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |



## <a id="premis%3ALicense"></a>Licence <small>[(premis:License)](http://www.loc.gov/premis/rdf/v3/License)</small>


**Sous-classe de:** 
[Base des droits](#premis%3ARightsBasis)

Un accord de licence ou un autre document juridique qui accorde les droits.




## <a id="odrl%3APolicy"></a>Politique <small>[(odrl:Policy)](http://www.w3.org/ns/odrl/2/Policy)</small>


Un groupe non vide d’autorisations et/ou d’interdictions.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3Atarget'></a>Cible <br> <small>[(odrl:target)](http://www.w3.org/ns/odrl/2/target)</small> | La propriété cible indique la ressource à laquelle l’action de la règle s’applique directement. | `1..*` | [Représentation digitale](#haObj%3ADigitalRepresentation)  |
| <a id='odrl%3Apermission'></a>autorisation d'accès <br> <small>[(odrl:permission)](http://www.w3.org/ns/odrl/2/permission)</small> | Relie une autorisation individuelle à une politique. | `0..*` | [Autorisation](#odrl%3APermission)  |
| <a id='odrl%3Aprohibition'></a>limitation de l'accès <br> <small>[(odrl:prohibition)](http://www.w3.org/ns/odrl/2/prohibition)</small> | Relie une interdiction individuelle à une politique. | `0..*` | [Interdiction](#odrl%3AProhibition)  |

## <a id="haObj%3ADigitalRepresentation"></a>Représentation digitale <small>[(haObj:DigitalRepresentation)](https://data.hetarchief.be/ns/object/DigitalRepresentation)</small>


**Sous-classe de:** 
[Représentation](#premis%3ARepresentation)

**Sous-classes:** 
[Représentation fragment](#haObj%3AFragmentRepresentation)

Représentation digitale d'une entité intellectuelle (Intellectual Entity) archivée.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='odrl%3AhasPolicy'></a>Politique cible <br> <small>[(odrl:hasPolicy)](http://www.w3.org/ns/odrl/2/hasPolicy)</small> | Identifie une politique ODRL pour laquelle la ressource identifiée est la ressource cible de toutes les règles. | `0..1` | [Politique](#odrl%3APolicy)  |
| <a id='dct%3Alicense'></a>condition de réutilisation <br> <small>[(dct:license)](http://purl.org/dc/terms/license)</small> | Un document juridique permettant à l'autorisation officielle de faire quelque chose avec la ressource. | `0..1` | [Licence](#premis%3ALicense)  |
| <a id='premis%3ArightsStatus'></a>statut de droit <br> <small>[(premis:rightsStatus)](http://www.loc.gov/premis/rdf/v3/rightsStatus)</small> |  | `1..3` | [Statut de droits](#premis%3ARightsStatus)  |



## <a id="premis%3ARightsStatus"></a>Statut de droits <small>[(premis:RightsStatus)](http://www.loc.gov/premis/rdf/v3/RightsStatus)</small>


**Sous-classes:** 
[domaine public](#copyrightStatus%3Apub)

Informations sur la façon dont une base de droits s'applique à un objet particulier.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='premis%3AstartDate'></a>date de début <br> <small>[(premis:startDate)](http://www.loc.gov/premis/rdf/v3/startDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='premis%3AendDate'></a>fin <br> <small>[(premis:endDate)](http://www.loc.gov/premis/rdf/v3/endDate)</small> |  | `0..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='premis%3Anote'></a>note <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> |  | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |

## <a id="copyrightStatus%3Apub"></a>domaine public <small>[(copyrightStatus:pub)](http://id.loc.gov/vocabulary/preservation/copyrightStatus/pub)</small>


**Sous-classe de:** 
[Statut de droits](#premis%3ARightsStatus)

Dans le domaine public et peut être utilisé sans restriction du droit d'auteur.


_Propriétés de [Statut de droits](#premis%3ARightsStatus):_  [date de début](#premis%3AstartDate),  [fin](#premis%3AendDate),  [note](#premis%3Anote)

[^1]: Étiquettes de langue uniques requises
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
