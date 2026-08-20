students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89]
}

averages = {
    name: sum(grades) / len(grades)
    for name, grades in students.items()
    if len(grades) > 0
}
print("Averages:", averages)

above_80 = {
    name
    for name, grades in students.items()
    if grades and all(grade > 80 for grade in grades)
}
print("Students above 80:", above_80)

sorted_students = sorted(
    averages.items(),
    key=lambda x: x[1],
    reverse=True
)
print("Sorted students:", sorted_students)

# Output:
# Averages: {'alice': 86.33333333333333, 'bob': 67.66666666666667, 'carol': 91.66666666666667}
# Students above 80: {'carol'}
# Sorted students: [('carol', 91.66666666666667), ('alice', 86.33333333333333), ('bob', 67.66666666666667)]