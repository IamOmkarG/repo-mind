from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from backend.services.rag_service import (
    answer_repository_question,
    stream_repository_answer
)

from backend.vectorstore.store import load_documents

from backend.models.request_models import (
    AskRequest,
    IndexRequest
)

from backend.services.rag_service import (
    answer_repository_question
)

from backend.services.indexing_service import (
    index_repository
)


router = APIRouter()


@router.get("/health")
def health():

    return {
        "status": "healthy"
    }


@router.post("/index")
def index_repository_route(request: IndexRequest):

    total_documents = index_repository(
        request.repo_url
    )

    return {
        "message": "Repository indexed successfully",
        "documents_indexed": total_documents
    }


@router.post("/ask")
def ask_repository(request: AskRequest):

    documents = load_documents()

    result = answer_repository_question(
        query=request.question,
        documents=documents
    )

    return {
        "question": request.question,
        "answer": result["answer"],
        "sources": result["sources"]
    }

@router.post("/ask-stream")
def ask_repository_stream(request: AskRequest):

    documents = load_documents()

    stream = stream_repository_answer(
        query=request.question,
        documents=documents
    )

    return StreamingResponse(
        stream,
        media_type="text/plain"
    )