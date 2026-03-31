import random

async def fetch_products():
    return [
        {
            "name": "Bag A",
            "category": "bags",
            "source": "Grailed",
            "price": random.randint(100, 200)
        },
        {
            "name": "Watch B",
            "category": "watches",
            "source": "1stdibs",
            "price": random.randint(300, 500)
        }
    ]