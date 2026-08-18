import csv
import json

# Exercise 26: Safe score loader (function)
def load_scores(path):
    scores = {}
    try:
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    scores[row["name"]] = int(row["score"])
                except ValueError:
                    continue
    except FileNotFoundError:
        return {}
    return scores
print(load_scores("scores.csv"))
# Output:
# {'Amit': 85, 'Varsha': 95, 'Tara': 120, 'Anu': -10}



# Exercise 27: Validate and summarise
def summarise(scores):
    return {
        "count": len(scores),
        "average": sum(scores.values()) / len(scores),
        "highest": max(scores.values()),
        "lowest": min(scores.values())
    }
scores = {
    "Amit": 85,
    "Varsha": 95,
    "Tara": 78,
    "Rahul": 88
}
print(summarise(scores))
# Output:
# {
#   'count': 4,
#   'average': 86.5,
#   'highest': 95,
#   'lowest': 78
# }



# Exercise 28: Word frequency counter
def word_frequencies(path):
    frequencies = {}

    with open(path, "r") as f:
        for line in f:
            words = line.lower().split()

            for word in words:
                frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies
print(word_frequencies("notes.txt"))
# Output:
# {
#   'python': 1,
#   'is': 2,
#   'easy': 1,
#   'to': 1,
#   'learn.': 1,
#   'files': 2,
#   'help': 1,
#   'store': 1,
#   'information.': 1,
#   'reading': 1,
#   'important.': 1,
#   'practice': 1,
#   'every': 1,
#   'day.': 1,
#   'coding': 1,
#   'improves': 1,
#   'skills.': 1
# }



# Exercise 29: JSON config with validation
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
config = {
    "batch_size": 32,
    "learning_rate": 0.01
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

try:
    print(load_config("config.json"))

except MissingConfigKeyError as e:
    print("Configuration Error:", e)

# Output:
# {'batch_size': 32, 'learning_rate': 0.01}