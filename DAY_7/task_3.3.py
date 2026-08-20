import json
import os

base = os.path.dirname(__file__)
config_path = os.path.join(base, "config.json")

config = {
    "app_name": "InventoryApp",
    "version": 1.2,
    "features": ["export", "search", "notifications"],
    "limits": {"max_users": 100, "max_items": 5000}
}

# Write config to JSON (pretty-printed)
with open(config_path, "w") as f:
    json.dump(config, f, indent=2)

print("Written config.json")

# Read back and access nested value
with open(config_path, "r") as f:
    loaded = json.load(f)

print("max_users:", loaded["limits"]["max_users"])

# Modify features and save back
loaded["features"].append("dark_mode")
with open(config_path, "w") as f:
    json.dump(loaded, f, indent=2)

print("Updated features:", loaded["features"])

# Deliberately corrupt the JSON and observe the error
with open(config_path, "r") as f:
    good_content = f.read()

corrupted = good_content[:-1]  # remove the last closing brace
with open(config_path, "w") as f:
    f.write(corrupted)

print("\nAttempting to load corrupted JSON...")
try:
    with open(config_path, "r") as f:
        json.load(f)
except json.JSONDecodeError as e:
    print(f"JSONDecodeError caught: {e}")

# Restore valid config for future runs
with open(config_path, "w") as f:
    json.dump(loaded, f, indent=2)
