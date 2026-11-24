# organizations



Retrieve data about all organizations in a paginated manner. By default, the query never returns more than 500 results. Offset should be used to get more results.


```graphql
organizations(
  iri: String
  id: String
  offset: Int
  limit: Int
  label: String
  type: OrgType
  sector: Sector
): [Organization]
```


### Arguments

#### [`organizations.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../../types/scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the organization.


#### [`organizations.id`](#id)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../../types/scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#id} 
The persistent identifier of the organization.


#### [`organizations.offset`](#offset)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Int`](../../types/scalars/int.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#offset} 
The specified number of results after which it should start generating results.


#### [`organizations.limit`](#limit)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Int`](../../types/scalars/int.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#limit} 
The upper bound on the number of solutions returned. The query never returns more than 500 results, even if limit is set to a higher number.


#### [`organizations.label`](#label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../../types/scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#label} 
A simple search by organization label.


#### [`organizations.type`](#type)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`OrgType`](../../types/enums/org-type.md) <mark class="gqlmd-mkdocs-badge">enum</mark> {#type} 
Only return a specific type of organization. The results also include instances of subtypes.


#### [`organizations.sector`](#sector)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Sector`](../../types/enums/sector.md) <mark class="gqlmd-mkdocs-badge">enum</mark> {#sector} 
Only return organizations in a specific sector.




### Type

#### [`Organization`](../../types/objects/organization.md) <mark class="gqlmd-mkdocs-badge">object</mark> 
A generic organization.