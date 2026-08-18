# Catch your custom exception

import csv

def load_scores(path):
    scores = {}

    try:
        with open(path, "r") as f:
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

result = load_scores("Day6/scores.csv")
print(result)

# Output:
# {'Gokul': 80, 'Bala': 95, 'Jeeva': 110, 'Logesh': 70}