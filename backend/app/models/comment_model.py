from sqlmodel import Field, SQLModel, Relationship, create_engine, Session, select
from typing import Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from .post_model import Post
    from .user_model import User

class CommentBase(SQLModel):
    content: str

class Comment(CommentBase, table=True):
    id: int = Field(default=None, primary_key=True)
    post_id: int = Field(foreign_key="post.id")
    user_id: int = Field(foreign_key="user.id")
    post: Optional["Post"] = Relationship(back_populates="comments")
    user: Optional["User"] = Relationship(back_populates="comments")

class CommentCreate(CommentBase):
    pass

class CommentRead(CommentBase):
    id: int
    post_id: int

class CommentUpdate(SQLModel):
    content: str


