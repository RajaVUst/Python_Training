import json

session = {
    "topic": "File Handling and Exceptions",
    "duration_minutes": 90,
    "format": "hands-on lab"
}

json_string = json.dumps(session)
print("JSON string:", json_string)
print("Type:", type(json_string))

back_to_dict = json.loads(json_string)
print("Converted back:", back_to_dict)
print("Type:", type(back_to_dict))
