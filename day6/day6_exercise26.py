import csv

def load_scores(path):
    scores = {}

    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    scores[row["name"]] = int(row["score"])
                except ValueError:
                    # Skip rows with invalid scores
                    continue

    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return {}

    return scores

print(load_scores("day6/scores.csv"))

"""
OUTPUT:
{'Lekhya': 100, 'Pranav': 209, 'Chris': 87, 'Chaila': -38}
"""