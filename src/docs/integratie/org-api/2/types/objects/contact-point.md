# ContactPoint



A contact point.


```graphql
type ContactPoint implements IContactPoint {
  iri: ID!
  contact_type: String
  email: String
  telephone: String
}
```


### Fields

#### [`ContactPoint.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ID!`](../scalars/id.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the contact point.


#### [`ContactPoint.contact_type`](#contact-type)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#contact-type} 
The type of contact, eg. primary, financial, delivery, etc.


#### [`ContactPoint.email`](#email)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#email} 
The contact's email address.


#### [`ContactPoint.telephone`](#telephone)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#telephone} 
The contact's telephone number.




### Interfaces

#### [`IContactPoint`](../interfaces/icontact-point.md) <mark class="gqlmd-mkdocs-badge">interface</mark> 





### Member Of

[`ContentPartner`](./content-partner.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`IOrganization`](../interfaces/iorganization.md)  <mark class="gqlmd-mkdocs-badge">interface</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Organization`](./organization.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`OrganizationalUnit`](./organizational-unit.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`School`](./school.md)  <mark class="gqlmd-mkdocs-badge">object</mark>