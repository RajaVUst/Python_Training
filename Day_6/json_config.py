import json

class MissingConfigKeyError(Exception):
    pass

def load_config(path):
    with open(path, "r") as f:
        data = json.load(f)

    if "batch_size" not in data:
        raise MissingConfigKeyError("batch_size is missing")

    if "learning_rate" not in data:
        raise MissingConfigKeyError("learning_rate is missing")

    return data


try:
    config = load_config("config.json")
    print(config)

except MissingConfigKeyError as e:
    print(f"Configuration error: {e}")

# output:
# {'batch_size': 32, 'learning_rate': 0.001}