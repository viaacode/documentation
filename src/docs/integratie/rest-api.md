**REST API v1 vs v2**

**Note**

    Please: the REST API version 1 was phased out and is no longer supported
    starting June 1st '23!

MediaHaven has offered a REST API since the beginning to perform operations on
media objects. Since MediaHaven version 21.1 (released on April 16, 2021) a new
version of this REST API has been rolled out. We will further discuss these two
versions of each other with the designations "v1" and "v2".

Although much of the basic functionality in the new REST API (such as querying a
_resource_, executing a search,...) has remained largely unchanged, changes have
been introduced that are **backwards incompatible**. This means that existing
integrations that use the REST API v1 could break when they are transferred to the
new endpoint.

The old REST API v1, at the current endpoint, is still supported until
**MediaHaven version 22.1**, but we strongly recommend switching to the new REST
API v2, at the new endpoint.

## Endpoints

Zeticon chose to manage their REST API versioning via the URL path. This means
that the version number is added to the URL path to reach the v2 of the REST API.
Specifically:

| API version | Endpoint                                    |
|-------------:|---------------------------------------------|
| v1           | https://archief.viaa.be/mediahaven-rest-api/ |
| v2           | https://archief.viaa.be/mediahaven-rest-api/v2/ |

**Note**: These are the endpoints for the production environment! For a
description of the different environments and their endpoints, see [Everything to
get started with building an integration](index.md).

## Differences between REST API v1 and v2

First, we list here the main **backwards incompatible** differences between the
REST API v1 and v2. Then we go into detail about what this means concretely.

- authentication can be done **only via OAuth2**: **Basic Auth** is no longer
  supported
- the structure of the JSON response changes
- the resource `/media` has become `/records`

For a full overview of the differences, see the links below this page.

### Authentication

- **Authentication** is the process where users prove they are who they claim to
  be, or more precisely: that they are the actual owner of the identity they claim
  to have.
- **Authorization** is the process where an application, based on the verified
  identity, allows or denies certain actions.

The REST API v1 allowed two ways of authentication:

- **basic authentication**
- OAuth2

**Basic authentication** is a very simple form of authentication that is part of
the HTTP protocol. Here, the username and password are included with each call to
the API in the HTTP `Authorization` header with the `Basic` prefix, for example:

    Authorization: Basic ZGVtbzpwQDU1dzByZA==

OAuth2, on the other hand, is an "authorization framework", a standard alongside the
HTTP protocol. Here, access tokens with a short lifespan are used. These are
usually included in the HTTP requests via the `Authorization` header but with the
`Bearer` prefix, for example:

    Authorization: Bearer RsT5OjbzRn430zqMLgV3Ia

On this page you can find more information about the OAuth2 authentication:
[Everything to get started with building an integration](index.md).

**Why is this important?** Integrations based on REST API v1 will no longer work
since they are no longer authenticated.

### Response Formats

In REST API v1 it was already possible to obtain the new response formats (both
for JSON and XML) via content negotiation in the HTTP `Accept` header. In the
REST API v1 the following response formats were possible:

| Format | `Accept` header                      |
|--------:|--------------------------------------|
| JSON v1 | `application/json`                   |
|  XML v1 | `application/xml`                    |
| JSON v2 | `application/vnd.mediahaven.v2+json` |
|  XML v2 | `application/vnd.mediahaven.v2+xml`  |

The newer response formats in the REST API v1 (shown in the table above:
`JSON v2` and `XML v2`) are now the standard in the REST API v2. This means that
the `Accept` headers `application/vnd.mediahaven.v2+json` and
`application/vnd.mediahaven.v2+xml` will become obsolete. The default format of
the response in the REST API v2 is now essentially the same as the v2 format in
the REST API v1.

In addition to a change in the structure (i.e., where certain data is located in
the JSON) of the response, the casing has also changed:

- the JSON keys in the v1 format are camelCase (e.g., `totalNrOfResults`)
- the JSON keys in the v2 format are PascalCase (e.g., `TotalNrOfResults`)

#### Examples

- JSON response format `application/json` in REST API v1

```json
{
    "totalNrOfResults": 10,
    "startIndex": 0,
    "mediaDataList": [
        {
        ...
        }
    ]
}
```

- JSON response format `application/vnd.mediahaven.v2+json` in REST API v1

```json
{
    "TotalNrOfResults": 10,
    "StartIndex": 0,
    "MediaDataList": [
        {
        ...
        }
      ]
}
```

- JSON response format `application/json` in REST API v2

```json
{
    "NrOfResults" : 5
    "TotalNrOfResults": 10,
    "StartIndex": 0,
    "Results": [
        {
        ...
        }
    ]
}
```

We see here that the array containing the results is now always `Results` in the
REST API v2.

**Why is this important?** Integrations are usually case-sensitive and expect
certain data to be located at a certain place, these assumptions would no longer
hold in the REST API v2.

### From `/media` resource to `/records`

The main resource, the media objects, used to be called `media` in the REST API
v1. This has been changed to `records`.

## New Features

See [MediaHaven Customer Support > REST API > Rest V2 vs v1 changes >
New-features](https://mediahaven.atlassian.net/wiki/spaces/CS/pages/2432303184/Rest+V2+vs+v1+changes#New-features)

## Links

### Documentation

The documentation for both versions can be found here:

- REST API v1:
  [https://archief.viaa.be/mediahaven-rest-api](https://archief.viaa.be/mediahaven-rest-api)
- REST API v2:
  [https://archief.viaa.be/mediahaven-rest-api/v2/api-docs/index.html](https://archief.viaa.be/mediahaven-rest-api/v2/api-docs/index.html)

Please refer to the MediaHaven documentation about the differences between REST
API v1 and v2:

- [MediaHaven Customer Support > REST API > Rest V2 vs v1 changes](https://mediahaven.atlassian.net/wiki/spaces/CS/pages/2432303184/Rest+V2+vs+v1+changes)
