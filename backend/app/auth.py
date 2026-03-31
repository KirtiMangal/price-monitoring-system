from fastapi import Header, HTTPException

API_KEY = "secret123"   # 👉 SIMPLE rakh lo

def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")