import json

session = {
    "topic": "File Handling",
    "duration_minutes": 60,
    "format": "Practical"
}

json_string = json.dumps(session)

print(json_string)

session_dict = json.loads(json_string)

print(type(session_dict))


# {"topic": "File Handling", "duration_minutes": 60, "format": "Practical"}
# <class 'dict'>