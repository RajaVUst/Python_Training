# Task 2 - Define the Models
# Adds Pydantic models (NoteIn / NoteOut) with field validation to the Notes API.
# Run with: uvicorn task_2:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="Notes API")


# NoteIn — used for the POST request body (like a Java DTO + @Valid)
class NoteIn(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    body: str = Field(min_length=1)
    tags: list[str] = Field(default=[], max_length=5)  # stretch: max 5 tags

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v):
        if not v.strip():
            raise ValueError("title cannot be whitespace only")
        return v


# NoteOut — used for responses (adds the auto-generated id)
class NoteOut(BaseModel):
    id: int
    title: str
    body: str
    tags: list[str]


# In-memory store
notes: dict[int, NoteOut] = {}
next_id = 1


def send_notification(note: NoteOut):
    # Stub: in a real app this would call an email / webhook service
    print(f"Notification sent for note id={note.id}: '{note.title}'")


@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return notes[note_id]


@app.get("/notes", response_model=list[NoteOut])
def list_notes(limit: int = 10):
    return list(notes.values())[:limit]


@app.post("/notes", response_model=NoteOut, status_code=201)
def create_note(note_in: NoteIn):
    global next_id
    note = NoteOut(id=next_id, title=note_in.title, body=note_in.body, tags=note_in.tags)
    notes[next_id] = note
    next_id += 1
    send_notification(note)
    return note
