from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Notes API")


class Note(BaseModel):
    title: str
    content: str


notes = [
    {
        "id": 1,
        "title": "Python",
        "content": "Learn Python basics"
    },
    {
        "id": 2,
        "title": "FastAPI",
        "content": "Learn FastAPI endpoints"
    },
    {
        "id": 3,
        "title": "Pydantic",
        "content": "Learn Pydantic models"
    }
]


@app.get("/notes/{note_id}")
def get_note(note_id: int):

    for note in notes:
        if note["id"] == note_id:
            return note

    return {"error": "Note not found"}


@app.get("/notes")
def get_notes(limit: int = 10):

    return notes[:limit]


@app.post("/notes")
def create_note(note: Note):

    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content
    }

    notes.append(new_note)

    return new_note