import shutil
import subprocess

from pathlib import Path


TEMP_REPO_PATH = Path("temp_repo")


def clone_repository(repo_url: str):

    # Remove old repo if exists
    if TEMP_REPO_PATH.exists():

        shutil.rmtree(TEMP_REPO_PATH)

    # Clone repository
    subprocess.run(
        [
            "git",
            "clone",
            repo_url,
            str(TEMP_REPO_PATH)
        ],
        check=True
    )

    return TEMP_REPO_PATH