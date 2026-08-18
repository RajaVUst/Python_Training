import csv
scores = []

with open("scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))

if scores:
    average = sum(scores) / len(scores)
    print("Average:", average)
else:
    print("No valid scores found.")

#output
'''
Average: 69.0
'''