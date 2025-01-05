from fastapi import FastAPI
from contextlib import asynccontextmanager

from .api.post_api import post_router
from .api.user_api import auth
from .models.database import Database 



@asynccontextmanager
async def life_span(app: FastAPI):
    Database.create_db_and_tables()
    print("Application started")
    yield
    print("Application stopped")

version="0.0.1"

app = FastAPI(
    title="Social box API",
    description="API for Social box",
    version=version,
    lifespan=life_span
    )
app.include_router(auth, prefix=f"/users", tags=["user"])
app.include_router(post_router, prefix=f"/posts", tags=["post"])

