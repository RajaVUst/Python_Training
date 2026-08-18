
import json

with open("Day6/profile.json") as f:
    profile = json.load(f)
print(profile["name"])
print(len(profile["completed_days"]))

#output
# Asha
# 5