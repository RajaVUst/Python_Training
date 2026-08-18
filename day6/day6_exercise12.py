import csv

scores = []

with open("day6/scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))

average = sum(scores) / len(scores)

print("Scores:", scores)
print("Average:", average)

"""
OUTPUT:
Scores: [100, 209, 87, -38]
Average: 89.5
"""