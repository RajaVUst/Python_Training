# Task 3 - Read the Docs
#
# Steps to try in the browser:
#   1. Run:  uvicorn task_2:app --reload
#   2. Open: http://127.0.0.1:8000/docs
#
# Part a) Click POST /notes → "Try it out" → send a valid body:
#   { "title": "My Note", "body": "Hello World", "tags": ["python"] }
#   You should see a 201 response with the created note including an id.
#
# Part b) Send an invalid body (empty title):
#   { "title": "   ", "body": "Hello" }
#   You should see a 422 Unprocessable Entity with a validation error message.
#
# Part c) Where does the /docs schema come from?
#   FastAPI reads the type hints on each route function and the fields defined
#   in NoteIn / NoteOut (our Pydantic BaseModel classes) to auto-build an
#   OpenAPI schema. There is no separate YAML or config file to maintain —
#   the schema is always in sync with the code automatically.

import json
from task_2 import app

# Print the raw OpenAPI schema that /docs is built from
schema = app.openapi()
print(json.dumps(schema, indent=2))
