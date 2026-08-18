import csv

with open("scores.csv", "r") as f:
    reader = csv.reader(f)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)



# Header: ['name', 'score']
# ['Alice', '85']
# ['Bob', '105']
# ['Charlie', '']
# ['David', '72']
# ['Eva', '-10']