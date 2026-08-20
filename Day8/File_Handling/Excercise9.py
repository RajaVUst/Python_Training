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

# Write json
with open("Day8/config.json", "w") as file:
    json.dump(config, file, indent=2)
print("Config saved")

# Read Json
with open("Day8/config.json", "r") as file:
    config = json.load(file)
print(config["limits"]["max_users"])

# Output:100

# Add dark mode
config["features"].append("dark_mode")
with open("Day8/config.json", "w") as file:
    json.dump(config, file, indent=2)
print("dark_mode added")

# # Output: dark_mode added


# Handle Incorrect json
import json
try:
    with open("Day8/config.json", "r") as file:
        config = json.load(file)
except json.JSONDecodeError:
    print("Invalid JSON file")