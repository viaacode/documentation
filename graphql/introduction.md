# meemoo Organization API V2 { #introduction }

Documentation for meemoo's Organization API V2. This API provides access to
information about organizations and people within the meemoo context, such as
content partners, educational partners, address sites, contact information,
account managers, and meemoo personnel. It is a
[GraphQL API](https://graphql.org/) that conforms to the
[October 2021 specification](https://spec.graphql.org/October2021/).

## Authentication { #introduction-item-0 }

This API uses authentication via [JSON Web Tokens (JWT)](https://jwt.io/). You
can request a JWT using your meemoo username and password:

1. Request a token from QAS or production:

    ```bash
    curl -v -u '<username/email/...>:<password>' "https://oas-qas.meemoo.be/token?grant_type=client_credentials&expires_in=31536000"
    curl -v -u '<username/email/...>:<password>' "https://oas.meemoo.be/token?grant_type=client_credentials&expires_in=31536000"
    ```

2. Send the token in the `Authorization: Bearer` header or in the `jwtauth`
   query parameter:

    ```bash
    curl -v https://services-qas.viaa.be/organisation_v2/?jwtauth="eyJ0eXAiOiJKV1......tbjz4-r4"
    curl -v https://services.viaa.be/organisation_v2/?jwtauth="eyJ0eXAiOiJKV1......tbjz4-r4"
    ```

## GET request { #introduction-item-1 }

A GraphQL GET request contains the GraphQL query in the `query` query string:

```bash
curl -v 'https://services-qas.viaa.be/organisation_v2?query=<graphql_query>'
curl -v 'https://services.viaa.be/organisation_v2?query=<graphql_query>'
```

## POST request { #introduction-item-2 }

A GraphQL POST request expects a JSON-encoded payload and the
`Content-Type: application/json` header:

```json
{
  "query": "...",
  "operationName": "...",
  "variables": { "myVariable": "someValue" }
}
```

## Testing { #introduction-item-3 }

The QAS API also serves [GraphQL Playground](https://github.com/graphql/graphql-playground)
at <https://services-qas.viaa.be/organisation_v2>. Authentication is required.

## Queries { #group-Operations-Queries }

- <a id="query-contentpartners"></a>`contentpartners`
- <a id="query-organizations"></a>`organizations`
- <a id="query-persons"></a>`persons`
- <a id="query-schools"></a>`schools`

## Types { #group-Types }

- `Query`
- <a id="definition-Boolean"></a>`Boolean`
- <a id="definition-Concept"></a>`Concept`
- <a id="definition-ContactPoint"></a>`ContactPoint`
- <a id="definition-ContentPartner"></a>`ContentPartner`
- <a id="definition-IContactPoint"></a>`IContactPoint`
- <a id="definition-ID"></a>`ID`
- <a id="definition-IOrganization"></a>`IOrganization`
- <a id="definition-Int"></a>`Int`
- <a id="definition-Logo"></a>`Logo`
- <a id="definition-OrgType"></a>`OrgType`
- <a id="definition-Organization"></a>`Organization`
- <a id="definition-OrganizationalUnit"></a>`OrganizationalUnit`
- <a id="definition-Person"></a>`Person`
- <a id="definition-Post"></a>`Post`
- <a id="definition-PostalAddress"></a>`PostalAddress`
- <a id="definition-School"></a>`School`
- <a id="definition-Sector"></a>`Sector`
- <a id="definition-Site"></a>`Site`
- <a id="definition-String"></a>`String`

## Endpoints

- Production: <https://services.viaa.be/organisation_v2>
- QAS: <https://services-qas.viaa.be/organisation_v2>

All calls require an `Authorization: Bearer <YOUR_TOKEN_HERE>` header or the
equivalent `jwtauth` query parameter.

## Contact and license

Contact [meemoo support](mailto:support@meemoo.be) or visit
[meemoo.be](https://meemoo.be). The API documentation is licensed under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html).

<span id="content"></span><span id="docs"></span><span id="logo"></span><span id="mobile-navbar"></span><span id="nav"></span><span id="page"></span><span id="sidebar"></span><span id="spectaql"></span><span id="welcome"></span>
