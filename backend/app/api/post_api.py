from fastapi import APIRouter
from app.models.database import Database


def get_db():
    with Database.get_session() as db:
        yield db

post_router = APIRouter()

@post_router.get("/")
def read_posts():
    return [{"title": "Post 1"}, {"title": "Post 2"}]


@post_router.get("/{post_id}")
def read_post(post_id: int):
    return {"post_id": post_id}


@post_router.post("/")
def create_post(title: str):
    return {"title": title}


@post_router.put("/{post_id}")
def update_post(post_id: int):
    return {"post_id": post_id}


@post_router.delete("/{post_id}")
def delete_post(post_id: int):
    return {"post_id": post_id}
