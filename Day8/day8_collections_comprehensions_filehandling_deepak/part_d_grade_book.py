students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89],
    "dave": [],
}

def safe_average(grades):
    return sum(grades) / len(grades) if grades else None

averages = {name: safe_average(g) for name, g in students.items()}
top_students = {name for name, g in students.items() if g and all(x > 80 for x in g)}
sorted_by_avg = sorted(averages.items(), key=lambda p: (p[1] is None, -(p[1] or 0)))

print(averages)
print(top_students)
print(sorted_by_avg)
# Output:
# {'alice': 86.33333333333333, 'bob': 67.66666666666667, 'carol': 91.66666666666667, 'dave': None}
# {'carol'}
# [('carol', 91.66666666666667), ('alice', 86.33333333333333), ('bob', 67.66666666666667), ('dave', None)]