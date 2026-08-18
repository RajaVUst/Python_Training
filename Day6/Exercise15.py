
import json


with open("Day6/profile.json") as f:
    profile = json.load(f)
profile["completed_days"].append(6)
with open("Day6/profile.json", "w") as f:
    json.dump(profile, f, indent=2)

with open("Day6/profile.json") as f:
    print(f.read())
#output
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