# contentpartners



Retrieve data about contentpartners of meemoo.


```graphql
contentpartners(
  iri: String
  id: String
  offset: Int
  limit: Int
): [ContentPartner]
```


### Arguments

#### [`contentpartners.iri`](#iri)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../../types/scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#iri} 
The persistent meemoo URI of the contentpartner.


#### [`contentpartners.id`](#id)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`String`](../../types/scalars/string.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#id} 
The persistent meemoo identifier of the contentpartner.


#### [`contentpartners.offset`](#offset)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Int`](../../types/scalars/int.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#offset} 
The specified number of results after which it should start generating results.


#### [`contentpartners.limit`](#limit)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Int`](../../types/scalars/int.md) <mark class="gqlmd-mkdocs-badge">scalar</mark> {#limit} 
The upper bound on the number of solutions returned.




### Type

#### [`ContentPartner`](../../types/objects/content-partner.md) <mark class="gqlmd-mkdocs-badge">object</mark> 
A meemoo content partner.