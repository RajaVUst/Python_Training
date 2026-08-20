def load_scores(path):
    scores = {}

    try:
        with open(path, "r") as file:
            for line in file:
                try:
                    name, score = line.strip().split(",")
                    scores[name] = int(score)
                except ValueError:
                    # Skip rows with bad format or non-integer scores
                    continue
    except FileNotFoundError:
        return {}
    return scores
result = load_scores("scores.csv")
print(result)
# ouput 
# {'senin': 65, 'akshay': 80, 'ameen': 86, 'ashik': -77}

# Exercise 28: Word frequency counter 

def word_frequencies(path):
    frequencies = {}

    with open(path, "r") as file:
        text = file.read().lower()

    words = text.split()

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies
result = word_frequencies("diary.txt")
print(result)

#output 

# {'learned': 4, 'how': 1, 'to': 1, 'create': 1, 'funtion.': 1, 'about': 2, 'list,': 1, 'tuple,': 1, 'dict.': 1, 'statements.': 1, 'read': 1, 'and': 1, 'write.': 1}

# Exercise 29: JSON config with validation 

import json

class MissingConfigKeyError(Exception):
    pass

def load_config(path):
    with open(path, "r") as file:
        data = json.load(file)

    if "batch_size" not in data:
        raise MissingConfigKeyError("Missing required key: batch_size")

    if "learning_rate" not in data:
        raise MissingConfigKeyError("Missing required key: learning_rate")

    return data

try:
    config = load_config("config.json")
    print(config)
except MissingConfigKeyError as e:
    print("Configuration error:", e)