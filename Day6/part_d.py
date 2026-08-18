import json
import csv
from constants import PROFILE_JSON, SCORES_CSV, SCORES_JSON

# Create profile.json
profile = {
    "name": "Asha",
    "track": "Python Readiness",
    "completed_days": [1, 2, 3, 4, 5]
}
with open(PROFILE_JSON, "w") as f:
    json.dump(profile, f, indent=2)


# Exercise 14: Read a JSON file
with open(PROFILE_JSON, "r") as f:
    data = json.load(f)
print("Name:", data["name"])
print("Completed Days:", len(data["completed_days"]))
# Output:
# Name: Asha
# Completed Days: 5


# Exercise 15: Modify and re-save JSON
with open(PROFILE_JSON, "r") as f:
    data = json.load(f)
data["completed_days"].append(6)
with open(PROFILE_JSON, "w") as f:
    json.dump(data, f, indent=2)
with open(PROFILE_JSON, "r") as f:
    print(f.read())
# Output:
# {
#   "name": "Asha",
#   "track": "Python Readiness",
#   "completed_days": [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6
#   ]
# }


# Exercise 16: String <-> JSON with loads/dumps
session = {
    "topic": "File Handling",
    "duration_minutes": 60,
    "format": "Practice"
}
json_string = json.dumps(session)
print(json_string)
converted_back = json.loads(json_string)
print(type(converted_back))
# Output:
# {"topic": "File Handling", "duration_minutes": 60, "format": "Practice"}
# <class 'dict'>


# Exercise 17: CSV to JSON
rows = []
with open(SCORES_CSV, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(dict(row))
with open(SCORES_JSON, "w") as f:
    json.dump(rows, f, indent=2)
with open(SCORES_JSON, "r") as f:
    print(f.read())
# Output:
# [
#   {
#     "name": "Amit",
#     "score": "85"
#   },
#   {
#     "name": "Varsha",
#     "score": "95"
#   },
#   {
#     "name": "Tara",
#     "score": "120"
#   },
#   {
#     "name": "Rahul",
#     "score": ""
#   },
#   {
#     "name": "Anu",
#     "score": "-10"
#   }
# ]
