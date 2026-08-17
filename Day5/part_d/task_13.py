roster = [
    {"name": "Aish", "scores": [85, 90, 88]},
    {"name": "Amit", "scores": [78, 82, 80]},
    {"name": "Tara", "scores": [92, 95, 90]}
]

for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {round(average, 1)}")

# Aish: 87.7
# Amit: 80.0
# Tara: 92.3