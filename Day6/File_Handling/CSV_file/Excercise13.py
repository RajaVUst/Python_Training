# Write a CSV file

import csv

students = [
    ["Arun", 80],
    ["Bala", 90],
    ["Cathy", 75],
    ["David", 88]
]

with open("Day6/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])

    for student in students:
        writer.writerow(student)


# Output:
# It will create the nes CSV file in Day 6 folder.