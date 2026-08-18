import csv
import json

rows = []

with open("day6/scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        rows.append(dict(row))

with open("day6/scores.json", "w") as f:
    json.dump(rows, f, indent=2)
    
"""
OUTPUT:
[
  {
    "name": "Aron",
    "score": ""
  },
  {
    "name": "Lekhya",
    "score": "100"
  },
  {
    "name": "Pranav",
    "score": "209"
  },
  {
    "name": "Chris",
    "score": "87"
  },
  {
    "name": "Chaila",
    "score": "-38"
  }
]
"""