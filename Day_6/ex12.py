import csv

scores = []

with open(r"Day_6\Ref doc\scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["Score"] != "":
            scores.append(int(row["Score"]))

average = sum(scores) / len(scores)

print("Scores:", scores)
print("Average:", average)

# Output:
# Scores: [85, 92, 78]
# Average: 85.0