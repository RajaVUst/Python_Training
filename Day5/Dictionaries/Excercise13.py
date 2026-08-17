# Class roster

roster = [
    {"name": "Logesh", "scores": [80, 90, 85]},
    {"name": "Rohit", "scores": [90, 95, 88]},
    {"name": "Dev", "scores": [70, 75, 80]}
]

for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(student["name"], round(average, 1))


# Output:
# Amit 85.0
# Reni 91.0
# Tara 75.0