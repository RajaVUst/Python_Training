import csv

students = [
    ["Amit", 78],
    ["Reni", 91],
    ["Tara", 65],
    ["Sam", 88]
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows(students)

