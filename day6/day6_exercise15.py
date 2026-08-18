import json

# Read the file
with open("day6/profile.json", "r") as f:
    data = json.load(f)

# Update the data
data["completed_days"].append(6)

# Write it back
with open("day6/profile.json", "w") as f:
    json.dump(data, f, indent=2)
    
"""
OUTPUT:
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