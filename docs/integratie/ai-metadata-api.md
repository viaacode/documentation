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

# AI metadata API

Status: `v1.0.0`  
Laatst bijgewerkt: `16/2/26`

## Inleiding

De AI metadata API ontsluit alle door meemoo gegenereerde AI-metadata voor
contentpartners. Die metadata wordt opgebouwd tijdens de verwerking van
video- en audiofragmenten door verschillende AI-services.

De API maakt onder meer volgende gegevens beschikbaar:

- taakresultaten van AI-verwerkingen op fragmenten
- matches tussen gedetecteerde personen en de referentieset
- metadata van personen in de referentieset
- transcripties en speech-to-textresultaten
- output van Named Entity Recognition (NER)

De API is bedoeld voor ontwikkelaars die AI-resultaten willen integreren in hun
eigen systemen.

## API architectuur

Deze API gebruikt GraphQL. Je stuurt dus een query naar één endpoint en bepaalt
zelf welke velden je terugkrijgt.

De API is opgebouwd rond verschillende query views. Elke view ontsluit een
specifiek type AI-metadata:

- `face_(image_)tasks`
- `face_(image_)matches`
- `refset_persons`
- `speech_tasks`
- `ner_tasks`

## Athenticatie

De API gebruikt Bearer-tokenauthenticatie.

Vraag eerst een access token aan via `https://oas.hetarchief.be/token`:

```bash
curl -X POST "https://oas.hetarchief.be/token" \
  -u "<email>:<password>" \
  -d "grant_type=client_credentials" \
  -d "expires_in=3600"
```

Voorbeeldresponse:

```json
{
  "access_token": "<bearer token>",
  "expires_in": 3600,
  "token_type": "bearer"
}
```

Gebruik het ontvangen token daarna in de `Authorization` header:

```http
Authorization: Bearer <bearer token>
```

## Endpoint

Alle GraphQL-requests worden gestuurd naar:

```text
https://services.viaa.be/ai-results/v1/graphql
```

## Request naar de API

Een GraphQL-request is een `POST`-request met een JSON-body. De query staat in
het `query`-veld van die body.

### Voorbeeld request

```bash
curl -X POST "https://services.viaa.be/ai-results/v1/graphql" \
  -H "Authorization: Bearer <bearer token>" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query GetSpeechTasks($limit: Int!, $offset: Int!, $status: [String!]) { speech_tasks(limit: $limit, offset: $offset, where: { status: { _in: $status } }) { task_id processed_time status cp title } }",
    "variables": {
      "limit": 10,
      "offset": 0,
      "status": ["succeeded"]
    }
  }'
```

### Voorbeeld response

```json
{
  "data": {
    "speech_tasks": [
      {
        "task_id": "<task id>",
        "processed_time": "<processed time>",
        "status": "succeeded",
        "cp": "OR-xxxxxxxx",
        "title": "Voorbeeld fragment"
      }
    ]
  }
}
```

Voor meer achtergrond over de opbouw van GraphQL-queries, zie
[Queries | GraphQL](https://graphql.org/learn/queries/).

## Views

### `face_(image_)matches`

Geeft matches terug tussen gedetecteerde personen en personen in de
referentieset.

#### Velden

| Veld | Beschrijving |
| --- | --- |
| `cluster_uuid` | Unieke identifier van de cluster waartoe de match behoort. |
| `cp` | Unieke identifier van de contentpartner. |
| `match_score` | Score van de match. |
| `matched_time` | Tijdstip waarop de match gemaakt is, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601). |
| `refset_person_id` | Refset-identifier van de gematchte persoon. |
| `refset_person_name` | Naam van de gematchte persoon. |
| `refset_person_wiki_id` | Wikidata-/Q-identifier van de gematchte persoon. |
| `time_intervals` | Lijst van start- en eindtijden, in seconden, waarin de gematchte persoon voorkomt. |

### `face_(image_)tasks`

Geeft resultaten terug van gezichts- en persoonsdetectie op fragmenten.

#### Velden

| Veld | Beschrijving |
| --- | --- |
| `cluster_uuids` | Lijst van cluster-UUID's. |
| `cp` | Unieke identifier van de contentpartner. |
| `error` | Foutmelding wanneer de taskstatus `failed` is. |
| `external_id` | Externe identifier van het fragment gelinkt aan de task. |
| `main_local_id` | Interne cp-id indien ingevuld op main-fragmentniveau. Niet beschikbaar voor give-cp's, wel voor shared-AI-cp's. |
| `media_object_id` | Mediaobject-id van het fragment gelinkt aan de task. |
| `n_faces` | Totaal aantal gezichten in de task. |
| `n_faces_per_frame` | Aantal gezichten per frame. |
| `n_persons` | Totaal aantal personen in de task. |
| `n_persons_per_frame` | Aantal personen per frame. |
| `n_scenes` | Totaal aantal scènes in de task. |
| `perc_frames_met_faces` | Percentage frames waarin een gezicht voorkomt. |
| `pid` | PID van het fragment gelinkt aan de task. |
| `processed_time` | Tijdstip waarop de task verwerkt is, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601). |
| `status` | Verwerkingsstatus van de task, bijvoorbeeld `succeeded` of `failed`. |
| `task_id` | Unieke identifier van de task. |
| `title` | Titel van het fragment. |

#### Voorbeeld query

```graphql
query GetFaceTasks($limit: Int!, $offset: Int!, $status: [String!]) {
  face_tasks(
    limit: $limit
    offset: $offset
    where: { status: { _in: $status } }
  ) {
    task_id
    pid
    title
    n_faces
    n_persons
    n_scenes
    processed_time
    status
  }
}
```

### `ner_tasks`

Geeft NER-resultaten en gerelateerde ruwe output terug.

#### Velden

| Veld | Beschrijving |
| --- | --- |
| `cp` | Unieke identifier van de contentpartner. |
| `error` | Foutmelding wanneer de taskstatus `failed` is. |
| `fragment_id` | Unieke identifier van het fragment gelinkt aan de task. |
| `pid` | PID van het fragment gelinkt aan de task. |
| `processed_json` | Ruwe output van de task in JSON-vorm. |
| `processed_time` | Tijdstip waarop de task verwerkt is, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601). |
| `status` | Verwerkingsstatus van de task, bijvoorbeeld `succeeded` of `failed`. |
| `task_id` | Unieke identifier van de task. |
| `textrazor_json` | Ruwe output van TextRazor. |

#### Voorbeeld query

```graphql
query GetNerTasks($limit: Int!, $offset: Int!, $status: [String!]) {
  ner_tasks(
    limit: $limit
    offset: $offset
    where: { status: { _in: $status } }
  ) {
    task_id
    pid
    cp
    status
    processed_time
    processed_json
    textrazor_json
  }
}
```

### `speech_tasks`

Geeft speech-to-textresultaten, transcripties en aanverwante metadata terug.

#### Velden

| Veld | Beschrijving |
| --- | --- |
| `cp` | Unieke identifier van de contentpartner. |
| `error` | Foutmelding wanneer de taskstatus `failed` is. |
| `external_id` | Externe identifier van het fragment gelinkt aan de task. |
| `fragment_id` | Unieke identifier van het fragment gelinkt aan de task. |
| `main_local_id` | Interne cp-id indien ingevuld op main-fragmentniveau. Niet beschikbaar voor give-cp's, wel voor shared-AI-cp's. |
| `media_object_id` | Mediaobject-id van het fragment gelinkt aan de task. |
| `pid` | PID van het fragment gelinkt aan de task. |
| `processed_time` | Tijdstip waarop de task verwerkt is, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601). |
| `statistics` | Reeks Speechmatics-statistieken. |
| `status` | Verwerkingsstatus van de task, bijvoorbeeld `succeeded` of `failed`. |
| `task_id` | Unieke identifier van de task. |
| `title` | Titel van het fragment. |
| `transcript_json` | Transcriptie in JSON-formaat. |
| `transcript_srt` | Transcriptie in SRT-formaat. |
| `transcript_txt` | Transcriptie als platte tekst. |
| `transcript_vtt` | Transcriptie in VTT-formaat. |
| `audio_classification_json` | Resultaten van de audioclassificatiepipeline. |

#### Voorbeeld query

```graphql
query GetSpeechTasks($limit: Int!, $offset: Int!, $status: [String!]) {
  speech_tasks(
    limit: $limit
    offset: $offset
    where: { status: { _in: $status } }
  ) {
    task_id
    processed_time
    status
    cp
    title
    transcript_txt
  }
}
```

#### Voorbeeld query met transcript formats

```graphql
query GetSpeechTaskTranscripts($limit: Int!, $offset: Int!) {
  speech_tasks(limit: $limit, offset: $offset) {
    task_id
    pid
    title
    transcript_txt
    transcript_srt
    transcript_vtt
    transcript_json
  }
}
```

### `refset_persons`

Geeft metadata terug over personen in de referentieset.

#### Velden

| Veld | Beschrijving |
| --- | --- |
| `created_at` | Tijdstip waarop de refset-entry is aangemaakt, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601). |
| `description` | Omschrijving van de refset-entry. |
| `id` | Unieke identifier van de refset-entry. |
| `label` | Label van de refset-entry, bijvoorbeeld een naam. |
| `modified_at` | Tijdstip waarop de refset-entry het laatst aangepast is, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601). |
| `public_links` | Lijst van publieke links van de refset-entry. |
| `status` | Status van de refset-entry. |

#### Voorbeeld query

```graphql
query GetRefsetPersons {
  refset_persons {
    id
    label
    description
    public_links
    status
  }
}
```

#### Voorbeeld query met timestamps

```graphql
query GetRefsetPersonsmetTimestamps {
  refset_persons {
    id
    label
    created_at
    modified_at
    status
    public_links
  }
}
```

## Notes

- Timestamps worden weergegeven in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601) waar van toepassing.
- De precieze velden die je opvraagt, bepaal je zelf in je GraphQL-query.
- Ruwe outputvelden zoals `processed_json`, `textrazor_json`,
  `transcript_json` en `audio_classification_json` zijn bedoeld voor
  integraties die de volledige service-output willen verwerken.

## Voorbeeldimplementaties
## Over Hasura
Hasura is een open-source engine die automatisch een GraphQL APO genereert bovenop een relationele database, zoals PostgreSQL.
Hierdoor kan je queries uitvoeren zonder zelf complexe backend code te schrijven.

## Over de repository
Er worden twee voorbeeldscript ter beschikking gesteld om alle data gelinkt aan een contentpartner te downloaden via Hasura en GraphQL queries.

## Vooraf te doen
- Zorg dat python beschikbaar is op je systeem:
  - [Python installatie](https://www.python.org/downloads/)

- Kopieer het [`.env-template`]({{ site.baseurl }}/assets/ai_scripts/.env-template) en hernoem het naar `.env`
- In het nieuwe `.env` bestand:
  - Vul de USER_EMAIL en PASSWORD velden in van een account gelinkt aan jouw organisatie

- Voer de volgende commando's uit in een terminal om de virtuele omgeving te activeren zodat de scripts kunnen gerund worden:

Linux:
```
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip wheel
python -m pip install -r requirements.txt
```

Windows:
```
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install -U pip wheel
python -m pip install -r requirements.txt
```

## De voorbeeldscripts uitvoeren

### Metadata downloaden
Gebruik [`download_meemoo_ai_data.py`]({{ site.baseurl }}/assets/ai_scripts/download_meemoo_ai_data.py) om alle beschikbare metadata voor je organisatie op te halen en lokaal als JSON op te slaan.

Het script maakt in `output/` een submap per view aan:

- `face_tasks`
- `face_image_tasks`
- `face_matches`
- `face_image_matches`
- `refset_persons`
- `speech_tasks`
- `ner_tasks`

In elke submap wordt de data paginagewijs opgeslagen. Elk JSON-bestand bevat dus een pagina met resultaten.

Het script verwacht dat de uitvoermap nog niet bestaat. Wil je de export opnieuw uitvoeren, verwijder dan eerst de map `output/`.

```
# vergeet niet eerst je virtuele omgeving te activeren
python download_meemoo_ai_data.py
```

### Ruwe AI output downloaden
Gebruik daarna [`download_meemoo_raw_ai_files.py`]({{ site.baseurl }}/assets/ai_scripts/download_meemoo_raw_ai_files.py) om per taak de ruwe bestanden op te halen.

Voer dit script pas uit nadat `download_meemoo_ai_data.py` succesvol heeft gedraaid. Het script gebruikt namelijk de eerder geëxporteerde metadata in `output/` om te bepalen welke taken moeten worden opgehaald.

In de huidige versie van het script worden ruwe bestanden voor `speech_tasks` gedownload naar `output/speech_tasks/tasks/<task_id>/`. Per taak kunnen daar onder meer volgende bestanden in terechtkomen:

- `metadata.json`: metadata van de taak
- `speechmatics_raw.json`: ruwe JSON-respons van Speechmatics
- `subtitles.srt`: transcriptie in SRT-formaat
- `subtitles.vtt`: transcriptie in VTT-formaat
- `transcription.txt`: platte tekstversie van de transcriptie
- `audio_classification.json`: output van de audio-classificatie

De map `output/speech_tasks/tasks/` mag nog niet bestaan wanneer je het script start. Wil je de ruwe bestanden opnieuw downloaden, verwijder die map dan eerst.

Afhankelijk van het aantal taken kan dit script enige tijd duren. Tijdens het uitvoeren toont het script een voortgangsbalk.

```
# vergeet niet eerst je virtuele omgeving te activeren
python download_meemoo_raw_ai_files.py
```
