# Post



A position some person has at an organization.


```graphql
type Post {
  iri: ID!
  role: Concept
  post_in: [Organization]!
}
```


### Fields

#### [`Post.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ID!`](../scalars/id.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI.


#### [`Post.role`](#role)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Concept`](./concept.md) <mark class="gqlmd-mkdocs-badge">object</mark> {#role} 
The role that this position fills, eg. manager, technical analyst, accountant, etc.


#### [`Post.post_in`](#post-in)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Organization]!`](./organization.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#post-in} 
The organization that this post is at.




### Member Of

[`ContentPartner`](./content-partner.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`IOrganization`](../interfaces/iorganization.md)  <mark class="gqlmd-mkdocs-badge">interface</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Organization`](./organization.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`OrganizationalUnit`](./organizational-unit.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Person`](./person.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`School`](./school.md)  <mark class="gqlmd-mkdocs-badge">object</mark>