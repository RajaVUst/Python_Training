import json

# Exercise 14 - Read a JSON file
with open("profile.json", "r") as f:
    data = json.load(f)

print(data["name"])
print(len(data["completed_days"]))
# Output:
# Navya
# 5


# Exercise 15 - Modify and re-save JSON
with open("profile.json", "r") as f:
    data = json.load(f)

data["completed_days"].append(6)

with open("profile.json", "w") as f:
    json.dump(data, f, indent=2)


# Exercise 16 - String <-> JSON with loads/dumps
session = {
    "topic": "File Handling and Exceptions",
    "duration_minutes": 90,
    "format": "Practice Lab"
}

session_str = json.dumps(session)
print(session_str)

session_back = json.loads(session_str)
print(type(session_back))
# Output:
# {"topic": "File Handling and Exceptions", "duration_minutes": 90, "format": "Practice Lab"}
# <class 'dict'>


# Exercise 17 - CSV to JSON
import csv

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = [dict(row) for row in reader]

with open("scores.json", "w") as f:
    json.dump(rows, f, indent=2)