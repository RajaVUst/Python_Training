import csv
import json

with open("../part_c/scores.csv", "r") as f:
    reader = csv.DictReader(f)

    data = []

    for row in reader:
        data.append(dict(row))

with open("scores.json", "w") as f:
    json.dump(data, f, indent=2)

print("scores.json created successfully.")

# scores.json created successfully.
