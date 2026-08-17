roster = [
    {"name": "Amit", "scores": [78, 82, 80]},
    {"name": "Reni", "scores": [91, 89, 94]},
    {"name": "Tara", "scores": [65, 72, 70]}
]

for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {average:.1f}")

    '''
    Amit: 80.0
    Reni: 91.3
    Tara: 69.0
    '''