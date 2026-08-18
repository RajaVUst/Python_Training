# Read a CSV with DictReader

import csv

with open("Day6/scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row["name"], ":", row["score"])


# Output:
# Gokul : 80
# Bala : 95
# Jeeva : 110
# Timmy : 
# Logesh : 70