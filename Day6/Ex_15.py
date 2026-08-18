import json
 
with open(r"Day_6\Ref doc\profile.json", "r") as f:
    profile = json.load(f)
 
profile["completed_days"].append(6)
 
 
with open(r"Day_6\Ref doc\profile.json", "w") as f:
    json.dump(profile, f, indent=2)
 
print("profile.json updated successfully!")
 
# Output:
# profile.json updated successfully!
 