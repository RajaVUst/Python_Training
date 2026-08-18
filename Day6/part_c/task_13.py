import csv

students = [
    ["Alice", 90],
    ["Bob", 85],
    ["Charlie", 78],
    ["David", 95]
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "score"])
    writer.writerows(students)