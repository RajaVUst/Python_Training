import csv
import json

data = []

with open("../part_C/scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        data.append(dict(row))

with open("scores.json", "w") as f:
    json.dump(data, f, indent=2)