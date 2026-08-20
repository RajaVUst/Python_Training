students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89],
    "dave": []
}

averages = {
    name: (sum(grades) / len(grades) if grades else 0)
    for name, grades in students.items()
}

print(averages)

high_performers = {
    name for name, grades in students.items()
    if grades and all(grade > 80 for grade in grades)
}

print(high_performers)

ranked_students = sorted(
    averages.items(),
    key=lambda item: item[1],
    reverse=True
)

print(ranked_students)

# Output:
# [('carol', 91.66666666666667), ('alice', 86.33333333333333), ('bob', 67.66666666666667), ('dave', 0)]
# {'carol', 'alice'}
