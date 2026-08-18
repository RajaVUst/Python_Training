# Compute an average from CSV data

import csv

scores = []

with open("Day6/scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))

average = sum(scores) / len(scores)
print("Average:", average)


# Output:
# Average: 88.75