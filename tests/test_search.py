from backend.ingestion.repo_loader import load_repository
from backend.embeddings.chunker import chunk_text
from backend.embeddings.embedder import generate_embedding
from backend.vectorstore.search import semantic_search


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


query = "FastAPI application setup"

results = semantic_search(query, documents)

for result in results:

    print("\n====================")
    print(f"Path: {result['path']}")
    print(f"Score: {result['score']}")
    print(result["content"][:300])