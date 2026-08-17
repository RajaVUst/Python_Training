
roster = [
    {"name": "Amit", "scores": [80, 90, 70]},
    {"name": "Reni", "scores": [95, 91, 88]},
    {"name": "Tara", "scores": [60, 75, 82]},
]
for student in roster:
    avg = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {round(avg, 1)}")

#output
# Amit: 80.0
# Reni: 91.3
# Tara: 72.3