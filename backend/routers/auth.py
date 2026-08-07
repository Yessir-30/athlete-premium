from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User
from schemas.auth import Register, Login
from utils.auth import decode_token
from utils.security import create_access_token, create_refresh_token, hash_password, verify_password

router = APIRouter(prefix="/auth")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", status_code=201)
def register(payload: Register, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="email already registered")

    user = User(email=payload.email, password_hash=hash_password(payload.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"status": "created", "user_id": user.id}


@router.post("/login")
def login(payload: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="invalid credentials")

    if not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="invalid credentials")

    access_token = create_access_token({"user_id": user.id, "token_type": "access"})
    refresh_token = create_refresh_token({"user_id": user.id, "token_type": "refresh"})
    return {"access_token": access_token, "refresh_token": refresh_token}


@router.post("/refresh")
def refresh(payload: dict, db: Session = Depends(get_db)):
    token = payload.get("refresh_token")
    if not token:
        raise HTTPException(status_code=401, detail="Missing refresh token")

    try:
        data = decode_token(token)
    except Exception as exc:
        raise HTTPException(status_code=401, detail="Invalid refresh token") from exc

    if data.get("token_type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user = db.query(User).filter(User.id == data["user_id"]).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    access_token = create_access_token({"user_id": user.id, "token_type": "access"})
    return {"access_token": access_token}
