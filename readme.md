# Social Media WebApp

This is a CRUD social media web application that allows users to create, read, update, and delete posts and comments. The application is built with a RESTful API for posts, users, and comments, and uses SQLModel with SQLite for the database.

## Features

- User authentication and management
- Create, read, update, and delete posts
- Comment on posts
- Like and unlike posts
- Follow and unfollow users

## API Endpoints

### User API

- `POST /users/` - Create a new user
- `GET /users/{user_id}` - Get user details
- `PUT /users/{user_id}` - Update user details
- `DELETE /users/{user_id}` - Delete a user

### Post API

- `POST /posts/` - Create a new post
- `GET /posts/{post_id}` - Get post details
- `PUT /posts/{post_id}` - Update a post
- `DELETE /posts/{post_id}` - Delete a post

### Comment API

- `POST /posts/{post_id}/comments/` - Add a comment to a post
- `GET /posts/{post_id}/comments/` - Get all comments for a post
- `PUT /comments/{comment_id}` - Update a comment
- `DELETE /comments/{comment_id}` - Delete a comment

## Database Model

The database is modeled using SQLModel with SQLite. Below are the main models:

### User Model

```python
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
```

### Post Model

```python
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
```

### Comment Model

```python
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



```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/manitreasure1/Social-Box.git
    ```
2. Navigate to the project directory:
    ```sh
    cd social-box
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the application:
    ```sh
    uvicorn main:app --reload
    ```

## License

This project is licensed under the MIT License.


