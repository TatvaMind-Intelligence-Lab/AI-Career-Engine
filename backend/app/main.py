from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="TatvaMind AI Career Engine")

app.include_router(router)