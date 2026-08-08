from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home_page() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Olá, Mestre" in response.text


def test_empty_chat_message_is_rejected() -> None:
    response = client.post("/api/chat", json={"message": ""})
    assert response.status_code == 422
