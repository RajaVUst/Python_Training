# Day 6 - Exercise 26

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

                except (ValueError, TypeError, KeyError):
                    continue

    except FileNotFoundError:
        print(f"{path} was not found.")
        return {}

    return scores


loaded_scores = load_scores("scores.csv")
print(loaded_scores)

