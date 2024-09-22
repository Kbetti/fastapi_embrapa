from fastapi import Security, HTTPException
from fastapi.security import HTTPBearer
import jwt

security = HTTPBearer()
SECRET_KEY = "mysecret"

def verify_token(http_auth: str = Security(security)):
    token = http_auth.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

