from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies.auth import get_current_user, get_db
from models.training import Training
from schemas.training import TrainingCreate

router = APIRouter(prefix="/training")

@router.get("/")
def get_training(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Training).filter(Training.user_id == current_user.id).all()

@router.post("/")
def add_training(payload: TrainingCreate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    session = Training(user_id=current_user.id, **payload.dict())
    db.add(session)
    db.commit()
    db.refresh(session)
    return session
