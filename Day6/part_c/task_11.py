import csv

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['name']}: {row['score']}")


# Alice: 85
# Bob: 105
# Charlie: 
# David: 72
# Eva: -10