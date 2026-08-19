import csv

students = [
    ["Amit", 85],
    ["Reni", 92],
    ["Tara", 78],
    ["Sam", 88]
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "score"])
    writer.writerows(students)