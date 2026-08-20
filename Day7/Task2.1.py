students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89],
    "sai": []
}

averages = {
    name: sum(grades) / len(grades) if grades else 0.0
    for name, grades in students.items()
}

students_above_80 = {
    name
    for name, grades in students.items()
    if grades and all(grade > 80 for grade in grades)
}

sorted_students = sorted(
    averages.items(),
    key=lambda student: student[1],
    reverse=True
)

print("Average grades:", averages)
print("Students with every grade above 80:", students_above_80)
print("Students sorted by average:", sorted_students)


#output

'''

Average grades: {'alice': 86.33333333333333, 'bob': 67.66666666666667, 'carol': 91.66666666666667, 'sai': 0.0}
Students with every grade above 80: {'carol'}
Students sorted by average: [('carol', 91.66666666666667), ('alice', 86.33333333333333), ('bob', 67.66666666666667), ('sai', 0.0)]
'''