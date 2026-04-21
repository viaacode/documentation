import os
from pathlib import Path

from dotenv import load_dotenv
from utils.auth import get_bearer_token
from utils.constants import OUTPUT_DIR
from utils.hasura import yield_results_pages
from utils.inout import write_page_data
from utils.queries import (
    FACE_IMAGE_MATCHES_QUERY,
    FACE_IMAGE_TASKS_QUERY,
    FACE_MATCHES_QUERY,
    FACE_TASKS_QUERY,
    NER_TASKS_QUERY,
    REFSET_PERSONS_QUERY,
    SPEECH_TASKS_QUERY,
)

VIEW_TO_ID_TYPE_MAPPER = {
    'face_matches': 'cluster_uuid',
    'face_image_matches': 'cluster_uuid',
    'face_tasks': 'task_id',
    'face_image_tasks': 'task_id',
    'ner_tasks': 'task_id',
    'refset_persons': 'id',
    'speech_tasks': 'task_id',
}
VIEW_TO_QUERY_MAPPER = {
    'face_matches': FACE_MATCHES_QUERY,
    'face_image_matches': FACE_IMAGE_MATCHES_QUERY,
    'face_tasks': FACE_TASKS_QUERY,
    'face_image_tasks': FACE_IMAGE_TASKS_QUERY,
    'ner_tasks': NER_TASKS_QUERY,
    'refset_persons': REFSET_PERSONS_QUERY,
    'speech_tasks': SPEECH_TASKS_QUERY,
}


def download_meemoo_ai_data(url: str, token: str, output_dir: Path, page_size: int):
    for view, query in VIEW_TO_QUERY_MAPPER.items():
        variables = {'limit': page_size, 'offset': 0}

        pages_folder = output_dir / view
        if pages_folder.exists():
             raise FileExistsError(
                'Remove the outputs folder before running this script.'
            )
        pages_folder.mkdir(parents=True)

        for page, offset in yield_results_pages(
            url=url,
            token=token,
            view=view,
            query=query,
            variables=variables,
            page_size=page_size,
        ):
            id_type = VIEW_TO_ID_TYPE_MAPPER[view]
            write_page_data(
                id_type=id_type,
                folder=pages_folder,
                page=page,
                offset=offset,
                page_size=page_size,
            )


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

    # download the metadata
    download_meemoo_ai_data(
        url=url, token=token, output_dir=OUTPUT_DIR, page_size=page_size
    )