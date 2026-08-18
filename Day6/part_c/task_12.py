import csv

scores = []

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))
        else:
            print(f"Skipping {row['name']} because score is blank")

average = sum(scores) / len(scores)

print("Scores:", scores)
print("Average:", average)



# Skipping Charlie because score is blank
# Scores: [85, 105, 72, -10]
# Average: 63.0