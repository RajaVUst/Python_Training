import csv

# Exercise 10
with open("scores.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)

    print("Header:", header)

    for row in reader:
        print(row)

#output
'''
Header: ['name', 'score']
['Saikiran', '85']
['vignesh', '91']
['aishwarya', '']
['Sam', '105']
['Asha', '-5']
'''