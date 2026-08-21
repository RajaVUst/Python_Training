import json

config = {
    "app_name": "MyApp",
    "features": ["login", "reports"],
    "limits": {
        "max_users": 100,
        "timeout": 30
    }
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=2)
    
with open("config.json", "r") as f:
    config = json.load(f)

print(config["limits"]["max_users"])


config["features"].append("dark_mode")

with open("config.json", "w") as f:
    json.dump(config, f, indent=2)
    
    
# OUTPUT

# {
#   "app_name": "MyApp",
#   "features": [
#     "login",
#     "reports",
#     "dark_mode"
#   ],
#   "limits": {
#     "max_users": 100,
#     "timeout": 30
#   }
# }

# 100