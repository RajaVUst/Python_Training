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
    {"name": "Amit", "scores": [88, 85, 90]},
    {"name": "Reni", "scores": [85, 90, 90]},
    {"name": "Tara", "scores": [95, 92, 68]}
]

print(grade_summary(roster))

"""
Output->
[{'name': 'Amit', 'average': 87.7, 'grade': 'B'}, {'name': 'Reni', 'average': 88.3, 'grade': 'B'}, {'name': 'Tara', 'average': 85.0, 'grade': 'B'}]
"""