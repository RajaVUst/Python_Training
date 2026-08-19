import json

session = {
    "topic": "File Handling",
    "duration_minutes": 60,
    "format": "Practice"
}

json_string = json.dumps(session)

print(json_string)

result = json.loads(json_string)

print(type(result))

# output:
# {"topic": "File Handling", "duration_minutes": 60, "format": "Practice"}
# <class 'dict'>