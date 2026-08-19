import csv
import json

rows = []

with open("scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        rows.append(dict(row))

with open("scores.json", "w") as f:
    json.dump(rows, f, indent=2)