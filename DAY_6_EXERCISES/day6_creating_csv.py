import csv

students = [
    ["Alice", 95],
    ["Bob", 88],
    ["Charlie", 76],
    ["David", 91]
]

with open("DAY_6_EXERCISES/results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "score"])

    for student in students:
        writer.writerow(student)

"""
Output file->
name,score
Alice,95
Bob,88
Charlie,76
David,91
"""