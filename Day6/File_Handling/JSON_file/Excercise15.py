# Modify and re-save JSON

import json

with open("Day6/profile.json", "r") as f:
    data = json.load(f)
data["completed_days"].append(6)

with open("Day6/profile.json", "w") as f:
    json.dump(data, f, indent=2)