# Meemoo public technical documentation

This repository generates [https://developer.meemoo.be/](https://developer.meemoo.be/).

## Run the docs locally

Install Python 3.12, then run:

```bash
git submodule update --init --recursive
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
zensical serve
```

Open `http://127.0.0.1:8000` to browse the docs.

## Add a table preview

Wrap a Markdown table in `<div class="preview-table" markdown="1">`, with blank
lines around the table, and close it with `</div>`. Tables show their first three
rows with a “See more” / “See less” button in a full-width footer row. Tables with
three or fewer rows stay fully visible. Without JavaScript, all rows remain visible.

## Run the docs with Docker

Build and run the preview image:

```bash
docker build -t meemoo-docs .
docker run --rm -it -p 8000:8000 meemoo-docs
```

Open `http://127.0.0.1:8000`. This image is for local preview only; production serves the static `site/` artifact.

## Update the Organizations API documentation

[Install Docker](https://docs.docker.com/get-docker/), then regenerate the committed Markdown from the current schema snapshot:

```bash
make graphql-docs
```

To refresh the schema snapshot first, provide the URL of the introspection JSON:

```bash
make graphql-schema SCHEMA_URL=https://example.test/schema.json
make graphql-docs
```

Commit changes to `graphql/schema.json`, `graphql/introduction.md`, and the generated files under `src/docs/integratie/org-api/` together. Node.js and npm run inside `graphql/Dockerfile`; they are not host prerequisites.

## Convert legacy files

Install Pandoc, then run:

```bash
pandoc -s <file> -t markdown -o ./docs/output.md --wrap=none
```
