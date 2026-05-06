from openai import OpenAI

from backend.vectorstore.search import semantic_search


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
You are an AI repository assistant.

Use the repository context below to answer the question.

Repository Context:
{context}

Question:
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

    return response.choices[0].message.content