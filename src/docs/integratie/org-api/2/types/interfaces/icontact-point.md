# IContactPoint



No description


```graphql
interface IContactPoint {
  iri: ID!
  contact_type: String
  email: String
  telephone: String
}
```


### Fields

#### [`IContactPoint.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ID!`](../scalars/id.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the contact point.


#### [`IContactPoint.contact_type`](#contact-type)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#contact-type} 
The type of contact, eg. primary, financial, delivery, etc.


#### [`IContactPoint.email`](#email)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#email} 
The contact's email address.


#### [`IContactPoint.telephone`](#telephone)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#telephone} 
The contact's telephone number.




### Implemented By

[`ContactPoint`](../objects/contact-point.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`PostalAddress`](../objects/postal-address.md)  <mark class="gqlmd-mkdocs-badge">object</mark>