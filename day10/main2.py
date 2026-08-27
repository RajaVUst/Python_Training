from fastapi import FastAPI
from pydantic import BaseModel,Field,field_validator
from typing import Optional

class NoteIn(BaseModel):
    title:str=Field(...,min_length=1,max_length=100)
    body:str=Field(...,min_length=1)
    tags:Optional[list[str]]=None
    
    @field_validator("title")
    @classmethod
    def validate_title(cls,value):
        if not value.strip():
            raise ValueError("Title cannot contain only whitespace")
        return value
    
class NoteOut(BaseModel):
    id:int
    title:str
    body:str
    tags:Optional[list[str]]=None
    
    
app=FastAPI()

notes = [
    {
        "id": 1,
        "title": "First note",
        "body": "This is the first note",
        "tags": ["sample"]
    },
    {
        "id": 2,
        "title": "Second note",
        "body": "This is the second note",
        "tags": None
    },
    {
        "id": 3,
        "title": "Third note",
        "body": "This is the third note",
        "tags": ["test"]
    }
]

def send_notification(note):
    print("Notification sent for:", note["title"])


@app.get("/notes/{note_id}")
def get_note(note_id:int):
    return{"note_id":note_id}

@app.get("/notes")
def get_notes(limit:int=10):
    return notes[:limit]


@app.post("/notes",response_model=NoteOut)
def create_note(note:NoteIn):
    new_note={
        "id":len(notes)+1,
        "title":note.title,
        "body":note.body,
        "tags":note.tags
    }
    
    notes.append(new_note)
    send_notification(new_note)

    return new_note




# OUTPUT

# {
#   "id": 5,
#   "title": "Study FastAPI",
#   "body": "Complete Task 2",
#   "tags": [
#     "python",
#     "api"
#   ]
# }

# whitespace testing 

# 422
# Error: Unprocessable Entity

# The request and response schemas shown in docs are generated
# automatically from the Pydantic models like NoteIn and NoteOut,
# together with the FastAPI endpoint type hints.They are not written separately.