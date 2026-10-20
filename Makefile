GRAPHQL_IMAGE := documentation-graphql

.PHONY: graphql-schema graphql-docs

graphql-schema:
	@test -n "$(SCHEMA_URL)" || (echo "SCHEMA_URL is required" >&2; exit 2)
	curl --fail --silent --show-error "$(SCHEMA_URL)" --output graphql/schema.json.tmp
	mv graphql/schema.json.tmp graphql/schema.json

graphql-docs:
	docker build -f graphql/Dockerfile -t $(GRAPHQL_IMAGE) graphql
	docker run --rm --network none -v "$(CURDIR):/workspace" -w /workspace/graphql $(GRAPHQL_IMAGE) graphql-to-doc --root ../src/docs/integratie/org-api --force
	mv src/docs/integratie/org-api/2/introduction.md src/docs/integratie/org-api/2/index.md
	@test -f src/docs/integratie/org-api/2/index.md
