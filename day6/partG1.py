import csv


def load_scores(path):
    scores = {}
    try:
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    scores[row["name"]] = int(row["score"])
                except (ValueError, TypeError):
                    continue
    except FileNotFoundError:
        return {}
    return scores


print(load_scores("scores.csv"))

# OUTPUT

# {'Asha': 92, 'Ben': 105, 'Divya': -4, 'Eli': 78}
