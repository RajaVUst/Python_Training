import json

session = {
    "topic": "File Handling",
    "duration_minutes": 60,
    "format": "Hands-On"
}

# Dict to JSON string
json_string = json.dumps(session)

print(json_string)

# JSON string back to dict
loaded_data = json.loads(json_string)

print(type(loaded_data))

"""
OUTPUT:
{"topic": "File Handling", "duration_minutes": 60, "format": "Hands-On"}
<class 'dict'>
"""