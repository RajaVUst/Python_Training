import json

with open("profile.json", "r") as f:
    profile = json.load(f)

profile["completed_days"].append(6)

with open("profile.json", "w") as f:
    json.dump(profile, f, indent=2)

print("profile.json updated:", profile["completed_days"])
