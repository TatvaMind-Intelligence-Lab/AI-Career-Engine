from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.api.auth import router as auth
from app.db.database import engine, Base

# ✅ Create tables
Base.metadata.create_all(bind=engine)

# ✅ Create app
app = FastAPI(title="TatvaMind AI Career Engine")

# ✅ Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include routers separately
app.include_router(router, prefix="/api/v1")
app.include_router(auth, prefix="/api/v1/auth")