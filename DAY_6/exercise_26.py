import csv

def load_scores(path):
    try:
        f = open(path, "r")
    except FileNotFoundError:
        print(f"File '{path}' not found. Returning empty dict.")
        return {}

    scores = {}
    with f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                scores[row["name"]] = int(row["score"])
            except (ValueError, KeyError):
                print(f"Skipping bad row: {row}")
    return scores

result = load_scores("scores.csv")
print(result)
