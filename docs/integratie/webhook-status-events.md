---
layout: default
title: Webhook Status Events
parent: Een integratie ontwikkelen
has_children: false
has_toc: true
nav_order: 5
last_modified_date: 2025-12-02 17:14:05 +0200
---

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Inleiding

Dit document beschrijft het gebruik van webhooks om update events te ontvangen over aangeleverde [meemoo SIP v2.x]({{ site.baseurl }}{% link docs/diginstroom/sip/index.md %}) bestanden.

Na aanlevering wordt er een event uitgestuurd als:
- het SIP-pakket volledig en correct gearchiveerd is in het meemoo-archiefsysteem
- er ergens een fout is opgetreden in het verwerkingsproces, inclusief het meemoo-archiefsysteem Deze events bevatten een beschrijving van de fout.

Er worden geen tussentijdse _in progress_ events uitgestuurd. Enkel als de status verandert.

# Het proces vooraf

## Aanlevering van de SIP op S3

Op [de SIP-aanlevering pagina]({{ site.baseurl }}{% link docs/diginstroom/aanlevering-van-sips.md %}) staat de procedure om een S3-token aan te vragen, zodat het pakket opgeladen kan worden. Na een succesvolle transfer, vind je in de headers van het response object van de S3-transfer een correlation ID terug in de custom key `X-Correlation-ID`. Zie voorbeeld via `aws s3 cp` commando:

``` json
{
    "Server": "nginx/1.26.2",
    "Date": "Fri,11 Jul 2025 15:56:30 GMT",
    "Transfer-Encoding": "chunked",
    "Connection": "keep-alive",
    "x-amz-request-id": "981F27F72E5E7EBF-843e9ba457593d0edf69a24baa0babf3",
    "Via": "1.1 s3-qas.do.viaa.be (Cloud Gateway S3/8.2.0)",
    "Gateway-Protocol": "s3",
    "ETag": "294a6020d4588dfd92b936a1a620fcd2",
    "X-Correlation-ID": "843e9ba457593d0edf69a24baa0babf3"
}
```

Indien je bv. de Python bibliotheek `boto3` gebruikt, is het response object in de vorm van een Python dictionary, met de volgende structuur:

``` json
{
    <SNIP>
    "ResponseMetadata": {
        "HTTPStatusCode": 200,
        "RetryAttempts": 0,
        "HostId": "",
        "RequestId": "5916962FB12A52B7-a5f7312a0b9555b747361c4c407924eb",
        "HTTPHeaders": {
            "via": "1.1 s3.viaa.be (Cloud Gateway S3/7.5.0)",
            "transfer-encoding": "chunked",
            "x-correlation-id": "a5f7312a0b9555b747361c4c407924eb",
            "server": "nginx/1.21.3",
            "connection": "keep-alive",
            "x-amz-request-id": "5916962FB12A52B7-a5f7312a0b9555b747361c4c407924eb",
            "date": "Wed, 05 Apr 2023 13:11:34 GMT",
            "gateway-protocol": "s3",
            "content-type": "application/zip"
        }
    }
}
```
De correlation ID is beschikbaar via `response['ResponseMetadata']['HTTPHeaders']['x-correlation-id']`.

Deze correlation ID wordt gebruikt door het hele proces heen om de levensloop van die SIP te identificeren. Deze correlation ID is eigen aan één aanlevering van één SIP. Indien dezelfde SIP meerdere malen wordt aangeleverd dan resulteert dit in verschillende correlation ID's.

# Webhook

De implementatie van de webhooks is geïnspireerd op de [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md) richtlijnen.  Er is [een formele specificatie]({{ site.baseurl }}{% link assets/webhooks/openapi.yml %}) beschikbaar in de vorm van [de OpenAPI specificatie v3.1.x](https://spec.openapis.org/oas/v3.1.1.html). Dit beschrijft zowel de HTTP-request als de structuur van het uitgestuurde event.

Hieronder staan we even stil bij enkele elementen van de specificatie, maar ook bij bepaalde aspecten die buiten de scope van de formele specificatie vallen.

## Registratie

Indien je geïnteresseerd bent om statusupdates te krijgen via webhooks moet je contact opnemen met [meemoo support](mailto:support@meemoo.be). Het is momenteel niet mogelijk om op een automatische manier, zoals bv. web-interface of REST API, webhooks te registreren en/of te beheren.

Er zijn wel enkele administratieve zaken die moeten gedeeld worden, met name de `endpoint` en de `shared secret` (Zie: [Headers](#headers)). Dit gebeurt in samenspraak met meemoo. 

Eén webhook registratie heeft betrekking tot één S3-bucket. Dit wil zeggen dat er naar de endpoint van de webhook events gestuurd worden voor alle SIP-bestanden die in die bucket opgeladen worden.

## Payload

De webhook is een HTTP POST-verzoek. Het feitelijke event bevindt zich in de HTTP-body in de vorm van een JSON.

De structuur van de payload:
- `type`: Het type van het event, in dot-notated vorm. Dit is momenteel altijd `meemoo.sip.archived`.
- `timestamp`: De tijdstempel wanneer het event heeft plaats gevonden. Dit is niet noodzakelijk wanneer het event wordt verzonden.  Deze tijdstempel is in het ISO 8601 formaat.
- `data`: De eigenlijke event data geassocieerd met het event.
    - `correlation_id`: Dit is de correlation ID zoals [hierboven](#aanlevering-van-de-sip-op-s3) beschreven.
    - `outcome`: De uitkomst van het event: "success" of "failure".
    - `message`: Bijhorende informatie over het event, in het geval van een gefaald event. [Optioneel]
    - `pid`: De meemoo-PID van de ingestroomde SIP, indien aanwezig. [Optioneel]


Voorbeeld:
``` json
{
  "type": "meemoo.sip.archived",
  "timestamp": "2025-09-03T20:26:10.344522Z",
  "data": {
    "correlation_id": "843e9ba457593d0edf69a24baa0babf3",
    "outcome": "success",
    "pid": "kdleipkyuj"
  }
}
```

Een SIP is succesvol gearchiveerd indien het event, met bijhorende `correlation_id`, als `type` de waarde `meemoo.sip.archived` én als `outcome` de waarde `success` heeft. Indien de `outcome` de waarde `failure` heeft, onafhankelijk van het `type`, is de SIP gefaald tijdens instroom. Opgepast: wanneer er niet-fatale (herstelbare) fouten voorkomen tijdens instroom, is het mogelijk dat er een "success" wordt uitgestuurd voor een SIP waarvoor er eerder een "failure" werd uitgestuurd.

De formele specificatie in de vorm van een JSON-schema vind je in de [OpenAPI specificatie](https://github.com/viaacode/sipin-status-webhook-documentation/blob/main/openapi.yml)

## Headers

De payload van de webhook wordt verzonden als de body van een HTTP POST-verzoek. De aanvullende data over de webhook zit dan vervat in de HTTP-headers:

- `webhook-id`: de unieke identificatie van het event van de webhook. Deze is geassocieerd met het event en blijft dezelfde indien het event meerdere malen zou uitgestuurd worden.
- `webhook-timestamp`: een integer UNIX tijdstempel (aantal seconden sinds de epoch). Deze tijdstempel beschrijft het moment van het uitsturen van de webhook. Indien éénzelfde event meerdere malen wordt uitgestuurd, zal deze tijdstempel een andere waarde hebben.
- `webhook-signature`: één of meerdere (door een spatie gescheiden) handtekening(en) van deze webhook, waarvan er minstens 1 geldig is.

Een handtekening in `webhook-signature` is een symmetrische handtekening met de volgende inhoud: `{msg_id}.{timestamp}.{payload}` (concatenatie van deze drie velden, gescheiden door een punt), en met de volgende eigenschappen:

|                         | Symmetrische handtekening                                             |
| ----------------------- | --------------------------------------------------------------------- |
| Handtekening schema     | `HMAC-SHA256`                                                         |
| Signering secret        | Shared secret. Willekeurig, minstens 24 bytes (192 bits)              |
| Serialisatie secret     | base64 geëncodeerd, met prefix `whsec_` voor eenvoudige identificatie. |
| Handtekening identifier | `v1`                                                                  |

De "serialisatie secret" beschrijft hoe de secret geserialiseerd wordt. Zoals hierboven beschreven, is de secret key een aantal willekeurige bytes. Stel dat de eigenlijke secret b"alongwebhookmeemoosecret" is, dan is de serialisatie `whsec_YWxvbmd3ZWJob29rbWVlbW9vc2VjcmV0` (whsec_{base64encode(b"alongwebhookmeemoosecret")}).

De "handtekening identifier" wordt als een soort versie vooraan aan de handtekening toegevoegd, wanneer deze geserialiseerd en doorgestuurd wordt in de webhook. De handtekening zelf wordt geëncodeerd als base64. Bijvoorbeeld: `v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=` (v1,{base64encode(signature_in_bytes)}).

### Voorbeeld
Laten we even alles samen brengen. Neem een webhook met volgende `id` en `tijdstempel`:

```
webhook-id: msg_333a3NGSYKk1vyFtMgj9Qy8gm3y
webhook-timestamp: 1758548009
```

Met als payload (de exacte body van het HTTP-verzoek):
``` json
{"type": "meemoo.sip.archived", "timestamp": "2025-09-03T20:26:10.344522Z", "data": {"correlation_id": "843e9ba457593d0edf69a24baa0babf3", "outcome": "success", "pid": "kdleipkyuj"}}
```

Dit resulteert in de volgende te signeren inhoud:
```
msg_333a3NGSYKk1vyFtMgj9Qy8gm3y.1758548009.{"type": "meemoo.sip.archived", "timestamp": "2025-09-03T20:26:10.344522Z", "data": {"correlation_id": "843e9ba457593d0edf69a24baa0babf3", "outcome": "success", "pid": "kdleipkyuj"}}
```
Voor de secret `whsec_YWxvbmd3ZWJob29rbWVlbW9vc2VjcmV0` krijg je de volgende handtekening, geserialiseerd in de header:
```
webhook-signature: v1,cVueLJYV5JY6qXHw3+MIHbZCPHHnX7N7jjaebaI2+5o=
```


Je vindt in de [standard-webhooks repo](https://github.com/standard-webhooks/standard-webhooks/tree/main/libraries) bibliotheken voor enkele gangbare talen zoals bv. Python, Golang, Java... Deze faciliteren o.m. het signeren en het valideren van de webhook. We raden aan deze implementaties, indien mogelijk, te gebruiken, of op zijn minst op een manier te incorporeren. Vele van deze bibliotheken zijn ook gepubliceerd in hun respectievelijke repositories.

## Beveiliging
In het kader van webhooks, kunnen we deze verschillende beveiligingsaspecten identificeren:
- `authenticiteit`: is de afzender wel degelijk de afzender die die beweert te zijn?
- `integriteit`: is de webhook onderweg niet onderschept, en aangepast?
- `herspeelbaarheid`: kunnen we identificeren of een webhook al uitgezonden en verwerkt is?


| Authenticiteit   | Integriteit  | Herspeelbaarheid                                          |
| ---------------- | ------------ | --------------------------------------------------------  |
| handtekening     | handtekening | Combinatie van webhook identifier en webhook tijdstempel  | 

De serverimplementatie heeft een zekere vrijheid om te verifiëren wat die zelf nodig acht.

Er is nog een extra laag van beveiliging in de vorm van TLS. De endpoint **moet** een HTTPS-endpoint zijn. Op deze manier is de payload geëncrypteerd.

## Leverbaarheid en betrouwbaarheid
Het uitsturen van webhooks kan op meerdere manieren falen, van problemen in de connectie, tot problemen aan de serverkant. Als het event succesvol is toegekomen, stuurt de webhook een response met de status code `2xx` terug. In alle andere gevallen proberen we het event opnieuw uit te sturen gebaseerd op een herhalingsschema met een *incremental backoff*. Een mogelijk herhalingsschema:

| Vertraging      | Tijd sinds start  |
| --------------- | ----------------- |
| Onmiddellijk    | 00:00:00          |
| 5 seconden      | 00:00:05          |
| 5 minuten       | 00:05:05          |
| 30 minuten      | 00:35:05          |
| 2 uren          | 02:35:05          |
| 5 uren          | 07:35:05          |
| 10 uren         | 17:35:05          |
| 10 uren         | 27:35:05          |

Indien er na een periode van 72 uur geen succesvolle webhooks kunnen uitgestuurd worden, zal het systeem stoppen met het uitsturen van events naar de afgesproken endpoint. Er moet dan contact opgenomen worden met [meemoo support](mailto:support@meemoo.be).

Merk op dat we een time-out implementeren van 15 seconden. Indien er na 15 seconden geen antwoord is, wordt de webhook als gefaald geïnterpreteerd. De webhook zal opnieuw uitgestuurd worden volgens het hierboven beschreven principe.

We garanderen niet dat elk event exact eenmaal wordt uitgestuurd. Hou er dus rekening mee dat (in uitzonderlijke gevallen) een event meerdere keren kan uitgezonden worden ("at least once semantics").
