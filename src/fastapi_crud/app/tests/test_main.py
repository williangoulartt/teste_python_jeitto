import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app
from ..database import get_db, Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_cliente():
    response = client.post(
        "/clientes/",
        json={"nome": "John Doe", "email": "johndoe@example.com", "telefone": "123456789"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["nome"] == "John Doe"
    assert data["email"] == "johndoe@example.com"
    assert "id" in data


def test_read_cliente():
    response = client.post(
        "/clientes/",
        json={"nome": "Jane Doe", "email": "janedoe@example.com", "telefone": "987654321"}
    )
    assert response.status_code == 200
    data = response.json()
    cliente_id = data["id"]

    response = client.get(f"/clientes/{cliente_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Jane Doe"
    assert data["email"] == "janedoe@example.com"


def test_create_cliente_duplicate_email():
    response = client.post(
        "/clientes/",
        json={"nome": "Alice", "email": "alice@example.com", "telefone": "111111111"}
    )
    assert response.status_code == 200

    response = client.post(
        "/clientes/",
        json={"nome": "Bob", "email": "alice@example.com", "telefone": "222222222"}
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Email already registered"
