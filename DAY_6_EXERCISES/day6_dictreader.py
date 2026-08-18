import csv

with open("DAY_6_EXERCISES/scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['name']}: {row['score']}")

"""
Output->
Alice: 95
Bob: 110
Charlie: 78
David: 
Eva: -5
"""