from pydantic import BaseModel

class Register(BaseModel):
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str
