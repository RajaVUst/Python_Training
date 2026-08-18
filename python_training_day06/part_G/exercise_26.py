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


scores = load_scores("../part_C/scores.csv")

print(scores)



#output:
'''{'Alice': 85, 'Bob': 72, 'Charlie': 95}'''