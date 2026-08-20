
import json
config = {
    "app_name": "InventoryApp",
    "version": 1.2,
    "features": [
        "export",
        "search",
        "notifications"
    ],
    "limits": {
        "max_users": 100,
        "max_items": 5000
    }
}


#  config to config.json using json.dump.

with open("config.json", "w") as file:
    json.dump(config, file, indent=2)


#  Read config.json using json.load  and print max_users

with open("config.json", "r") as file:
    loaded_config = json.load(file)

print("Maximum users:", loaded_config["limits"]["max_users"])


# Add "dark_mode" to features and save again

loaded_config["features"].append("dark_mode")

with open("config.json", "w") as file:
    json.dump(loaded_config, file, indent=2)


# Deliberately corrupt the JSON file   The closing } is intentionally removed.

with open("config.json", "w") as file:
    file.write("""
{
  "app_name": "InventoryApp",
  "version": 1.2,
  "features": ["export", "search", "notifications", "dark_mode"],
  "limits": {
    "max_users": 100,
    "max_items": 5000
  }
""")


#  Try to load the corrupted JSON

try:
    with open("config.json", "r") as file:
        corrupted_config = json.load(file)

except json.JSONDecodeError as error:
    print("JSON Error occurred!")
    print(error)


# Expected exception:
# json.JSONDecodeError

# output
# Maximum users: 100
# JSON Error occurred!
# Expecting ',' delimiter: line 10 column 1 (char 179)
# 
# This occurs because the JSON file is missing
# the final closing curly bracket }.