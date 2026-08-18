import json

with open("profile.json", "r") as f:
    data = json.load(f)

print(data["name"])
print(len(data["completed_days"]))


#output:
'''Asha
5'''