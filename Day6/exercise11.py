import csv

with open("scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['name']}: {row['score']}")


#output
'''
Saikiran: 85
vignesh: 91
aishwarya: 
Sam: 105
Asha: -5
'''