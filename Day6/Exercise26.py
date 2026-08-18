
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
print(loaded)
print(load_scores("missing.csv"))
#output
# {'Amit': 78, 'Reni': 105, 'Sam': 65, 'Neha': -10}
# {}