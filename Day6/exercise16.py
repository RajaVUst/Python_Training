import json

session = {
    "topic": "File Handling and Exceptions",
    "duration_minutes": 90,
    "format": "Hands-on practice"
}

json_string = json.dumps(session)

print("JSON string:", json_string)

converted_data = json.loads(json_string)

print("Converted data:", converted_data)
print("Type:", type(converted_data))

#output
'''
JSON string: {"topic": "File Handling and Exceptions", "duration_minutes": 90, "format": "Hands-on practice"}
Converted data: {'topic': 'File Handling and Exceptions', 'duration_minutes': 90, 'format': 'Hands-on practice'}
Type: <class 'dict'>
'''