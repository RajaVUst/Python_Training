import json


session = {
    "topic": "Files and exceptions",
    "duration_minutes": 90,
    "format": "practice",
}

json_string = json.dumps(session)
print(json_string)

restored_session = json.loads(json_string)
print(type(restored_session))

# OUTPUT

# {"topic": "Files and exceptions", "duration_minutes": 90, "format": "practice"}
# <class 'dict'>
