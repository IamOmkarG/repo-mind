from openai import OpenAI

from backend.vectorstore.search import (
    semantic_search
)


client = OpenAI()


def answer_repository_question(query, documents):

    search_results = semantic_search(
        query=query,
        documents=documents,
        top_k=3
    )

    context = "\n\n".join(
        [
            result["content"]
            for result in search_results
        ]
    )

    prompt = f"""
You are RepoMind, an AI repository intelligence assistant.

Your job is to answer developer questions about a code repository.

Guidelines:
- Be concise and technical.
- Avoid repetition.
- Focus on implementation details when possible.
- Use bullet points when useful.
- If the repository context is insufficient, say so clearly.
- Do not invent functionality not present in the repository.
- Prioritize source code behavior over configs/docs.

Repository Context:
{context}

Developer Question:
{query}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    sources = [
        {
            "path": result["path"],
            "score": round(result["score"], 4)
        }
        for result in search_results
    ]

    return {
        "answer": answer,
        "sources": sources
    }