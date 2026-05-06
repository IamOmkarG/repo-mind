import numpy as np

from backend.embeddings.embedder import generate_embedding


def cosine_similarity(vec1, vec2):

    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )


def semantic_search(query, documents, top_k=3):

    query_embedding = generate_embedding(query)

    results = []

    for document in documents:

        similarity = cosine_similarity(
            query_embedding,
            document["embedding"]
        )

        results.append(
            {
                "content": document["content"],
                "score": similarity,
                "path": document["path"]
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]