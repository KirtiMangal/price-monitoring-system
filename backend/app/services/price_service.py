# from ..db.models import Product, PriceHistory
# from ..db.database import SessionLocal
# from .notifier import notify_price_change

# def update_products(data):
#     db = SessionLocal()

#     for item in data:
#         product = db.query(Product).filter_by(
#             name=item["name"], source=item["source"]
#         ).first()

#         # 🆕 New product
#         if not product:
#             product = Product(
#                 name=item["name"],
#                 category=item["category"],
#                 source=item["source"],
#                 current_price=item["price"]
#             )
#             db.add(product)
#             db.commit()
#             db.refresh(product)

#             history = PriceHistory(
#                 product_id=product.id,
#                 price=item["price"]
#             )
#             db.add(history)

#         # 🔄 Existing product
#         else:
#             if product.current_price != item["price"]:
#                 product.current_price = item["price"]

#                 history = PriceHistory(
#                     product_id=product.id,
#                     price=item["price"]
#                 )
#                 db.add(history)

#                 notify_price_change(product.name, item["price"])

#                 # print("Price changed!")

#         db.commit()

#     db.close()

from ..db.models import Product, Listing, PriceHistory, PriceChangeEvent
from ..db.database import SessionLocal
from .notifier import notify_price_change

def update_products(data):
    db = SessionLocal()

    try:
        for item in data:
            # product = db.query(Product).filter_by(
            #     name=item["name"],
            #     source=item["source"]
            # ).first()

            product = db.query(Product).filter_by(
                name=item["name"]
            ).first()

            # 🆕 NEW PRODUCT
            # if not product:
            #     product = Product(
            #         name=item["name"],
            #         category=item["category"],
            #         source=item["source"],
            #         current_price=item["price"]
            #     )
            #     db.add(product)
            #     db.flush()   # 🔥 better than commit (gets ID immediately)

            #     db.add(PriceHistory(
            #         product_id=product.id,
            #         price=item["price"]
            #     ))

            # # 🔄 EXISTING PRODUCT
            # else:
            #     if product.current_price != item["price"]:
            #         old_price = product.current_price
            #         product.current_price = item["price"]

            #         db.add(PriceHistory(
            #             product_id=product.id,
            #             price=item["price"]
            #         ))

            #         db.add(PriceChangeEvent(
            #             product_id=product.id,
            #             old_price=old_price,
            #             new_price=item["price"]
            #         ))

            #         # 🔥 SAFE NOTIFY (won't break system)
            #         try:
            #             notify_price_change(
            #                 product.name,
            #                 old_price,
            #                 item["price"]
            #             )
            #         except Exception as e:
            #             print("Notifier failed:", e)

            # 🆕 NEW PRODUCT
            if not product:
                product = Product(
                    name=item["name"],
                    category=item["category"]
                )
                db.add(product)
                db.flush()

            # 🟢 LISTING CHECK
            listing = db.query(Listing).filter_by(
                product_id=product.id,
                source=item["source"]
            ).first()

            # 🆕 NEW LISTING
            if not listing:
                listing = Listing(
                    product_id=product.id,
                    source=item["source"],
                    current_price=item["price"],
                    url=item.get("url")
                )
                db.add(listing)
                db.flush()

                db.add(PriceHistory(
                    listing_id=listing.id,
                    price=item["price"]
                ))

            # 🔄 EXISTING LISTING
            else:
                if listing.current_price != item["price"]:
                    old_price = listing.current_price
                    listing.current_price = item["price"]

                    db.add(PriceHistory(
                        listing_id=listing.id,
                        price=item["price"]
                    ))

                    db.add(PriceChangeEvent(
                        listing_id=listing.id,
                        old_price=old_price,
                        new_price=item["price"]
                    ))

                    try:
                        notify_price_change(
                            item["name"],
                            old_price,
                            item["price"]
                        )
                    except Exception as e:
                        print("Notifier failed:", e)

        db.commit()

    except Exception as e:
        db.rollback()
        raise e
        # print("DB error:", e)

    finally:
        db.close()