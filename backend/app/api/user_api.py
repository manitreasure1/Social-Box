from fastapi import APIRouter
from app.models.database import Database


def get_db():
    with Database.get_session() as db:
        yield db
    
user_router = APIRouter()

@user_router.get("/")
def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@user_router.get("/{user_id}")
def read_user(user_id: int):
    return {"username": user_id}


@user_router.post("/")
def create_user(username: str):
    return {"username": username}


@user_router.put("/{username}")
def update_user(username: str):
    return {"username": username}


@user_router.delete("/{username}")
def delete_user(username: str):
    return {"username": username}