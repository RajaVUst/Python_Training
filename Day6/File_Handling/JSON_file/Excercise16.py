# String <-> JSON with loads/dumps

import json

data = {
    "topic": "File Handling",
    "duration_minutes": 60,
    "format": "Practice"
}

json_string = json.dumps(data)
print(json_string)
new_data = json.loads(json_string)
print(type(new_data))


# Output:
# {"topic": "File Handling", "duration_minutes": 60, "format": "Practice"}
# <class 'dict'>