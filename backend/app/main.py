from fastapi import FastAPI, HTTPException
from sqlalchemy import func
from pydantic import BaseModel

from .db.database import engine, SessionLocal
from .db.models import Base
from .db import models

from .services.fetcher import fetch_products
from .services.price_service import update_products

from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import joinedload

from fastapi import Depends
from .auth import verify_api_key

from .auth import (
    hash_password,
    verify_password,
    create_access_token
)

request_count=0
app = FastAPI()
Base.metadata.create_all(bind=engine)

class AuthRequest(BaseModel):
    username: str
    password: str

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
async def refresh(api_key: str = Depends(verify_api_key)):
    data = await fetch_products()
    update_products(data)
    return {"message": "data refreshed"}

@app.get("/events")
def get_events(api_key: str = Depends(verify_api_key)):
    db = SessionLocal()
    events = db.query(models.PriceChangeEvent).all()
    db.close()
    return events


@app.get("/products")
def get_products(
    category: str = None,
    min_price: float = None,
    max_price: float = None,
    api_key: str = Depends(verify_api_key)
):
    global request_count
    request_count += 1

    db = SessionLocal()

    products = db.query(models.Product).all()
    result = []

    for p in products:
        listings = db.query(models.Listing).filter_by(product_id=p.id).all()

        # get first listing price (simple approach)
        price = listings[0].current_price if listings else None

        # apply filters manually (since price is in Listing)
        if min_price and price is not None and price < min_price:
            continue
        if max_price and price is not None and price > max_price:
            continue
        if category and p.category != category:
            continue

        result.append({
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "price": price
        })

    db.close()
    return result


@app.get("/products/{id}")
def get_product(id: int, api_key: str = Depends(verify_api_key)):

    global request_count
    request_count += 1

    db = SessionLocal()

    # db = SessionLocal()

    product = db.query(models.Product).filter_by(id=id).first()

    if not product:
        db.close()
        raise HTTPException(status_code=404, detail="Product not found")

    # history = db.query(models.PriceHistory).filter_by(product_id=id).all()

    # pehle listing nikaal
    listings = db.query(models.Listing).filter_by(product_id=id).all()

    history = []

    for listing in listings:
        h = db.query(models.PriceHistory).filter_by(listing_id=listing.id).all()
        history.extend(h)

    db.close()

    return {
        "product": product,
        "history": history
    }


@app.get("/analytics")
def analytics(api_key: str = Depends(verify_api_key)):

    global request_count
    request_count += 1

    db = SessionLocal()

    total_products = db.query(models.Product).count()

    # ✅ FIX: get avg price from Listing table
    avg_price = db.query(func.avg(models.Listing.current_price)).scalar()

    db.close()

    return {
        "total_products": total_products,
        "avg_price": avg_price
    }

@app.get("/usage")
def usage(api_key: str = Depends(verify_api_key)):
    return {"total_requests": request_count}

@app.post("/signup")
def signup(data: AuthRequest):
    db = SessionLocal()

    existing_user = db.query(models.User).filter(models.User.username == data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = models.User(
        username=data.username,
        password=hash_password(data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {"message": "User created successfully"}


@app.post("/login")
def login(data: AuthRequest):
    db = SessionLocal()

    user = db.query(models.User).filter(models.User.username == data.username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Wrong password")

    token = create_access_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }