---
layout: default
title: REST API v1 en v2
parent: Een integratie ontwikkelen
has_children: false
has_toc: true
nav_order: 1
last_modified_date: 2021-04-19T09:27:33+02:00
---

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


# REST API v1 vs v2

{: .note }
Opgelet: de REST API versie 1 werd uitgefaseerd en is vanaf 1 juni '23 niet meer ondersteund!

MediaHaven biedt sinds het begin een REST API aan om bewerkingen uit te kunnen
voeren op mediaobjecten. Vanaf MediaHaven versie 21.1 (uitgebracht op 16 april
2021) werd van deze REST API een nieuwe versie uitgerold. We zullen verder in
de tekst deze twee versies van elkaar onderscheiden met de aanduidingen "v1" en
"v2".

Hoewel veel van de basisfuncties in de nieuwe REST API (zoals het opvragen
van een _resource_, het uitvoeren van een zoekopdracht,...) quasi onveranderd
zijn gebleven, werden er ook wijzigingen ingevoerd die _backwards incompatible_
zijn. Hierdoor zouden bestaande integraties die gebruik maken van de REST API
v1 kunnen breken wanneer ze naar het nieuwe _endpoint_ worden overgezet.

De oude REST API v1, op het huidige _endpoint_, wordt nog ondersteund tot
**MediaHaven versie 22.1**, maar we raden sterk aan om naar de nieuwe REST
API v2, op het nieuwe _endpoint_, over te stappen.

## Endpoints

Zeticon koos voor het versiebeheer van hun REST API voor versiebeheer via het
URL-pad. Dit betekent dat het versienummer toegevoegd wordt aan het URL-pad om
de v2 van de REST API te bereiken. Concreet:

| API versie | Endpoint                                        |
|-----------:|-------------------------------------------------|
| v1         | https://archief.viaa.be/mediahaven-rest-api/    |
| v2         | https://archief.viaa.be/mediahaven-rest-api/v2/ |

**Note**: Dit zijn de _endpoints_ voor de productieomgeving! Voor een
beschrijving van de verschillende omgevingen en hun _endpoints_, zie [Alles om te
starten met het bouwen van een integratie]({{ site.baseurl }}{% link
docs/integratie/index.md %}).

## Verschillen tussen REST API v1 en v2

Hieronder lijsten we eerst kort de belangrijkste _backwards incompatible_
verschillen op tussen de REST API v1 en v2. Daarna gaan we dieper in op wat
dat concreet inhoudt.

- authenticatie kan énkel nog via OAuth2: _Basic Auth_ wordt niet meer ondersteund
- de structuur van de JSON _response_ wijzigt
- de _resource_ `/media` is nu `/records` geworden

Voor een volledig overzicht van de verschillen verwijzen we je naar de links
onderaan deze pagina.

### Authenticatie

- **Authenticatie** is het proces waarbij gebruikers aantonen dat ze werkelijk
  zijn wie ze beweren te zijn, of liever: dat ze de werkelijke eigenaar zijn
  van de identiteit die ze beweren te hebben.
- **Autorisatie** is het proces waarbij een applicatie, op basis van de
  vastgestelde en geverifieerde identiteit, bepaalde acties toelaat of net
  weigert.

De REST API v1 liet twee manieren van authenticatie toe:

- _basic authentication_
- OAuth2

_Basic authentication_ is een heel simpele vorm van authenticatie die deel
uitmaakt van het HTTP-protocol. Hierbij worden gebruikersnaam en wachtwoord met
elke _call_ naar de API meegegeven in de HTTP `Authorization` _header_ met de
`Basic` prefix, bijvoorbeeld:

    Authorization: Basic ZGVtbzpwQDU1dzByZA==

OAuth2 daarentegen is een "autorisatie framework", een standaard op zich naast
het HTTP-protocol. Hierbij wordt gebruik gemaakt van _access tokens_ met een
korte levensduur. Ook deze worden − gewoonlijk − meegegeven in de HTTP-requests
via de `Authorization` _header_ maar met de  `Bearer` prefix, bijvoorbeeld:

    Authorization: Bearer RsT5OjbzRn430zqMLgV3Ia

Op deze pagina vind je meer informatie over de OAuth2 authenticatie: [Alles om
te starten met het bouwen van een integratie]({{ site.baseurl }}{% link
docs/integratie/index.md %}).

**Waarom is dit belangrijk?** Integraties gebaseerd op REST API v1 zullen niet
meer werken aangezien ze niet meer geauthenticeerd zijn.

### Responseformaten

In REST API v1 was het al mogelijk om de nieuwe responseformaten (zowel voor
JSON als voor XML) te verkrijgen via _content negotiation_ in de HTTP `Accept`
_header_. In de REST API v1 waren volgende responseformaten mogelijk:

| Formaat | `Accept` header                      |
|--------:|--------------------------------------|
| JSON v1 | `application/json`                   |
|  XML v1 | `application/xml`                    |
| JSON v2 | `application/vnd.mediahaven.v2+json` |
|  XML v2 | `application/vnd.mediahaven.v2+xml`  |

De nieuwere responseformaten in de REST API v1 (in de tabel hierboven: `JSON
v2` en `XML v2`) worden de standaard in de REST API v2. Dit betekent dat de
`Accept` _headers_ `application/vnd.mediahaven.v2+json` en
`application/vnd.mediahaven.v2+xml` komen te vervallen. Het standaardformaat
van de _response_ in de REST API v2 is nu quasi gelijk aan het v2 formaat in
de REST API v1.

Naast een wijziging aan de structuur (i.e. op welk JSON-pad bepaalde data te
vinden is) van de _response_, is ook de _casing_ gewijzigd:

- de JSON _keys_ in het v1 formaat zijn camelCase (e.g., `totalNrOfResults`)
- de JSON _keys_ in het v2 formaat zijn PascalCase (e.g., `TotalNrOfResults`)

#### Voorbeelden

- JSON responseformaat `application/json` in REST API v1

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

- JSON responseformaat `application/vnd.mediahaven.v2+json` in REST API v1

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

- JSON responseformaat `application/json` in REST API v2

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

Zo zien we hier ook dat de _array_ die de resultaten bevat in de REST API v2
nu altijd `Results` is.

**Waarom is dit belangrijk?** Integraties zijn meestal hoofdlettergevoelig en
verwachten bepaalde data op een bepaalde plaats te vinden, deze assumpties
zouden niet meer gelden in de REST API v2.

### Van `/media` resource naar `/records`

De belangrijkste resource, de mediaobjecten, heetten in de REST API v1 `media`.
Dit is nu gewijzigd naar `records`.

## Nieuwe _features_

Zie [MediaHaven Customer Support > REST API > Rest V2 vs v1 changes >
New-features](https://mediahaven.atlassian.net/wiki/spaces/CS/pages/2432303184/Rest+V2+vs+v1+changes#New-features)

## Links

### Documentatie

De documentatie van beide versies is hier te vinden:

- REST API v1:
  [https://archief.viaa.be/mediahaven-rest-api](https://archief.viaa.be/mediahaven-rest-api)
- REST API v2:
  [https://archief.viaa.be/mediahaven-rest-api/v2/api-docs/index.html](https://archief.viaa.be/mediahaven-rest-api/v2/api-docs/index.html)

Raadpleeg hier de MediaHaven-documentatie over de verschillen tussen REST API
v1 en v2:

- [MediaHaven Customer Support > REST API > Rest V2 vs v1
  changes](https://mediahaven.atlassian.net/wiki/spaces/CS/pages/2432303184/Rest+V2+vs+v1+changes)

