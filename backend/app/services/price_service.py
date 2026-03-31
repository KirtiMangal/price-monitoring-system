from ..models import Product, PriceHistory
from ..db import SessionLocal

def update_products(data):
    db = SessionLocal()

    for item in data:
        product = db.query(Product).filter_by(
            name=item["name"], source=item["source"]
        ).first()

        # 🆕 New product
        if not product:
            product = Product(
                name=item["name"],
                category=item["category"],
                source=item["source"],
                current_price=item["price"]
            )
            db.add(product)
            db.commit()
            db.refresh(product)   # 🔥 IMPORTANT FIX

            history = PriceHistory(
                product_id=product.id,
                price=item["price"]
            )
            db.add(history)

        # 🔄 Existing product
        else:
            if product.current_price != item["price"]:
                product.current_price = item["price"]

                history = PriceHistory(
                    product_id=product.id,
                    price=item["price"]
                )
                db.add(history)

                print("Price changed!")

        db.commit()

    db.close()