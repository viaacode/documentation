**AI Metadata API**

**Version:** `v1.1.1`

# Using the AI Metadata API

## 1. Introduction

With various AI techniques such as speech- and face recognition, meemoo generates specific, enriching metadata for selected audiovisual material. This metadata is generated in so-called pipelines. Running a pipeline on a single object is a task (or *task*), for example: creating a transcript for an audio file.

The AI metadata API makes the generated metadata available for content partners, including:

- Task results of AI processing on fragments
- Matches between detected persons and the reference set
- Metadata of persons in the reference set
- Transcripts and speech-to-text results
- Output of Named Entity Recognition (NER)

The API is intended for (external) developers of content partners who want to integrate the AI-generated metadata into their systems.

## 2. Authentication & Authorization

The API is only accessible to authorized users. Authorization proceeds via an OAuth2.0 flow with Bearer Token, requesting it from the following URL: <https://oas.hetarchief.be/token>.

The authentication flow uses `client_credentials` as `grant_type` with the e-mail address and password of your meemoo account as credentials ([Client Credentials - OAuth 2.0 Simplified](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/)).

### REQUEST

```shell
curl -X POST "https://oas.hetarchief.be/token" \
-u "<email>:<password>" \
-d "grant_type=client_credentials" \
-d "expires_in=3600"
```

### RESPONSE

```json
{
  "access_token": "<bearer token>",
  "expires_in": 3600,
  "token_type": "bearer"
}
```

## 3. API Architecture

This API is a GraphQL endpoint to which you send a query specifying which fields you want data for.

The API provides a *view* per metadata type as the result of a pipeline. At the task level, each view contains the result of processing performed on a media fragment or a match with the reference set.

The available views and metadata descriptions are:

- `face_tasks`: detection of faces/people on video fragments
- `image_tasks`: detection of faces/people on photos
- `face_matches`: matches between detected persons and the reference set for video
- `image_matches`: matches between detected persons and the reference set for photo
- `refset_persons`: metadata of persons in the reference set
- `speech_tasks`: speech-to-text metadata and transcripts
- `ner_tasks`: NER and textrazor metadata

## 4. Endpoints

The API is offered at: <https://services.viaa.be/ai-results/v1/graphql>. The endpoint is secured and can only be accessed by providing a Bearer token (see above: 2. Authentication & Authorization). With typical GraphQL queries, you can flexibly request all or part of the (meta)data of one or more tasks from a pipeline.

It is possible to limit the number of results of the query with a `limit` and by providing an `offset` to paginate results, for example. You can also filter results by a `where` clause in the query. The fields on which you can filter can be obtained by a standard introspection query or by using a query builder.

For example, for `face_matches`:

- `cluster_uuid`
- `cp`
- `match_score`
- `matched_time`
- `refset_person_id`
- `refset_person_name`
- `refset_person_wiki_id`
- `time_intervals`

For more information about GraphQL queries, see [Learn GraphQL: Queries](https://graphql.org/learn/queries/).

The following example of a typical query requests the `face_tasks` view via the GraphQL endpoint, where `<...>` are the desired data fields of the view. See section '5. Data views' for a complete overview of the available fields per view.

### GRAPHQL QUERY

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

### cURL REQUEST

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
    "status": ["succeeded"]
  }
}' | tr -d '\n' | curl --silent \
  -X POST "https://services.viaa.be/ai-results/v1/graphql" \
  -H "Authorization: Bearer <bovenstaand bearer token>" \
  -H "Content-Type: application/json" \
  -d @-
```

### RESPONSE

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

## 5. Data Views

- Timestamps are displayed in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601) where applicable.
- The exact fields you request are determined by your GraphQL query.
- Raw output fields such as `processed_json`, `textrazor_json`, `transcript_json` and `audio_classification_json` are intended for integrations that want to process the full service output.

### 5.1 face_matches | image_matches

Returns matches between detected persons and persons in the reference set.

**Field** | **Description**
--- | ---
`cluster_uuid` | a unique identifier for the cluster to which the match belongs
`cp` | the unique identifier of the content partner
`match_score` | the match score
`matched_time` | the moment the match was made, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601)
`refset_person_id` | the refset identifier of the matched person
`refset_person_name` | the name of the matched person
`refset_person_wiki_id` | the wiki/Q-identifier of the matched person
`time_intervals` | a list of start and end times (in seconds) where the matched person occurs

### 5.2 face_tasks | image_tasks

Returns results of face and person detection on fragments.

**Field** | **Description**
--- | ---
`cluster_uuids` | a list of cluster uuids
`cp` | the unique identifier of the content partner
`error` | the error message if the task status is `failed`
`external_id` | the external identifier of the fragment linked to the task
`main_local_id` | the internal cp-id, filled on main-fragment level and only for shared-AI CPs (not GiVE)
`media_object_id` | the media object ID of the fragment linked to the task
`n_faces` | total number of faces in the task
`n_faces_per_frame` | number of faces per frame
`n_persons` | total number of persons in the task
`n_persons_per_frame` | number of persons per frame
`n_scenes` | total number of scenes in the task
`perc_frames_with_faces` | percentage of frames with a face
`pid` | the pid of the fragment linked to the task
`processed_time` | the processing time of the task, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601)
`status` | the processing status of the task, e.g., `succeeded` or `failed`
`task_id` | a unique identifier for the task
`title` | the title of the fragment

### 5.3 ner_tasks

Returns NER results and related raw output.

**Field** | **Description**
--- | ---
`cp` | the unique identifier of the content partner
`fragment_id` | the unique identifier of the fragment linked to the task
`error` | the error message if the task status is `failed`
`pid` | the pid of the fragment linked to the task
`processed_json` | the raw output of the task in JSON format
`processed_time` | the processing time of the task, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601)
`status` | the processing status of the task, e.g., `succeeded` or `failed`
`task_id` | a unique identifier for the task
`textrazor_json` | the raw output of textrazor

### 5.4 speech_tasks

Returns speech-to-text results, transcripts, and related metadata.

**Field** | **Description**
--- | ---
`cp` | the unique identifier of the content partner
`error` | the error message if the task status is `failed`
`external_id` | the external identifier of the fragment linked to the task
`main_local_id` | the internal cp-id, filled on main-fragment level and only for shared-AI CPs (not GiVE)
`fragment_id` | the unique identifier of the fragment linked to the task
`media_object_id` | the media object ID of the fragment linked to the task
`pid` | the pid of the fragment linked to the task
`processed_time` | the processing time of the task, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601)
`statistics` | a series of Speechmatics statistics
`status` | the processing status of the task, e.g., `succeeded` or `failed`
`task_id` | a unique identifier for the task
`title` | the title of the fragment
`transcript_json` | the raw transcript output in JSON format
`transcript_srt` | the transcript as .srt subtitles
`transcript_txt` | the transcript as plain text
`transcript_vtt` | the transcript as .vtt subtitles
`audio_classification_json` | the results of the audio classification pipeline

### 5.5 refset_persons

Returns metadata about persons in the reference set.

**Field** | **Description**
--- | ---
`created_at` | the time the reference set entry was created, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601)
`id` | the unique identifier of the reference set entry
`label` | a label of the reference set entry, e.g., a name
`description` | a description of the reference set entry
`modified_at` | the time the reference set entry was last modified, in [ISO-8601](https://developer.meemoo.be/docs/metadata/viaa/datatypes.html#iso8601)
`public_links` | a list of public links of the reference set entry
`status` | the status of the reference set entry

## 6. Examples of Use

Usage of the API is illustrated with two concrete examples in: [give-graphql-query-examples](https://github.com/viaacode/give-graphql-query-examples).

This repository contains two use cases that utilize the AI metadata API:

- retrieving all available metadata
- downloading raw data

See also the [README.md in the repository](https://github.com/viaacode/give-graphql-query-examples/blob/main/README.md) for explanation.

### 6.1 Preparation

- Ensure Python 3.11+ is installed on your system: [Python installation](https://www.python.org/downloads/)
- git clone [the repository](https://github.com/viaacode/give-graphql-query-examples)
- Copy the `.env-template` and rename it to `.env`
- Fill in the `USER_EMAIL` and `PASSWORD` fields in `.env` with the values of an account linked to your organization
- Run the following commands in a terminal to activate the virtual environment so the scripts can be executed:

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

### 6.2 Running the Scripts

#### Download Metadata

Use `download_meemoo_ai_data.py` to retrieve all available metadata for your organization and store it locally as JSON.

The script creates a subfolder per view in:

- `face_tasks`
- `image_tasks`
- `face_matches`
- `image_matches`
- `refset_persons`
- `speech_tasks`
- `ner_tasks`

Each JSON file contains one page of results.

The script expects the output folder to not exist yet. If you want to re-run the export, delete the `output/` folder first.

```shell
# Remember to first activate your virtual environment
python download_meemoo_ai_data.py
```

#### Download Raw AI Files

Use `download_meemoo_raw_ai_files.py` to retrieve raw files for each task.

Run this script only after `download_meemoo_ai_data.py` has successfully completed. The current version of the script uses the previously exported metadata in `output/` to determine which tasks to fetch.

In the current version, raw files for `speech_tasks` are downloaded to `output/speech_tasks/tasks/<task_id>/`. For each task, you may find files such as:

- `metadata.json`: metadata of the task
- `speechmatics_raw.json`: raw JSON response from Speechmatics
- `subtitles.srt`: transcript in SRT format
- `subtitles.vtt`: transcript in VTT format
- `transcription.txt`: plain text version of the transcript
- `audio_classification.json`: output of the audio classification pipeline

The `output/speech_tasks/tasks/` folder must not exist when you start the script. If you want to re-download the raw files, delete that folder first.

Depending on the number of tasks, this script may take some time. During execution, it displays a progress bar.

```shell
# Remember to first activate your virtual environment
python download_meemoo_raw_ai_files.py
```
