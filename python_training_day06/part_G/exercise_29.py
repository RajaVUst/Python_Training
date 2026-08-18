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
    print("Configuration error:", e)



#output:
'''Configuration error: batch_size is missing'''