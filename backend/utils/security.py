import os
from datetime import datetime, timedelta, timezone

import bcrypt
from dotenv import load_dotenv
from jose import jwt

load_dotenv()


def _get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"{name} is required. Set it in backend/.env or your environment.")
    return value


SECRET_KEY = _get_required_env("SECRET_KEY")
ALGORITHM = _get_required_env("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(_get_required_env("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(_get_required_env("REFRESH_TOKEN_EXPIRE_DAYS"))


def _create_token(data: dict, expires_delta: timedelta) -> str:
    payload = dict(data)
    payload["exp"] = datetime.now(timezone.utc) + expires_delta
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def create_access_token(data: dict) -> str:
    return _create_token(data, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))


def create_refresh_token(data: dict) -> str:
    return _create_token(data, timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))


def create_token(data: dict) -> str:
    return create_access_token(data)


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())
