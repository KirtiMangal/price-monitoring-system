from fastapi import FastAPI
from .db import engine, Base
from . import models
from .services.fetcher import fetch_products
from .services.price_service import update_products

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "API running"}


@app.post("/refresh")
async def refresh():
    data = await fetch_products()
    update_products(data)
    return {"message": "data refreshed"}