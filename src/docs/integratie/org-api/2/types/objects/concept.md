# Concept



A taxonomy concept.


```graphql
type Concept {
  iri: ID!
  label: String
  alt_label: String
  broader: [Concept]
  narrower: [Concept]
}
```


### Fields

#### [`Concept.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ID!`](../scalars/id.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 



#### [`Concept.label`](#label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#label} 
The concept label.


#### [`Concept.alt_label`](#alt-label)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#alt-label} 
The concept's alternative label.


#### [`Concept.broader`](#broader)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Concept]`](./concept.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#broader} 
Any parent concept.


#### [`Concept.narrower`](#narrower)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Concept]`](./concept.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#narrower} 
Any child concepts.




### Member Of

[`Concept`](./concept.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ContentPartner`](./content-partner.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`IOrganization`](../interfaces/iorganization.md)  <mark class="gqlmd-mkdocs-badge">interface</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Logo`](./logo.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Organization`](./organization.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`OrganizationalUnit`](./organizational-unit.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Post`](./post.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`School`](./school.md)  <mark class="gqlmd-mkdocs-badge">object</mark>