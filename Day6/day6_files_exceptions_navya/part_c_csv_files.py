import csv

# Exercise 10 - Read a CSV with csv.reader
with open("scores.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)
# Output:
# ['name', 'score']
# ['Navya', '85']
# ['Deepak', '105']
# ['Varsha', '']
# ['Hema', '45']
# ['Mamatha', '-10']


# Exercise 11 - Read a CSV with DictReader
with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['score']}")
# Output:
# Navya: 85
# Deepak: 105
# Varsha:
# Hema: 45
# Mamatha: -10


# Exercise 12 - Compute an average from CSV data
with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    scores = []
    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))

average = sum(scores) / len(scores)
print(average)
# Output: 56.25


# Exercise 13 - Write a CSV file
students = [
    ["Navya", 85],
    ["Deepak", 90],
    ["Varsha", 78],
    ["Hema", 92]
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows(students)