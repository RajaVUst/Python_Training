# Day 6 - Exercise 27
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


def summarise(scores):
    if not scores:
        return {
            "count": 0,
            "average": None,
            "highest": None,
            "lowest": None
        }

    values = list(scores.values())

    return {
        "count": len(values),
        "average": sum(values) / len(values),
        "highest": max(values),
        "lowest": min(values)
    }


scores = load_scores("scores.csv")
summary = summarise(scores)

print(summary)


#output
'''

'''
