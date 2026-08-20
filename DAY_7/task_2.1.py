students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89],
}

# Dict comprehension: student -> average grade (guard against empty list)
averages = {
    name: (sum(grades) / len(grades) if grades else None)
    for name, grades in students.items()
}

# Set of students with every grade above 80
above_80 = {name for name, grades in students.items() if grades and all(g > 80 for g in grades)}

# Sorted list of (name, avg) tuples, descending by average
sorted_students = sorted(
    [(name, avg) for name, avg in averages.items() if avg is not None],
    key=lambda x: x[1],
    reverse=True
)

print("Averages:", averages)
print("All grades above 80:", above_80)
print("Ranked students:", sorted_students)
