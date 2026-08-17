def grade_summary(roster):
    summary = []

    for student in roster:
        average = sum(student["scores"]) / len(student["scores"])

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        summary.append({
            "name": student["name"],
            "average": round(average, 1),
            "grade": grade
        })

    return summary


roster = [
    {"name": "Amit", "scores": [85, 90, 88]},
    {"name": "Reni", "scores": [95, 92, 89]},
    {"name": "Tara", "scores": [72, 68, 75]}
]

print(grade_summary(roster))

"""
OUTPUT:
[{'name': 'Amit', 'average': 87.7, 'grade': 'B'}, {'name': 'Reni', 'average': 92.0, 'grade': 'A'}, {'name': 'Tara', 'average': 71.7, 'grade': 'C'}]
"""
