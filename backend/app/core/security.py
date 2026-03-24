from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "supersecret"  # change later

def hash_password(password):
    # bcrypt max length = 72 bytes
    password = password[:72]
    return pwd_context.hash(password)

def verify_password(password, hashed):
    password = password[:72]
    return pwd_context.verify(password, hashed)

def create_token(data):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(days=1)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")