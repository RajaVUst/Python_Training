def grade_summary(roster):
    result = []
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
        result.append({
            "name": student["name"],
            "average": round(average, 1),
            "grade": grade
        })

    return result
roster = [
    {"name": "Reni", "scores": [85, 90, 88]},
    {"name": "Amit", "scores": [78, 82, 80]},
    {"name": "Tara", "scores": [92, 95, 90]}
]
print(grade_summary(roster))

# output
# [{'name': 'Reni', 'average': 87.7, 'grade': 'B'}, {'name': 'Amit', 'average': 80.0, 'grade': 'B'}, {'name': 'Tara', 'average': 92.3, 'grade': 'A'}]