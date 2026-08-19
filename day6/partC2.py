import csv


with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f'{row["name"]}: {row["score"]}')

# OUTPUT

# Asha: 92
# Ben: 105
# Chen:
# Divya: -4
# Eli: 78
