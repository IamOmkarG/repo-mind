from backend.ingestion.repo_loader import load_repository
from backend.embeddings.chunker import chunk_text
from backend.embeddings.embedder import generate_embedding
from backend.services.rag_service import answer_repository_question


files = load_repository(".")

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


query = "What does this repository do?"

answer = answer_repository_question(
    query=query,
    documents=documents
)

print("\n====================\n")

print(answer)