import csv
import json

records = []

with open("DAY_6_EXERCISES/scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        records.append(dict(row))

with open("DAY_6_EXERCISES/scores.json", "w") as f:
    json.dump(records, f, indent=2)

print("scores.json created")

"""
Output->
scores.json created
"""