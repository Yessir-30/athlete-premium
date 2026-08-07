from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies.auth import get_current_user, get_db
from models.nutrition import Nutrition
from schemas.nutrition import NutritionUpdate

router = APIRouter(prefix="/nutrition")

@router.get("/")
def get_nutrition(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Nutrition).filter(Nutrition.user_id == current_user.id).first()

@router.put("/")
def update_nutrition(payload: NutritionUpdate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    nutrition = db.query(Nutrition).filter(Nutrition.user_id == current_user.id).first()
    if not nutrition:
        nutrition = Nutrition(user_id=current_user.id)
        db.add(nutrition)

    for field, value in payload.dict().items():
        if value is not None:
            setattr(nutrition, field, value)

    db.commit()
    db.refresh(nutrition)
    return nutrition
