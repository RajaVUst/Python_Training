

import csv

with open("Day6/scores.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)
        
#output
# Header: ['name', 'score']
# ['Amit', '78']
# ['Reni', '105']
# ['Tara', '']
# ['Sam', '65']
# ['Neha', '-10']