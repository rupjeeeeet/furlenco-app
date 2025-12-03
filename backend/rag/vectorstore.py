# rag/vectorstore.py

from database import SessionLocal
from models import ProductChunk

def save_chunk(product_id, text, embedding):
    db = SessionLocal()
    row = ProductChunk(
        product_id=product_id,
        chunk_text=text,
        embedding=embedding
    )
    db.add(row)
    db.commit()
    db.close()
