from pydantic import BaseModel

class ProgressCreate(BaseModel):
    weight: int
    muscle_mass: str
    comment: str | None = None
