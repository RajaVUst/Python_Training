import csv

def load_scores(path):
    scores = {}
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    scores[row["name"]] = int(row["score"])
                except ValueError:
                    continue
    except FileNotFoundError:
        return {}
    return scores

loaded = load_scores("Day6/scores.csv")

def summarise(scores):
    values = list(scores.values())
    return {
        "count": len(values),
        "average": sum(values) / len(values),
        "highest": max(values),
        "lowest": min(values),
    }

print(summarise(loaded))

#output
# {'count': 4, 'average': 59.5, 'highest': 105, 'lowest': -10}