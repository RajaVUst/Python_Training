roster = [
    {"name": "Amit", "scores": [85, 90, 88]},
    {"name": "Shashi", "scores": [92, 95, 89]},
    {"name": "Tara", "scores": [84, 81]}
]

for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {round(average, 1)}")

# Output:
# Amit: 87.7    
# Shashi: 92.0
# Tara: 82.5