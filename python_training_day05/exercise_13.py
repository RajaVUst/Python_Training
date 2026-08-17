roster = [
    {"name": "Deepa", "scores": [80, 85, 90]},
    {"name": "Sruthie", "scores": [75, 88, 92]},
    {"name": "Varsha", "scores": [90, 95, 85]}
]

for student in roster:
    average = sum(student["scores"]) / len(student["scores"])
    print(student["name"], "Average:", round(average, 1))



#output:
'''Amit Average: 85.0
Reni Average: 85.0
Tara Average: 90.0'''