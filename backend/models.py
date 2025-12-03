from sqlalchemy import Column, Integer, Float, Text, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from pgvector.sqlalchemy import Vector
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text, unique=True)
    title = Column(Text)
    price = Column(Float)
    description = Column(Text)
    images = Column(ARRAY(Text))
    features = Column(ARRAY(Text))
    category = Column(Text)

class ProductChunk(Base):
    __tablename__ = "product_chunks"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    chunk_text = Column(Text)
    embedding = Column(Vector(384))
