# from fastapi import FastAPI
# from .db import engine, Base
# from . import models
# from .services.fetcher import fetch_products
# from .services.price_service import update_products
# from .db import engine, Base, SessionLocal
# from fastapi import HTTPException

# app = FastAPI()

# # create tables
# Base.metadata.create_all(bind=engine)

# @app.get("/")
# def home():
#     return {"message": "API running"}


# @app.post("/refresh")
# async def refresh():
#     data = await fetch_products()
#     update_products(data)
#     return {"message": "data refreshed"}

    

# @app.get("/products")

# def get_products(category: str = None, min_price: float = None, max_price: float = None):
#     db = SessionLocal()
#     query = db.query(models.Product)

#     if category:
#         query = query.filter(models.Product.category == category)

#     if min_price:
#         query = query.filter(models.Product.current_price >= min_price)

#     if max_price:
#         query = query.filter(models.Product.current_price <= max_price)

#     products = query.all()
#     db.close()

#     return products

    

    

    

# # def get_products():
# #     db = SessionLocal()
# #     products = db.query(models.Product).all()
# #     db.close()
# #     return products

from fastapi import FastAPI, HTTPException
from sqlalchemy import func

from .db.database import engine, SessionLocal
from .db.models import Base
from .db import models

from .services.fetcher import fetch_products
from .services.price_service import update_products

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "API running"}


# 🔥 REFRESH API
@app.post("/refresh")
async def refresh():
    data = await fetch_products()
    update_products(data)
    return {"message": "data refreshed"}


# 🔥 GET ALL PRODUCTS (WITH FILTERING)
@app.get("/products")
def get_products(category: str = None, min_price: float = None, max_price: float = None):
    db = SessionLocal()
    query = db.query(models.Product)

    if category:
        query = query.filter(models.Product.category == category)

    if min_price:
        query = query.filter(models.Product.current_price >= min_price)

    if max_price:
        query = query.filter(models.Product.current_price <= max_price)

    products = query.all()
    db.close()

    return products


# 🔥 GET PRODUCT BY ID + HISTORY
@app.get("/products/{id}")
def get_product(id: int):
    db = SessionLocal()

    product = db.query(models.Product).filter_by(id=id).first()

    if not product:
        db.close()
        raise HTTPException(status_code=404, detail="Product not found")

    history = db.query(models.PriceHistory).filter_by(product_id=id).all()

    db.close()

    return {
        "product": product,
        "history": history
    }


# 🔥 ANALYTICS
@app.get("/analytics")
def analytics():
    db = SessionLocal()

    total = db.query(models.Product).count()
    avg_price = db.query(func.avg(models.Product.current_price)).scalar()

    db.close()

    return {
        "total_products": total,
        "avg_price": avg_price
    }