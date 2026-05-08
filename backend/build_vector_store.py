from backend.ingestion.repo_loader import load_repository
from backend.embeddings.chunker import chunk_text
from backend.embeddings.embedder import generate_embedding
from backend.vectorstore.store import save_documents


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


save_documents(documents)

print(f"Saved {len(documents)} documents")