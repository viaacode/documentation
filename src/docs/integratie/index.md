---
layout: default
title: Een integratie ontwikkelen
has_children: true
has_toc: true
nav_order: 3
last_modified_date: 2021-03-25T06:33:08+0100
---

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

Status: WIP
{: .label .label-yellow }

# Ontwikkeling van een integratie

## Introductie

Contentpartners (verder gewoon "CP" genoemd) kunnen zelf aan de slag met onze
API's en services om een integratie te bouwen. Hieronder vind je informatie om
hier mee te kunnen starten.

We leggen uit wat de verschillende software-omgevingen zijn en waarvoor ze
dienen gebruikt te worden, en, welke publieke API's beschikbaar zijn en hoe
daarmee te werken.

## De verschillende omgevingen en hun endpoints

Meemoo heeft twee - publieke - omgevingen:

- QAS: of "staging", een omgeving die productie nabootst en waarin
  ontwikkelaars en CP's kunnen testen.
- PRD: of "production", de werkelijke omgeving voor eindgebruikers.

De gewoonlijke (en **sterk** aangeraden) procedure is om eerst in de
QAS-omgeving te testen en pas als alles naar behoren werkt en uitvoerig is
getest, naar productie te gaan.

### Netwerk locaties

Hieronder vind je de verschillende netwerk locaties eigen aan elke omgeving.

| QAS                 | PRD             |
|---------------------|-----------------|
| archief-qas.viaa.be | archief.viaa.be |

**Note**: de transitie naar het meemoo-domein is nog niet volledig afgerond.
Voorlopig is het beter en veiliger om nog het viaa-domein te gebruiken. Sowieso
is het goed om bovenstaande netwerk locaties als omgevingsvariabelen
("_environment variables_") te configureren in je applicatie of integratie. Op
die manier kan er later triviaal geswitched worden naar het nieuwe domain.

### Netwerk paden

Dit zijn de paden waarop de verschillende API's bereikbaar zijn. Onderstaande
paden, gecombineerd met de netwerk locaties van hierboven, geven je de
volledige URL waarop de API kan worden aangesproken.

| Documentatie                                                                                   | Pad                                                      |
|------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [OAI-PMH API]({{ site.baseurl }}{% link docs/integratie/oai-pmh.md %})                         | /mediahaven-oai/oai/                                     |
| [MH REST API v1](https://archief.viaa.be/mediahaven-rest-api/)                                 | ~~/mediahaven-rest-api/~~ **Deprecated sinds juni '23!** |
| [MH REST API v2](https://archief.viaa.be/mediahaven-rest-api/v2/api-docs/)                     | /mediahaven-rest-api/v2/                                 |
| [IIIF 3.0 Image API]({{ site.baseurl }}{% link docs/integratie/iiif.md %})                     |                                                          |
| [Organizations API v2]({{ site.baseurl }}{% link docs/integratie/org-api/index.md %})          |                                                          |
| [Webhook Status Events]({{ site.baseurl }}{% link docs/integratie/webhook-status-events.md %}) |                                                          |

# Mediahaven API's

Twee grote API's zijn beschikbaar voor de content partners:

- REST API
- OAI-PMH API

Daar waar je via de REST API volledige _CRUD_-functionaliteit hebt ("_Create,
Read, Update, Delete_"), is de OAI-PMH alleen-lezen. Anderzijds is een OAI-PMH
API een welomlijnde standaard en is de REST API MediaHaven-specifiek.

## REST API

{: .note }
Opgelet: de REST API versie 1 werd uitgefaseerd en is vanaf 1 juni '23 niet meer ondersteund!

De documentatie is hier te vinden:

- REST API v2:
  [https://archief.viaa.be/mediahaven-rest-api/v2/api-docs/index.html](https://archief.viaa.be/mediahaven-rest-api/v2/api-docs/index.html)

### Authenticatie voor de MediaHaven REST API v2

Authenticatie op v2 is **uitsluitend** mogelijk via OAuth 2.0! Basic Auth, zoals mogelijk was in de REST API v1, is nu niet meer ondersteund.

De referentie-documentatie voor OAuth 2.0 vind je hier:
[https://oauth.net/2/](https://oauth.net/2/).

Voor de autorisatie zijn op de MediaHaven REST API v2 momenteel twee
OAuth2 flows geïmplementeerd:

- “Authorization Code Grant Type”
- “Resource Owner Credentials Grant Type”

De keuze voor een flow hangt af van de use-case:

- user-facing web applicatie → "Authorization Code Grant Type"
- machine-to-machine applicatie integratie → "Resource Owner Credentials Grant
  Type"

(Zie bv [A Guide To OAuth 2.0 Grants](https://alexbilbie.github.io/guide-to-oauth-2-grants/))

(De auth-flow die typisch gebruikt wordt voor machine-to-machine integraties is
de "Client Credentials Grant Type". Deze is echter - nog - niet geïmplementeerd
in de MediaHaven REST API).

Om een applicatie via OAuth2 te laten authenticeren tegen MediaHaven, moet deze
applicatie geregistreerd worden. We hebben dan van je nodig:

- Organisatienaam
- Naam van de integratie (of applicatie)
- Korte beschrijving van de integratie
- Destination server(s) (*)
- Redirect-URL (*)

(*) Enkel in het geval van de “Authorization Code Grant Type”.

Je krijgt dan een "client_id" en een "client_secret". Om te authenticeren met
deze client_id en client_secret, heb je een account nodig. Dat kan een
persoonlijke account zijn of een "technische" account (bv. `mediahaven.api@<org>.be`)

## OAI-PMH API

Zie [https://developer.meemoo.be/docs/integratie/oai-pmh]({{ site.baseurl }}{% link docs/integratie/oai-pmh.md %}) voor meer informatie.
