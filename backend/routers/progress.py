from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies.auth import get_current_user, get_db
from models.progress import Progress
from schemas.progress import ProgressCreate

router = APIRouter(prefix="/progress")

@router.get("/")
def get_progress(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Progress).filter(Progress.user_id == current_user.id).all()

@router.post("/")
def add_progress(payload: ProgressCreate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    entry = Progress(user_id=current_user.id, **payload.dict())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry
