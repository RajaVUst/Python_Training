import csv

scores = []

with open("scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))

average = sum(scores) / len(scores)

print(average)

# output:
# 68.0