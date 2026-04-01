# import random

# async def fetch_products():
#     return [
#         {
#             "name": "Bag A",
#             "category": "bags",
#             "source": "Grailed",
#             "price": random.randint(100, 200)
#         },
#         {
#             "name": "Watch B",
#             "category": "watches",
#             "source": "1stdibs",
#             "price": random.randint(300, 500)
#         }
#     ]

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

async def fetch_products():

    sources = [
    ("data/grailed_amiri_apparel_02.json", "grailed"),
    ("data/fashionphile_tiffany_01.json", "fashionphile"),
    ("data/1stdibs_chanel_belts_01.json", "1stdibs"),
]

    # sources = [
    #     (os.path.join(BASE_DIR, "data/grailed_amiri.json"), "grailed"),
    #     (os.path.join(BASE_DIR, "data/fashionphile.json"), "fashionphile"),
    #     (os.path.join(BASE_DIR, "data/1stdibs.json"), "1stdibs"),
    # ]

    all_products = []

    for file_path, source in sources:

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            # handle single object vs list
            if isinstance(data, dict):
                data = [data]

        for item in data:
            normalized = normalize_data(item, source)
            all_products.append(normalized)

    return all_products

def normalize_data(item, source):

    if source == "grailed":
        return {
            "name": f"{item.get('brand', '')} {item.get('model', '')}".strip(),
            "category": item.get("metadata", {}).get("style", "unknown"),
            "source": "grailed",
            "price": float(item.get("price", 0)),
            "url": item.get("product_url")
        }

    elif source == "fashionphile":
        return {
            "name": item.get("model"),
            "category": item.get("metadata", {}).get("garment_type", "unknown"),
            "source": "fashionphile",
            "price": float(item.get("price", 0)),
            "url": item.get("product_url")
        }

    elif source == "1stdibs":
        return {
            "name": item.get("model"),
            "category": "accessories",
            "source": "1stdibs",
            "price": float(item.get("price", 0)),
            "url": item.get("product_url")
        }