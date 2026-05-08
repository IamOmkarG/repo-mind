from backend.services.github_service import clone_repository


repo_path = clone_repository(
    "https://github.com/tiangolo/fastapi"
)

print(f"Repository cloned to: {repo_path}")