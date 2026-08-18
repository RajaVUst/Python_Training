from constants import SCORES_CSV, RESULTS_CSV
import csv

# Create scores.csv

with open(SCORES_CSV, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["Amit", 85])
    writer.writerow(["Varsha", 95])
    writer.writerow(["Tara", 120])   # Out of range
    writer.writerow(["Rahul", ""])   # Blank score
    writer.writerow(["Anu", -10])    # Out of range


# Exercise 10: Read a CSV with csv.reader
with open(SCORES_CSV, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)
# Output:
# Header: ['name', 'score']
# ['Amit', '85']
# ['Varsha', '95']
# ['Tara', '120']
# ['Rahul', '']
# ['Anu', '-10']


# Exercise 11: Read a CSV with DictReader
with open(SCORES_CSV, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['score']}")
# Output:
# Amit: 85
# Varsha: 95
# Tara: 120
# Rahul:
# Anu: -10


# Exercise 12: Compute an average from CSV data
scores = []
with open(SCORES_CSV, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))
average = sum(scores) / len(scores)
print("Average:", average)
# Output:
# Average: 72.5


# Exercise 13: Write a CSV file
students = [
    ["Amit", 85],
    ["Varsha", 92],
    ["Tara", 78],
    ["Rahul", 88]
]
with open(RESULTS_CSV, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    for student in students:
        writer.writerow(student)
with open(RESULTS_CSV, "r") as f:
    print(f.read())
# Output:
# name,score
# Amit,85
# Varsha,92
# Tara,78
# Rahul,88