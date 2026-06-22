---
layout: default
title: AI metadata API
parent: Een integratie ontwikkelen
has_children: false
has_toc: true
nav_order: 8
last_modified_date: 2026-04-21
---

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## AI metadata API

Status: `v1.1.0`  
Laatst bijgewerkt: `28/05/26`

## 1. Inleiding

Met verschillende AI-technieken zoals spraak- en gezichtsherkenning, wordt door
meemoo voor geselecteerd audiovisueel materiaal specifieke, verrijkende metadata
gegenereerd. Het genereren gebeurt in zogeheten pipelines. Het uitvoeren van een
pipeline op een enkel object is een taak (of *task*), bijvoorbeeld: de
transcriptie aanmaken van een audiobestand.

De AI metadata API maakt de gegenereerde metadata
beschikbaar voor contentpartners, onder meer:

- taakresultaten van AI-verwerkingen op fragmenten
- matches tussen gedetecteerde personen en de referentieset
- metadata van personen in de referentieset
- transcripties en speech-to-textresultaten
- output van Named Entity Recognition (NER)

De API is bedoeld voor (externe) ontwikkelaars van contentpartners die de
AI-gegenereerde metadata in hun systemen willen integreren.

## 2. Authenticatie & Autorisatie

De API is alleen toegankelijk voor geautoriseerde gebruikers. Autorisatie
verloopt via een OAuth2.0 flow met Bearer Token, aan te vragen via de volgende
URL: <https://oas.hetarchief.be/token>.

De authenticatieflow gebruikt `client_credentials` als
`grant_type` met het e-mailadres en het wachtwoord van je meemoo-account als credentials
([Client Credentials - OAuth 2.0 Simplified](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/)).

### REQUEST

```shell
curl -X POST "https://oas.hetarchief.be/token" \
–u "<email>:<password>" \
-d "grant_type=client_credentials" \
-d "expires_in=3600
```

### RESPONSE

```json
{
  "access_token": "<bearer token>",
  "expires_in": 3600,
  "token_type": "bearer"
}
```

## 3. API architectuur

Deze API is een GraphQL endpoint waarnaar je een query stuurt
waarin je zelf bepaalt voor welke velden je data wil krijgen.

De API biedt een *view* per metadatatype als resultaat van een
pipeline. Elke view bevat op taakniveau het resultaat van de verwerking
uitgevoerd op een mediafragment of een match met een referentieset.

De beschikbare views en de metadatabeschrijving zijn:

- `face_tasks:` detectie van gezichten/personen op videofragmenten
- `image_tasks:` detectie van gezichten/personen op foto
- `face_matches:` matches tussen gedetecteerde personen en de referentieset voor video
- `image_matches:` matches tussen gedetecteerde personen en de referentieset voor foto
- `refset_persons`: metadata van personen in de referentieset
- `speech_tasks`: speech-to-text metadata en transcripties
- `ner_tasks`: NER en textrazor metadata

## 4. Endpoints

De API wordt aangeboden via:
<https://services.viaa.be/ai-results/v1/graphql>. De endpoint is beveiligd en
kan alleen bevraagd worden door een Bearer token mee te geven (zie boven: 2.
Authenticatie & Autorisatie). Met typische GraphQL queries kan flexibel alle of
een deel van de (meta)data van een of meer taken uit een pipeline opgevraagd
worden.

Het is mogelijk het aantal resultaten van de query te beperken met een `limit`
en door een `offset` mee te geven om bijvoorbeeld de resultaten te pagineren.
Je kan de resultaten ook filteren door een `where` clause mee te geven in de
query. De velden waarop gefiltered kan worden kunnen met een standaard
introspect query opgevraagd worden of worden ingevuld door een query builder te
gebruiken.

Bijvoorbeeld voor face_tasks:

- cluster_uuid
- cp
- match_score
- matched_time
- refset_person_id
- refset_person_name
- refset_person_wiki_id
- time_intervals

Voor meer informatie over GraphQL queries, zie [Queries | GraphQL](https://graphql.org/learn/queries/).

Het onderstaande voorbeeld van een typische query vraagt de `face_tasks` view op
via het GraphQL endpoint, waarbij `<...>` de in de response gewenste datavelden
van de view zijn. Zie verder bij hoofdstuk '5. Data views' voor een volledig
overzicht van de beschikbare velden per view.

## GRAPHQL QUERY

```graphql
query GetFaceTasks($limit: Int!, $offset: Int!, $status: [String!]) {
 face_tasks(
   limit: $limit
   offset: $offset
   where: { status: { _in: $status } }
 ) {
   <...>
 }
}
```

## cURL REQUEST

```shell
echo '{
  "query": "query GetFaceTasks($limit: Int!, $offset: Int!, $status: [String!]) {
    face_tasks(
      limit: $limit
      offset: $offset
      where: { 
        status: {
          _in: $status
        }
      }
    )
    {
      task_id
      processed_time
      status
      cp
      title
    }
  }",
  "variables": {
    "limit": 1,
    "offset": 1,
    "status": "succeeded"
  }
}' | tr -d '\n' | curl --silent \
  -X POST "https://services.viaa.be/ai-results/v1/graphql" \
  -H "Authorization: Bearer <bovenstaand bearer token>" \
  -H "Content-Type: application/json" \
  -d @-
```

## RESPONSE

```json
{
  "data": {
    "face_tasks": [
      {
        "task_id": "<task id>",
        "processed_time": "<processed time>",
        "status": "succeeded",
        "cp": "OR-xxxxxxxx",
        "title": "Example fragment"
      }
    ]
  }
}
```

## 5. Data views

- Timestamps worden weergegeven in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601) waar van toepassing.
- De precieze velden die je opvraagt, bepaal je zelf in je GraphQL-query.
- Ruwe outputvelden zoals `processed_json`, `textrazor_json`,
  `transcript_json` en `audio_classification_json` zijn bedoeld voor
  integraties die de volledige service-output willen verwerken.

### 5.1 face_matches | image_matches

Geeft matches terug tussen gedetecteerde personen en personen in de
referentieset.

#### Velden

| **Veld**                | **Beschrijving**                                             |
| :---------------------- | :----------------------------------------------------------- |
| `cluster_uuid`          | een unieke identifier voor de cluster waartoe de match behoort |
| `cp`                    | de unieke identifier van de content partner                  |
| `match_score`           | de score van de match                                      |
| `matched_time`          | het moment waarop de match gemaakt is in in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601)|
| `refset_person_id`      | de refset identifier van de gematchte persoon        |
| `refset_person_name`    | de naam van de gematchte persoon                             |
| `refset_person_wiki_id` | de wiki/Q-identifier van de gematchte persoon                |
| `time_intervals`        | een lijst van start- en eindtijden (in seconden) waarin de gematchte persoon voorkomt |

### 5.2 face_tasks | image_tasks

Geeft resultaten terug van gezichts- en persoonsdetectie op fragmenten.

| **Veld**                 | **Beschrijving**                                             |
| :----------------------- | :----------------------------------------------------------- |
| `cluster_uuids`          | een lijst van cluster uuids                                  |
| `cp`                     | de unieke identifier van de content partner                  |
| `error`                  | de foutmelding indien de task status `failed` is             |
| `external_id`            | de externe identifier van het fragment gelinkt aan de task              |
| `main_local_id`          | de interne cp-id, indien ingevuld op main-fragmentniveau en alleen voor shared-AI CP's (niet GiVE) |
| `media_object_id`        | het mediaobject-id van het fragment gelinkt aan de task         |
| `n_faces`                | het totaal aantal gezichten in de task                           |
| `n_faces_per_frame`      | het aantal gezichten per frame                        |
| `n_persons`              | het totaal aantal personen in de task                            |
| `n_persons_per_frame`    | het aantal personen per frame                         |
| `n_scenes`               | het totaal aantal scènes in de task                              |
| `perc_frames_with_faces` | het  precentage aan frames met een gezicht             |
| `pid`                    | de pid van het fragment gelinkt aan de task                     |
| `processed_time`         | het tijdstip waarop de task verwerkt is, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601)         |
| `status`                 | de verwerkingsstatus van de task, bijvoorbeeld `succeeded` of `failed`                     |
| `task_id`                | een unieke identifier voor de task                           |
| `title`                  | de titel van het fragment                                    |

### 5.3 ner_tasks

Geeft NER-resultaten en gerelateerde ruwe output terug.

| **Veld**         | **Beschrijving**                                       |
| :--------------- | :----------------------------------------------------- |
| `cp`             | de unieke identifier van de content partner            |
| `fragment_id`    | de unieke identifier van het fragment gelinkt aan de task |
| `error`          | de foutmelding indien de task status `failed` is               |
| `pid`            | de pid van het fragment gelinkt aan de task               |
| `processed_json` | de onbewerkte output van de task in JSON-formaat                         |
| `processed_time` | het tijdstip waarop de task verwerkt is, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601)      |
| `status`         | de verwerkingsstatus van de task, bijvoorbeeld `succeeded` of `failed`                  |
| `task_id`        | een unieke identifier voor de task                     |
| `textrazor_json` | de onbewerkte output van textrazor                           |

### 5.4 speech_tasks

Geeft speech-to-textresultaten, transcripties en aanverwante metadata terug.

| **Veld**                    | **Beschrijving**                                             |
| :-------------------------- | :----------------------------------------------------------- |
| `cp`                        | de unieke identifier van de content partner                  |
| `error`                     | de foutmelding indien de task status `failed` is             |
| `external_id`               | de externe identifier van het fragment gelinkt aan de task   |
| `main_local_id`             | de interne cp-id, indien ingevuld op main-fragmentniveau en alleen voor shared-AI CP's (niet GiVE) |
| `fragment_id`               | de unieke identifier van het fragment gelinkt aan de task        |
| `media_object_id`           | het mediaobject-id van het fragment gelinkt aan de task          |
| `pid`                       | de pid van het fragment gelinkt aan de task                     |
| `processed_time`            | het tijdstip waarop de task verwerkt is, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601)             |
| `statistics`                | een reeks van speechmatics stastieken                        |
| `status`                    | de verwerkingsstatus van de task, bijvoorbeeld `succeeded` of `failed`                       |
| `task_id`                   | een unieke identifier voor de task                           |
| `title`                     | de titel van het fragment                                    |
| `transcript_json`           | de onbewerkte output van textrazor in JSON-formaat                           |
| `transcript_srt`            | de transcriptie als .srt ondertitels            |
| `transcript_txt`            | de transcriptie als platte tekst      |
| `transcript_vtt`            | de transcriptie als .vtt ondertitels              |
| `audio_classification_json` | de resultaten van de audioclassificatie pipeline             |

### 5.5 refset_persons

Geeft metadata terug over personen in de referentieset.

| **Veld**       | **Beschrijving**                                             |
| :------------- | :----------------------------------------------------------- |
| `created_at`   | het tijdstip waarop de refset-entry is aangemaakt, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601)  |
| `id`           | de unieke identifier van de refset-entry                     |
| `label`        | een label van de refset-entry, bijvoorbeeld een naam                     |
| `description`  | een omschrijving van de refset entry                         |
| `modified_at`  | het tijdstip waarop de refset-entry het laatst aangepast is, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601) |
| `public_links` | een lijst van publieke links van de refset-entry             |
| `status`       | de status van de refset-entry  |

## 6. Voorbeelden van gebruik

Het gebruik van de API wordt toegelicht met 2 concrete voorbeelden in:
[give-graphql-query-examples](https://github.com/viaacode/give-graphql-query-examples).

Deze repository bevat twee use cases die de AI metadata API gebruiken:
- alle beschikbare metadata ophalen
- ruwe data downloaden

Zie ook de [README.md in de repository](https://github.com/viaacode/give-graphql-query-examples/blob/main/README.md) voor uitleg.

### 6.1 Voorbereiding

- Zorg dat Python 3.11+ geïnstalleerd is op je systeem: [Python installatie](https://www.python.org/downloads/)
- git clone [de repository](https://github.com/viaacode/give-graphql-query-examples)
- Kopieer het `.env-template` en hernoem het naar `.env`
- Vul in het `.env` bestand de `USER_EMAIL` en `PASSWORD` velden in met de waarden van een account gelinkt aan jouw organisatie
- Voer de volgende commando's uit in een terminal om de virtuele omgeving te activeren zodat de scripts kunnen gerund worden:

**Linux/MacOS:**

```shell
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip wheel
python -m pip install -r requirements.txt
```

**Windows:**

```shell
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install -U pip wheel
python -m pip install -r requirements.txt
```

### 6.2 De scripts uitvoeren

#### Metadata downloaden

Gebruik `download_meemoo_ai_data.py` om alle beschikbare metadata voor je
organisatie op te halen en lokaal als JSON op te slaan.

Het script maakt in `output/` een submap per view aan:

- `face_tasks`
- `face_image_tasks`
- `face_matches`
- `face_image_matches`
- `refset_persons`
- `speech_tasks`
- `ner_tasks`

In elke submap wordt de data gepagineerd opgeslagen. Elk JSON-bestand bevat dus
1 pagina met resultaten.

Het script verwacht dat de uitvoermap nog niet bestaat. Wil je de export opnieuw
uitvoeren, verwijder dan eerst de map `output/`.

```shell-script
# vergeet niet eerst je virtuele omgeving te activeren
python download_meemoo_ai_data.py
```

### Ruwe AI output downloaden

Gebruik daarna `download_meemoo_raw_ai_files.py` om per taak de ruwe bestanden
op te halen.

Voer dit script pas uit nadat `download_meemoo_ai_data.py` succesvol heeft
gedraaid. Het script gebruikt namelijk de eerder geëxporteerde metadata in
`output/` om te bepalen welke taken moeten worden opgehaald.

In de huidige versie van het script worden ruwe bestanden voor `speech_tasks`
gedownload naar `output/speech_tasks/tasks/<task_id>/`. Per taak kunnen daar
onder meer volgende bestanden in terechtkomen:

- `metadata.json`: metadata van de taak
- `speechmatics_raw.json`: ruwe JSON-respons van Speechmatics
- `subtitles.srt`: transcriptie in SRT-formaat
- `subtitles.vtt`: transcriptie in VTT-formaat
- `transcription.txt`: platte tekstversie van de transcriptie
- `audio_classification.json`: output van de audio-classificatie

De map `output/speech_tasks/tasks/` mag nog niet bestaan wanneer je het script
start. Wil je de ruwe bestanden opnieuw downloaden, verwijder die map dan eerst.

Afhankelijk van het aantal taken kan dit script enige tijd duren. Tijdens het
uitvoeren toont het script een voortgangsbalk.

```shell-script
# vergeet niet eerst je virtuele omgeving te activeren
python download_meemoo_raw_ai_files.py
```
