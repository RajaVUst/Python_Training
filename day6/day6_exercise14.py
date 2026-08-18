import json

with open("day6/profile.json", "r") as f:
    data = json.load(f)

print("Name:", data["name"])
print("Completed days:", len(data["completed_days"]))

"""
OUTPUT:
Name: Asha
Completed days: 5
"""