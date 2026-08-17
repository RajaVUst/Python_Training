roster = [
    {"name": "Amit", "scores": [85, 90, 88]},
    {"name": "Reni", "scores": [92, 87, 95]},
    {"name": "Tara", "scores": [78, 84, 81]}
]

for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {round(average, 1)}")

"""
Output->
Amit: 87.7
Reni: 91.3
Tara: 81.0
"""