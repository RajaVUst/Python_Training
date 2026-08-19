import csv

with open("scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['name']}: {row['score']}")

# output:
# s/308239/Python/Python_Training/Day_6/dict_reader.py
# Amit: 85
# Reni: 92
# Tara: 105
# Sam: 
# John: -10