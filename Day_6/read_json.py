import json

with open("profile.json", "r") as f:
    profile = json.load(f)

print(profile["name"])
print(len(profile["completed_days"]))

# output:
# Asha
# 5