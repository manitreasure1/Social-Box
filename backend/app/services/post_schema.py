from pydantic import BaseModel


class CreateAndUploadPostscheme(BaseModel):
    title: str
    content: str
    images: bytes | str
    