from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_get_note():
    response = client.get("/notes/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "tags" in data


def test_create_note():
    response = client.post(
        "/notes",
        json={
            "title": "Test Note",
            "body": "This is a test note.",
            "tags": ["test"]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert data["title"] == "Test Note"
    assert data["body"] == "This is a test note."
    assert data["tags"] == ["test"]


def test_create_note_invalid():
    response = client.post(
        "/notes",
        json={
            "body": "This note has no title."
        }
    )

    assert response.status_code == 422
@patch("main.send_notification")
def test_create_note_sends_notification(mock_send_notification):
    response = client.post(
        "/notes",
        json={
            "title": "Notification Test",
            "body": "Testing the notification mock.",
            "tags": ["test"]
        }
    )

    assert response.status_code == 200
    mock_send_notification.assert_called_once()