# include



Directs the executor to include this field or fragment only when the `if` argument is true.


```graphql
directive @include(
  if: Boolean!
) on 
  | FIELD
  | FRAGMENT_SPREAD
  | INLINE_FRAGMENT
```


### Arguments

#### [`include.if`](#if)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean!`](../../types/scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#if} 
Included when true.