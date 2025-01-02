from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .user_model import User
    from .comment_model import Comment

class PostBase(SQLModel):
    title: str
    content: str

class Post(PostBase, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="posts")
    comments: Optional["Comment"] = Relationship(back_populates="post")

class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    user_id: int

class PostUpdate(SQLModel):
    title: str
    content: str