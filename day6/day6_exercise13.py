import csv

students = [
    ["Aswin", 95],
    ["Reni", 88],
    ["Logesh", 91],
    ["Preetham,", 84]
]

with open("day6/results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(["name", "score"])

    # Write the student data rows
    writer.writerows(students)
    
"""
OUTPUT:
name,score
Aswin,95
Reni,88
Logesh,91
"Preetham,",84
"""