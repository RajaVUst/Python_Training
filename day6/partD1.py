import json


with open("profile.json", "r") as f:
    profile = json.load(f)

print("Name:", profile["name"])
print("Completed days:", len(profile["completed_days"]))

# OUTPUT

# Name: Asha
# Completed days: 5
