import csv
with open("scores.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)


#         output
#         ['name', 'score']
# ['Asha', '85']
# ['Rahul', '92']
# ['Priya', '78']
# ['Arun', '105']
# ['Meena', '']