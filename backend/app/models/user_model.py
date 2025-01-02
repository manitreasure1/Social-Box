from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .post_model import Post
    from .comment_model import Comment

class UserBase(SQLModel):
    username: str
    email: str

class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    password: str
    posts:Optional["Post"] = Relationship(back_populates="user")
    comments:Optional["Comment"] = Relationship(back_populates="user")

class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

class UserUpdate(SQLModel):
    username: str
    email: str
    password: str




