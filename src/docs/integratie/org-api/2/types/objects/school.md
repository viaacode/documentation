# School



A school.


```graphql
type School implements IOrganization {
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
}
```


### Fields

#### [`School.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ID!`](../scalars/id.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the school.


#### [`School.id`](#id)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String!`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#id} 
The school ID of the school.


#### [`School.label`](#label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#label} 
The label of the school.


#### [`School.alt_label`](#alt-label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#alt-label} 
The alternative label of the school.


#### [`School.mam_label`](#mam-label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#mam-label} 
The tenant name of the school in the meemoo MAM.


#### [`School.slug`](#slug)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#slug} 
A slugified version of the label to create in an URL.


#### [`School.homepage`](#homepage)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#homepage} 
The website of the school.


#### [`School.description`](#description)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#description} 
The description of the school (in Dutch).


#### [`School.logo`](#logo)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Logo`](./logo.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#logo} 
The logo of the school.


#### [`School.overlay`](#overlay)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#overlay} 
A flag indicating whether the school allows media overlays.


#### [`School.bzt`](#bzt)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#bzt} 
A flag indicating whether the school allows content to be included in meemoo's Bezoekertool.


#### [`School.iiif`](#iiif)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iiif} 
A flag indicating whether the organization allows content to be included in meemoo's IIIF service.


#### [`School.form_url`](#form-url)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#form-url} 
The URL to a request content from the school.


#### [`School.sector`](#sector)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#sector} 
The sector the school in active in.


#### [`School.account_manager`](#account-manager)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Person`](./person.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#account-manager} 
The account manager at meemoo responsible for this school.


#### [`School.classification`](#classification)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Concept`](./concept.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#classification} 
The school type.


#### [`School.units`](#units)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[OrganizationalUnit]`](./organizational-unit.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#units} 
The units belonging to this school.


#### [`School.contact_point`](#contact-point)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[ContactPoint]`](./contact-point.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#contact-point} 
The points of contact in this organizaton.


#### [`School.primary_site`](#primary-site)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Site`](./site.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#primary-site} 
The primary physical site of the school.


#### [`School.sites`](#sites)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Site]`](./site.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#sites} 
The physical sites of the school.


#### [`School.posts`](#posts)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Post]`](./post.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#posts} 
The known jobpositions at the school, eg. english teacher, director, etc.




### Interfaces

#### [`IOrganization`](../interfaces/iorganization.md) <mark class="gqlmd-mkdocs-badge">interface</mark> 
Interface for all organizations.




### Returned By

[`schools`](../../operations/queries/schools.md)  <mark class="gqlmd-mkdocs-badge">query</mark>