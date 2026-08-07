from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User
from utils.auth import decode_token


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(authorization: str = Header(None), db: Session = Depends(get_db)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    token = authorization.replace("Bearer ", "")
    data = decode_token(token)
    user = db.query(User).filter(User.id == data["user_id"]).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return user
