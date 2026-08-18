
import csv


students = [["Priya", 88], ["Karan", 72], ["Divya", 95], ["Rohit", 60]]
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows(students)

with open("results.csv") as f:
    print(f.read())
    
#output
# name,score
# Priya,88
# Karan,72
# Divya,95
# Rohit,60