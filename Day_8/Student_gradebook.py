students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89],
    "david": []
}
average_grades = {
    name: (sum(grades) / len(grades) if grades else 0)
    for name, grades in students.items()
}
top_students = {
    name
    for name, grades in students.items()
    if grades and all(grade > 80 for grade in grades)
}
sorted_students = sorted(
    average_grades.items(),
    key=lambda x: x[1],
    reverse=True
)
print("Average Grades:", average_grades)
print("Students with all grades above 80:", top_students)
print("Sorted Students:", sorted_students)
# Output:
# Average Grades: {'alice': 86.33333333333333,
#                  'bob': 67.66666666666667,
#                  'carol': 91.66666666666667,
#                  'david': 0}
# Students with all grades above 80: {'carol'}
# Sorted Students: [('carol', 91.66666666666667),
#                   ('alice', 86.33333333333333),
#                   ('bob', 67.66666666666667),
#                   ('david', 0)]




