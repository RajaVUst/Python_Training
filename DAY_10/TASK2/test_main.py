from fastapi.testclient import TestClient
from unittest.mock import patch

from main import app

client = TestClient(app)


def test_get_note():
    response = client.get("/notes/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Python"
    assert data["body"] == "Learn Python"
    assert "tags" in data


def test_create_note():
    response = client.post(
        "/notes",
        json={
            "title": "FastAPI",
            "body": "Learn FastAPI",
            "tags": ["python", "api"]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "FastAPI"
    assert data["body"] == "Learn FastAPI"
    assert "id" in data


def test_create_note_invalid():
    response = client.post(
        "/notes",
        json={
            "body": "Learn FastAPI"
        }
    )

    assert response.status_code == 422


@patch("main.send_notification")
def test_create_note_notification(mock_notification):

    response = client.post(
        "/notes",
        json={
            "title": "Testing",
            "body": "Testing notification",
            "tags": ["test"]
        }
    )

    assert response.status_code == 200

    mock_notification.assert_called_once()