from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    first_name: str
    height: int
    weight: int
    goal_weight: int

class UserUpdate(BaseModel):
    first_name: str | None = None
    height: int | None = None
    weight: int | None = None
    goal_weight: int | None = None
