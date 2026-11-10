# ContentPartner



A meemoo content partner.


```graphql
type ContentPartner implements IOrganization {
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

#### [`ContentPartner.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ID!`](../scalars/id.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the content partner.


#### [`ContentPartner.id`](#id)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String!`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#id} 
The persistent identifier of the content partner.


#### [`ContentPartner.label`](#label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#label} 
The label of the content partner.


#### [`ContentPartner.alt_label`](#alt-label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#alt-label} 
The alternative label of the content partner.


#### [`ContentPartner.mam_label`](#mam-label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#mam-label} 
The tenant name of the content partner in the meemoo MAM.


#### [`ContentPartner.slug`](#slug)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#slug} 
A slugified version of the label to create in an URL.


#### [`ContentPartner.homepage`](#homepage)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#homepage} 
The website of the content partner.


#### [`ContentPartner.description`](#description)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#description} 
The description of the content partner (in Dutch).


#### [`ContentPartner.logo`](#logo)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Logo`](./logo.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#logo} 
The logo of the content partner.


#### [`ContentPartner.overlay`](#overlay)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#overlay} 
A flag indicating whether the content partner allows media overlays.


#### [`ContentPartner.bzt`](#bzt)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#bzt} 
A flag indicating whether the content partner allows content to be included in meemoo's Bezoekertool.


#### [`ContentPartner.iiif`](#iiif)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iiif} 
A flag indicating whether the organization allows content to be included in meemoo's IIIF service.


#### [`ContentPartner.form_url`](#form-url)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#form-url} 
The URL to a request content from the content partner.


#### [`ContentPartner.sector`](#sector)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#sector} 
The sector the content partner in active in.


#### [`ContentPartner.account_manager`](#account-manager)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Person`](./person.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#account-manager} 
The account manager at meemoo responsible for this content partner.


#### [`ContentPartner.classification`](#classification)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Concept`](./concept.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#classification} 
The content partner type.


#### [`ContentPartner.units`](#units)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[OrganizationalUnit]`](./organizational-unit.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#units} 
The units belonging to this content partner.


#### [`ContentPartner.contact_point`](#contact-point)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[ContactPoint]`](./contact-point.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#contact-point} 
The points of contact in this organizaton.


#### [`ContentPartner.primary_site`](#primary-site)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Site`](./site.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#primary-site} 
The primary physical site of the content partner.


#### [`ContentPartner.sites`](#sites)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Site]`](./site.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#sites} 
The physical sites of the content partner.


#### [`ContentPartner.posts`](#posts)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Post]`](./post.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#posts} 
The known jobpositions at the content partner, eg. technical manager, project manager, accountant etc.




### Interfaces

#### [`IOrganization`](../interfaces/iorganization.md) <mark class="gqlmd-mkdocs-badge">interface</mark> 
Interface for all organizations.




### Returned By

[`contentpartners`](../../operations/queries/contentpartners.md)  <mark class="gqlmd-mkdocs-badge">query</mark>