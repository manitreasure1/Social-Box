from fastapi import APIRouter, Form #, Depends, UploadFile, File
from app.models.database import Database
# from app.models.user_model import User, UserCreate
from sqlmodel import Session
from app.services.user_schema import UserLoginSchema, UserSignUpSchema
from typing import Annotated


def get_db():
    with Database.get_session() as db:
        yield db
    
auth = APIRouter()

@auth.post("/sign_up/")
def create_user(data: Annotated[UserSignUpSchema, Form()]):
    return data.model_dump()

@auth.post("/login/")
def login_user(data: Annotated[UserLoginSchema, Form()]):
    return data.model_dump()





#  Todo: updata user info
# @user_router.put("/{username}")
# def update_user(username: str):
#     return {"username": username}


# @user_router.delete("/{username}")
# def delete_user(username: str):
# @user_router.get("/")
# def read_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]


# @user_router.get("/{user_id}")
# def read_user(user_id: int):
#     return {"username": user_id}
#     return {"username": username}