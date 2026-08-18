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
    config = load_config(r"Day_6\Ref doc\config.json")
    print(config)

except MissingConfigKeyError as e:
    print("Configuration Error:", e)

except FileNotFoundError:
    print("Config file not found.")

# Output:
# Config file not found.