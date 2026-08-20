
students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89],
}

averages = {
    name: sum(grades) / len(grades) if grades else 0
    for name, grades in students.items()
}

above_80 = {
    name
    for name, grades in students.items()
    if grades and all(grade > 80 for grade in grades)
}

sorted_students = sorted(
    averages.items(),
    key=lambda item: item[1],
    reverse=True
)

print("Averages:", averages)
print("Every grade above 80:", above_80)
print("Sorted students:", sorted_students)

# Output:
# Averages: {'alice': 86.33333333333333, 'bob': 67.66666666666667, 'carol': 91.66666666666667}
# Every grade above 80: {'alice', 'carol'}
# Sorted students: [('carol', 91.66666666666667), ('alice', 86.33333333333333), ('bob', 67.66666666666667)]