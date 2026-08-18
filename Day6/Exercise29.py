import json

class MissingConfigKeyError(Exception):
    pass

def load_config(path):
    with open(path) as f:
        data = json.load(f)
    if "batch_size" not in data:
        raise MissingConfigKeyError("Missing 'batch_size' in config")
    if "learning_rate" not in data:
        raise MissingConfigKeyError("Missing 'learning_rate' in config")
    return data

with open("config.json", "w") as f:
    json.dump({"batch_size": 32}, f)

try:
    cfg = load_config("config.json")
    print(cfg)
except MissingConfigKeyError as e:
    print("Config error:", e)

#output
# Config error: Missing 'learning_rate' in config
