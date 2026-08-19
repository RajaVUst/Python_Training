import csv


with open("scores.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# OUTPUT

# Header: ['name', 'score']
# ['Asha', '92']
# ['Ben', '105']
# ['Chen', '']
# ['Divya', '-4']
# ['Eli', '78']
