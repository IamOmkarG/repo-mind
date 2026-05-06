from backend.embeddings.embedder import generate_embedding


text = "authentication middleware using JWT tokens"

embedding = generate_embedding(text)

print(f"Embedding length: {len(embedding)}")

print(embedding[:10])