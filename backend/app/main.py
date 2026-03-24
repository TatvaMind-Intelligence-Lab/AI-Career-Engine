from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.api.auth import router as auth
from app.db.database import engine, Base
Base.metadata.create_all(bind=engine)


# ✅ Create app FIRST
app = FastAPI(title="TatvaMind AI Career Engine")

# ✅ Then add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Then include routes  
app.include_router(router)
app.include_router(auth, prefix="/api/v1")