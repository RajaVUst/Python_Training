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
    loaded_config = json.load(file)
print("Max Users:", loaded_config["limits"]["max_users"])
loaded_config["features"].append("dark_mode")
with open("config.json", "w") as file:
    json.dump(loaded_config, file, indent=2)
with open("config.json", "w") as file:
    file.write('{"app_name":"InventoryApp"}')
try:
    with open("config.json", "r") as file:
        json.load(file)
except json.JSONDecodeError as e:
    print("Exception Raised:", type(e).__name__)
#  Output:
# Max Users: 100
# Exception Raised: JSONDecodeError
