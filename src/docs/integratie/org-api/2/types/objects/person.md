# Person



A person.


```graphql
type Person {
  iri: ID!
  given_name: String
  family_name: String
  telephone: String
  email: String
  holds: [Post]
  account_manager_of: [Organization]
}
```


### Fields

#### [`Person.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`ID!`](../scalars/id.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the person.


#### [`Person.given_name`](#given-name)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#given-name} 
The given or first name of the person.


#### [`Person.family_name`](#family-name)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#family-name} 
The family or last name of the person.


#### [`Person.telephone`](#telephone)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#telephone} 
The telephone number of the person.


#### [`Person.email`](#email)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#email} 
The email address of the person.


#### [`Person.holds`](#holds)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Post]`](./post.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#holds} 
The posts or positions that this person holds.


#### [`Person.account_manager_of`](#account-manager-of)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`[Organization]`](./organization.md) <mark class="gqlmd-mkdocs-badge">list</mark> <mark class="gqlmd-mkdocs-badge">object</mark> {#account-manager-of} 
The organizations that this person is account manager of.




### Returned By

[`persons`](../../operations/queries/persons.md)  <mark class="gqlmd-mkdocs-badge">query</mark>

### Member Of

[`ContentPartner`](./content-partner.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`IOrganization`](../interfaces/iorganization.md)  <mark class="gqlmd-mkdocs-badge">interface</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Organization`](./organization.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`OrganizationalUnit`](./organizational-unit.md)  <mark class="gqlmd-mkdocs-badge">object</mark><span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`School`](./school.md)  <mark class="gqlmd-mkdocs-badge">object</mark>