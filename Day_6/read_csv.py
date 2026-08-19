import csv

with open("scores.csv", "r", newline="") as f:
    reader = csv.reader(f)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

# output:
# s/308239/Python/Python_Training/Day_6/read_csv.py
# Header: ['name', 'score']
# ['Amit', '85']
# ['Reni', '92']
# ['Tara', '105']
# ['Sam', '']
# ['John', '-10']