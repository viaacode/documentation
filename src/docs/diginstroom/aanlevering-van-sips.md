---
layout: default
title: Aanlevering van SIPs
parent: Digitale instroom
has_children: false
has_toc: true
nav_order: 2
last_modified_date: 2024-01-25T11:15:40+0100
---

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


# Introductie

Deze pagina beschrijft hoe een meemoo-SIP aan te leveren via S3.

# Vooraf

* Je kan meemoo-SIPs maken (zie: [docs/diginstroom/sip/]({{ site.baseurl }}{% link docs/diginstroom/sip/index.md %})).
* Je hebt een S3-bucket aangevraagd via [support@meemoo.be](mailto:support@meemoo.be).

# S3-token aanvragen

Met je meemoo-account kan je een S3-token aanvragen. Hiervoor heb je nodig:

* je "_common name_": dit is jouw naam zoals die in [LDAP](https://nl.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol) is gekend,
* het paswoord van jouw account,
* een vrij te kiezen _secret_ (een combinatie van letters, cijfers en tekens dat verschilt van je paswoord) die je zal gebruiken samen met je S3-token,
* de [OR-id](https://support.meemoo.be/hc/nl/articles/6089958726673-Communicatie-over-mijn-organisatie#hoe-vermeldt-meemoo-mijn-organisatienaam-op-interne-en-externe-platformen) van de organisatie waartoe je behoort.

Je "_common name_" is doorgaans gewoon je voornaam en je familienaam. Om zeker te zijn van de schrijfwijze kan je dit verifiëren via de _Mijn profiel_ pagina. 
De _Mijn profiel_ pagina is – afhankelijk van de omgeving – beschikbaar op volgende URL's:

<table >
  <colgroup>
    <col style="width: 15%;">
    <col style="width: 85%;">
  </colgroup>
  <tbody>
    <tr>
      <th>
        <p style="text-align: center;"><strong>QAS</strong></p>
      </th>
      <td>
        <p>https://qas.hetarchief.be/nl/account/mijn-profiel</p>
      </td>
    </tr>
    <tr>
      <th>
        <p style="text-align: center;"><strong>PRD</strong></p>
      </th>
      <td>
        <p>https://hetarchief.be/nl/account/mijn-profiel</p>
      </td>
    </tr>
  </tbody>
</table>

De OR-id van jouw organisatie vind je terug in de metadata van elk object in het [MAM](https://support.meemoo.be/hc/nl/categories/6039894771857-Het-meemoo-archiefsysteem), naast _CP ID_. 
Het MAM is - afhankelijk van de omgeving - beschikbaar op volgende URL's:

<table >
  <colgroup>
    <col style="width: 15%;">
    <col style="width: 85%;">
  </colgroup>
  <tbody>
    <tr>
      <th>
        <p style="text-align: center;"><strong>INT</strong></p>
      </th>
      <td>
        <p>https://archief-int.do.viaa.be/</p>
      </td>
    </tr>
    <tr>
      <th>
        <p style="text-align: center;"><strong>QAS</strong></p>
      </th>
      <td>
        <p>https://archief-qas.viaa.be/</p>
      </td>
    </tr>
    <tr>
      <th>
        <p style="text-align: center;"><strong>PRD</strong></p>
      </th>
      <td>
        <p>https://archief.viaa.be/</p>
      </td>
    </tr>
  </tbody>
</table>

De gebruikersnaam waarmee je een S3-token aanvraagt is: `common name+or-id`. Bijvoorbeeld:

```
Jef Metdepet+or-123abcd
```

{: .important }
**Let op**: zet het `or`\-gedeelte van je OR-id om in kleine letters! `OR-123abcd` moet dus `or-123abcd` worden.

Een token vraag je aan via een POST-call naar het token-endpoint per omgeving:

<table >
  <colgroup>
    <col style="width: 15%;">
    <col style="width: 85%;">
  </colgroup>
  <tbody>
    <tr>
      <th>
        <p style="text-align: center;"><strong>INT</strong></p>
      </th>
      <td>
        <p>https://s3-int.do.viaa.be/_admin/manage/tenants/&lt;tenant&gt;/tokens</p>
      </td>
    </tr>
    <tr>
      <th>
        <p style="text-align: center;"><strong>QAS</strong></p>
      </th>
      <td>
        <p>https://s3-qas.viaa.be/_admin/manage/tenants/&lt;tenant&gt;/tokens</p>
      </td>
    </tr>
    <tr>
      <th>
        <p style="text-align: center;"><strong>PRD</strong></p>
      </th>
      <td>
        <p>https://s3.viaa.be/_admin/manage/tenants/&lt;tenant&gt;/tokens</p>
      </td>
    </tr>
  </tbody>
</table>

{: .important }
**Let op**: de INT-omgeving is niet publiek bereikbaar! Wens je hiervoor een token aan te vragen, neem dan contact op met meemoo via [support@meemoo.be](mailto:support@meemoo.be).

Om voor een gebruiker een token aan te vragen, voer je een POST-call uit met de nodige metadata als headers naar het endpoint van de omgeving waarvoor je een token wil aanvragen.

Een token aanvragen voor de QAS-omgeving zou er dan zo uitzien:

```bash
curl -X POST \
    -H "X-User-Secret-Key-Meta: MyS3Secret" \
    -H "X-User-Token-Expires-Meta: +10" \
    -u "Jef Metdepet+or-123abcd" https://s3-qas.viaa.be/_admin/manage/tenants/OR-123abcd/tokens
```

Waarbij de headers volgende betekenis hebben:

*   `X-User-Secret-Key-Meta`: dit is het vrij te kiezen _secret_ waarmee je samen met de token zult authenticeren (dit is dus verschillend van het paswoord dat je gebruikt om in te loggen).
*   `X-User-Token-Expires-Meta`: dit is de levensduur van je token, uitgedrukt in dagen. Het is een goed idee deze levensduur zo kort mogelijk te zetten.
*   Je gebruikt de gebruikersnaam zoals hierboven vermeld (`Jef Metdepet+or-123abcd`).
*   In het endpoint gebruik je als `<tenant>` de OR-id van jouw organisatie (hier met `OR` in hoofdletters!).


Vervolgens wordt er naar je paswoord gevraagd. Daarna krijg je een token terug in de volgende vorm:

```json
{
  "token": "8b89d382891a33f8f05f875c7086f1f3",
  "owner": "Jef Metdepet",
  "scope": "+or-123abcd",
  "expiration": "2024-01-10T12:39:08.877Z",
  "creation": "2024-01-05T12:39:08.000Z",
  "secret": "MyS3Secret"
}
```

Met deze `token` en `secret` kan je nu verbinden met de S3-server en SIP's uploaden. Voor meer info over het werken met S3 of het opzetten van een integratie met S3, zie: [https://docs.aws.amazon.com/s3/index.html](https://docs.aws.amazon.com/s3/index.html).

# S3 benaderen met de AWS CLI

Alle Amazon Web Services kunnen ook via CLI ("_command line interface_")
benaderd worden via de _AWS Command Line Interface_. Alle documentatie over
deze tool kan je vinden op
[https://aws.amazon.com/cli/](https://aws.amazon.com/cli/). We gaan er hier
verder van uit dat de AWS CLI is geïnstalleerd op jouw systeem.

## Configuratie

Met de in de vorige sectie bekomen token en jouw secret, kan een AWS profiel
worden ingesteld. Bv.:

```shell
aws configure --profile jef@s3-qas
```

Volgende configuratie opties moeten dan meegegeven worden:

```
AWS Access Key ID [None]:       <- vul hier het token in
AWS Secret Access Key [None]:   <- vul hier je gekozen secret in
Default region name [None]:     <- mag leeg blijven
Default output format [None]:   <- mag leeg blijven
```

Dit profiel wordt geactiveerd door de `AWS_PROFILE` variabele te exporteren in je shell:

```
export AWS_PROFILE=jef@s3-qas
```

## Operaties

**Opgelet**

Je moet altijd het meemoo-specifieke S3-endpoint configureren in je integratie of meegeven bij elke operatie. Dit zijn:

* **INT**: `s3-int.do.viaa.be`
* **QAS**: `s3-qas.viaa.be`
* **PRD**: `s3.viaa.be`

### Objecten oplijsten: `ls`

Bijvoorbeeld:

```
aws s3 ls s3://or-123abcd/ --endpoint https://s3-qas.viaa.be --recursive --human-readable --summarize
```

### Objecten opladen: `cp`

Bijvoorbeeld:

```
aws s3 cp ./local-file.ext s3://or-123abcd/ --endpoint https://s3-qas.viaa.be
```

