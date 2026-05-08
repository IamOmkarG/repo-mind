from fastapi import FastAPI

from backend.api.routes import router


app = FastAPI(title="RepoMind")


app.include_router(router)