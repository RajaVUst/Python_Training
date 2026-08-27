from fastapi.testclient import TestClient
from unittest.mock import patch

from main2 import app


client = TestClient(app)


def test_get_note():
    response = client.get("/notes/1")

    assert response.status_code == 200
    assert response.json() == {"note_id": 1}


def test_create_note():
    response = client.post(
        "/notes",
        json={
            "title": "Study Python",
            "body": "Prepare for exam",
            "tags": ["python"]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Study Python"
    assert data["body"] == "Prepare for exam"
    assert "id" in data


def test_invalid_note():
    response = client.post(
        "/notes",
        json={
            "title": "   ",
            "body": "Invalid title"
        }
    )

    assert response.status_code == 422


@patch("main2.send_notification")
def test_notification(mock_notification):
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
    
# OUTPUT 

# test_main.py ....                                                                 [100%]

# =================================== warnings summary ===================================
# ..\..\..\..\..\Python312\Lib\site-packages\fastapi\testclient.py:1
#   C:\Python312\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
#     from starlette.testclient import TestClient as TestClient  # noqa

# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ============================= 4 passed, 1 warning in 0.67s =============================
# PS C:\Users\308231\Desktop\PYHTON REFRESHMENT\day10> 