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

                except (ValueError, TypeError):
                    continue

    except FileNotFoundError:
        return {}

    return scores


result = load_scores("scores.csv")
print(result)