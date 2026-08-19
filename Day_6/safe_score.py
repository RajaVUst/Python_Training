import csv

def load_scores(path):
    scores = {}

    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    score = int(row["score"])
                    scores[row["name"]] = score

                except ValueError:
                    continue

    except FileNotFoundError:
        return {}

    return scores

print(load_scores("scores.csv"))

# output:
# {'Amit': 85, 'Reni': 92, 'Tara': 105, 'John': -10}