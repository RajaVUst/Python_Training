import csv
students = [
    ["Asha", 85],
    ["Rahul", 92],
    ["Priya", 78],
    ["Arun", 88]
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows(students)