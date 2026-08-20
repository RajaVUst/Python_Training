import json

config = {
    "app_name": "InventoryApp",
    "version": 1.2,
    "features": ["export", "search", "notifications"],
    "limits": {
        "max_users": 100,
        "max_items": 5000
    }
}

with open(r"Day_8/refdoc/config.json", "w") as file:
    json.dump(config, file, indent=2)

print("config.json created\n")

with open(r"Day_8/refdoc/config.json", "r") as file:
    config_data = json.load(file)

print("Max Users:", config_data["limits"]["max_users"])

config_data["features"].append("dark_mode")

with open(r"Day_8/refdoc/config.json", "w") as file:
    json.dump(config_data, file, indent=2)

print("\ndark_mode added and config.json updated")

with open(r"Day_8/refdoc/config_bad.json", "w") as file:
    file.write("""
{
  "app_name": "InventoryApp",
  "version": 1.2
""")   

try:
    with open(r"Day_8/refdoc/config_bad.json", "r") as file:
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