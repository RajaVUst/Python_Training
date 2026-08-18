
import csv

with open("Day6/scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['score']}")
        
#output
# Amit: 78
# Reni: 105
# Tara:
# Sam: 65
# Neha: -10