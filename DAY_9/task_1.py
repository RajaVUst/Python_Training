# Task 1 - Build the API
# A tiny "Notes" FastAPI app with 3 endpoints.
# Run with: uvicorn task_1:app --reload

from fastapi import FastAPI

app = FastAPI(title="Notes API")

# Simple in-memory store — like a Java Map<Integer, Map>
notes = {1: {"id": 1, "title": "First note", "body": "Hello World"}}
next_id = 2


# 1. GET /notes/{note_id} — path parameter
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    if note_id not in notes:
        return {"error": "Note not found"}
    return notes[note_id]


# 2. GET /notes — optional query parameter 'limit' (default 10)
@app.get("/notes")
def list_notes(limit: int = 10):
    return list(notes.values())[:limit]


# 3. POST /notes — JSON body creates a new note
@app.post("/notes")
def create_note(data: dict):
    global next_id
    note = {"id": next_id, **data}   # merge id + incoming fields
    notes[next_id] = note
    next_id += 1
    return note
