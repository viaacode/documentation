# PostalAddress



A postal address.


```graphql
type PostalAddress implements IContactPoint {
  iri: ID!
  contact_type: String
  email: String
  telephone: String
  country: String
  locality: String
  region: String
  post_office_box_number: String
  postal_code: String
  street: String
}
```


### Fields

#### [`PostalAddress.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ID!`](../scalars/id.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the address.


#### [`PostalAddress.contact_type`](#contact-type)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#contact-type} 
The type of address, eg. primary, financial, delivery, etc.


#### [`PostalAddress.email`](#email)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#email} 
The email address.


#### [`PostalAddress.telephone`](#telephone)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#telephone} 
The telephone number to reach the address.


#### [`PostalAddress.country`](#country)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#country} 
The country the address is located in.


#### [`PostalAddress.locality`](#locality)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#locality} 
The city the address is located in.


#### [`PostalAddress.region`](#region)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#region} 
The region the address is located in.


#### [`PostalAddress.post_office_box_number`](#post-office-box-number)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#post-office-box-number} 
The box number of the address.


#### [`PostalAddress.postal_code`](#postal-code)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#postal-code} 
The postal code of the address.


#### [`PostalAddress.street`](#street)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#street} 
The street and number of the address.




### Interfaces

#### [`IContactPoint`](../interfaces/icontact-point.md) <mark class="gqlmd-mkdocs-badge">interface</mark> 





### Member Of

[`Site`](./site.md)  <mark class="gqlmd-mkdocs-badge">object</mark>