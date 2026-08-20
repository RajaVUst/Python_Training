import json

config = {"app_name": "InventoryApp", "version": 1.2,
          "features": ["export", "search", "notifications"],
          "limits": {"max_users": 100, "max_items": 5000}}

with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

with open("config.json", "r") as f:
    loaded = json.load(f)
print(loaded["limits"]["max_users"])

loaded["features"].append("dark_mode")
with open("config.json", "w") as f:
    json.dump(loaded, f, indent=2)

with open("config_bad.json", "w") as f:
    f.write(json.dumps(loaded, indent=2)[:-1])   # drop closing brace

try:
    with open("config_bad.json", "r") as f:
        json.load(f)
except json.JSONDecodeError as e:
    print(f"Caught json.JSONDecodeError: {e}")
# Output:
# 100
# Caught json.JSONDecodeError: Expecting ',' delimiter: line 14 column 1 (char 198)