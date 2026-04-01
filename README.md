                                                       Price Monitoring System

1. Overview
- The Price Monitoring System is a backend application that tracks product prices across multiple sources and maintains historical price data.
- It is designed to simulate real-world e-commerce price tracking systems.

2. Features 
- Track products from multiple sources
- Monitor price changes over time
- Maintain complete price history
- Provide analytics (total products, average price)
- Filter products by category & price range
- Detect and log price change events

3. Tech Stack

| Layer    | Technology |
| -------- | ---------- |
| Backend  | FastAPI    |
| Database | SQLite     |
| ORM      | SQLAlchemy |
| Language | Python     |

4. Architecture

Product -> Listing -> PriceHistory

Explanation:

- Product → Unique item (e.g., Amiri Jacket)
- Listing → Same product on different sources (Grailed, Fashionphile)
- PriceHistory → Tracks price changes over time per listing

5. Project Structure
   
```
price-monitoring-system/
│
├── backend/
│   ├── app/
│   │   └── main.py          # FastAPI entry point
│   │
│   ├── db/
│   │   ├── database.py      # DB connection
│   │   └── models.py        # DB models
│   │
│   ├── services/
│   │   ├── fetcher.py       # Data ingestion
│   │   └── price_service.py # Business logic
│   │
│   ├── auth.py              # API key & JWT auth
│   └── test.db              # SQLite database
│
└── README.md
```


6. Setup Instructions

1️⃣ Clone Repository
`git clone <your-repo-link>`
`cd price-monitoring-system/backend`

2️⃣ Create Virtual Environment
`python -m venv venv`
`venv\Scripts\activate`

3️⃣ Install Dependencies
`pip install -r requirements.txt`

4️⃣ Run Server
`uvicorn app.main:app --reload`

5️⃣ Open API Docs
`http://127.0.0.1:8000/docs`

7. API Endpoints

i. Authentication

- All protected endpoints require:

Header:
`x-api-key: secret123`

ii. Refresh Products

- Fetch and store product data from sources.

POST `/refresh`

iii. Get All Products

- Returns all products with optional filtering.

GET `/products`

Query Params:
- category
- min_price
- max_price

Example:

`/products?category=accessories`
`/products?min_price=100&max_price=500`

iv. Get Product Details + History

- Returns product info along with price history.

GET `/products/{id}`

Response:

{
  "product": {...},
  "history": [...]
}

v. Analytics

- Returns summary of product data.

GET `/analytics`

- Response includes:

a) Total number of products
b) Average price

{
  "total_products": 3,
  "avg_price": 350.0
}

vi. Price Change Events

GET `/events`

vii. API Usage Tracking

GET `/usage`

8. Testing

You can test APIs using:

Swagger UI → `http://127.0.0.1:8000/docs`
Thunder Client (VS Code Extension)

9. Design Decisions
- Used SQLite for simplicity and easy setup
- Structured project into services for better scalability
- Stored price history separately for tracking changes
- Designed APIs with filtering support for flexibility

10. Limitations
- Uses mock data instead of real marketplace APIs
- No frontend UI implemented
- Basic authentication (can be improved using JWT/OAuth)

11. Future Improvements
- Integrate real-time web scraping
- Add frontend dashboard
- Implement authentication & authorization
- Deploy application on cloud (AWS/Render)
- Add Redis caching

12. Author
    
  ~ `Kirti`
