import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from tqdm import tqdm
from utils.auth import get_bearer_token
from utils.constants import OUTPUT_DIR
from utils.hasura import get_presigned_urls_by_task_id
from utils.inout import write_task_data

RAW_FILE_KEY_FILE_NAME_MAPPER = {
    'presigned_json': 'speechmatics_raw.json',
    'presigned_vtt': 'subtitles.vtt',
    'presigned_srt': 'subtitles.srt',
    'presigned_txt': 'transcription.txt',
    'presigned_processed_json': 'processed.json',
    'presigned_textrazor_json': 'textrazor_raw.json',
    'presigned_audio_classification_json': 'audio_classification.json',
}


def download_meemoo_raw_files(url: str, token: str, output_dir: Path):
    # folders = ['ner_tasks', 'speech_tasks']
    folders = ['speech_tasks']
    for folder in folders:
        pages_folder = output_dir / folder
        if not pages_folder.exists():
            raise FileNotFoundError(
                'Run the download_meemoo_ai_data script before this one.'
            )
        tasks_folder = pages_folder / 'tasks'
        if tasks_folder.exists():
            raise FileExistsError(
                (
                    f'Remove the tasks folder in the {folder} folder'
                    ' before running this script.'
                )
            )
        tasks_folder.mkdir(parents=True)
        files = pages_folder.rglob('*.json')
        for file in files:
            with file.open('r') as fid:
                page_proc = json.load(fid)

            for task_id, task in tqdm(
                page_proc.items(), desc=f'Processing {file.name}'
            ):
                presigned_urls = get_presigned_urls_by_task_id(
                    url=url, token=token, view=folder, task_id=task_id
                )

                # download all files with a proper file name
                files = {
                    RAW_FILE_KEY_FILE_NAME_MAPPER[k]: requests.get(url).content
                    for k, url in presigned_urls.items()
                    if url is not None
                }
                task_folder = tasks_folder / task_id
                task_folder.mkdir(parents=True, exist_ok=True)
                write_task_data(folder=task_folder, files=files, task=task)


if __name__ == '__main__':
    # load all environment variables from .env file
    load_dotenv()
    url = os.getenv('ENDPOINT')
    token_url = os.getenv('TOKEN_ENDPOINT')
    email = os.getenv('USER_EMAIL')
    password = os.getenv('PASSWORD')
    expires_in = int(os.getenv('EXPIRES_IN'))
    page_size = int(os.getenv('PAGE_SIZE'))

    # get a token
    token = get_bearer_token(
        url=token_url, email=email, password=password, expires_in=expires_in
    )

    # download the raw files
    download_meemoo_raw_files(url=url, token=token, output_dir=OUTPUT_DIR)