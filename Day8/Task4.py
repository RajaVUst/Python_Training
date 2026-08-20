students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89],
    "dave": [],
}

# Compute average grades, using 0 for students with no grades.
averages = {
    name: sum(grades) / len(grades) if grades else 0
    for name, grades in students.items()
}

# Find students whose grades are all above 80.
above_80 = {
    name
    for name, grades in students.items()
    if grades and all(grade > 80 for grade in grades)
}

# Sort students by average grade in descending order.
sorted_students = sorted(
    averages.items(),
    key=lambda student: student[1],
    reverse=True,
)

print("Averages:", averages)
print("All grades above 80:", above_80)
print("Sorted students:", sorted_students)