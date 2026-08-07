from pydantic import BaseModel

class TrainingCreate(BaseModel):
    session_type: str
    notes: str | None = None
