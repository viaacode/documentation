# Meemoo public technical documentation

This repository generates [https://developer.meemoo.be/](https://developer.meemoo.be/).

## Build the docs locally

First, [install Ruby 2.7.](https://www.ruby-lang.org/en/documentation/installation/)

Next, install [Jekyll](https://jekyllrb.com/) and other dependencies from the `Gemfile` with 

```bash
bundle install
```

Finally, run

```bash
bundle exec jekyll serve
```

## Convert legacy files

Get pandoc

```
pandoc -s <file> -t markdown -o ./docs/output.md --wrap=none
```
