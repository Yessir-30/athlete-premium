from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from dependencies.auth import get_current_user
from models.user import User
from schemas.user import UserCreate, UserUpdate

router = APIRouter(prefix="/user")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_user(current_user = Depends(get_current_user)):
    return current_user

@router.post("/")
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    user = User(**payload.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.put("/")
def update_user(payload: UserUpdate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == current_user.id).first()
    if not user:
        return {"error": "no user to update"}

    for field, value in payload.dict().items():
        if value is not None:
            setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user
