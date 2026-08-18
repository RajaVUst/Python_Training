# Day 6 - Exercise 29
import json
#for creating files
# config={
#     "batch_size":32,
#     "learning_rate":0.001
# }
#
# with open("config.json","w") as f:
#     json.dump(config,f,indent=2)

import json


class MissingConfigKeyError(Exception):
    pass


def load_config(path):
    with open(path, "r") as f:
        data = json.load(f)

    required_keys = ["batch_size", "learning_rate"]

    for key in required_keys:
        if key not in data:
            raise MissingConfigKeyError(
                f"Required configuration key '{key}' is missing."
            )

    return data


try:
    config = load_config("config.json")
    print("Configuration loaded:", config)

except FileNotFoundError:
    print("The configuration file was not found.")

except json.JSONDecodeError:
    print("The configuration file contains invalid JSON.")

except MissingConfigKeyError as error:
    print("Configuration error:", error)

#output
'''
Configuration loaded: {'batch_size': 32, 'learning_rate': 0.001}
'''

