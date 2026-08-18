import json
with open("profile.json", "r") as f:
    profile = json.load(f)

if 6 not in profile["completed_days"]:
    profile["completed_days"].append(6)

with open("profile.json", "w") as f:
    json.dump(profile, f, indent=2)

#output
'''
{
  "name": "Saikiran",
  "track": "Python Readiness",
  "completed_days": [
    1,
    2,
    3,
    4,
    5,
    6
  ]
}
'''
