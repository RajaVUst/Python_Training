import json
 
# Original config
config = {
    "app_name": "InventoryApp",
    "version": 1.2,
    "features": ["export", "search", "notifications"],
    "limits": {
        "max_users": 100,
        "max_items": 5000
    }
}
 
# 1. Write to config.json (pretty printed)
with open("config.json", "w") as file:
    json.dump(config, file, indent=2)
 
print("config.json created\n")
 
# 2. Read it back
with open("config.json", "r") as file:
    config_data = json.load(file)
 
print("Max Users:", config_data["limits"]["max_users"])
 
# 3. Add dark_mode feature
config_data["features"].append("dark_mode")
 
# Save updated config
with open("config.json", "w") as file:
    json.dump(config_data, file, indent=2)
 
print("\ndark_mode added and config.json updated")
 
# 4. Deliberately create a corrupted JSON file
with open("config_bad.json", "w") as file:
    file.write("""
{
  "app_name": "InventoryApp",
  "version": 1.2
""")   # Missing closing brace
 
# 5. Try to load corrupted JSON
try:
    with open("config_bad.json", "r") as file:
        bad_config = json.load(file)
 
except json.JSONDecodeError as e:
    print("\nJSONDecodeError caught:")
    print(e)
 
# Output:
"""
config.json created
Max Users: 100
dark_mode added and config.json updated
JSONDecodeError caught:
Expecting ',' delimiter: line 5 column 1 (char 49)
"""
 