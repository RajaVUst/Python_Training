import json

# Setup: profile.json
with open("profile.json", "w") as f:
    json.dump({"name": "Asha", "track": "Python Readiness", "completed_days": [1, 2, 3, 4, 5]}, f, indent=2)

# Exercise 14 - Read a JSON file
with open("profile.json", "r") as f:
    data = json.load(f)
print(data["name"])
print(len(data["completed_days"]))
# Output:
# Asha
# 5

# Exercise 15 - Modify and re-save JSON
with open("profile.json", "r") as f:
    data = json.load(f)
data["completed_days"].append(6)
with open("profile.json", "w") as f:
    json.dump(data, f, indent=2)

with open("profile.json", "r") as f:
    print(f.read())
# Output:
# {
#   "name": "Asha",
#   "track": "Python Readiness",
#   "completed_days": [1, 2, 3, 4, 5, 6]
# }

# Exercise 16 - String <-> JSON with loads/dumps
session = {"topic": "File Handling & Exceptions", "duration_minutes": 90, "format": "hands-on lab"}
session_str = json.dumps(session)
print(session_str)
session_back = json.loads(session_str)
print(type(session_back))
# Output:
# {"topic": "File Handling & Exceptions", "duration_minutes": 90, "format": "hands-on lab"}
# <class 'dict'>

# Exercise 17 - CSV to JSON
import csv
rows = []
with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(dict(row))
with open("scores.json", "w") as f:
    json.dump(rows, f, indent=2)
with open("scores.json", "r") as f:
    print(f.read())
# Output:
# [
#   {"name": "Asha", "score": "88"},
#   {"name": "Ravi", "score": "91"},
#   {"name": "Kiran", "score": "150"},
#   {"name": "Meera", "score": ""},
#   {"name": "Zoya", "score": "76"}
# ]