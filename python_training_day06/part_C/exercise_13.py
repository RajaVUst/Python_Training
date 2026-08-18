import csv

students = [
    ["Asha", 85],
    ["Rahul", 92],
    ["Priya", 88],
    ["Meena", 95]
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "score"])
    writer.writerows(students)