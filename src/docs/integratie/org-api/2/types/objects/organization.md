# Organization



A generic organization.


```graphql
type Organization implements IOrganization {
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
  category: String
}
```


### Fields

#### [`Organization.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ID!`](../scalars/id.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the organization.


#### [`Organization.id`](#id)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String!`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#id} 
The persistent identifier of the organization.


#### [`Organization.label`](#label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#label} 
The label of the organization.


#### [`Organization.alt_label`](#alt-label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#alt-label} 
The alternative label of the organization.


#### [`Organization.mam_label`](#mam-label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#mam-label} 
The tenant name of the organization in the meemoo MAM.


#### [`Organization.slug`](#slug)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#slug} 
A slugified version of the label to create in an URL.


#### [`Organization.homepage`](#homepage)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#homepage} 
The website of the organization.


#### [`Organization.description`](#description)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#description} 
The description of the organization (in Dutch).


#### [`Organization.logo`](#logo)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Logo`](./logo.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#logo} 
The logo of the organization.


#### [`Organization.overlay`](#overlay)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#overlay} 
A flag indicating whether the organization allows media overlays.


#### [`Organization.bzt`](#bzt)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#bzt} 
A flag indicating whether the organization allows content to be included in meemoo's Bezoekertool.


#### [`Organization.iiif`](#iiif)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iiif} 
A flag indicating whether the organization allows content to be included in meemoo's IIIF service.


#### [`Organization.form_url`](#form-url)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#form-url} 
The URL to a request content from the organization.


#### [`Organization.sector`](#sector)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#sector} 
The sector the organization in active in.


#### [`Organization.account_manager`](#account-manager)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Person`](./person.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#account-manager} 
The account manager at meemoo responsible for this organization.


#### [`Organization.classification`](#classification)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Concept`](./concept.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#classification} 
The organization type.


#### [`Organization.units`](#units)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[OrganizationalUnit]`](./organizational-unit.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#units} 
The units belonging to this organization.


#### [`Organization.contact_point`](#contact-point)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[ContactPoint]`](./contact-point.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#contact-point} 
The points of contact in this organizaton.


#### [`Organization.primary_site`](#primary-site)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Site`](./site.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#primary-site} 
The primary physical site of the organization.


#### [`Organization.sites`](#sites)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Site]`](./site.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#sites} 
The physical sites of the organization.


#### [`Organization.posts`](#posts)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Post]`](./post.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#posts} 
The known jobpositions at the organization, eg. technical manager, project manager, accountant etc.


#### [`Organization.category`](#category)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#category} 
The meemoo category of the organization.




### Interfaces

#### [`IOrganization`](../interfaces/iorganization.md) <mark class="gqlmd-mkdocs-badge">interface</mark> 
Interface for all organizations.




### Returned By

[`organizations`](../../operations/queries/organizations.md)  <mark class="gqlmd-mkdocs-badge">query</mark>

### Member Of

[`Person`](./person.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Post`](./post.md)  <mark class="gqlmd-mkdocs-badge">object</mark>