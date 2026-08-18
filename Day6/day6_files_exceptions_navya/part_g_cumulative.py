import csv

# Exercise 26 - Safe score loader (function)
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

loaded = load_scores("scores.csv")
print(loaded)
# Output: {'Navya': 85, 'Deepak': 105, 'Hema': 45, 'Mamatha': -10}


# Exercise 27 - Validate and summarise
def summarise(scores):
    values = list(scores.values())
    return {
        "count": len(values),
        "average": sum(values) / len(values),
        "highest": max(values),
        "lowest": min(values)
    }

summary = summarise(loaded)
print(summary)
# Output: {'count': 4, 'average': 56.25, 'highest': 105, 'lowest': -10}


# Exercise 28 - Word frequency counter
def word_frequencies(path):
    word_counts = {}
    with open(path, "r") as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

frequencies = word_frequencies("notes.txt")
print(frequencies)
# Output: {'started': 1, 'learning': 2, 'python': 1, 'this': 1, 'week': 1, 'practiced': 1, 'loops': 1, 'and': 1, 'conditionals': 1, 'built': 1, 'small': 1, 'scripts': 1, 'daily': 1, 'file': 1, 'handling': 1, 'now': 1, 'excited': 1, 'for': 1, 'the': 1, 'next': 1, 'module': 1}


# Exercise 29 - JSON config with validation
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
    print(e)