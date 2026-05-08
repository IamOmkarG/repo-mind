import json

from pathlib import Path


VECTOR_STORE_PATH = Path(
    "backend/storage/vector_store.json"
)


def save_documents(documents):

    with open(VECTOR_STORE_PATH, "w") as file:

        json.dump(documents, file)


def load_documents():

    if not VECTOR_STORE_PATH.exists():

        return []

    with open(VECTOR_STORE_PATH, "r") as file:

        return json.load(file)