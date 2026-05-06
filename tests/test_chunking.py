from backend.ingestion.repo_loader import load_repository
from backend.embeddings.chunker import chunk_text


files = load_repository(".")

first_file = files[0]

chunks = chunk_text(first_file["content"])

print(f"File: {first_file['path']}")
print(f"Generated {len(chunks)} chunks")

for chunk in chunks[:2]:
    print("\n--- CHUNK ---\n")
    print(chunk[:300])