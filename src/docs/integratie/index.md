---
title: Developing an Integration
nav_order: 3
---

<span class="label label-yellow">Status: WIP</span>

# Developing an Integration

## Introduction

Content partners (further just "CP" referred) can start working with our
APIs and services themselves. Here you will find the information needed to get
started.

We explain what the different software environments are and for what they are
used, and which public APIs are available and how to work with them.

## The Different Environments and Their Endpoints

Meemoo has two public environments:

- QAS: or "staging", an environment that mimics production and in which
  developers and CPs can test.
- PRD: or "production", the actual environment for end users.

The usual (and **strongly** recommended) procedure is to first test in the
QAS environment and only if everything works properly and has been thoroughly
tested, to move to production.

### Network Locations

Below you will find the different network locations specific to each environment.

| QAS                 | PRD             |
|---------------------|-----------------|
| archief-qas.viaa.be | archief.viaa.be |

**Note**: The transition to the meemoo domain is not yet complete. For now, it
is better and safer to still use the viaa domain. Anyway, it is good practice to
configure the above network locations as environment variables ("_environment
variables_") in your application or integration. This way, you can easily switch
to the new domain later.

### Network Paths

These are the paths where the different APIs are reachable. The below paths,
combined with the network locations above, give you the full URL where the API
can be accessed.

| Documentation                                                                                   | Path                                                      |
|------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [OAI-PMH API](oai-pmh.md)                         | /mediahaven-oai/oai/                                     |
| [MH REST API v1](https://archief.viaa.be/mediahaven-rest-api/)                                 | ~~/mediahaven-rest-api/~~ **Deprecated since June '23!** |
| [MH REST API v2](https://archief.viaa.be/mediahaven-rest-api/v2/api-docs/)                     | /mediahaven-rest-api/v2/                                 |
| [IIIF 3.0 Image API](iiif.md)                     |                                                          |
| [Organizations API v2](org-api/2/index.md)        |                                                          |
| [Webhook Status Events](webhook-status-events.md) |                                                          |

# Mediahaven APIs

Two large APIs are available for the content partners:

- REST API
- OAI-PMH API

Where you have full "_Create, Read, Update, Delete_" functionality via the REST
API ("_CRUD_"), the OAI-PMH is only read-only. Conversely, an OAI-PMH API is a
well-defined standard and the REST API is MediaHaven-specific.

## REST API

!!! note

    Note: REST API version 1 has been phased out and is no longer supported from
    June 1st '23!

The documentation can be found here:

- REST API v2:
  [https://archief.viaa.be/mediahaven-rest-api/v2/api-docs/index.html](https://archief.viaa.be/mediahaven-rest-api/v2/api-docs/index.html)

### Authentication for the MediaHaven REST API v2

Authentication for the MediaHaven REST API v2 is **exclusively** possible via
OAuth 2.0! Basic Auth, which was possible in the REST API v1, is no longer
supported.

The reference documentation for OAuth 2.0 can be found here:
[https://oauth.net/2/](https://oauth.net/2/).

For authorization, currently two OAuth2 flows are implemented on the MediaHaven
REST API v2:

- “Authorization Code Grant Type”
- “Resource Owner Credentials Grant Type”

The choice for a flow depends on the use case:

- user-facing web application → “Authorization Code Grant Type”
- machine-to-machine application integration → “Resource Owner Credentials Grant
  Type”

(See e.g. [A Guide To OAuth 2.0 Grants](https://alexbilbie.github.io/guide-to-oauth-2-grants/))

(The auth-flow typically used for machine-to-machine integrations is the
"_Client Credentials Grant Type_". However, this is **still not implemented** in
the MediaHaven REST API.)

To let an application authenticate via OAuth2 against MediaHaven, the application
must be registered. We need from you:

- Organization name
- Name of the integration (or application)
- Short description of the integration
- Destination server(s) (*)
- Redirect URL (*)

(*) Only for the “Authorization Code Grant Type”.

You will then receive a "client_id" and a "client_secret". To authenticate with
these client_id and client_secret, you need an account. This can be a personal
account or a "technical" account (e.g., `mediahaven.api@<org>.be`).

## OAI-PMH API

See [https://developer.meemoo.be/docs/integratie/oai-pmh](oai-pmh.md) for more information.
