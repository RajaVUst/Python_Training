import json

with open("profile.json", "r") as f:
    data = json.load(f)

data["completed_days"].append(6)

with open("profile.json", "w") as f:
    json.dump(data, f, indent=2)


