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
    {"name": "Aish", "scores": [90, 85, 95]},
    {"name": "Amit", "scores": [75, 80, 70]},
    {"name": "Tara", "scores": [55, 60, 50]}
]

print(grade_summary(roster))


# [{'name': 'Aish', 'average': 90.0, 'grade': 'A'}, {'name': 'Amit', 'average': 75.0, 'grade': 'C'}, {'name': 'Tara', 'average': 55.0, 'grade': 'F'}]