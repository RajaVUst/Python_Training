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
        print("File not found.")
        return {}

    return scores

result = load_scores("DAY_6_EXERCISES/scores.csv")
print(result)

"""
Output->
{'Alice': 95, 'Bob': 110, 'Charlie': 78, 'Eva': -5}
"""
