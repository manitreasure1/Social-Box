from pydantic import BaseModel

class UserLoginSchema(BaseModel):
    email: str
    password: str
    model_config = {"extra": "forbid"}

class UserSignUpSchema(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    model_config = {"extra": "forbid"}

    