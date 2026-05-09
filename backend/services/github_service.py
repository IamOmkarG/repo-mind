import os
import shutil
import zipfile
import requests


TEMP_REPO_PATH = "temp_repo"
ZIP_PATH = "repo.zip"


def clone_repository(repo_url: str):

    if os.path.exists(TEMP_REPO_PATH):
        shutil.rmtree(TEMP_REPO_PATH)

    if os.path.exists(ZIP_PATH):
        os.remove(ZIP_PATH)

    zip_url = repo_url.rstrip("/") + "/archive/refs/heads/master.zip"

    response = requests.get(zip_url)

    if response.status_code != 200:
        zip_url = repo_url.rstrip("/") + "/archive/refs/heads/main.zip"
        response = requests.get(zip_url)

    response.raise_for_status()

    with open(ZIP_PATH, "wb") as file:
        file.write(response.content)

    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall(".")

    extracted_folder = [
        name
        for name in os.listdir(".")
        if name.startswith(repo_url.split("/")[-1] + "-")
    ][0]

    os.rename(extracted_folder, TEMP_REPO_PATH)

    return TEMP_REPO_PATH