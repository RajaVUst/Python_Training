import csv
scores = []

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))

if len(scores) > 0:
    average = sum(scores) / len(scores)
else:
    average = 0
print("Average:", average)

# OUTPUT

# Average: 67.75
