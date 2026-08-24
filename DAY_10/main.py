from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="Notes API")
class NoteIn(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    body: str = Field(min_length=1)
    tags: list[str] = Field(default_factory=list)

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
    tags: list[str]

notes = [
    {
        "id": 1,
        "title": "Python",
        "content": "Learn FastAPI basics"
    },
    {
        "id": 2,
        "title": "FastAPI",
        "content": "Practice API endpoints"
    }
]
@app.get("/")
def home():
    return {"message": "Hello World"}

# 1. GET /notes/{note_id}
@app.get("/notes/{note_id}" , response_model=NoteOut)
def get_note(note_id: int):

    for note in notes:
        if note["id"] == note_id:
            return note

    return {"message": "Note not found"}


# 2. GET /notes?limit=10
@app.get("/notes" , response_model=list[NoteOut])
def get_notes(limit: int = 10):

    return notes[:limit]


# 3. POST /notes
@app.post("/notes", response_model=NoteOut)
def create_note(note: NoteIn):

    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content
    }

    notes.append(new_note)

    return new_note