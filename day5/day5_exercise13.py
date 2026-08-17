roster = [
    {"name": "Aron", "scores": [85, 90, 88]},
    {"name": "Pranav", "scores": [92, 95, 89]},
    {"name": "Lekhya", "scores": [78, 81, 84]}
]

for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {round(average, 1)}")
    
"""
OUTPUT:
Aron: 87.7
Pranav: 92.0
Lekhya: 81.0
"""