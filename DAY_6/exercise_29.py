import json

class MissingConfigKeyError(Exception):
    pass

def load_config(path):
    with open(path, "r") as f:
        data = json.load(f)
    if "batch_size" not in data:
        raise MissingConfigKeyError("Missing required key: 'batch_size'")
    if "learning_rate" not in data:
        raise MissingConfigKeyError("Missing required key: 'learning_rate'")
    return data

# Create a sample config file for testing
import json
with open("config.json", "w") as f:
    json.dump({"batch_size": 32, "learning_rate": 0.001}, f)

# Test with valid config
try:
    config = load_config("config.json")
    print("Config loaded:", config)
except MissingConfigKeyError as e:
    print("Config error:", e)

# Test with missing key
with open("bad_config.json", "w") as f:
    json.dump({"batch_size": 32}, f)

try:
    config = load_config("bad_config.json")
    print("Config loaded:", config)
except MissingConfigKeyError as e:
    print("Config error:", e)
