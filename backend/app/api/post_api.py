from fastapi import APIRouter, Form, File, UploadFile, Depends
from app.models.database import Database
from typing import Annotated
from app.services.post_schema import CreateAndUploadPostscheme
from fastapi.responses import HTMLResponse

def get_db():
    with Database.get_session() as db:
        yield db

post_router = APIRouter()


# @post_router.get("/")
# def read_posts():
#     return [{"title": "Post 1"}, {"title": "Post 2"}]


# @post_router.get("/{post_id}")
# def read_post(post_id: int):
#     return {"post_id": post_id}


@post_router.post("/")
def create_post(
    images: Annotated[UploadFile, File()],
    form_data: Annotated[CreateAndUploadPostscheme, Form()]
    ):
    
    # Todo: Save the image to the database, and save the form data to the database
    return {
            "uploaded file": images.filename,
            "form data": form_data
            }   

            
@post_router.get("/")
def read_posts():
    content = """
    <body>
    <h1>Upload a file</h1>
    <form action="/posts/" enctype="multipart/form-data" method="post">
    <input name="title" type="text" placeholder="Enter title">
    <input name="content" type="text" placeholder="Enter content">
    <input name="images" type="file">
    <button type="submit">Upload</button>
    </form>
    </body>
    """
    return HTMLResponse(content=content)

@post_router.put("/{post_id}")
def update_post(post_id: int):
    return {"post_id": post_id}


@post_router.delete("/{post_id}")
def delete_post(post_id: int):
    return {"post_id": post_id}
