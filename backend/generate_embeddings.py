# generate_embeddings.py

from database import SessionLocal
from models import Product
from rag.chunker import chunk_product
from rag.embedder import get_embedding
from rag.vectorstore import save_chunk

def run():
    db = SessionLocal()

    products = db.query(Product).all()
    print(f"Found {len(products)} products.")

    for product in products:
        chunks = chunk_product(product)
        print(f"Product {product.id}: {len(chunks)} chunks")

        for chunk in chunks:
            emb = get_embedding(chunk)
            save_chunk(product.id, chunk, emb)

    print("Embedding generation complete!")

if __name__ == "__main__":
    run()
