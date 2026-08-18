
import csv


with open("Day6/scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    valid_scores = []
    for row in reader:
        if row["score"] != "":
            valid_scores.append(int(row["score"]))
        else:
            print(f"Skipping {row['name']}: blank score")
average = sum(valid_scores) / len(valid_scores)
print("Average:", average)

#output
# Skipping Tara: blank score
# Average: 59.5