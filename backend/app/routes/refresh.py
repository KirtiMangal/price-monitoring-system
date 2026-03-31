@app.post("/refresh")
async def refresh(api_key: str = Depends(verify_api_key)):
    data = await fetch_products()
    db = SessionLocal()

    for item in data:
        product = db.query(models.Product).filter_by(name=item["name"]).first()

        if product:
            old_price = product.current_price

            # update price
            product.current_price = item["current_price"]

            # CHECK PRICE CHANGE
            if old_price != item["current_price"]:
                event = models.PriceChangeEvent(
                    product_id=product.id,
                    old_price=old_price,
                    new_price=item["current_price"]
                )
                db.add(event)

    db.commit()
    db.close()

    return {"message": "data refreshed + notifications checked"}