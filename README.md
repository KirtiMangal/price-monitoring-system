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