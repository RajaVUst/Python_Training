import csv

with open("day6/scores.csv", "r", newline="") as f:
    reader = csv.reader(f)

    header = next(reader)
    print("Header:", header)

    print("Data Rows:")
    for row in reader:
        print(row)
        
"""
OUTPUT:
Header: ['name', 'score']
Data Rows:
['Aron', '']
['Lekhya', '100']
['Pranav', '209']
['Chris', '87']
['Chaila', '-38']
"""