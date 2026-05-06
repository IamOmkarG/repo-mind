from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".java",
    ".go",
    ".md",
    ".json",
    ".yaml",
    ".yml",
}

IGNORED_DIRECTORIES = {
    "venv",
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    "node_modules",
    "tests",
}


def load_repository(repo_path: str):
    """
    Scan repository files and load supported code/content files.
    """

    repo_files = []

    root_path = Path(repo_path)

    for file_path in root_path.rglob("*"):

        # Skip ignored directories
        if any(part in IGNORED_DIRECTORIES for part in file_path.parts):
            continue

        # Skip directories
        if file_path.is_dir():
            continue

        # Skip unsupported files
        if file_path.suffix not in SUPPORTED_EXTENSIONS:
            continue

        try:
            content = file_path.read_text(encoding="utf-8")

            repo_files.append(
                {
                    "path": str(file_path),
                    "content": content,
                }
            )

        except Exception:
            # Skip unreadable files
            continue

    return repo_files