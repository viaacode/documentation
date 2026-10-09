# skip



Directs the executor to skip this field or fragment when the `if` argument is true.


```graphql
directive @skip(
  if: Boolean!
) on 
  | FIELD
  | FRAGMENT_SPREAD
  | INLINE_FRAGMENT
```


### Arguments

#### [`skip.if`](#if)<span class="gqlmd-mdx-bullet">&nbsp;●&nbsp;</span>[`Boolean!`](../../types/scalars/boolean.md) <mark class="gqlmd-mkdocs-badge">non-null</mark> <mark class="gqlmd-mkdocs-badge">scalar</mark> {#if} 
Skipped when true.