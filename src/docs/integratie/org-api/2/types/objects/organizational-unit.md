# OrganizationalUnit



A unit of an organization.


```graphql
type OrganizationalUnit implements IOrganization {
  iri: ID!
  id: String!
  label: String
  alt_label: String
  mam_label: String
  slug: String
  homepage: String
  description: String
  logo: Logo
  overlay: Boolean
  bzt: Boolean
  iiif: Boolean
  form_url: String
  sector: String
  account_manager: Person
  classification: Concept
  units: [OrganizationalUnit]
  contact_point: [ContactPoint]
  primary_site: Site
  sites: [Site]
  posts: [Post]
  unit_of: IOrganization!
}
```


### Fields

#### [`OrganizationalUnit.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ID!`](../scalars/id.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the unit.


#### [`OrganizationalUnit.id`](#id)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String!`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#id} 
The persistent identifier of the unit.


#### [`OrganizationalUnit.label`](#label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#label} 
The label of the unit.


#### [`OrganizationalUnit.alt_label`](#alt-label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#alt-label} 
The alternative label of the unit.


#### [`OrganizationalUnit.mam_label`](#mam-label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#mam-label} 
The tenant name of the unit in the meemoo MAM.


#### [`OrganizationalUnit.slug`](#slug)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#slug} 
A slugified version of the label to create in an URL.


#### [`OrganizationalUnit.homepage`](#homepage)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#homepage} 
The website of the unit.


#### [`OrganizationalUnit.description`](#description)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#description} 
The description of the unit (in Dutch).


#### [`OrganizationalUnit.logo`](#logo)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Logo`](./logo.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#logo} 
The logo of the unit.


#### [`OrganizationalUnit.overlay`](#overlay)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#overlay} 
A flag indicating whether the unit allows media overlays.


#### [`OrganizationalUnit.bzt`](#bzt)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#bzt} 
A flag indicating whether the unit allows content to be included in meemoo's Bezoekertool.


#### [`OrganizationalUnit.iiif`](#iiif)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iiif} 
A flag indicating whether the organization allows content to be included in meemoo's IIIF service.


#### [`OrganizationalUnit.form_url`](#form-url)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#form-url} 
The URL to a request content from the unit.


#### [`OrganizationalUnit.sector`](#sector)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#sector} 
The sector the unit in active in.


#### [`OrganizationalUnit.account_manager`](#account-manager)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Person`](./person.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#account-manager} 
The account manager at meemoo responsible for this unit.


#### [`OrganizationalUnit.classification`](#classification)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Concept`](./concept.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#classification} 
The unit type.


#### [`OrganizationalUnit.units`](#units)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[OrganizationalUnit]`](./organizational-unit.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#units} 
The units belonging to this unit.


#### [`OrganizationalUnit.contact_point`](#contact-point)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[ContactPoint]`](./contact-point.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#contact-point} 
The points of contact in this organizaton.


#### [`OrganizationalUnit.primary_site`](#primary-site)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Site`](./site.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#primary-site} 
The primary physical site of the unit.


#### [`OrganizationalUnit.sites`](#sites)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Site]`](./site.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#sites} 
The physical sites of the unit.


#### [`OrganizationalUnit.posts`](#posts)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Post]`](./post.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#posts} 
The known jobpositions at the unit, eg. technical manager, project manager, accountant etc.


#### [`OrganizationalUnit.unit_of`](#unit-of)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`IOrganization!`](../interfaces/iorganization.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">interface</mark> {#unit-of} 
The unit that this unit is part of.




### Interfaces

#### [`IOrganization`](../interfaces/iorganization.md) <mark class="gqlmd-mkdocs-badge">interface</mark> 
Interface for all organizations.




### Member Of

[`ContentPartner`](./content-partner.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`IOrganization`](../interfaces/iorganization.md)  <mark class="gqlmd-mkdocs-badge">interface</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Organization`](./organization.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`OrganizationalUnit`](./organizational-unit.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`School`](./school.md)  <mark class="gqlmd-mkdocs-badge">object</mark>