import json


class MissingConfigKeyError(Exception):
    pass


def load_config(path):
    with open(path, "r") as f:
        data = json.load(f)

    if "batch_size" not in data:
        raise MissingConfigKeyError("Missing required config key: batch_size")

    if "learning_rate" not in data:
        raise MissingConfigKeyError("Missing required config key: learning_rate")

    return data


try:
    config = load_config("config.json")
    print(config)
except MissingConfigKeyError as error:
    print("Configuration error:", error)

# OUTPUT

# {'batch_size': 32, 'learning_rate': 0.001}
