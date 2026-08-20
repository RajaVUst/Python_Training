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


# Write JSON
with open(
    "config.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(config, file, indent=2)


# Read JSON
with open(
    "config.json",
    "r",
    encoding="utf-8"
) as file:

    loaded_config = json.load(file)


print(
    "Maximum users:",
    loaded_config["limits"]["max_users"]
)


# Add dark_mode
if "dark_mode" not in loaded_config["features"]:
    loaded_config["features"].append("dark_mode")


# Save changes
with open(
    "config.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(loaded_config, file, indent=2)


# Create deliberately corrupted JSON
with open(
    "config_corrupted.json",
    "w",
    encoding="utf-8"
) as file:

    file.write('{"app_name": "InventoryApp"')


# Attempt to read corrupted JSON
try:
    with open(
        "config_corrupted.json",
        "r",
        encoding="utf-8"
    ) as file:

        json.load(file)

except json.JSONDecodeError as error:
    print("JSONDecodeError caught:", error)

#output

'''
Maximum users: 100
JSONDecodeError caught: Expecting ',' delimiter: line 1 column 28 (char 27)

'''