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

with open("config.json", "w") as file:
    json.dump(config, file, indent=2)

with open("config.json", "r") as file:
    config = json.load(file)

print("Maximum users:", config["limits"]["max_users"])

# Output:
# Maximum users: 100


config["features"].append("dark_mode")

with open("config.json", "w") as file:
    json.dump(config, file, indent=2)

print("Configuration updated.")

# Output:
# Configuration updated.

# JSON Exception Handling

with open("config.json", "w") as file:
    file.write('{"app_name": "InventoryApp", "version": 1.2, invalid}')

try:
    with open("config.json", "r") as file:
        config = json.load(file)

    print(config)

except json.JSONDecodeError:
    print("Invalid JSON format.")

# If the JSON file is deliberately corrupted:
# Output:
# Invalid JSON format.