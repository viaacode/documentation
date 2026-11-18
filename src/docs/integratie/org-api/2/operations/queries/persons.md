# persons



Retrieve data about personnel or persons known to meemoo.


```graphql
persons(
  iri: String
  given_name: String
  family_name: String
  offset: Int
  limit: Int
): [Person]
```


### Arguments

#### [`persons.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../../types/scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the person.


#### [`persons.given_name`](#given-name)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../../types/scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#given-name} 
The first name of the person.


#### [`persons.family_name`](#family-name)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../../types/scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#family-name} 
The last name of the person.


#### [`persons.offset`](#offset)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Int`](../../types/scalars/int.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#offset} 
The specified number of results after which it should start generating results.


#### [`persons.limit`](#limit)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Int`](../../types/scalars/int.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#limit} 
The upper bound on the number of solutions returned.




### Type

#### [`Person`](../../types/objects/person.md) <mark class="gqlmd-mkdocs-badge">object</mark> 
A person.