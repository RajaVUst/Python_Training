def grade_summary(roster):
    summary = []

    for student in roster:
        avg = sum(student["scores"]) / len(student["scores"])

        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"

        summary.append({
            "name": student["name"],
            "average": round(avg, 1),
            "grade": grade
        })

    return summary


roster = [
    {"name": "Amit", "scores": [80, 85, 90]},
    {"name": "Reni", "scores": [95, 92, 97]},
    {"name": "Tara", "scores": [65, 72, 68]}
]

print(grade_summary(roster))

# Output:
# [{'name': 'Amit', 'average': 85.0, 'grade': 'B'}, 
# {'name': 'Reni', 'average': 94.7, 'grade': 'A'}, 
# {'name': 'Tara', 'average': 68.3, 'grade': 'D'}]