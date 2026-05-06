from fastapi import FastAPI

app = FastAPI(title="RepoMind")


@app.get("/")
def health_check():
    return {"status": "RepoMind is running"}