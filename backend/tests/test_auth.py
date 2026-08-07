import os
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

os.environ["DATABASE_URL"] = "sqlite:///./test_auth.db"
os.environ["SECRET_KEY"] = "test-secret"
os.environ["ALGORITHM"] = "HS256"
os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"] = "30"
os.environ["REFRESH_TOKEN_EXPIRE_DAYS"] = "7"

from database import Base, engine
from main import app


@pytest.fixture()
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as test_client:
        yield test_client
    Base.metadata.drop_all(bind=engine)


def test_register_login_and_protected_user(client):
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "secret123"},
    )
    assert response.status_code == 201

    login_response = client.post(
        "/auth/login",
        json={"email": "test@example.com", "password": "secret123"},
    )
    assert login_response.status_code == 200
    body = login_response.json()
    assert "access_token" in body
    assert "refresh_token" in body

    user_response = client.get(
        "/user/",
        headers={"Authorization": f"Bearer {body['access_token']}"},
    )
    assert user_response.status_code == 200
