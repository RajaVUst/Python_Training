import json

class MissingConfigKeyError(Exception):
    pass

def load_config(path):
    with open(path, "r") as f:
        data = json.load(f)

    if "batch_size" not in data:
        raise MissingConfigKeyError("Missing key: batch_size")

    if "learning_rate" not in data:
        raise MissingConfigKeyError("Missing key: learning_rate")

    return data

try:
    config = load_config("config.json")
    print(config)

except MissingConfigKeyError as e:
    print("Configuration error:", e)

except FileNotFoundError:
    print("Configuration file not found.")

"""
OUTPUT:
Configuration file not found.
"""