roster = [
    {"name": "Amit",  "scores": [85, 90, 78]},
    {"name": "Reni",  "scores": [92, 88, 95]},
    {"name": "Tara",  "scores": [70, 65, 80]},
]

for student in roster:
    avg = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {round(avg, 1)}")
