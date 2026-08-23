"""
#-----------------------------TASk-1[Note-In Model]------------------------------------
from fastapi import FastAPI

app = FastAPI()

# Temporary notes data
notes = {
    1: {
        "id": 1,
        "title": "First Note",
        "body": "This is my first note."
    },
    2: {
        "id": 2,
        "title": "Second Note",
        "body": "This is my second note."
    }
}


# GET /notes/{note_id}
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    return notes.get(
        note_id,
        {"error": "Note not found"}
    )


# GET /notes
@app.get("/notes")
def get_notes(limit: int = 10):
    return list(notes.values())[:limit]


# POST /notes
@app.post("/notes")
def create_note(note: dict):
    new_id = max(notes.keys()) + 1 if notes else 1

    new_note = {
        "id": new_id,
        "title": note["title"],
        "body": note["body"]
    }

    notes[new_id] = new_note

    return new_note
"""


# ----------------------------- TASK-2 [Pydantic Models] -----------------------------

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator


app = FastAPI()


# Request model
class NoteIn(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    body: str
    tags: list[str] | None = Field(default=None, max_length=5)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Title cannot be only whitespace")
        return value


# Response model
class NoteOut(BaseModel):
    id: int
    title: str
    body: str
    tags: list[str] | None = None


# Temporary notes data
notes = {
    1: {
        "id": 1,
        "title": "First Note",
        "body": "This is my first note.",
        "tags": ["example"]
    },
    2: {
        "id": 2,
        "title": "Second Note",
        "body": "This is my second note.",
        "tags": ["example", "test"]
    }
}


# GET /notes/{note_id}
@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int):
    return notes.get(
        note_id,
        {"error": "Note not found"}
    )


# GET /notes
@app.get("/notes", response_model=list[NoteOut])
def get_notes(limit: int = 10):
    return list(notes.values())[:limit]


# POST /notes

def send_notification(note):
    print(f"Notification sent for note: {note['id']}")

@app.post("/notes", response_model=NoteOut)
def create_note(note: NoteIn):
    new_id = max(notes.keys()) + 1 if notes else 1

    new_note = {
        "id": new_id,
        "title": note.title,
        "body": note.body,
        "tags": note.tags
    }

    notes[new_id] = new_note

    send_notification(new_note)

    return new_note





#-----------------TASK 3(c) — Swagger Documentation----------------------
# The request and response schemas shown in /docs are automatically generated
# from the Pydantic models (NoteIn and NoteOut) and the function type hints
# used in the FastAPI endpoints. They do not need to be written separately.


