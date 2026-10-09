# IOrganization



Interface for all organizations.


```graphql
interface IOrganization {
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

#### [`IOrganization.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ID!`](../scalars/id.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the organization.


#### [`IOrganization.id`](#id)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String!`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#id} 
The persistent identifier of the organization.


#### [`IOrganization.label`](#label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#label} 
The label of the organization.


#### [`IOrganization.alt_label`](#alt-label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#alt-label} 
The alternative label of the organization.


#### [`IOrganization.mam_label`](#mam-label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#mam-label} 
The tenant name of the organization in the meemoo MAM.


#### [`IOrganization.slug`](#slug)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#slug} 
A slugified version of the label to create in an URL.


#### [`IOrganization.homepage`](#homepage)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#homepage} 
The website of the organization.


#### [`IOrganization.description`](#description)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#description} 
The description of the organization (in Dutch).


#### [`IOrganization.logo`](#logo)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Logo`](../objects/logo.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#logo} 
The logo of the organization.


#### [`IOrganization.overlay`](#overlay)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#overlay} 
A flag indicating whether the organization allows media overlays.


#### [`IOrganization.bzt`](#bzt)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#bzt} 
A flag indicating whether the organization allows content to be included in meemoo's Bezoekertool.


#### [`IOrganization.iiif`](#iiif)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean`](../scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iiif} 
A flag indicating whether the organization allows content to be included in meemoo's IIIF service.


#### [`IOrganization.form_url`](#form-url)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#form-url} 
The URL to a request content from the organization.


#### [`IOrganization.sector`](#sector)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#sector} 
The sector the organization in active in.


#### [`IOrganization.account_manager`](#account-manager)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Person`](../objects/person.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#account-manager} 
The account manager at meemoo responsible for this organization.


#### [`IOrganization.classification`](#classification)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Concept`](../objects/concept.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#classification} 
The organization type.


#### [`IOrganization.units`](#units)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[OrganizationalUnit]`](../objects/organizational-unit.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#units} 
The units belonging to this organization.


#### [`IOrganization.contact_point`](#contact-point)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[ContactPoint]`](../objects/contact-point.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#contact-point} 
The points of contact in this organizaton.


#### [`IOrganization.primary_site`](#primary-site)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Site`](../objects/site.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#primary-site} 
The primary physical site of the organization.


#### [`IOrganization.sites`](#sites)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Site]`](../objects/site.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#sites} 
The physical sites of the organization.


#### [`IOrganization.posts`](#posts)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Post]`](../objects/post.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#posts} 
The known jobpositions at the organization, eg. technical manager, project manager, accountant etc.




### Member Of

[`OrganizationalUnit`](../objects/organizational-unit.md)  <mark class="gqlmd-mkdocs-badge">object</mark>

### Implemented By

[`ContentPartner`](../objects/content-partner.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Organization`](../objects/organization.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`OrganizationalUnit`](../objects/organizational-unit.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`School`](../objects/school.md)  <mark class="gqlmd-mkdocs-badge">object</mark>