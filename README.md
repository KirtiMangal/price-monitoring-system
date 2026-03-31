              Price Monitoring System

1. Overview

The Price Monitoring System is a backend application designed to track product prices from different sources and maintain their price history over time.

2. It helps in:

- Monitoring price changes
- Storing historical price data
- Filtering products based on category and price
- Providing basic analytics

3. 🛠️ Tech Stack
Backend: FastAPI
Database: SQLite
ORM: SQLAlchemy
Language: Python


4. 📂 Project Structure
price-monitoring-system/
│
├── backend/
│   ├── app/
│   │   ├── main.py              # Main FastAPI application
│   │   ├── db.py                # Database configuration
│   │   ├── models.py            # Database models
│   │   └── services/
│   │       ├── fetcher.py       # Mock data fetching
│   │       └── price_service.py # Price update logic
│   └── requirements.txt
│
└── README.md


5. ⚙️ Setup Instructions

1️⃣ Clone Repository
git clone <your-repo-link>
cd price-monitoring-system/backend

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Server
uvicorn app.main:app --reload

6. 📡 API Endpoints

🔄 Refresh Products

- Fetches new data and updates price history.

POST /refresh
📦 Get All Products

- Returns all products with optional filtering.

GET /products
Optional Query Parameters:
category → filter by category
min_price → minimum price
max_price → maximum price

Example:

/products?category=bags
/products?min_price=100&max_price=300

📄 Get Product Details

- Returns product info along with price history.

GET /products/{id}

7. 📊 Analytics

- Returns summary of product data.

GET /analytics

- Response includes:

a) Total number of products
b) Average price

8. 🧪 Testing

You can test APIs using:

Swagger UI → http://127.0.0.1:8000/docs
Thunder Client (VS Code Extension)

⚠️ Make sure to call /refresh before fetching products.

9. 🧠 Design Decisions
- Used SQLite for simplicity and easy setup
- Structured project into services for better scalability
- Stored price history separately for tracking changes
- Designed APIs with filtering support for flexibility

10. ⚠️ Limitations
- Uses mock data instead of real scraping
- No frontend interface
- No authentication implemented (can be added)


11. 🚀 Future Improvements
- Integrate real-time web scraping
- Add frontend dashboard
- Implement authentication & authorization
- Deploy application on cloud (AWS/Render)


👨‍💻 Author
~ Kirti