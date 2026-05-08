from fastapi import APIRouter

from backend.ingestion.repo_loader import load_repository
from backend.embeddings.chunker import chunk_text
from backend.embeddings.embedder import generate_embedding
from backend.services.rag_service import answer_repository_question
from backend.models.request_models import AskRequest


router = APIRouter()


# Load repository files
files = load_repository(".")


# Build searchable document store
documents = []


for file in files:

    chunks = chunk_text(file["content"])

    for chunk in chunks:

        embedding = generate_embedding(chunk)

        documents.append(
            {
                "path": file["path"],
                "content": chunk,
                "embedding": embedding
            }
        )


@router.get("/health")
def health():

    return {
        "status": "healthy"
    }


@router.post("/ask")
def ask_repository(request: AskRequest):

    answer = answer_repository_question(
        query=request.question,
        documents=documents
    )

    return {
        "question": request.question,
        "answer": answer
    }