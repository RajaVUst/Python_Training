# Read a JSON file

import json

with open("Day6/profile.json", "r") as f:
    data = json.load(f)

print("Name:", data["name"])
print("Completed days:", len(data["completed_days"]))


# output:
# Name: Logesh
# Completed days: 5