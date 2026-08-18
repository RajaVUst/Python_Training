import csv

with open("day6/scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['name']}: {row['score']}")
        
"""
OUTPUT:
Aron: 
Lekhya: 100
Pranav: 209
Chris: 87
Chaila: -38
"""