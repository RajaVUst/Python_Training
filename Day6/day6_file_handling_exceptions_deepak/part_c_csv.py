import csv

# Setup: scores.csv - 5 rows, one out-of-range (150), one blank
with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["Asha", "88"])
    writer.writerow(["Ravi", "91"])
    writer.writerow(["Kiran", "150"])
    writer.writerow(["Meera", ""])
    writer.writerow(["Zoya", "76"])

# Exercise 10 - Read a CSV with csv.reader
with open("scores.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)
# Output:
# ['name', 'score']
# ['Asha', '88']
# ['Ravi', '91']
# ['Kiran', '150']
# ['Meera', '']
# ['Zoya', '76']

# Exercise 11 - Read a CSV with DictReader
with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f'{row["name"]}: {row["score"]}')
# Output:
# Asha: 88
# Ravi: 91
# Kiran: 150
# Meera:
# Zoya: 76

# Exercise 12 - Compute an average from CSV data
valid_scores = []
with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["score"] != "":
            valid_scores.append(int(row["score"]))
print(valid_scores)
print(round(sum(valid_scores) / len(valid_scores), 2))
# Output:
# [88, 91, 150, 76]
# 101.25

# Exercise 13 - Write a CSV file
students = [["name", "score"], ["Nina", 82], ["Farid", 95], ["Leo", 67], ["Tara", 74]]
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

with open("results.csv", "r") as f:
    print(f.read())
# Output:
# name,score
# Nina,82
# Farid,95
# Leo,67
# Tara,74