roster = [
    {"name": "Reni", "scores": [85, 90, 88]},
    {"name": "Amit", "scores": [78, 82, 80]},
    {"name": "Tara", "scores": [92, 95, 90]}
]
for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(student["name"], round(average, 1))

# output
# Reni 87.7
# Amit 80.0
# Tara 92.3