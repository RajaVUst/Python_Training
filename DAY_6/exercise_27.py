import csv

def load_scores(path):
    try:
        f = open(path, "r")
    except FileNotFoundError:
        return {}
    scores = {}
    with f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                scores[row["name"]] = int(row["score"])
            except (ValueError, KeyError):
                pass
    return scores

def summarise(scores):
    values = scores.values()
    return {
        "count":   len(values),
        "average": sum(values) / len(values),
        "highest": max(values),
        "lowest":  min(values),
    }

scores = load_scores("scores.csv")
print("Scores:", scores)
print("Summary:", summarise(scores))
