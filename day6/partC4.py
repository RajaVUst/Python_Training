import csv
students = [["Asha", 92], ["Ben", 85], ["Chen", 88], ["Divya", 95]]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows(students)

# OUTPUT

# No console output
