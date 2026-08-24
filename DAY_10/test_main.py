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
            "title": "Testing",
            "body": "Learn pytest",
            "tags": ["python", "testing"]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert data["title"] == "Testing"
    assert data["body"] == "Learn pytest"
    assert data["tags"] == ["python", "testing"]


def test_create_note_invalid():

    response = client.post(
        "/notes",
        json={
            "body": "This has no title"
        }
    )

    assert response.status_code == 422


def test_create_note_sends_notification():

    with patch("main.send_notification") as mock_notification:

        response = client.post(
            "/notes",
            json={
                "title": "Mock Test",
                "body": "Testing notification",
                "tags": ["test"]
            }
        )

        assert response.status_code == 200

        mock_notification.assert_called_once()