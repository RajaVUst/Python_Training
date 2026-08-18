
import json

session = {"topic": "File Handling & Exceptions", "duration_minutes": 90, "format": "hands-on lab"}
session_str = json.dumps(session)
print(session_str)
session_back = json.loads(session_str)
print(type(session_back))

#output
# {"topic": "File Handling & Exceptions", "duration_minutes": 90, "format": "hands-on lab"}
# <class 'dict'>
