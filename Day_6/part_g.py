import csv
import json


def load_scores(path):
    scores = {}

    try:
        with open(path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    scores[row["name"]] = int(row["score"])
                except ValueError:
                    print(f"Skipping invalid score for {row['name']}")
                    continue

    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return {}

    return scores



def summarise(scores):
    if not scores:
        return {
            "count": 0,
            "average": 0,
            "highest": None,
            "lowest": None
        }

    values = scores.values()

    return {
        "count": len(values),
        "average": sum(values) / len(values),
        "highest": max(values),
        "lowest": min(values)
    }



def word_frequencies(path):
    frequencies = {}

    try:
        with open(path, "r") as f:
            text = f.read().lower()

            for word in text.split():
                frequencies[word] = frequencies.get(word, 0) + 1

    except FileNotFoundError:
        print(f"File '{path}' not found.")

    return frequencies



class MissingConfigKeyError(Exception):
    pass


def load_config(path):
    with open(path, "r") as f:
        data = json.load(f)

    if "batch_size" not in data:
        raise MissingConfigKeyError("Missing required key: batch_size")

    if "learning_rate" not in data:
        raise MissingConfigKeyError("Missing required key: learning_rate")

    return data




#output
'''Exercise 26
Skipping invalid score for Priya
{'Amit': 78, 'Reni': 91, 'Tara': 85, 'Sam': 67}

Exercise 27
{'count': 4, 'average': 80.25, 'highest': 91, 'lowest': 67}

Exercise 28
{'python': 2, 'is': 3, 'a': 1, 'popular': 1, 'programming': 2, 'language.': 1, 'it': 1, 'used': 1, 'for': 1, 'web': 1, 'development,': 1, 'data': 1, 'analysis,': 1, 'automation,': 1, 'and': 2, 'machine': 1, 'learning.': 1, 'files': 2, 'allow': 1, 'programs': 1, 'to': 2, 'store': 1, 'retrieve': 1, 'information.': 1, 'reading': 1, 'an': 1, 'important': 1, 'skill.': 1, 'practice': 1, 'every': 1, 'day': 1, 'improve': 1, 'your': 1, 'abilities.': 1}

Exercise 29
Config loaded: {'batch_size': 32, 'learning_rate': 0.01}
'''