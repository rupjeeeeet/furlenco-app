# rag/pipeline.py

from rag.retriever import retrieve
from rag.llm import llm_answer

def rag_chat(query: str):
    # Step 1 — Retrieve vector matches
    results = retrieve(query)

    # Combine chunk_text for LLM
    context = "\n\n".join([row.chunk_text for row in results])

    # Step 2 — LLM reasoning
    answer = llm_answer(query, context)

    # Unique product IDs
    product_ids = list({row.product_id for row in results})

    return {
        "answer": answer,
        "products": product_ids
    }
