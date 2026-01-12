---
layout: default
title: Hasura API
parent: Een integratie ontwikkelen
has_children: false
nav_order: 6
---

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


# Hasura API documentatie
## Over Hasura
Hasura is een open-source engine die automatisch een GraphQL API genereert bovenop een relationele database, zoals PostgreSQL.
Hierdoor kan je queries uitvoeren zonder zelf complexe backend code te schrijven.

## Over de repository
Er worden twee voorbeeldscript ter beschikking gesteld om alle data gelinkt aan een CP te downloaden via Hasura en GraphQL queries.

## Vooraf te doen
- Zorg dat python beschikbaar is op je systeem:
  - [Python installatie](https://www.python.org/downloads/)

- Kopieer het `.env-template` en hernoem het naar `.env`
- In het nieuwe `.env` bestand:
  - Vul de USER_EMAIL en PASSWORD veldjes in van een account gelinkt aan jouw CP

- Voer de volgende commando's uit in een terminal om de virtuele omgeving te activeren zodat de scripts kunnen gerund worden:

## Linux:
```
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip wheel
python -m pip install -r requirements.txt
```

## Windows:
```
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install -U pip wheel
python -m pip install -r requirements.txt
```

## De voorbeeldscripts uitvoeren
### Metadata downloaden
Het script `download_meemoo_ai_data.py` is bedoeld om één keer te draaien om alle data in JSON-formaat op te halen.
De data wordt opgeslagen in de map `./output/<table_name>` voor alle tabellen:

- **face_(image)_tasks**: alle face-taken waarbij gezichten/personen worden gedetecteerd in video’s(/afbeeldingen) (draait slechts één keer per fragment)
- **face_(image)_matches**: alle overeenkomsten van de gedetecteerde personen in de video’s(/afbeeldingen) (draait elke nacht)
- **refset_persons**: metadata van alle personen in de refset (alleen metadata, geen vingerafdrukken of afbeeldingen)
- **speech_tasks**: alle speech-taken waarbij STT wordt uitgevoerd op video/audio
- **ner_tasks**: alle NER-taken waarbij NER wordt uitgevoerd op de transcripties

Elk JSON-bestand vertegenwoordigt één pagina met data, waarbij het achtervoegsel van het JSON-bestand de specifieke pagina aangeeft.

Als je nieuwe data wilt ophalen, verwijder dan de map outputs (indien aanwezig) en voer het script opnieuw uit.
Het script zou binnen 5 minuten moeten draaien, afhankelijk van hoeveel data is verwerkt.

```
# vergeet niet de virtuele omgeving te activeren
python download_meemoo_ai_data.py
```

### De ruwe data downloaden
Daarnaast kan het script `download_meemoo_raw_files.py` worden uitgevoerd om alle ruwe bestanden van ner_tasks en speech_tasks te downloaden.

- **speech_tasks/tasks/<task_id>**
  - metadata.json: metadata van die individuele taak
  - speechmatics_raw.json: ruwe JSON-respons van Speechmatics
  - subtitles.srt: ondertitels in SRT-formaat
  - subtitles.vtt: ondertitels in VTT-formaat
  - transcription.txt: ruwe tekst van de transcriptie
  - adio_classfication.json: metadata van de audio-classificatie
- **ner_tasks/tasks/<task_id>**
  - metadata.json: metadata van die individuele taak
  - textrazor_raw.json: ruwe Textrazor-respons
  - processed.json: verwerkte NER-data met tijdstempels

Het script downloadt ALLE ruwe data, dus zorg ervoor dat de map tasks binnen de mappen ner_tasks en speech_tasks nog niet bestaat.

Dit script zal lang duren omdat het de ruwe bestanden voor elke NER-/speech-taak moet downloaden.
De voortgangsbalk geeft een indicatie van de duur.

```
# vergeet niet de virtuele omgeving te activeren
python download_meemoo_raw_files.py
```
