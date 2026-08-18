import csv

students = [
    ["Rahul", 92],
    ["Priya", 88],
    ["Arjun", 95],
    ["Sneha", 90]
]

with open(r"Day_6\Ref doc\results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["Name", "Score"])
    writer.writerows(students)

print("results.csv created successfully!")

# Output:
# results.csv created successfully!