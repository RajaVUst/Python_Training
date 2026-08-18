# CSV to JSON

import csv
import json

data = []

with open("Day6/scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        data.append(dict(row))

with open("Day6/scores.json", "w") as f:
    json.dump(data, f, indent=2)


# Output:
# It will convert the scores.csv file into the scores.json file 