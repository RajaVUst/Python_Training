
import csv
import json

with open("Day6/scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    rows = [dict(row) for row in reader]

with open("Day6/scores.json", "w") as f:
    json.dump(rows, f, indent=2)

with open("Day6/scores.json") as f:
    print(f.read())
    
#output
# [
#   {
#     "name": "Amit",
#     "score": "78"
#   },
#   {
#     "name": "Reni",
#     "score": "105"
#   },
#   {
#     "name": "Tara",
#     "score": ""
#   },
#   {
#     "name": "Sam",
#     "score": "65"
#   },
#   {
#     "name": "Neha",
#     "score": "-10"
#   }
# ]