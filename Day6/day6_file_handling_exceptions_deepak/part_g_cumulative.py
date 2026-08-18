import csv, json

# Setup: scores.csv with one extra bad row (non-numeric)
with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["Asha", "88"])
    writer.writerow(["Ravi", "91"])
    writer.writerow(["Kiran", "150"])
    writer.writerow(["Meera", ""])
    writer.writerow(["Zoya", "76"])
    writer.writerow(["Omar", "not_a_number"])

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
                    print(f"Skipping bad row: {row}")
    except FileNotFoundError:
        print(f"{path} not found -- returning empty results.")
    return scores

loaded = load_scores("scores.csv")
print(loaded)
print(load_scores("does_not_exist.csv"))
# Output:
# Skipping bad row: {'name': 'Meera', 'score': ''}
# Skipping bad row: {'name': 'Omar', 'score': 'not_a_number'}
# {'Asha': 88, 'Ravi': 91, 'Kiran': 150, 'Zoya': 76}
# does_not_exist.csv not found -- returning empty results.
# {}

# Exercise 27 - Validate and summarise
def summarise(scores):
    values = list(scores.values())
    return {"count": len(values), "average": round(sum(values) / len(values), 2),
             "highest": max(values), "lowest": min(values)}

print(summarise(loaded))
# Output: {'count': 4, 'average': 101.25, 'highest': 150, 'lowest': 76}

# Exercise 28 - Word frequency counter
def word_frequencies(path):
    frequencies = {}
    with open(path, "r") as f:
        for line in f:
            for word in line.lower().split():
                frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

print(word_frequencies("notes.txt"))
# Output:
# {'python': 1, 'is': 2, 'a': 1, 'beginner-friendly': 1, 'language.': 1, 'today': 1,
#  'we': 1, 'are': 1, 'learning': 1, 'file': 1, 'handling.': 1, 'files': 1, 'can': 1,
#  'be': 1, 'read,': 1, 'written,': 1, 'and': 1, 'appended.': 1, 'exceptions': 1,
#  'help': 1, 'programs': 1, 'avoid': 1, 'crashing.': 1, 'practice': 1, 'the': 1,
#  'key': 1, 'to': 1, 'mastering': 1, 'this': 1, 'topic.': 1}

# Exercise 29 - JSON config with validation
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

with open("config_good.json", "w") as f:
    json.dump({"batch_size": 32, "learning_rate": 0.001}, f)
with open("config_bad.json", "w") as f:
    json.dump({"batch_size": 32}, f)

try:
    print(load_config("config_good.json"))
except MissingConfigKeyError as e:
    print(f"Config error: {e}")

try:
    print(load_config("config_bad.json"))
except MissingConfigKeyError as e:
    print(f"Config error: {e}")
# Output:
# {'batch_size': 32, 'learning_rate': 0.001}
# Config error: Missing key: learning_rate