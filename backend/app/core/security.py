from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "supersecret"  # change later

# Bearer auth scheme
security = HTTPBearer()


# -----------------------------
# PASSWORD HASHING
# -----------------------------
def hash_password(password):
    password = password[:72]  # bcrypt limit
    return pwd_context.hash(password)


def verify_password(password, hashed):
    password = password[:72]
    return pwd_context.verify(password, hashed)


# -----------------------------
# TOKEN CREATION
# -----------------------------
def create_token(data):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(days=1)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


# -----------------------------
# TOKEN VERIFICATION (NEW)
# -----------------------------
def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


# -----------------------------
# CURRENT USER DEPENDENCY (NEW)
# -----------------------------
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    payload = decode_token(token)
    return payload