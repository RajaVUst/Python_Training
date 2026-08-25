# Task 4 - Write the Tests
# Run with: pytest task_4.py -v

import unittest
from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
import task_2

client = TestClient(task_2.app)


# Reset the in-memory store before each test so tests don't affect each other
@pytest.fixture(autouse=True)
def reset_notes():
    task_2.notes.clear()
    task_2.next_id = 1
    yield


# ─── 1. GET /notes/{note_id} ──────────────────────────────────────────────────

def test_get_note_returns_200():
    client.post("/notes", json={"title": "Hello", "body": "World"})
    resp = client.get("/notes/1")
    assert resp.status_code == 200
    assert resp.json()["title"] == "Hello"
    assert resp.json()["id"] == 1


def test_get_note_not_found():
    resp = client.get("/notes/999")
    assert resp.status_code == 404


# ─── 2. POST /notes ───────────────────────────────────────────────────────────

def test_create_note_valid():
    resp = client.post("/notes", json={"title": "Buy milk", "body": "From the store"})
    assert resp.status_code == 201
    assert resp.json()["title"] == "Buy milk"
    assert "id" in resp.json()


def test_create_note_whitespace_title_returns_422():
    resp = client.post("/notes", json={"title": "   ", "body": "some body"})
    assert resp.status_code == 422


def test_create_note_missing_body_returns_422():
    resp = client.post("/notes", json={"title": "No body note"})
    assert resp.status_code == 422


# ─── 3. Mocked send_notification ──────────────────────────────────────────────

@patch("task_2.send_notification")  # like Mockito @Mock
def test_notification_called_once(mock_notify):
    client.post("/notes", json={"title": "Ping", "body": "Pong"})
    mock_notify.assert_called_once()   # like verify(mock, times(1))


# ─── Stretch goal: same test using unittest.TestCase style ────────────────────

class TestCreateNoteUnittest(unittest.TestCase):

    def setUp(self):           # like @BeforeEach
        task_2.notes.clear()
        task_2.next_id = 1

    def test_create_note(self):
        resp = client.post("/notes", json={"title": "Unit style", "body": "Hello"})
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json()["title"], "Unit style")

    def test_invalid_title(self):
        resp = client.post("/notes", json={"title": "", "body": "Hello"})
        self.assertEqual(resp.status_code, 422)
