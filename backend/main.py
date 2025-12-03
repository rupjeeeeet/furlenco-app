from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from scraper import scrape_furlenco
from database import get_db
from models import Product

# RAG pipeline import
from rag.pipeline import rag_chat

import os
print(">>> USING DB:", os.getenv("DATABASE_URL"))

from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="Scraper + PostgreSQL API + RAG Chatbot",
    description="Scrapes products, stores them in PostgreSQL, and provides a RAG chatbot for recommendations.",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Scraping endpoint
@app.get("/get-data", summary="Scrape 25–30 Furlenco products")
def scrape_many(limit: int = Query(30), db: Session = Depends(get_db)):
    try:
        products = scrape_furlenco(limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    inserted = 0
    updated = 0

    for prod in products:
        existing = db.query(Product).filter(Product.url == prod["url"]).first()
        if existing:
            existing.title = prod["title"]
            existing.price = prod["price"]
            existing.description = prod["description"]
            existing.images = prod["images"]
            existing.features = prod["features"]
            updated += 1
        else:
            new = Product(
                url=prod["url"],
                title=prod["title"],
                price=prod["price"],
                description=prod["description"],
                images=prod["images"],
                features=prod["features"],
            )
            db.add(new)
            inserted += 1

    db.commit()

    return {
        "inserted": inserted,
        "updated": updated,
        "scraped": len(products),
        "products": products
    }



@app.get("/products", summary="Get all products")
def get_products(db: Session = Depends(get_db)):
    items = db.query(Product).all()
    return items

@app.get("/product/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    item = db.query(Product).filter(Product.id == product_id).first()
    if not item:
        raise HTTPException(404, "Product not found")
    return item


@app.post("/chat", summary="Ask AI for product recommendations")
def chat(body: dict):
    query = body.get("query")
    if not query:
        raise HTTPException(400, "Missing 'query' in body")

    response = rag_chat(query)
    return response
