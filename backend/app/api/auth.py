from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import User
from app.core.security import hash_password, verify_password, create_token
from app.schemas.autho import AuthRequest

router = APIRouter(prefix="/auth")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup")
def signup(data: AuthRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == data.email).first()

    if existing:
        return {"status": "error", "message": "User already exists"}

    user = User(
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(user)
    db.commit()

    return {"status": "success"} 


@router.post("/login")
def login(data: AuthRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.password):
        return {"status": "error", "message": "Invalid credentials"}

    token = create_token({"user_id": user.id, "email": user.email})

    return {
        "status": "success",
        "token": token,
        "user": {
            "email": user.email,
            "plan": user.plan
        }
    }