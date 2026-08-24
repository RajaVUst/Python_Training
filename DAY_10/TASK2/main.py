from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="Notes API")


class NoteIn(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    body: str = Field(min_length=1)
    tags: list[str] | None = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("title cannot be blank")
        return value


class NoteOut(BaseModel):
    id: int
    title: str
    body: str
    tags: list[str] | None = None


notes = [
    {
        "id": 1,
        "title": "Python",
        "body": "Learn Python",
        "tags": ["python"]
    }
]


def send_notification(note):
    pass


@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note

    return {"error": "Note not found"}


@app.get("/notes")
def get_notes():
    return notes


@app.post("/notes", response_model=NoteOut)
def create_note(note: NoteIn):

    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "body": note.body,
        "tags": note.tags
    }

    notes.append(new_note)

    send_notification(new_note)

    return new_note