roster = [
    {"name": "Amit", "scores": [85, 90, 88]},
    {"name": "Reni", "scores": [91, 95, 89]},
    {"name": "Tara", "scores": [78, 82, 80]}
]

for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {round(average, 1)}")

#     output:
#     Amit: 87.7
# Reni: 91.7
# Tara: 80.0