# rag/retriever.py

from sqlalchemy import text
from database import SessionLocal
from rag.embedder import get_embedding

def retrieve(query: str, k: int = 5):
    db = SessionLocal()

    query_embedding = get_embedding(query)

    sql = text("""
    SELECT product_id, chunk_text,
    embedding <=> (:embedding)::vector AS distance
    FROM product_chunks
    ORDER BY distance ASC
    LIMIT :k;
    """)

    rows = db.execute(sql, {"embedding": query_embedding, "k": k}).fetchall()

    db.close()
    return rows
