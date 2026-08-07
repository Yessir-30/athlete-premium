from pydantic import BaseModel

class NutritionUpdate(BaseModel):
    calories: int | None = None
    proteins: int | None = None
    hydration: str | None = None
