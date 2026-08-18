import json

with open(r"Day_6\Ref doc\profile.json", "r") as f:
    profile = json.load(f)

print("Name:", profile["name"])
print("Completed days:", len(profile["completed_days"]))

# Output:
# Name: John Doe
# Completed days: 5