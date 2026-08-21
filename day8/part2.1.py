students = {
    "alice": [88, 92, 79],
    "bob":   [65, 70, 68],
    "carol": [95, 91, 89],
}


avg_grade = {
    name: sum(scores) / len(scores) if scores else 0
    for name, scores in students.items()
}


above_80 = {
    name
    for name, scores in students.items()
    if scores and all(score > 80 for score in scores)
}


sorted_students = sorted(
    avg_grade.items(),
    key=lambda item: item[1],
    reverse=True
)

print(avg_grade)
print(above_80)
print(sorted_students)

# OUTPUT
# {'alice': 86.33333333333333, 'bob': 67.66666666666667, 'carol': 91.66666666666667}
# {'carol'}
# [('carol', 91.66666666666667), ('alice', 86.33333333333333), ('bob', 67.66666666666667)]