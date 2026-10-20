# schools



Retrieve data about schools known to meemoo.


```graphql
schools(
  iri: String
  id: String
  offset: Int
  limit: Int
): [School]
```


### Arguments

#### [`schools.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../../types/scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the school.


#### [`schools.id`](#id)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../../types/scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#id} 
The school ID of the school.


#### [`schools.offset`](#offset)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Int`](../../types/scalars/int.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#offset} 
The specified number of results after which it should start generating results.


#### [`schools.limit`](#limit)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Int`](../../types/scalars/int.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#limit} 
The upper bound on the number of solutions returned.




### Type

#### [`School`](../../types/objects/school.md) <mark class="gqlmd-mkdocs-badge">object</mark> 
A school.