import csv
with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], ":", row["score"])

#      output
#     Asha : 85
# Rahul : 92
# Priya : 78
# Arun : 105
# Meena : 