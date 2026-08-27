from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
notes = [
    {"id": 1, "title": "First note"},
    {"id": 2, "title": "Second note"},
    {"id": 3, "title": "Third note"}
]


@app.get("/notes/{note_id}")
def get_note(note_id:int):
    return{"note_id":note_id}

@app.get("/notes")
def get_notes(limit:int=10):
    return notes[:limit]

class Note(BaseModel):
    title:str
    
    
@app.post("/notes")
def create_note(note:Note):
    new_note={
        "id":len(notes)+1,
        "title":note.title
    }
    
    notes.append(new_note)
    
    return new_note
    
# OUTPUT

# 1st Endpoint
    
# {
#   "note_id": 1
# }


# 2nd Endpoint

# [
#   {
#     "id": 1,
#     "title": "First note"
#   },
#   {
#     "id": 2,
#     "title": "Second note"
#   }
# ]

# 3rd Endpoint

# {
#   "title": "Study FastAPI"
# }