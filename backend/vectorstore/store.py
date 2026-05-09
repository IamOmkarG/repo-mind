import json
import os


VECTOR_STORE_PATH = "backend/storage/vector_store.json"


def save_documents(documents):

    os.makedirs(
        "backend/storage",
        exist_ok=True
    )

    with open(VECTOR_STORE_PATH, "w") as file:

        json.dump(documents, file)


def load_documents():

    if not os.path.exists(VECTOR_STORE_PATH):

        return []

    with open(VECTOR_STORE_PATH, "r") as file:

        return json.load(file)