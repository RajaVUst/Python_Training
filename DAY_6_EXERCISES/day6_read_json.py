import json

with open("DAY_6_EXERCISES/profile.json", "r") as f:
    profile = json.load(f)

print("Name:", profile["name"])
print("Completed Days:", len(profile["completed_days"]))

"""
Output->
Name: Asha
Completed Days: 5
"""
