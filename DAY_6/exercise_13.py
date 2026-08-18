import csv

students = [
    ["Amit", 85],
    ["Reni", 92],
    ["Tara", 78],
    ["Sam",  61],
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows(students)

print("results.csv written successfully.")
