import csv

scores = []

with open("DAY_6_EXERCISES/scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))

average = sum(scores) / len(scores)

print("Scores:", scores)
print("Average:", average)

"""
Output->
Scores: [95, 110, 78, -5]
Average: 69.5
"""