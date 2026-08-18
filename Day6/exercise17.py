# Day 6 - Exercise 17
import csv
import json
score_rows = []

with open("scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        score_rows.append(dict(row))

with open("scores.json", "w") as f:
    json.dump(score_rows, f, indent=2)