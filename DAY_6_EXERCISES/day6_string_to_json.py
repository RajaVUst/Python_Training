import json

session = {
    "topic": "File Handling",
    "duration_minutes": 60,
    "format": "Hands-on"
}

json_string = json.dumps(session)

print(json_string)

data = json.loads(json_string)

print(type(data))

"""
Output->
{"topic": "File Handling", "duration_minutes": 60, "format": "Hands-on"}
<class 'dict'>
"""