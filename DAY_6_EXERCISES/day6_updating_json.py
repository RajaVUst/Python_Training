import json

with open("DAY_6_EXERCISES/profile.json", "r") as f:
    profile = json.load(f)

profile["completed_days"].append(6)

with open("DAY_6_EXERCISES/profile.json", "w") as f:
    json.dump(profile, f, indent=2)

"""
Output JSON->
{
  "name": "Asha",
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
"""
